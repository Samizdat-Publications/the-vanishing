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

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GROUPS = ["cases", "entities", "timeline", "graph", "photos", "taxonomy", "case_defaults"]

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

    for key in data["photos"]:
        if key not in ids:
            problems.append("PHOTOS key %r is not a case id" % key)
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
