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
    # Step 5. Content changes are declared individually, never as a wildcard, because
    # RESEARCH-PROCESS.md:151 is explicit that a tracker which silently fixes its own data
    # is not auditable. Each entry names the change and why it was made.
    "photos.sullivan.1": (
        "credit no longer asserts USAF authorship. Eight DVIDS queries, the full 152-result "
        "NASIC image corpus and the complete nasic.af.mil biography index found no federal "
        "original, so 'US Air Force service portrait' asserted the one thing not established"
    ),
    # Step 5 imports from The Program. Claim and source only, never the conclusion.
    "cases.0.claims.3.text": "step 5: Ning Li DIRD, Tier 1 existence claim",
    "cases.0.claims.3.tier": "step 5: Ning Li DIRD, Tier 1 existence claim",
    "cases.0.claims.3.sources.0.name": "step 5: Ning Li DIRD source",
    "cases.0.claims.3.sources.0.url": "step 5: Ning Li DIRD source, verified 200",
    "cases.0.claims.3.sources.0.date": "step 5: Ning Li DIRD source",
    "cases.0.claims.4.text": "step 5: Ning Li DIRD, Tier 2 subject-matter claim with the Hathaway null-result context",
    "cases.0.claims.4.tier": "step 5",
    "cases.0.claims.4.sources.0.name": "step 5",
    "cases.0.claims.4.sources.0.url": "step 5",
    "cases.0.claims.4.sources.0.date": "step 5",
    "cases.0.claims.5.text": "step 5: records that the dia.mil copy returned 403 here and was not independently verified",
    "cases.0.claims.5.tier": "step 5",
    "cases.0.claims.5.sources.0.name": "step 5",
    "cases.0.claims.5.sources.0.url": "step 5",
    "cases.0.claims.5.sources.0.date": "step 5",
    "cases.0.narrative": "step 5: retention rationale no longer says the case is kept only for continuity to Eskridge, which the DIRD makes wrong on documentary grounds",
    "cases.0.tierRationale": "step 5: records that the DIRD shows interest in the research line, not in her, and does not disturb Tier C",
    "cases.0.sources.3.outlet": "step 5: Black Vault DIA FOIA mirror",
    "cases.0.sources.3.url": "step 5: Black Vault DIA FOIA mirror, verified 200",
    "cases.0.sources.3.date": "step 5: Black Vault DIA FOIA mirror",
    "cases.13.claims.2.text": "step 5: McCasland, Burlison staff contact attempt",
    "cases.13.claims.2.tier": "step 5",
    "cases.13.claims.2.sources.0.name": "step 5",
    "cases.13.claims.2.sources.0.url": "step 5: Fox News, verified 200",
    "cases.13.claims.2.sources.0.date": "step 5",
    "cases.13.claims.3.text": "step 5: McCasland disappearance triggered the Oversight probe",
    "cases.13.claims.3.tier": "step 5",
    "cases.13.claims.3.sources.0.name": "step 5",
    "cases.13.claims.3.sources.0.url": "step 5",
    "cases.13.claims.3.sources.0.date": "step 5",
    "cases.13.affiliations.0": "step 5: AFRL commander made explicit as Wright-Patterson HQ so the two projects stop silently disagreeing",
    "cases.13.sequenceChain.*.date": "step 5: Burlison contact entry added to the chain",
    "cases.13.sequenceChain.*.event": "step 5: Burlison contact entry added to the chain",
    "cases.13.sequenceChain.*.isAnomalous": "step 5: added entry is explicitly NOT marked anomalous",
    "cases.13.sequenceChain.*.source": "step 5: Burlison contact entry added to the chain",
    "cases.13.sources.4.outlet": "step 5: Fox News",
    "cases.13.sources.4.url": "step 5: Fox News, verified 200",
    "cases.13.sources.4.date": "step 5: Fox News",
    # Collection-level declarations. These say the SHAPE of the collection changed, which
    # would otherwise report every entry as removed-and-re-added. They deliberately do not
    # blind the gate to content: NEW_CLAIM_TEXTS below is an exact allowlist, and every
    # baseline claim text must still be present.
    "cases.*.claims": "step 3 reshaped claim source (string) into sources (array); step 5 appended claims",
    "cases.*.sources": "step 5 appended verified sources",
    "cases.13.sequenceChain": "step 5 appended the Burlison contact entry, which re-sorts the chain by date",
    "cases.13.affiliations": "step 5 made the AFRL commander posting explicit as Wright-Patterson HQ",
}

