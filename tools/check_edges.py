"""Reimplements deriveEdges() in Python and asserts the graph is unchanged.

While the byte gate is green this check is redundant. It earns its place the moment step 3
starts changing bytes deliberately, because it is the tripwire for the one change that
would otherwise be invisible: normalizing the leftBehind vocabulary.

The behavioural rule is exact string match on free text. 'phone', 'phones' and 'iPhone' are
three tokens for one concept and deliberately do not match. Tidying them silently adds
edges and changes the rendered map, which is exactly the kind of quiet mangling the
checkpoint exists to prevent.

    python3 tools/check_edges.py
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXPECTED_TOTAL = 151
EXPECTED_BY_TYPE = {
    "institutional": 19, "geographic": 42, "research": 44, "investigative": 16,
    "temporal": 11, "behavioral": 10, "witness-chain": 3, "programmatic": 6,
}


def days(a, b):
    """Mirror of the source's days(). Bare 'YYYY-MM' parses as the first of the month in
    V8, so the Python side pads the same way rather than 'improving' on it."""
    def parse(s):
        parts = s.split("-")
        while len(parts) < 3:
            parts.append("01")
        return datetime(int(parts[0]), int(parts[1]), int(parts[2]))
    return abs((parse(a) - parse(b)).days)


def derive(data):
    people = data["cases"]
    graph = data["graph"]
    window = graph["TEMPORAL_WINDOW_DAYS"]
    out = []

    for p in people:
        if p.get("instId"):
            out.append((p["id"], p["instId"], "institutional"))
        if p.get("locId"):
            out.append((p["id"], p["locId"], "geographic"))
        for d in p.get("domains", []):
            out.append((p["id"], d, "research"))
    for inst, place in graph["INSTITUTION_PLACES"]:
        out.append((inst, place, "geographic"))
    for cid in graph["IN_FBI"]:
        out.append((cid, "fbi", "investigative"))
    for cid in graph["IN_OVERSIGHT"]:
        out.append((cid, "oversight", "investigative"))

    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            a, b = people[i], people[j]
            if a.get("instId") and a.get("instId") == b.get("instId"):
                out.append((a["id"], b["id"], "institutional"))
            if a.get("cluster") == b.get("cluster") and a.get("cluster") != "other":
                out.append((a["id"], b["id"], "geographic"))
            if any(d in b.get("domains", []) for d in a.get("domains", [])):
                out.append((a["id"], b["id"], "research"))
            if days(a["date"], b["date"]) <= window:
                out.append((a["id"], b["id"], "temporal"))
            if any(x in b.get("leftBehind", []) for x in a.get("leftBehind", [])):
                out.append((a["id"], b["id"], "behavioral"))

    for e in graph["PROGRAM_EDGES"]:
        out.append((e["a"], e["b"], e["type"]))
    return out


def main():
    with open(os.path.join(ROOT, "data", "dataset.json"), encoding="utf-8") as fh:
        data = json.load(fh)
    edges = derive(data)
    counts = {}
    for _, _, t in edges:
        counts[t] = counts.get(t, 0) + 1

    ok = True
    if len(edges) != EXPECTED_TOTAL:
        print("FAIL  total %d, expected %d" % (len(edges), EXPECTED_TOTAL))
        ok = False
    for t, want in sorted(EXPECTED_BY_TYPE.items()):
        got = counts.get(t, 0)
        flag = "ok" if got == want else "MISMATCH"
        if got != want:
            ok = False
        print("  %-14s %3d  expected %3d  %s" % (t, got, want, flag))
    for t in sorted(set(counts) - set(EXPECTED_BY_TYPE)):
        print("  %-14s %3d  UNEXPECTED TYPE" % (t, counts[t]))
        ok = False

    print("\n%s  %d edges" % ("PASS" if ok else "FAIL", len(edges)))
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
