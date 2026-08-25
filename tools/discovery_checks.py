"""DISCOVERY-PROTOCOL.md section 3, automated. WARNINGS, never failures.

The protocol was written after a named recall failure: the old process searched victims and
institutions by name, so it structurally could not reach actors, mechanisms or precedents.
Doty was missed because no query pointed anywhere near him. These four checks are the
mechanical part of the fix, turning presence-only checking into something that also asks
what is missing.

They are warnings by design, per FIRST-TASKS.md:90. A candidate list is a research prompt,
not a defect. Failing a build because a narrative mentions an untracked name would make the
check something to silence rather than read.

**What these cannot do.** They read the corpus the project already has. They cannot find
what it does not contain, and six axes is a heuristic rather than proof of coverage. The
protocol says so itself, and these checks do not change that.

    python3 tools/discovery_checks.py
    python3 tools/discovery_checks.py --self-test
"""

from __future__ import annotations

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Capitalised multi-word sequences that are not people. Kept explicit rather than clever,
# because a stoplist that silently swallows a real name defeats the check.
NOT_PEOPLE = {
    "Los Alamos", "New Mexico", "National Forest", "Carson National", "Angeles National",
    "United States", "Air Force", "Space Force", "National Security", "Medical Examiner",
    "Medical Investigator", "State Police", "Sheriff", "County Sheriff", "Police Department",
    "Kansas City", "Huntsville International", "Walker County", "Union County",
    "Deep Space", "Jet Propulsion", "Propulsion Laboratory", "National Laboratory",
    "Research Laboratory", "Twin Towers", "Antelope Valley", "Superior Court",
    "District Attorney", "Public Affairs", "Wright Patterson", "Falls Church",
    "Plasma Science", "Fusion Center", "Materials Processing", "Security Campus",
    "House Oversight", "Congressional", "Committee", "Department", "University",
    "Institute", "Laboratory", "Center", "Centre", "Bureau", "Agency", "Office",
}

# Instrument-shaped tokens: document numbers, docket numbers, case references.
INSTRUMENT_PATTERNS = [
    (r"\b[A-Z]{2,4}-\d{2}-\d{3,4}-\d{2,4}\b", "document number"),
    (r"\b\d{2}[A-Z]{2,5}\d{4,6}\b", "court case number"),
    (r"\b[A-Z]{3,6}\s\d{4}-\d{1,3}\b", "agency case reference"),
    (r"\bPublic Law \d+-\d+\b", "statute"),
    (r"\b\d+\s+U\.S\.C\.\s+\d+\b", "statute"),
]

# Fields every case ought to be able to answer. Absence is the negative-space report.
EXPECTED_COVERAGE = {
    "investigating agency": r"police|sheriff|FBI|state police|deputies|investigat|detective|NTSB|OMI|medical examiner|medical investigator",
    "cause or manner": r"cause|manner|autopsy|ruled|undetermined|overdose|gunshot|natural causes|no cause",
    "employer": r"",  # structural, checked via instId rather than prose
}

# Single spaces only. \s would span newlines and glue the end of one field to the start
# of the next, manufacturing names like "Alabama Standalone" that nobody wrote.
NAME_RE = re.compile(r"\b[A-Z][a-z]+(?:[ ](?:[A-Z]\.|[A-Z][a-z]+)){1,2}\b")


def load():
    with open(os.path.join(ROOT, "data", "dataset.json"), encoding="utf-8") as fh:
        return json.load(fh)


def case_text(case):
    """All prose on a record, so a name mentioned anywhere is reachable."""
    parts = [case.get("narrative", ""), case.get("tierRationale", ""),
             case.get("unexplainedResidual") or "", case.get("sub", "")]
    parts += case.get("conflicts", []) + case.get("unverified", []) + case.get("affiliations", [])
    for coll in ("sequenceChain", "chronology"):
        parts += [x.get("event", "") for x in case.get(coll, [])]
    parts += [c.get("text", "") for c in case.get("claims", [])]
    return "\n".join(p for p in parts if p)


def known_names(data):
    known = set()
    for c in data["cases"]:
        known.add(c["label"])
        for tok in c["label"].split():
            known.add(tok)
    for group in ("INSTITUTIONS", "PROGRAMS", "LOCATIONS", "DOMAINS"):
        for r in data["entities"][group]:
            known.add(r.get("label", ""))
            for tok in r.get("label", "").split():
                known.add(tok)
    return known


