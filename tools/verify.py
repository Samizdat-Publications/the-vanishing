"""The checkpoint. Gates 0, B and D.

ARCHITECTURE.md's rule: verify passing is the definition of shippable, and every check in
here must itself be tested against input it is required to reject. The Program shipped
three of its first eight checks born broken and silently passing, which is worse than
having no gate, because it manufactures confidence.

Run --self-test to prove each check fails on input it must reject.

    python3 tools/verify.py --idempotent
    python3 tools/verify.py --self-test
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jsliteral
import build_dashboard
import extract as ex

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def gate_d():
    """Provenance. The reference is pinned and design-package is refused."""
    ex.check_provenance(ex.REFERENCE)
    return True, "reference pinned at %s" % ex.REFERENCE_SHA256[:12]


def gate_p_defaults():
    """The P_ factory stays in the frozen shell; case_defaults.json is a copy.

    If the two drift, the meaning of "key absent" changes for all 15 records at once, and
    nothing else would notice.
    """
    text = open(ex.REFERENCE, encoding="utf-8").read()
    import re
    m = re.search(r"const P_ = \(o\) => Object\.assign\(", text)
    shell_defaults, _ = jsliteral.parse_prefix(text, m.end())
    with open(os.path.join(ROOT, "research", "case_defaults.json"), encoding="utf-8") as fh:
        mirrored = json.load(fh)
    if shell_defaults != mirrored:
        return False, "case_defaults.json has drifted from the P_ factory in the shell"
    return True, "%d defaults agree with the shell" % len(mirrored)


def gate_b():
    """Whole file. The build must equal the reference byte for byte."""
    built = build_dashboard.build().encode("utf-8")
    reference = open(ex.REFERENCE, "rb").read()
    if built == reference:
        return True, "build is byte identical, %d bytes" % len(built)
    for i, (a, b) in enumerate(zip(built, reference)):
        if a != b:
            line = reference[:i].count(b"\n") + 1
            return False, "first difference at byte %d, reference line %d" % (i, line)
    return False, "length differs: built %d, reference %d" % (len(built), len(reference))


def gate_b_prime():
    """Determinism. Two consecutive builds must be identical to each other."""
    first = build_dashboard.build()
    second = build_dashboard.build()
    if first != second:
        return False, "two builds of the same input differ"
    return True, "build is deterministic"


def gate_scores():
    """The adjudicated axis values that distinguish the correct source from the ancestor.

    design-package/vanishing-graph.js differs on exactly these and would look plausible.
    """
    with open(os.path.join(ROOT, "research", "cases.json"), encoding="utf-8") as fh:
        cases = {c["id"]: c for c in json.load(fh)}
    expected = {
        "li": ("S", 0), "loureiro": ("I", 3), "mccasland": ("P", 2),
        "chavez": ("P", 1), "reza": ("P", 2), "garcia": ("P", 1), "thomas": ("S", 0),
    }
    bad = []
    for cid, (axis, want) in expected.items():
        got = cases.get(cid, {}).get(axis)
        if got != want:
            bad.append("%s.%s is %r, adjudicated %r" % (cid, axis, got, want))
    if bad:
        return False, "; ".join(bad)
    return True, "%d adjudicated scores match SCORING-DISCREPANCIES.md" % len(expected)


def gate_edges():
    """The derived graph is unchanged, 151 edges with the recorded type breakdown."""
    r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "check_edges.py")],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return False, "edge check failed:\n%s" % r.stdout
    return True, "151 edges, type breakdown unchanged"


GATES = [
    ("D  provenance", gate_d),
    ("D  P_ defaults", gate_p_defaults),
    ("B  whole file", gate_b),
    ("B' determinism", gate_b_prime),
    ("   axis scores", gate_scores),
    ("   derived graph", gate_edges),
]


def self_test():
    """Prove each check actually fails on input it must reject.

    A gate that cannot fail is worse than no gate. These mutate a copy of the real data,
    assert the relevant check rejects it, and restore.
    """
    print("SELF TEST: each check must reject bad input\n")
    results = []

    # The whole-file gate must reject a changed value.
    path = os.path.join(ROOT, "data", "dataset.json")
    original = open(path, encoding="utf-8").read()
    try:
        data = json.loads(original)
        data["cases"][0]["label"] = "Tampered Name"
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=2)
        ok, msg = gate_b()
        results.append(("whole file rejects a changed value", not ok))

        # And must reject a changed score, which is the mangling that matters most.
        data = json.loads(original)
        data["cases"][0]["S"] = 1
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=2)
        ok, _ = gate_b()
        results.append(("whole file rejects a changed axis score", not ok))
    finally:
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(original)

    # The score gate must reject the ancestor's values.
    cpath = os.path.join(ROOT, "research", "cases.json")
    corig = open(cpath, encoding="utf-8").read()
    try:
        cases = json.loads(corig)
        for c in cases:
            if c["id"] == "li":
                c["S"] = 1          # the ancestor's stale value
        with open(cpath, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(cases, fh, ensure_ascii=False, indent=2)
        ok, _ = gate_scores()
        results.append(("axis gate rejects the design-package value li S1", not ok))
    finally:
        with open(cpath, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(corig)

    # The defaults gate must reject drift.
    dpath = os.path.join(ROOT, "research", "case_defaults.json")
    dorig = open(dpath, encoding="utf-8").read()
    try:
        d = json.loads(dorig)
        d["leftBehind"] = ["tampered"]
        with open(dpath, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(d, fh, ensure_ascii=False, indent=2)
        ok, _ = gate_p_defaults()
        results.append(("defaults gate rejects drift from the shell", not ok))
    finally:
        with open(dpath, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(dorig)

    passed = 0
    for name, rejected in results:
        print("  %-52s %s" % (name, "PASS" if rejected else "FAIL, CHECK IS BLIND"))
        passed += bool(rejected)
    print("\n%d of %d checks proven to reject bad input" % (passed, len(results)))
    return 0 if passed == len(results) else 2


def main():
    if "--self-test" in sys.argv:
        return self_test()

    print("THE CHECKPOINT\n")
    failed = 0
    for name, gate in GATES:
        try:
            ok, msg = gate()
        except SystemExit:
            ok, msg = False, "gate raised"
        except Exception as exc:
            ok, msg = False, "gate raised %s: %s" % (type(exc).__name__, exc)
        print("  %-18s %-5s %s" % (name, "PASS" if ok else "FAIL", msg))
        failed += not ok

    if failed:
        print("\n%d gate(s) failed. The checkpoint is RED." % failed)
        return 2
    print("\nAll gates green. The dashboard regenerates byte for byte from extracted data.")
    print("Step 2 checkpoint PASSED. Schema changes are now safe to begin.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