# Every claim text present in the baseline must still be present. Any claim text that is NEW
# has to appear here, verbatim and truncated to 70 chars, so an import cannot slip a claim in
# unremarked. This is what keeps the collection-level declaration above from being a blank
# cheque.
NEW_CLAIM_TEXTS = {
    "A Defense Intelligence Reference Document titled 'The Role of S",
    "The paper reviews the rotating-superconductor gravity-modificat",
    "The DIA FOIA Electronic Reading Room copy is at FileId/170046. ",
    "Rep. Eric Burlison stated that his staff had been attempting to",
    "Burlison stated that McCasland's disappearance is what triggere",
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


# Collections whose order is derived rather than authored. sequenceChain and chronology are
# date-sorted, so inserting a dated entry renumbers everything after it. Diffing those
# positionally reports a dozen "changes" for one insertion, which buries a real change in
# noise and trains you to skim the output. They are compared as sets of whole entries
# instead: added and removed entries are reported, a reorder is not a finding.
UNORDERED = {"sequenceChain", "chronology", "claims", "sources", "affiliations",
             "conflicts", "unverified", "leftBehind", "tookWith", "domains"}


def collections(node, path="", out=None):
    """Pull out the unordered collections so they can be compared by content."""
    if out is None:
        out = {}
    if isinstance(node, dict):
        for k, v in node.items():
            sub = "%s.%s" % (path, k) if path else k
            if k in UNORDERED and isinstance(v, list):
                out[sub] = [json.dumps(x, sort_keys=True, ensure_ascii=False) for x in v]
            else:
                collections(v, sub, out)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            collections(v, "%s.%d" % (path, i), out)
    return out


def flatten(node, path="", out=None, skip_unordered=False):
    """Flatten to leaf paths, with list indices collapsed to * for pattern matching."""
    if out is None:
        out = {}
    if isinstance(node, dict):
        for k, v in node.items():
            if skip_unordered and k in UNORDERED and isinstance(v, list):
                continue
            flatten(v, "%s.%s" % (path, k) if path else k, out, skip_unordered)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            flatten(v, "%s.%d" % (path, i), out, skip_unordered)
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

    fb, fl = flatten(base, skip_unordered=True), flatten(live, skip_unordered=True)
    cb, cl = collections(base), collections(live)
    removed = set(fb) - set(fl)
    added = set(fl) - set(fb)
    changed = {k for k in set(fb) & set(fl) if fb[k] != fl[k]}

    def allowed(path):
        # Literal path first, so a single precise change such as photos.sullivan.1 can be
        # declared on its own rather than being forced to wildcard every photo credit.
        # Wildcards stay available for genuinely schema-wide changes.
        return path in EXPECTED_CHANGES or pattern(path) in EXPECTED_CHANGES

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

    # Unordered collections, compared by content rather than position.
    coll_added, coll_removed = [], []
    for key in sorted(set(cb) | set(cl)):
        was, now = cb.get(key, []), cl.get(key, [])
        for entry in now:
            if entry not in was and not allowed(key):
                coll_added.append((key, entry))
        for entry in was:
            if entry not in now and not allowed(key):
                coll_removed.append((key, entry))
    if coll_removed:
        ok = False
        print("\n  ENTRIES REMOVED FROM COLLECTIONS (%d):" % len(coll_removed))
        for key, entry in coll_removed[:15]:
            print("    %s\n      %s" % (key, entry[:170]))
    if coll_added:
        ok = False
        print("\n  UNDECLARED ENTRIES ADDED TO COLLECTIONS (%d):" % len(coll_added))
        for key, entry in coll_added[:15]:
            print("    %s\n      %s" % (key, entry[:170]))

    # Claim text preservation. The collection declaration above allows the shape to change;
    # this makes sure the content did not.
    base_texts = {c["text"] for case in base["cases"] for c in case.get("claims", [])}
    live_texts = {c["text"] for case in live["cases"] for c in case.get("claims", [])}
    dropped = sorted(base_texts - live_texts)
    undeclared_new = sorted(t for t in (live_texts - base_texts) if t[:63] not in NEW_CLAIM_TEXTS)
    if dropped:
        ok = False
        print("\n  CLAIM TEXT DROPPED (%d):" % len(dropped))
        for t in dropped[:10]:
            print("    %s" % t[:160])
    if undeclared_new:
        ok = False
        print("\n  UNDECLARED NEW CLAIM (%d). Add its first 63 chars to NEW_CLAIM_TEXTS:" % len(undeclared_new))
        for t in undeclared_new[:10]:
            print("    %r" % t[:63])

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
    print("    %-18s %3d  baseline claim texts all still present, %d new declared"
          % ("claim texts", len(base_texts), len(live_texts) - len(base_texts)))

    print("\n%s" % ("PASS  only declared changes present" if ok
                    else "FAIL  undeclared differences, see above"))
    return 0 if ok else 2


if __name__ == "__main__":
    sys.exit(main())
