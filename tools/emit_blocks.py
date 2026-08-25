"""Per-block emitters that reproduce the reference file's hand-authored formatting.

Each block gets its own emitter because the source is internally consistent per block and
inconsistent between blocks. Three apostrophe conventions and two key-spacing conventions
are in use, and no block mixes two, which is what makes a per-block policy correct and a
single global policy wrong.

Formatting rules that are genuinely rules were verified across all records. The handful of
authorial irregularities that are not rule-describable live in format_exceptions.json, and
there are only two of them.
"""

from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jsliteral
import extract

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(ROOT, "tools", "format_exceptions.json"), encoding="utf-8") as _fh:
    EXCEPTIONS = json.load(_fh)

# PEOPLE packs its opening keys onto three lines. The third group is an ordered filter over
# whichever keys are present, not a fixed tuple: thomas inserts isNonDefense and moffatt
# inserts mediaLinkedOnly between I and domains.
PEOPLE_GROUPS = [
    ["id", "label", "status", "outcome", "date", "age"],
    ["loc", "locId", "instId", "sub"],
    ["cluster", "tier", "S", "P", "I", "isNonDefense", "mediaLinkedOnly", "domains"],
]

# These three arrays are always exploded one element per line. Every other array stays on
# one line however long it runs, sources included. Verified across all 15 records with zero
# exceptions.
PEOPLE_EXPLODE = {"sequenceChain", "chronology", "claims"}


def emit_people(cases, defaults):
    """Emit the PEOPLE block, including its P_({...}) wrappers."""
    style = jsliteral.Style(apostrophe=jsliteral.APOS_U2019, key_sep=": ")
    packs = EXCEPTIONS.get("people.pack", {})

    out = ["["]
    for case in cases:
        out.append("  P_({")
        written = [k for k in case if not (k in defaults and case[k] == defaults[k])]
        grouped = set()

        for group in PEOPLE_GROUPS:
            members = [k for k in group if k in written]
            if not members:
                continue
            grouped.update(members)
            out.append("    " + ", ".join(
                "%s: %s" % (k, jsliteral.emit_inline(case[k], style)) for k in members
            ) + ",")

        # An authorial irregularity: garcia packs leftBehind and tookWith onto one line
        # where every other record gives each its own. Carried as data, not as a rule.
        packed_pairs = packs.get(case["id"], [])
        consumed = set()
        for pair in packed_pairs:
            members = [k for k in pair if k in written]
            if len(members) < 2:
                continue
            consumed.update(members)

        emitted_pair = False
        for key in case:
            if key in grouped or key not in written:
                continue
            if key in consumed:
                if emitted_pair:
                    continue
                for pair in packed_pairs:
                    members = [k for k in pair if k in written]
                    if len(members) >= 2:
                        out.append("    " + ", ".join(
                            "%s: %s" % (k, jsliteral.emit_inline(case[k], style))
                            for k in members
                        ) + ",")
                emitted_pair = True
                continue

            value = case[key]
            if key in PEOPLE_EXPLODE and isinstance(value, list) and value:
                out.append("    %s: [" % key)
                for item in value:
                    out.append("      %s," % jsliteral.emit_inline(item, style))
                out.append("    ],")
            else:
                out.append("    %s: %s," % (key, jsliteral.emit_inline(value, style)))

        out.append("  }),")
    out.append("]")
    return "\n".join(out)


def _key(name, quote_all):
    """Quote an object key iff the block quotes all keys, or it is not an identifier."""
    if quote_all or not (name and (name[0].isalpha() or name[0] in "_$")
                         and all(c.isalnum() or c in "_$" for c in name)):
        return "'%s'" % name
    return name


def emit_object_array(items, style, indent="  "):
    """One object literal per line. PRECEDENT, TIMELINE, AXES, STRANDS."""
    out = ["["]
    for item in items:
        out.append("%s%s," % (indent, jsliteral.emit_inline(item, style)))
    out.append("]")
    return "\n".join(out)


def emit_factory_array(records, fname, params, style, groups=None, indent="  "):
    """Positional factory calls. INSTITUTIONS, PROGRAMS, LOCATIONS, DOMAINS, PROGRAM_EDGES.

    Trailing arguments are truncated rather than omitted by name, so a record's arity is
    reproduced by emitting only the params it actually carries.
    """
    calls = []
    for rec in records:
        args = [jsliteral.emit_inline(rec[p], style) for p in params if p in rec]
        calls.append("%s(%s)" % (fname, ", ".join(args)))

    out = ["["]
    if groups:
        i = 0
        for count in groups:
            out.append(indent + ", ".join(calls[i:i + count]) + ",")
            i += count
        if i != len(calls):
            raise ValueError("%s line groups cover %d of %d calls" % (fname, i, len(calls)))
    else:
        for call in calls:
            out.append("%s%s," % (indent, call))
    out.append("]")
    return "\n".join(out)


def emit_map(mapping, style, quote_all=False, indent="  ", outer_sep=": "):
    """One key per line. CLUSTERS, TIERS, SOURCES, ENTITY_INFO, ENTITY_SOURCES.

    The outer separator is tracked apart from the inner one because ENTITY_INFO and
    ENTITY_SOURCES write `'l-hsv': { desc:'...' }`: a space after the outer key, none
    after the inner keys. Treating the two as one setting breaks whichever it is not
    tuned for.
    """
    out = ["{"]
    for key, value in mapping.items():
        out.append("%s%s%s%s," % (
            indent, _key(key, quote_all), outer_sep,
            jsliteral.emit_inline(value, style),
        ))
    out.append("}")
    return "\n".join(out)


