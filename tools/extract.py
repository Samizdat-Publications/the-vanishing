"""One-time extraction of case data out of the-vanishing-v2.html.

Reads the frozen reference, locates each data block by parsing its literal, writes the
data to research/*.json, and writes the remaining 87 percent of the file to
templates/dashboard.shell.html with a hole per block.

Then runs Gate 0: reassemble the shell with the ORIGINAL slices and assert the result is
byte identical to the reference. Gate 0 proves the splicing in isolation, before any
emitter exists, so that every later failure is an emitter failure rather than a mystery
somewhere in 325 KB.

This script runs once. Its output is committed and it then becomes the record of how the
data got there, which is why it stays in the repo.

    cd /home/user/the-vanishing
    python3 tools/extract.py
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jsliteral

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFERENCE = os.path.join(ROOT, "the-vanishing-v2.html")

# The reference is frozen for the duration of the rebuild. If this hash stops matching,
# someone edited the target the regenerator has to reproduce, and the checkpoint stops
# meaning anything. Fail rather than silently rebase onto the new file.
REFERENCE_SHA256 = "2dfc55e324b7535fbeea223e6b8699bf788ef60d9220417a81bf14bbff3d910a"
REFERENCE_BYTES = 324923

# Blocks to extract, grouped by destination file. Everything not listed stays in the
# shell. The boundary is a commitment rather than a convenience, because the checkpoint
# only proves what it covers, so research/README.md records the reason for each choice.
BLOCK_GROUPS = {
    "cases": ["PEOPLE"],
    "entities": [
        "INSTITUTIONS", "PROGRAMS", "LOCATIONS", "DOMAINS",
        "ENTITY_INFO", "ENTITY_SOURCES", "SOURCES",
    ],
    "timeline": ["PRECEDENT", "TIMELINE"],
    "graph": [
        "PROGRAM_EDGES", "IN_FBI", "IN_OVERSIGHT",
        "INSTITUTION_PLACES", "TEMPORAL_WINDOW_DAYS",
    ],
    "photos": ["PHOTOS"],
    "taxonomy": [
        "CLUSTERS", "TIERS", "AXES", "STRANDS", "STATUS_LABEL", "PRECISION_LABEL",
    ],
}

# Blocks deliberately left in the shell, with the reason. Written to research/README.md.
NOT_EXTRACTED = {
    "PALETTE": "design system, changes when the design changes, not when a case does",
    "EDGE_TYPES": "design system, colour and dash styling per edge type",
    "COUNTERS": (
        "analytical content, but the 'Where the skeptics overreach' table and the "
        "'Family positions' paragraph sit inline in viewCounterargs and exist nowhere "
        "else. Extracting one without the other splits a single argument across two "
        "files. Both go to step 3 together"
    ),
    "MODELS / EFFORTS / MODEL_CAPS / SUGGESTIONS / SYSTEM_PROMPT": (
        "analyst config, coupled to the Anthropic API, belongs with the code that calls it"
    ),
    "VIEW_LABEL / FILTER_GROUPS / TYPE_PRIORITY / STRENGTH_RAMP / shaders": (
        "renderer internals"
    ),
}

# Two blocks build their elements through positional factories rather than writing object
# literals. Trailing arguments are truncated rather than omitted by name, so a row's arity
# carries meaning and the emitter has to reproduce it.
#   other(id, cls, label, cluster, sub, desc, srcs)   line 1000
#   E(a, b, type)                                     line 1127
OTHER_PARAMS = ["id", "cls", "label", "cluster", "sub", "desc", "srcs"]
FACTORIES = {
    "INSTITUTIONS": ("other", OTHER_PARAMS),
    "PROGRAMS": ("other", OTHER_PARAMS),
    "LOCATIONS": ("other", OTHER_PARAMS),
    "DOMAINS": ("other", OTHER_PARAMS),
    "PROGRAM_EDGES": ("E", ["a", "b", "type"]),
}


def die(message):
    sys.stderr.write("FATAL: %s\n" % message)
    sys.exit(1)


def check_provenance(path):
    """Gate D. Pin the input and refuse the known-bad lookalike sources."""
    real = os.path.realpath(path)
    if "design-package" in real.replace("\\", "/").split("/"):
        die(
            "refusing to extract from design-package/.\n"
            "  vanishing-graph.js and vanishing-timeline.js are pre-August-7 ancestors.\n"
            "  They differ by three adjudicated axis scores: li S0 not S1, loureiro I3\n"
            "  not I1, mccasland P2 not P3. The declaration differs by one word."
        )
    data = open(real, "rb").read()
    digest = hashlib.sha256(data).hexdigest()
    if digest != REFERENCE_SHA256:
        die(
            "reference file hash mismatch.\n"
            "  expected %s\n  actual   %s\n"
            "  the-vanishing-v2.html is frozen until the checkpoint passes. If this\n"
            "  change was intentional, the pin in tools/ must be updated deliberately."
            % (REFERENCE_SHA256, digest)
        )
    if len(data) != REFERENCE_BYTES:
        die("reference byte count %d, expected %d" % (len(data), REFERENCE_BYTES))
    return data.decode("utf-8")


def locate(text, name):
    """Find a `const NAME = <literal>` declaration and return its span.

    The hole covers the literal only. The `const NAME = ` prefix and the trailing `;`
    stay in the shell, which keeps the emitter's job as small as possible.

    Spans are found by bracket scanning rather than by parsing, because several blocks
    wrap their elements in factory calls that the literal parser deliberately rejects.
    """
    match = re.search(r"^[ \t]*const[ \t]+%s[ \t]*=[ \t]*" % re.escape(name), text, re.M)
    if not match:
        die("could not locate declaration for %s" % name)
    start = match.end()
    if text[start] not in "[{":
        # A scalar such as TEMPORAL_WINDOW_DAYS = 60.
        end = start
        while end < len(text) and text[end] not in ";\n":
            end += 1
        return start, end
    try:
        end = jsliteral.scan_span(text, start)
    except jsliteral.JsParseError as exc:
        die("failed scanning %s: %s" % (name, exc))
    return start, end


def _rewrite_calls(raw, fname):
    """Turn `fname(a, b, c)` into `[a, b, c]` so the argument list parses as data.

    Used for the `other(...)` factory. The scan skips strings and comments, so a
    parenthesis inside prose cannot confuse it.
    """
    out = []
    i = 0
    needle = fname + "("
    while True:
        hit = raw.find(needle, i)
        if hit == -1:
            out.append(raw[i:])
            return "".join(out)
        # Only a bare identifier match counts, not a suffix of a longer name.
        if hit > 0 and raw[hit - 1] in jsliteral._IDENT_CHARS:
            out.append(raw[i:hit + len(needle)])
            i = hit + len(needle)
            continue
        close = jsliteral.scan_span(raw, hit + len(fname))
        out.append(raw[i:hit])
        out.append("[")
        out.append(_rewrite_calls(raw[hit + len(needle):close - 1], fname))
        out.append("]")
        i = close


def parse_block(name, raw):
    """Parse one block's raw source into plain Python data."""
    if name == "PEOPLE":
        # PEOPLE wraps every record in P_({...}). The block was verified to contain no
        # other function call, no template literal and no computed value, so rewriting
        # the wrappers cannot reach anything else.
        if raw.count("P_({") != raw.count("})"):
            die("PEOPLE wrapper count mismatch, refusing to guess")
        return jsliteral.parse(raw.replace("P_({", "{").replace("})", "}"))

    if name in FACTORIES:
        fname, params = FACTORIES[name]
        rows = jsliteral.parse(_rewrite_calls(raw, fname))
        records = []
        for row in rows:
            if len(row) > len(params):
                die("%s row has %d args, %s takes %d" % (name, len(row), fname, len(params)))
            # Trailing arguments are truncated rather than omitted by name, so zip on
            # the actual arity. Absence here is positional, not semantic.
            records.append(dict(zip(params, row)))
        return records

    return jsliteral.parse(raw)


