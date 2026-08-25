"""Compare the live dataset against the frozen semantic baseline.

Step 2's gate was byte equality against the hand-authored HTML. Step 3 changes the schema
on purpose, so that gate necessarily retires. This replaces it.

The question this answers is the one the byte gate answered: **did anything change that we
did not intend to change?** Intended changes are declared in EXPECTED_CHANGES. Anything
else is reported as an unexpected difference and fails the gate.

    python3 tools/semantic_diff.py
"""

from __future__ import annotations

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Keys that step 3 deliberately adds or reshapes. Everything else must be untouched.
# Removing an entry from here re-tightens the gate, which is the point: the list should
# shrink back toward empty once a migration has landed and been reviewed.
EXPECTED_CHANGES = {
    "cases.*.outcome": "step 3 adds the outcome field beside status",
    "cases.*.claims.*.sources.*.name": "step 3 converts claim source (string) to sources (array)",
    "cases.*.claims.*.sources.*.url": "step 3 claim sources may carry a verified url",
    "cases.*.claims.*.sources.*.date": "step 3 claim sources may carry a publication date",
    "cases.*.claims.*.source": "step 3 converts claim source (string) to sources (array)",
}

# Invariants that must hold no matter what the schema does. These are the facts the
# project would be wrong about if they silently changed.
INVARIANTS = {
    "case count": 15,
    "timeline entries": 42,
    "precedents": 4,
    "photos": 15,
    "programme edges": 10,
}


def flatten(node, path="", out=None):
    """Flatten to leaf paths, with list indices collapsed to * for pattern matching."""
    if out is None:
        out = {}
    if isinstance(node, dict):
        for k, v in node.items():
            flatten(v, "%s.%s" % (path, k) if path else k, out)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            flatten(v, "%s.%d" % (path, i), out)
    else:
        out[path] = node
    return out


def pattern(path):
    """Collapse numeric path segments so cases.3.claims.1.text -> cases.*.claims.*.text."""
    return ".".join("*" if seg.isdigit() else seg for seg in path.split("."))


def main():
    with open(os.path.join(ROOT, "data", "baseline.json"), encoding="utf-8") as fh:
        base = json.load(fh)
    with open(os.path.join(ROOT, "data", "dataset.json"), encoding="utf-8") as fh:
        live = json.load(fh)

    fb, fl = flatten(base), flatten(live)
    removed = set(fb) - set(fl)
    added = set(fl) - set(fb)
    changed = {k for k in set(fb) & set(fl) if fb[k] != fl[k]}

    def allowed(path):
        return pattern(path) in EXPECTED_CHANGES

    bad_removed = sorted(p for p in removed if not allowed(p))
    bad_added = sorted(p for p in added if not allowed(p))
    bad_changed = sorted(p for p in changed if not allowed(p))

    print("SEMANTIC DIFF against data/baseline.json\n")
    print("  expected schema changes declared: %d pattern(s)" % len(EXPECTED_CHANGES))
    print("  leaf values: %d baseline, %d live" % (len(fb), len(fl)))
    print("  added %d, removed %d, changed %d (before filtering)"
          % (len(added), len(removed), len(changed)))

    ok = True
    for label, items in (("UNEXPECTEDLY REMOVED", bad_removed),
                         ("UNEXPECTEDLY ADDED", bad_added),
                         ("UNEXPECTEDLY CHANGED", bad_changed)):
        if items:
            ok = False
            print("\n  %s (%d):" % (label, len(items)))
            for p in items[:25]:
                if label == "UNEXPECTEDLY CHANGED":
                    print("    %s\n      was: %r\n      now: %r" % (p, fb[p], fl[p]))
                else:
                    print("    %s" % p)
            if len(items) > 25:
                print("    ... and %d more" % (len(items) - 25))

    print("\n  invariants:")
    actual = {
        "case count": len(live["cases"]),
        "timeline entries": len(live["timeline"]["TIMELINE"]),
        "precedents": len(live["timeline"]["PRECEDENT"]),
        "photos": len(live["photos"]),
        "programme edges": len(live["graph"]["PROGRAM_EDGES"]),
    }
    for name, want in INVARIANTS.items():
        got = actual[name]
        if got != want:
            ok = False
        print("    %-18s %3d  expected %3d  %s" % (name, got, want, "ok" if got == want else "MISMATCH"))

    # Axis scores are the thing this project would be most damaged by losing quietly.
    bl = {c["id"]: (c["S"], c["P"], c["I"], c["tier"]) for c in base["cases"]}
    lv = {c["id"]: (c["S"], c["P"], c["I"], c["tier"]) for c in live["cases"]}
    drift = [cid for cid in bl if bl.get(cid) != lv.get(cid)]
    if drift:
        ok = False
        print("\n  AXIS SCORE DRIFT:")
        for cid in drift:
            print("    %-12s was %s  now %s" % (cid, bl[cid], lv.get(cid)))
    else:
        print("    %-18s %3d  all S/P/I/tier unchanged" % ("axis scores", len(bl)))

    # The claim source conversion must be lossless. A migration that quietly rewords a
    # citation is the exact failure this project cannot afford, so compare the old string
    # against the new first entry's name rather than trusting the shapes to line up.
    lost = []
    for b_case, l_case in zip(base["cases"], live["cases"]):
        for b_claim, l_claim in zip(b_case.get("claims", []), l_case.get("claims", [])):
            old = b_claim.get("source")
            if old is None:
                continue
            new = (l_claim.get("sources") or [{}])[0].get("name")
            if old != new:
                lost.append("%s: %r -> %r" % (b_case["id"], old, new))
    if lost:
        ok = False
        print("\n  CLAIM SOURCE TEXT ALTERED (%d):" % len(lost))
        for line in lost[:10]:
            print("    %s" % line)
    else:
        n = sum(len(c.get("claims", [])) for c in base["cases"])
        print("    %-18s %3d  every claim source string preserved verbatim" % ("claim sources", n))

    print("\n%s" % ("PASS  only declared changes present" if ok
                    else "FAIL  undeclared differences, see above"))
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
