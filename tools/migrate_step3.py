"""One-time step 3 migration: add the outcome field, convert claim sources to arrays.

Two changes, both deliberately conservative.

**outcome sits beside status, it does not replace it.** status is a factual disposition
that drives the UI (STATUS_LABEL: dead / missing / resolved). outcome is the analytic
dimension THESIS-NOTES proposes, whose whole purpose is to make the neutralisation frame
visible and checkable rather than baked silently into the axis scores. Collapsing a fact
into an interpretation is exactly what the frame's falsifiability problem warns against,
so they stay separate.

**Every case's outcome is seeded from its status and nothing more.** The novel values the
frame introduces (incapacitated, discredited, career-terminated) are NOT assigned here.
Assigning one is a research finding that needs a documented basis, in the same way an axis
score does. The field exists so those findings have somewhere to live; inventing them
during a mechanical migration would be the frame putting a thumb on the data, which
THESIS-NOTES:103 forbids.

**Claim sources become arrays, preserving the original string verbatim.** The existing
`source` is free text such as 'PolitiFact, April 28 2026'. Parsing that into structured
name and date would mean guessing, and a wrong guess here manufactures a citation. The
string is carried across unchanged as a single entry's name, so the shape is right and no
content is invented. Enriching individual entries with verified URLs is later research
work, not a migration.

    python3 tools/migrate_step3.py
"""

from __future__ import annotations

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CASES = os.path.join(ROOT, "research", "cases.json")

# THESIS-NOTES:89-101. status is a strict subset; the last three are the frame's additions
# and are populated only by sourced research, never by this migration.
VALID_OUTCOMES = {
    "dead", "missing", "resolved",
    "incapacitated", "discredited", "career-terminated",
}


def main():
    with open(CASES, encoding="utf-8") as fh:
        cases = json.load(fh)

    outcome_added = claims_converted = 0
    for case in cases:
        if "outcome" not in case:
            # Seeded from status. Nothing inferred.
            case["outcome"] = case["status"]
            outcome_added += 1
        if case["outcome"] not in VALID_OUTCOMES:
            sys.exit("FATAL: %s has invalid outcome %r" % (case["id"], case["outcome"]))

        for claim in case.get("claims", []):
            if "source" in claim and "sources" not in claim:
                # Verbatim carry-across. No parsing, no invented structure.
                claim["sources"] = [{"name": claim.pop("source")}]
                claims_converted += 1

        # Rebuild in a stable key order so outcome sits next to status rather than at the
        # end. Key order is data in this project, so it is set deliberately, not sorted.
        ordered = {}
        for key in ("id", "label", "status", "outcome", "date", "age"):
            if key in case:
                ordered[key] = case[key]
        for key in case:
            if key not in ordered:
                ordered[key] = case[key]
        case.clear()
        case.update(ordered)

    with open(CASES, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(cases, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    print("migrated %d cases" % len(cases))
    print("  outcome added to %d" % outcome_added)
    print("  claim sources converted to arrays: %d" % claims_converted)
    print("\noutcome distribution (seeded from status, nothing inferred):")
    dist = {}
    for c in cases:
        dist[c["outcome"]] = dist.get(c["outcome"], 0) + 1
    for k, v in sorted(dist.items()):
        print("  %-18s %d" % (k, v))
    print("\nNot assigned by this migration, and correctly so: incapacitated,")
    print("discredited, career-terminated. Each needs a sourced finding.")


if __name__ == "__main__":
    main()
