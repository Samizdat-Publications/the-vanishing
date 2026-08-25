"""Gate A. Per block: emit from data, compare bytes to the original reference slice.

This is the working gate during the rebuild. It is fast, it runs per block, and when it
fails it says which block, which record and which keys, so a mismatch is diagnosable
rather than "the files differ somewhere in 325 KB".

Failures are classified before printing. Four classes are cosmetic. The fifth, VALUE,
means data was lost, and preventing exactly that is why this checkpoint exists.
"""

from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jsliteral
import emit_blocks
import extract as ex

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def classify(ref, got, name):
    """Name the failure mode rather than dumping a byte diff."""
    try:
        ref_val = ex.parse_block(name, ref)
        got_val = ex.parse_block(name, got)
    except Exception:
        return "PARSE", "emitted text does not parse back"
    if ref_val != got_val:
        return "VALUE", "DATA LOST: values differ after decoding"
    if json.dumps(ref_val, sort_keys=True, ensure_ascii=False) == \
       json.dumps(got_val, sort_keys=True, ensure_ascii=False) and ref_val != got_val:
        return "KEY_ORDER", "same keys, different order"
    ref_c, got_c = ref.replace(" ", "").replace("\n", ""), got.replace(" ", "").replace("\n", "")
    if ref_c == got_c:
        return "LINE_PACKING", "same tokens, different line breaks or spacing"
    return "STRING_ESCAPE", "values equal but spelled differently (escaping)"


def first_diff(ref, got):
    for i, (a, b) in enumerate(zip(ref, got)):
        if a != b:
            return i
    return min(len(ref), len(got))


def main():
    text = ex.check_provenance(ex.REFERENCE)
    with open(os.path.join(ROOT, "research", "case_defaults.json"), encoding="utf-8") as fh:
        defaults = json.load(fh)
    with open(os.path.join(ROOT, "research", "cases.json"), encoding="utf-8") as fh:
        cases = json.load(fh)

    data = {"cases": cases, "case_defaults": defaults}
    for group in ("entities", "timeline", "graph", "photos", "taxonomy"):
        with open(os.path.join(ROOT, "research", "%s.json" % group), encoding="utf-8") as fh:
            data[group] = json.load(fh)
    emitters = emit_blocks.build_emitters(data)

    passed, failed = 0, 0
    for name, emit in emitters.items():
        start, end = ex.locate(text, name)
        ref = text[start:end]
        got = emit()
        if ref == got:
            print("PASS  %-18s %d chars" % (name, len(ref)))
            passed += 1
            continue

        failed += 1
        kind, why = classify(ref, got, name)
        pos = first_diff(ref, got)
        line_no = ref.count("\n", 0, pos)
        ref_line = ref.split("\n")[line_no] if line_no < len(ref.split("\n")) else ""
        got_line = got.split("\n")[line_no] if line_no < len(got.split("\n")) else ""
        abs_line = text.count("\n", 0, start) + line_no + 1
        print("\nFAIL  %s  [%s] %s" % (name, kind, why))
        print("      reference line %d (block line %d)" % (abs_line, line_no))
        print("      ref  : %s" % ref_line[:150])
        print("      emit : %s" % got_line[:150])
        if kind == "VALUE":
            print("      *** STOP. This is a correctness bug, not a formatting bug. ***")

    print("\n%d passed, %d failed" % (passed, failed))
    return 2 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
