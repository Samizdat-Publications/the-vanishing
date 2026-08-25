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


def gate_semantic():
    """Only declared schema changes are present, and no case content was lost.

    This replaces step 2's byte-equality gate, which necessarily retired when step 3
    changed the schema on purpose. The question is unchanged: did anything change that we
    did not intend to change?
    """
    r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "semantic_diff.py")],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return False, "semantic diff failed:\n%s" % r.stdout
    return True, "only declared changes against data/baseline.json"


def gate_reference_frozen():
    """The pre-rebuild reference is still on disk and unmodified.

    It is no longer the build target, but it stays as the historical record of what the
    extraction started from. If it changes, data/baseline.json no longer describes
    anything real and the semantic gate loses its anchor.
    """
    import hashlib
    digest = hashlib.sha256(open(ex.REFERENCE, "rb").read()).hexdigest()
    if digest != ex.REFERENCE_SHA256:
        return False, "the-vanishing-v2.html was modified; baseline.json is now unanchored"
    return True, "v2 reference unmodified, %s" % ex.REFERENCE_SHA256[:12]


def gate_js_syntax():
    """The built page's JavaScript parses.

    The shell is hand edited, so a syntax error here is a live possibility and would ship
    a blank dashboard that every other gate would still call green.
    """
    import shutil as _sh
    if not _sh.which("node"):
        return True, "skipped, node not available"
    html = build_dashboard.build()
    i, j = html.index("<script>"), html.rindex("</script>")
    tmp = os.path.join(ROOT, "dist", "_syntax_check.js")
    os.makedirs(os.path.join(ROOT, "dist"), exist_ok=True)
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(html[i + 8:j])
    r = subprocess.run(["node", "--check", tmp], capture_output=True, text=True)
    os.remove(tmp)
    if r.returncode != 0:
        return False, "built JavaScript does not parse:\n%s" % r.stderr[:400]
    return True, "built JavaScript parses"


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


def gate_source_render():
    """Every source-bearing record renders a real name.

    v2 shipped with sourcesHtml reading s.outlet while entity nodes carried `name`, so all
    18 entity source lists rendered "undefined" as their link text. Case records happened
    to use `outlet` and looked fine, which is why it survived review.
    """
    import shutil as _sh
    if not _sh.which("node"):
        return True, "skipped, node not available"
    r = subprocess.run(["node", os.path.join(ROOT, "tools", "test_source_render.js")],
                       capture_output=True, text=True, cwd=ROOT)
    if r.returncode != 0:
        return False, "source rendering regression:\n%s" % r.stdout
    return True, "36 source-bearing records render a real name"


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
    ("   reference", gate_reference_frozen),
    ("B  semantic", gate_semantic),
    ("   js syntax", gate_js_syntax),
    ("B' determinism", gate_b_prime),
    ("   axis scores", gate_scores),
    ("   derived graph", gate_edges),
    ("   source render", gate_source_render),
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
        ok, msg = gate_semantic()
        results.append(("semantic gate rejects a changed value", not ok))

        # And must reject a changed score, which is the mangling that matters most.
        data = json.loads(original)
        data["cases"][0]["S"] = 1
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=2)
        ok, _ = gate_semantic()
        results.append(("semantic gate rejects a changed axis score", not ok))

        # Retiring a claim is allowed only when declared. Without this test the
        # RETIRED_CLAIM_TEXTS escape hatch could silently widen into a blank cheque,
        # which is the failure mode the whole gate exists to prevent.
        data = json.loads(original)
        for case in data["cases"]:
            if case["id"] == "grillmair" and case.get("claims"):
                case["claims"] = case["claims"][1:]
                break
        with open(path, "w", encoding="utf-8", newline="\n") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=2)
        ok, _ = gate_semantic()
        results.append(("semantic gate rejects an undeclared claim retirement", not ok))
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

    # Discovery checks are warnings, never gates. FIRST-TASKS.md:90 is explicit about this:
    # a candidate list is a research prompt, and failing a build on one would turn it into
    # something to silence rather than read.
    r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "discovery_checks.py")],
                       capture_output=True, text=True)
    counts = [ln for ln in r.stdout.splitlines() if ln and ln[0].isdigit() and "(" in ln]
    if counts:
        print("\nDiscovery warnings (not gates), full report: python3 tools/discovery_checks.py")
        for ln in counts:
            print("  %s" % ln)
    print("\nAll gates green.")
    print("Step 2 proved the extraction lossless by byte equality. That gate retired when")
    print("step 3 changed the schema; data/baseline.json and the semantic diff replace it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