def check_actors(data):
    """Untracked people named in narratives. Candidate actor list."""
    known = known_names(data)
    found = {}
    for case in data["cases"]:
        for m in NAME_RE.finditer(case_text(case)):
            name = m.group(0)
            if name in known or name in NOT_PEOPLE:
                continue
            if any(part in NOT_PEOPLE for part in [name.rsplit(" ", 1)[0]]):
                continue
            if any(tok in known for tok in name.split() if len(tok) > 3):
                continue
            found.setdefault(name, set()).add(case["id"])
    return found


def check_instruments(data):
    """Document, docket and case numbers in prose but not in structured data."""
    found = {}
    for case in data["cases"]:
        text = case_text(case)
        for pattern, kind in INSTRUMENT_PATTERNS:
            for m in re.finditer(pattern, text):
                found.setdefault((m.group(0), kind), set()).add(case["id"])
    return found


def check_negative_space(data):
    """Which cases cannot answer a question every case ought to answer."""
    gaps = {}
    for case in data["cases"]:
        text = case_text(case).lower()
        missing = []
        for field, pattern in EXPECTED_COVERAGE.items():
            if field == "employer":
                if not case.get("instId"):
                    missing.append(field)
                continue
            if not re.search(pattern, text, re.I):
                missing.append(field)
        if not case.get("sources"):
            missing.append("sources")
        if missing:
            gaps[case["id"]] = missing
    return gaps


def check_adjacency(data, actors):
    """Names appearing in more than one case narrative. Cross-case actor candidates."""
    return {n: ids for n, ids in actors.items() if len(ids) > 1}


def run(verbose=True):
    data = load()
    actors = check_actors(data)
    instruments = check_instruments(data)
    gaps = check_negative_space(data)
    adjacency = check_adjacency(data, actors)
    doc_drift = check_doc_scores(data)

    if verbose:
        print("DISCOVERY CHECKS  (warnings, not failures)\n")

        print("1. Candidate actors, named in a narrative and not tracked (%d)" % len(actors))
        for name, ids in sorted(actors.items(), key=lambda kv: (-len(kv[1]), kv[0]))[:20]:
            print("   %-32s %s" % (name, ", ".join(sorted(ids))))
        if len(actors) > 20:
            print("   ... and %d more" % (len(actors) - 20))

        print("\n2. Candidate instruments, referenced in prose (%d)" % len(instruments))
        for (token, kind), ids in sorted(instruments.items()):
            print("   %-26s %-20s %s" % (token, kind, ", ".join(sorted(ids))))

        print("\n3. Negative space, cases that cannot answer an expected question (%d)"
              % len(gaps))
        for cid, missing in sorted(gaps.items()):
            print("   %-12s missing: %s" % (cid, ", ".join(missing)))
        if not gaps:
            print("   none. Every case names an investigating agency, a cause and an employer.")

        print("\n4. Adjacency, a name in more than one case (%d)" % len(adjacency))
        for name, ids in sorted(adjacency.items(), key=lambda kv: -len(kv[1])):
            print("   %-32s %s" % (name, ", ".join(sorted(ids))))
        if not adjacency:
            print("   none.")

        print("\n5. Documentation drift: S/P/I in prose disagreeing with the data (%d)"
              % len(doc_drift))
        for fname, n, cid, got, want in doc_drift:
            print("   %s:%d  %-12s says %s, data says %s" % (fname, n, cid, got, want))
        if not doc_drift:
            print("   none. Every scored triple in the prose files matches the data.")

        print("\nThese are research prompts, not defects. Anything worth pursuing goes into")
        print("LEADS.md as unverified. The checks read the corpus the project already has")
        print("and cannot find what it does not contain.")
    return actors, instruments, gaps, adjacency, doc_drift


