"""research/ -> data/dataset.json

At the step 2 checkpoint this is deliberately an IDENTITY transform. Its whole purpose
right now is to exist as the seam that step 3's per-claim tiering and outcome-field work
drops into. A merge step that changes nothing is the correct shape for a checkpoint whose
definition is that nothing changed.

It does validate cross references and field types, because those checks cost nothing here
and catch a hand edit later.

    python3 tools/merge.py
"""

from __future__ import annotations

import collections
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GROUPS = ["cases", "entities", "timeline", "graph", "taxonomy",
          "counterarguments", "case_defaults"]

# Variable precision is authored, not derived. '1953', '2026-04' and '2026-08-04' all occur
# and must survive as strings. Coercing to a date type would silently promote month
# precision to day precision, which the design explicitly forbids.
DATE_RE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")


def fail(msg):
    sys.stderr.write("MERGE FAILED: %s\n" % msg)
    sys.exit(1)


def check_dates(node, path, problems):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "date" and isinstance(v, str) and not DATE_RE.match(v):
                problems.append("%s.date is not a valid partial ISO date: %r" % (path, v))
            check_dates(v, "%s.%s" % (path, k), problems)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            check_dates(v, "%s[%d]" % (path, i), problems)


def main():
    data = {}
    for group in GROUPS:
        with open(os.path.join(ROOT, "research", "%s.json" % group), encoding="utf-8") as fh:
            data[group] = json.load(fh)

    cases, ent, tax = data["cases"], data["entities"], data["taxonomy"]
    ids = {c["id"] for c in cases}
    problems = []

    inst_ids = {r["id"] for r in ent["INSTITUTIONS"]}
    loc_ids = {r["id"] for r in ent["LOCATIONS"]}
    dom_ids = {r["id"] for r in ent["DOMAINS"]}

    for case in cases:
        if case.get("instId") and case["instId"] not in inst_ids:
            problems.append("%s.instId %r does not resolve" % (case["id"], case["instId"]))
        if case.get("locId") and case["locId"] not in loc_ids:
            problems.append("%s.locId %r does not resolve" % (case["id"], case["locId"]))
        for d in case.get("domains", []):
            if d not in dom_ids:
                problems.append("%s.domains %r does not resolve" % (case["id"], d))
        if case.get("cluster") and case["cluster"] not in tax["CLUSTERS"]:
            problems.append("%s.cluster %r does not resolve" % (case["id"], case["cluster"]))
        if case.get("tier") not in tax["TIERS"]:
            problems.append("%s.tier %r does not resolve" % (case["id"], case.get("tier")))
        for axis in ("S", "P", "I"):
            v = case.get(axis)
            if not isinstance(v, int) or isinstance(v, bool) or not 0 <= v <= 3:
                problems.append("%s.%s is %r, expected an int 0 to 3" % (case["id"], axis, v))

    # ------------------------------------------------------------------------------
    # Source independence, and contested claims.
    # ------------------------------------------------------------------------------
    # Two related problems the tier system alone could not express.
    #
    # ONE: convergence is not the same as repetition. The tracker's strongest cases are
    # convergence-shaped, where no single source carries the claim but several independent
    # ones agree. The tracker also holds a worked example of FALSE convergence: the four
    # Oversight letters footnote eight press reports that look like several sources and
    # trace to one chain. Without a way to say "this source repeats that one", five
    # citations of one origin score exactly like five independent attestations, and the
    # weakest kind of evidence looks like the strongest.
    #
    # A source may therefore declare `derivedFrom`, naming the source it repeats. A claim's
    # independent support is the number of distinct ROOTS after following those pointers,
    # not the number of citations.
    #
    # TWO: a record could carry only one side of a disagreement and nothing would notice.
    # A claim may declare `contested`, attaching the competing account to the claim it
    # competes with rather than leaving it loose in the narrative or absent entirely.
    #
    # Neither field asserts who is right. That stays an editorial judgement; these only
    # make the shape of the evidence visible and checkable.
    for case in cases:
        for ci, claim in enumerate(case.get("claims", [])):
            where = "%s.claims[%d]" % (case["id"], ci)
            names = [src.get("name") for src in claim.get("sources", [])]
            if len(names) != len(set(names)):
                problems.append("%s cites the same source name twice, so independence "
                                "cannot be counted" % where)

            for src in claim.get("sources", []):
                parent = src.get("derivedFrom")
                if parent is None:
                    continue
                if parent == src.get("name"):
                    problems.append("%s: source %r derives from itself" % (where, parent))
                elif parent not in names:
                    problems.append("%s: source %r derivesFrom %r, which it does not cite"
                                    % (where, src.get("name"), parent))

            # A cycle would make independence uncomputable and loop the resolver.
            edges = {src["name"]: src.get("derivedFrom")
                     for src in claim.get("sources", []) if src.get("name")}
            for start in edges:
                seen, node = set(), start
                while node is not None and node in edges:
                    if node in seen:
                        problems.append("%s: derivedFrom cycle through %r" % (where, node))
                        break
                    seen.add(node)
                    node = edges[node]

            for k, entry in enumerate(claim.get("contested", [])):
                if not isinstance(entry, dict) or not entry.get("text"):
                    problems.append("%s.contested[%d] has no text" % (where, k))
                elif not entry.get("sources"):
                    problems.append("%s.contested[%d] cites no source, so it is an "
                                    "assertion rather than a competing account"
                                    % (where, k))

    # PHOTOS is derived from the case records rather than authored beside them. It used to
    # be its own file keyed by case id, which meant adding a case was two edits in two
    # places in two formats, and nothing checked that the second one happened. Deriving it
    # makes the pairing structural: a case cannot have a photo that belongs to no case, and
    # a missing photo is a missing key on the record rather than a silently absent row.
    #
    # The emitted block is keyed by id and the page only ever does PHOTOS[p.id], so the
    # order this produces (case order) is not the order the hand-authored file used and
    # that difference is not observable in the rendered page.
    photos = collections.OrderedDict()
    for case in cases:
        shot = case.get("photo")
        if shot is None:
            problems.append("%s has no photo" % case["id"])
            continue
        if not (isinstance(shot, list) and len(shot) == 2
                and all(isinstance(x, str) for x in shot)):
            problems.append("%s.photo is %r, expected [path, credit]" % (case["id"], shot))
            continue
        photos[case["id"]] = shot
    data["photos"] = photos
    for key in data["graph"]["IN_FBI"] + data["graph"]["IN_OVERSIGHT"]:
        if key not in ids:
            problems.append("membership list names unknown case %r" % key)

    check_dates(cases, "cases", problems)
    check_dates(data["timeline"], "timeline", problems)

    if problems:
        for p in problems:
            sys.stderr.write("  %s\n" % p)
        fail("%d cross reference or type problem(s)" % len(problems))

    os.makedirs(os.path.join(ROOT, "data"), exist_ok=True)
    out = os.path.join(ROOT, "data", "dataset.json")
    with open(out, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    print("merge OK  %d cases, %d nodes, %d timeline entries -> data/dataset.json"
          % (len(cases), len(cases) + len(inst_ids) + len(ent["PROGRAMS"])
             + len(loc_ids) + len(dom_ids), len(data["timeline"]["TIMELINE"])))


if __name__ == "__main__":
    main()