def emit_inline_map(mapping, style, indent="  "):
    """Whole map on one line. STATUS_LABEL, PRECISION_LABEL."""
    inner = ", ".join(
        "%s: %s" % (_key(k, False), jsliteral.emit_inline(v, style))
        for k, v in mapping.items()
    )
    return "{\n%s%s,\n}" % (indent, inner)


def emit_packed_array(items, style, groups, indent="  "):
    """Array wrapped across lines at author-chosen points. INSTITUTION_PLACES."""
    rendered = [jsliteral.emit_inline(i, style) for i in items]
    out = ["["]
    i = 0
    for count in groups:
        out.append(indent + ", ".join(rendered[i:i + count]) + ",")
        i += count
    if i != len(rendered):
        raise ValueError("line groups cover %d of %d items" % (i, len(rendered)))
    out.append("]")
    return "\n".join(out)


def emit_single_line_array(items, style):
    """The whole array on the declaration line. IN_FBI, IN_OVERSIGHT."""
    return "[" + ", ".join(jsliteral.emit_inline(i, style) for i in items) + "]"


def emit_photos(photos, style, indent="  ", bracket_col=13, credit_col=45):
    """Aligned two-column table.

    The opening bracket sits at column 13 on every row. The credit string starts at
    column 45 on fourteen rows and at 44 on eskridge, because eskridge.png is a
    character shorter than its neighbours and the author added one padding space instead
    of two. That single row is carried in format_exceptions.json rather than pretended
    to be a rule.
    """
    pads = EXCEPTIONS.get("photos.padTo", {})
    out = ["{"]
    for key, (path, credit) in photos.items():
        line = "%s%s:" % (indent, _key(key, False))
        line += " " * max(1, bracket_col - len(line))
        line += "[%s," % jsliteral.emit_string(path, style)
        target = pads.get(key, credit_col)
        line += " " * max(1, target - len(line))
        line += "%s]," % jsliteral.emit_string(credit, style)
        out.append(line)
    out.append("}")
    return "\n".join(out)


def build_emitters(data):
    """Map every extracted block to its emitter and style."""
    J = jsliteral
    cases, defaults = data["cases"], data["case_defaults"]
    ent, tl, g, ph, tax = (data["entities"], data["timeline"], data["graph"],
                           data["photos"], data["taxonomy"])
    ca = data.get("counterarguments", {})
    EX = EXCEPTIONS.get("linebreaks", {})

    # PEOPLE and PRECEDENT escape U+2019 and never use \'. The four `other()` blocks and
    # the two ENTITY maps do the reverse. PHOTOS switches quotes instead. No block mixes.
    s_u = J.Style(apostrophe=J.APOS_U2019, key_sep=": ")
    s_b = J.Style(apostrophe=J.APOS_BACKSLASH, key_sep=": ")
    s_bt = J.Style(apostrophe=J.APOS_BACKSLASH, key_sep=":")
    s_ph = J.Style(apostrophe=J.APOS_SWITCH, key_sep=": ")
    OP = extract.OTHER_PARAMS

    return {
        "PEOPLE": lambda: emit_people(cases, defaults),
        "INSTITUTIONS": lambda: emit_factory_array(ent["INSTITUTIONS"], "other", OP, s_b),
        "PROGRAMS": lambda: emit_factory_array(ent["PROGRAMS"], "other", OP, s_b),
        "LOCATIONS": lambda: emit_factory_array(ent["LOCATIONS"], "other", OP, s_b),
        "DOMAINS": lambda: emit_factory_array(ent["DOMAINS"], "other", OP, s_b),
        "ENTITY_INFO": lambda: emit_map(ent["ENTITY_INFO"], s_bt, quote_all=True),
        "ENTITY_SOURCES": lambda: emit_map(ent["ENTITY_SOURCES"], s_bt, quote_all=True),
        "SOURCES": lambda: emit_map(ent["SOURCES"], s_b),
        "PRECEDENT": lambda: emit_object_array(tl["PRECEDENT"], s_u),
        "TIMELINE": lambda: emit_object_array(tl["TIMELINE"], s_u),
        "PROGRAM_EDGES": lambda: emit_factory_array(
            g["PROGRAM_EDGES"], "E", ["a", "b", "type"], s_b, groups=EX.get("PROGRAM_EDGES")),
        "IN_FBI": lambda: emit_single_line_array(g["IN_FBI"], s_b),
        "IN_OVERSIGHT": lambda: emit_single_line_array(g["IN_OVERSIGHT"], s_b),
        "INSTITUTION_PLACES": lambda: emit_packed_array(
            g["INSTITUTION_PLACES"], s_b, EX.get("INSTITUTION_PLACES")),
        "TEMPORAL_WINDOW_DAYS": lambda: str(g["TEMPORAL_WINDOW_DAYS"]),
        "PHOTOS": lambda: emit_photos(ph, s_ph),
        "CLUSTERS": lambda: emit_map(tax["CLUSTERS"], s_b),
        "TIERS": lambda: emit_map(tax["TIERS"], s_b),
        "AXES": lambda: emit_object_array(tax["AXES"], s_b),
        "STRANDS": lambda: emit_object_array(tax["STRANDS"], s_b),
        "STATUS_LABEL": lambda: emit_inline_map(tax["STATUS_LABEL"], s_b),
        "PRECISION_LABEL": lambda: emit_inline_map(tax["PRECISION_LABEL"], s_b),
        # COUNTERS uses the no-space inner convention, like ENTITY_INFO.
        "COUNTERS": lambda: emit_object_array(ca["COUNTERS"], s_bt),
        "SKEPTIC_OVERREACH": lambda: emit_object_array(ca["SKEPTIC_OVERREACH"], s_bt),
        "FAMILY_POSITIONS": lambda: J.emit_string(ca["FAMILY_POSITIONS"], s_bt),
    }