def main():
    text = check_provenance(REFERENCE)
    print("reference OK  sha256 %s...  %d bytes, %d chars"
          % (REFERENCE_SHA256[:12], REFERENCE_BYTES, len(text)))

    holes = []
    extracted = {}

    for group, names in BLOCK_GROUPS.items():
        payload = {}
        for name in names:
            start, end = locate(text, name)
            try:
                payload[name] = parse_block(name, text[start:end])
            except jsliteral.JsParseError as exc:
                die("failed parsing %s: %s" % (name, exc))
            holes.append({"block": name, "group": group, "start": start, "end": end})
        extracted[group] = payload

    # Holes must be ordered and non-overlapping for splicing to be well defined.
    holes.sort(key=lambda h: h["start"])
    for a, b in zip(holes, holes[1:]):
        if a["end"] > b["start"]:
            die("blocks %s and %s overlap" % (a["block"], b["block"]))

    print("located %d blocks across %d groups" % (len(holes), len(BLOCK_GROUPS)))
    covered = sum(h["end"] - h["start"] for h in holes)
    print("  %d of %d chars extracted (%.1f%%), %.1f%% stays in the shell"
          % (covered, len(text), 100.0 * covered / len(text),
             100.0 - 100.0 * covered / len(text)))

    # ---------------------------------------------------------------- Gate 0
    # Reassemble with the ORIGINAL slices. This must be identical before any emitter is
    # written, otherwise a later mismatch cannot be attributed.
    shell_parts = []
    slices = []
    cursor = 0
    for hole in holes:
        shell_parts.append(text[cursor:hole["start"]])
        slices.append(text[hole["start"]:hole["end"]])
        cursor = hole["end"]
    shell_parts.append(text[cursor:])

    rebuilt = []
    for i, part in enumerate(shell_parts):
        rebuilt.append(part)
        if i < len(slices):
            rebuilt.append(slices[i])
    rebuilt = "".join(rebuilt)

    if rebuilt != text:
        for i, (a, b) in enumerate(zip(rebuilt, text)):
            if a != b:
                die("GATE 0 FAILED: first difference at byte %d" % i)
        die("GATE 0 FAILED: length %d vs %d" % (len(rebuilt), len(text)))
    print("GATE 0 PASS  shell + original slices is byte identical to the reference")

    # ---------------------------------------------------------------- write outputs
    os.makedirs(os.path.join(ROOT, "research"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "tools", "templates"), exist_ok=True)

    for group, payload in extracted.items():
        # A single-block group unwraps, so cases.json is the array itself rather than
        # {"PEOPLE": [...]}. That keeps the hand-edited file as plain as possible.
        out = payload[BLOCK_GROUPS[group][0]] if len(payload) == 1 else payload
        path = os.path.join(ROOT, "research", "%s.json" % group)
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(out, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        print("  wrote research/%s.json" % group)

    # The P_ factory stays in the frozen shell, so its defaults are mirrored here and
    # verify asserts the two still agree. If they drift, the meaning of "key absent"
    # changes for all 15 records at once, silently.
    p_match = re.search(r"const P_ = \(o\) => Object\.assign\(", text)
    if not p_match:
        die("could not locate the P_ defaults factory")
    defaults, _ = jsliteral.parse_prefix(text, p_match.end())
    with open(os.path.join(ROOT, "research", "case_defaults.json"),
              "w", encoding="utf-8", newline="\n") as fh:
        json.dump(defaults, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("  wrote research/case_defaults.json (%d keys)" % len(defaults))

    shell_path = os.path.join(ROOT, "tools", "templates", "dashboard.shell.html")
    with open(shell_path, "w", encoding="utf-8", newline="") as fh:
        fh.write("\x00HOLE\x00".join(shell_parts))
    with open(os.path.join(ROOT, "tools", "templates", "holes.json"),
              "w", encoding="utf-8", newline="\n") as fh:
        json.dump([{"block": h["block"], "group": h["group"]} for h in holes],
                  fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("  wrote tools/templates/dashboard.shell.html and holes.json")

    print("\nextraction complete. Gate 0 green.")


if __name__ == "__main__":
    main()