def self_test():
    """Each check must fire on input that should trigger it.

    A discovery check that never fires is indistinguishable from a clean corpus, which is
    the failure mode this whole protocol exists to prevent.
    """
    print("SELF TEST: each discovery check must fire on input that should trigger it\n")
    fake = {
        "cases": [
            {"id": "t1", "label": "Test One", "status": "dead", "instId": "jpl",
             "narrative": "Richard Doty interviewed her. See DIA-08-1003-013 and case 26AVCF00232. "
                          "Police investigated. Cause undetermined.",
             "sources": [{"name": "x"}]},
            {"id": "t2", "label": "Test Two", "status": "dead",
             "narrative": "Richard Doty appears here too.", "sources": []},
        ],
        "entities": {"INSTITUTIONS": [], "PROGRAMS": [], "LOCATIONS": [], "DOMAINS": []},
    }
    actors = check_actors(fake)
    instruments = check_instruments(fake)
    gaps = check_negative_space(fake)
    adjacency = check_adjacency(fake, actors)

    results = [
        ("actor check finds an untracked person", "Richard Doty" in actors),
        ("instrument check finds a document number",
         any(t == "DIA-08-1003-013" for t, _ in instruments)),
        ("instrument check finds a court case number",
         any(t == "26AVCF00232" for t, _ in instruments)),
        ("negative space flags a case with no employer", "t2" in gaps and "employer" in gaps["t2"]),
        ("negative space flags a case with no sources", "t2" in gaps and "sources" in gaps["t2"]),
        ("adjacency finds a name in two cases", "Richard Doty" in adjacency),
        ("clean case is not flagged", "t1" not in gaps),
    ]

    # Documentation drift must fire on prose that contradicts the data.
    import tempfile
    real = load()
    first = real["cases"][0]
    bad = "The case of %s, S%d/P%d/I%d, is the model.\n" % (
        first["label"], first["S"], (first["P"] + 1) % 4, first["I"])
    tmp = os.path.join(ROOT, "README.md")
    original = open(tmp, encoding="utf-8").read()
    try:
        open(tmp, "a", encoding="utf-8").write("\n" + bad)
        fired = any(p[2] == first["id"] for p in check_doc_scores(real))
    finally:
        open(tmp, "w", encoding="utf-8").write(original)
    results.append(("doc-drift check catches a wrong score in prose", fired))
    results.append(("doc-drift check is clean on the real files", not check_doc_scores(real)))
    passed = 0
    for name, fired in results:
        print("  %-46s %s" % (name, "PASS" if fired else "FAIL, CHECK IS BLIND"))
        passed += bool(fired)
    print("\n%d of %d discovery checks proven to fire" % (passed, len(results)))
    return 0 if passed == len(results) else 2


# --------------------------------------------------------------------------------------
# Documentation drift
# --------------------------------------------------------------------------------------
# The prose files are load bearing in this project: CLAUDE.md tells a fresh session to read
# SESSION-HANDOFF.md first, and PROJECT.md is the master case documentation. They drift from
# the data silently, and a wrong score in a file people actually read is worse than a wrong
# score in a file they do not. On 25 August 2026 SESSION-HANDOFF.md described Monica Reza as
# P3 against an adjudicated P2, contradicting its own counts table on the same page.

DOC_FILES = ["SESSION-HANDOFF.md", "PROJECT.md", "README.md", "THESIS-NOTES.md"]
SCORE_RE = re.compile(r"\b(S[0-3])\s*/\s*(P[0-3])\s*/\s*(I[0-3])\b")


def check_doc_scores(data):
    """Find S/P/I triples in prose that disagree with the data.

    Only fires when a case name appears on the same line, so it cannot guess.
    """
    cases = {c["label"]: c for c in data["cases"]}
    surnames = {c["label"].split()[-1]: c for c in data["cases"]}
    problems = []
    for fname in DOC_FILES:
        path = os.path.join(ROOT, fname)
        if not os.path.exists(path):
            continue
        for n, line in enumerate(open(path, encoding="utf-8"), 1):
            m = SCORE_RE.search(line)
            if not m:
                continue
            case = None
            for label, c in cases.items():
                if label in line:
                    case = c
                    break
            if case is None:
                for sur, c in surnames.items():
                    if sur in line:
                        case = c
                        break
            if case is None:
                continue
            want = ("S%d" % case["S"], "P%d" % case["P"], "I%d" % case["I"])
            got = (m.group(1), m.group(2), m.group(3))
            if got != want:
                problems.append((fname, n, case["id"], "/".join(got), "/".join(want)))
    return problems


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        sys.exit(self_test())
    run()
