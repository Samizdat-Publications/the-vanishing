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
    # Outlets that are cited in prose without being a cited source name, so
    # outlet_names() below cannot derive them.
    "New York Post", "York Post", "Daily Mail", "Fox News", "LA Magazine",
    "Angeles Magazine", "Union Leader", "Scientific American", "Skeptic Magazine",
    "The Hill", "Hill",
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
#
# The first version of this check produced false positives that made it useless. It missed
# "shot", "killed", "murder" and "fatally", so Grillmair and Loureiro, both of whom were
# shot, reported as having no cause on file. It also asked missing persons for a cause of
# death, which they cannot have by definition. A check that fires on non-gaps trains you to
# skim past it, which is worse than not having it.
EXPECTED_COVERAGE = {
    "investigating agency": (r"police|sheriff|FBI|state police|deputies|investigat|detective|"
                             r"NTSB|OMI|medical examiner|medical investigator|coroner|"
                             r"district attorney|prosecut|LASD|BCSO|DPS|task force"),
    "cause or manner": (r"cause|manner|autopsy|ruled|undetermined|overdose|gunshot|shot|"
                        r"killed|murder|fatally|homicide|suicide|natural causes|no cause|"
                        r"crash|collision|drown|struck by"),
    "employer": r"",  # structural, checked via instId rather than prose
}

# A cause of death is only expected where there is a death. Asking a missing-person record
# for one is not a gap, it is the point of the record.
CAUSE_APPLIES_TO = {"dead", "resolved"}

# Negation reads as coverage unless it is handled, and that is a worse bug than the false
# positives fixed above. "No investigating agency has ever been publicly named" contains
# "investigat", so a record that documents an absence would score as having answered the
# question, and a real gap would go silent.
#
# So there are three states, not two:
#
#   answered           the record names the agency, or the cause
#   documented absence the record explicitly says no such fact is public
#   gap                the record says nothing either way
#
# The distinction is substantive rather than cosmetic. Maiwald's Tier A rests on the claim
# that there is nothing in the record at all, which is only meaningful if the tracker can
# tell "we looked and found nothing" apart from "we did not look."
# Stems are prefixes with a leading boundary only, never a trailing one, exactly as the
# EXPECTED_COVERAGE patterns are. A trailing \b silently excluded every plural: \bcause\b
# does not match "causes", so "listed as natural causes is unsourced" read as a positive
# statement of cause. The two pattern sets have to agree on word shape or the negation
# handling applies to a different vocabulary than the coverage test.
_STEMS = (r"cause|manner|autopsy|agency|agencies|investigat|disclos|releas|named|public|"
          r"determin|record|report")
NEGATION_RE = re.compile(
    r"\b(?:no|not|never|nothing|none|without|absence of|neither|unsourced)\b[^.;]{0,80}?"
    r"(?=[^.;]*\b(?:%s))"
    r"|\b(?:%s)[^.;]{0,80}?\b(?:no|not|never|nothing|none|unsourced)\b" % (_STEMS, _STEMS),
    re.I)


def strip_negated(text):
    """Drop clauses that assert an absence, so a documented absence stops reading as coverage.

    Clause-level rather than sentence-level: "He worked at JPL. No cause was released."
    must keep the first half. Splitting on sentence and clause boundaries both, then
    dropping only the clauses that carry a negation near a coverage term, is what keeps
    "Police investigated. No cause released." reporting a cause gap and not an agency gap.
    """
    keep = []
    for clause in re.split(r"[.;\n]", text):
        if NEGATION_RE.search(clause):
            continue
        keep.append(clause)
    return " ".join(keep)

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


def outlet_names(data):
    """Every source name the dataset already cites, as whole strings and as tokens.

    Outlets are the dominant false positive in the actor check, because "New York Post"
    and "The Hill" are capitalised multi-word sequences exactly like a person's name is.
    Deriving the list from the data beats hardcoding one: cite a new outlet and it is
    excluded automatically, with no stoplist to remember to update.

    Person tokens win ties. A tracked person's name is never excluded on the strength of
    a source that happens to share a word with it, because swallowing a real name is the
    one failure this check cannot afford.
    """
    person_tokens = set()
    for c in data["cases"]:
        person_tokens.update(c["label"].split())

    names = set()
    for c in data["cases"]:
        for src in c.get("sources", []):
            if src.get("name"):
                names.add(src["name"])
        for claim in c.get("claims", []):
            for src in claim.get("sources", []):
                if src.get("name"):
                    names.add(src["name"])

    out = set()
    for name in names:
        out.add(name)
        out.update(tok for tok in name.split() if tok not in person_tokens)
    return out


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
    known |= outlet_names(data)
    return known


def check_actors(data):
    """Untracked people named in narratives. Candidate actor list."""
    known = known_names(data)
    found = {}
    for case in data["cases"]:
        for m in NAME_RE.finditer(case_text(case)):
            name = m.group(0)
            # A leading "The" is never part of a person's name, and leaving it attached
            # let "The Committee" past a stoplist that already contained "Committee".
            if name.startswith("The ") and len(name.split()) > 1:
                name = name[4:]
            if name in known or name in NOT_PEOPLE:
                continue
            # Any two-word window landing in the stoplist disqualifies the whole match.
            # "Chief Medical Examiner" is three tokens, so testing only the whole string
            # or only the tail missed the "Medical Examiner" already sitting in the list.
            toks = name.split()
            if any(" ".join(toks[i:i + 2]) in NOT_PEOPLE for i in range(len(toks) - 1)):
                continue
            if toks[-1] in NOT_PEOPLE:
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
    gaps, absences = {}, {}
    for case in data["cases"]:
        text = case_text(case).lower()
        positive = strip_negated(text)
        missing, noted = [], []
        for field, pattern in EXPECTED_COVERAGE.items():
            if field == "employer":
                if not case.get("instId"):
                    missing.append(field)
                continue
            if field == "cause or manner" and case.get("status") not in CAUSE_APPLIES_TO:
                continue
            if re.search(pattern, positive, re.I):
                continue
            # Matches only inside a negated clause: the record answers the question by
            # documenting that there is no answer. That is a finding, not a gap.
            if re.search(pattern, text, re.I):
                noted.append(field)
            else:
                missing.append(field)
        if not case.get("sources"):
            missing.append("sources")
        if missing:
            gaps[case["id"]] = missing
        if noted:
            absences[case["id"]] = noted
    return gaps, absences


def independent_roots(claim):
    """How many genuinely independent sources stand behind a claim.

    Follows derivedFrom to a root and counts distinct roots. Five citations that all
    repeat one origin count as one, which is the whole point: the Oversight letters
    footnote eight press reports that trace to a single chain, and before this they
    scored exactly like eight independent attestations.
    """
    edges = {src["name"]: src.get("derivedFrom")
             for src in claim.get("sources", []) if src.get("name")}
    roots = set()
    for name in edges:
        node, seen = name, set()
        while edges.get(node) is not None and node not in seen:
            seen.add(node)
            node = edges[node]
        roots.add(node)
    return len(roots)


def check_convergence(data):
    """Claims whose support is thinner than their citation count suggests.

    Reports two things that are not defects and are worth looking at:

      repetition  more citations than independent roots. The gap is the exact size of
                  the overstatement a reader would make counting sources naively.
      contested   the record carries a competing account, attached to the claim it
                  competes with. A contested claim is a HEALTHY record, not a broken
                  one: the alternative is a file that carries one side and does not
                  know it.
    """
    repetition, contested = {}, {}
    for case in data["cases"]:
        for claim in case.get("claims", []):
            cited = len([s for s in claim.get("sources", []) if s.get("name")])
            roots = independent_roots(claim)
            if cited > roots:
                repetition.setdefault(case["id"], []).append(
                    (claim["text"][:60], cited, roots))
            if claim.get("contested"):
                contested.setdefault(case["id"], []).append(claim["text"][:60])
    return repetition, contested


def check_adjacency(data, actors):
    """Names appearing in more than one case narrative. Cross-case actor candidates."""
    return {n: ids for n, ids in actors.items() if len(ids) > 1}


def run(verbose=True):
    data = load()
    actors = check_actors(data)
    instruments = check_instruments(data)
    gaps, absences = check_negative_space(data)
    repetition, contested = check_convergence(data)
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

        print("\n3b. Documented absence, the record says plainly that no such fact is public (%d)"
              % len(absences))
        for cid, noted in sorted(absences.items()):
            print("   %-12s absent on record: %s" % (cid, ", ".join(noted)))
        if not absences:
            print("   none.")

        print("\n3c. Repetition, more citations than independent sources (%d)" % len(repetition))
        for cid, rows in sorted(repetition.items()):
            for text, cited, roots in rows:
                print("   %-12s %d cited, %d independent  %s" % (cid, cited, roots, text))
        if not repetition:
            print("   none. Every claim's citations are independent of each other.")

        print("\n3d. Contested, the record carries a competing account (%d)" % len(contested))
        for cid, rows in sorted(contested.items()):
            for text in rows:
                print("   %-12s %s" % (cid, text))
        if not contested:
            print("   none.")

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
    return actors, instruments, gaps, adjacency, doc_drift, absences, repetition, contested


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
    gaps, _abs = check_negative_space(fake)
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

    # The two false-positive classes that made the negative-space check useless.
    shot = {"cases": [{"id": "shot", "label": "S T", "status": "dead", "instId": "jpl",
                       "narrative": "He was shot on his porch. Deputies investigated.",
                       "sources": [{"name": "x"}]}],
            "entities": {"INSTITUTIONS": [], "PROGRAMS": [], "LOCATIONS": [], "DOMAINS": []}}
    results.append(("a shooting counts as a cause on file",
                    "cause or manner" not in check_negative_space(shot)[0].get("shot", [])))
    gone = {"cases": [{"id": "gone", "label": "G T", "status": "missing", "instId": "jpl",
                       "narrative": "Vanished. Police searched.", "sources": [{"name": "x"}]}],
            "entities": {"INSTITUTIONS": [], "PROGRAMS": [], "LOCATIONS": [], "DOMAINS": []}}
    results.append(("a missing person is not asked for a cause of death",
                    "cause or manner" not in check_negative_space(gone)[0].get("gone", [])))
    # Negation must not read as coverage. This is the hole that opening the third state
    # closes: before it, writing "no investigating agency was ever named" into a record
    # silenced that record's agency gap, because the sentence contains "investigat".
    def env(narr, status="dead"):
        return {"cases": [{"id": "n", "label": "N T", "status": status, "instId": "jpl",
                           "narrative": narr, "sources": [{"name": "x"}]}],
                "entities": {"INSTITUTIONS": [], "PROGRAMS": [], "LOCATIONS": [],
                             "DOMAINS": []}}

    g_neg, a_neg = check_negative_space(env(
        "No investigating agency has ever been publicly named. "
        "No cause of death was released."))
    results.append(("a documented absence is not counted as coverage",
                    "investigating agency" not in g_neg.get("n", [])
                    and "investigating agency" in a_neg.get("n", [])))
    results.append(("a documented absence is not counted as a gap either",
                    "cause or manner" not in g_neg.get("n", [])
                    and "cause or manner" in a_neg.get("n", [])))

    g_mix, a_mix = check_negative_space(env(
        "The Alabama Law Enforcement Agency investigated. "
        "No cause of death has been released."))
    results.append(("negation in one clause does not erase coverage in another",
                    "investigating agency" not in g_mix.get("n", [])
                    and "investigating agency" not in a_mix.get("n", [])
                    and "cause or manner" in a_mix.get("n", [])))

    # A plural must be caught too. \bcause\b does not match "causes", and that one missing
    # letter was enough to make a claim about the ABSENCE of a cause read as a cause.
    g_pl, a_pl = check_negative_space(env(
        "Police investigated. The line calling it natural causes is unsourced and no source "
        "for it was found."))
    results.append(("negation handles plurals, not just singulars",
                    "cause or manner" not in g_pl.get("n", [])
                    and "cause or manner" in a_pl.get("n", [])))

    # And the broadened negation must not swallow a record that plainly answers.
    g_ans, a_ans = check_negative_space(env(
        "Deputies investigated. The autopsy ruled the death an overdose."))
    results.append(("a plainly answered record is neither gap nor absence",
                    not g_ans.get("n") and not a_ans.get("n")))

    # Outlet names were the dominant false positive in the actor check. All four adjacency
    # hits at one point were outlets and titles, which is the same degradation that made
    # the negative-space check useless: a warning list that is entirely noise gets skimmed.
    outlets = {"cases": [{"id": "o", "label": "Case One", "status": "dead", "instId": "jpl",
                          "narrative": "Reported by the Gotham Herald. Jane Fairweather "
                                       "investigated. The Committee asked. Cause undetermined.",
                          "sources": [{"name": "Gotham Herald"}]}],
               "entities": {"INSTITUTIONS": [], "PROGRAMS": [], "LOCATIONS": [],
                            "DOMAINS": []}}
    found = check_actors(outlets)
    results.append(("an outlet named in a cited source is not a candidate actor",
                    "Gotham Herald" not in found))
    results.append(("a leading The does not smuggle a stoplisted word past the filter",
                    "The Committee" not in found and "Committee" not in found))
    results.append(("a real two-word person name is still found", "Jane Fairweather" in found))

    windows = {"cases": [{"id": "w", "label": "Case Two", "status": "dead", "instId": "jpl",
                          "narrative": "The Chief Medical Examiner ruled it. Police investigated.",
                          "sources": [{"name": "x"}]}],
               "entities": {"INSTITUTIONS": [], "PROGRAMS": [], "LOCATIONS": [],
                            "DOMAINS": []}}
    results.append(("a stoplisted two-word window disqualifies a longer match",
                    "Chief Medical Examiner" not in check_actors(windows)))

    g_sil, a_sil = check_negative_space(env("He worked on rocket engines."))
    results.append(("a silent record is still a gap, not an absence",
                    "investigating agency" in g_sil.get("n", [])
                    and "investigating agency" not in a_sil.get("n", [])))

    # Convergence. The failure this exists to prevent is FALSE convergence: several
    # citations that look independent and trace to one origin. The tracker holds a real
    # worked example in the Oversight letters, so this is not hypothetical.
    def claimcase(claim):
        return {"cases": [{"id": "c", "label": "C T", "status": "dead", "instId": "jpl",
                           "narrative": "Police investigated. Cause undetermined.",
                           "sources": [{"name": "x"}], "claims": [claim]}],
                "entities": {"INSTITUTIONS": [], "PROGRAMS": [], "LOCATIONS": [],
                             "DOMAINS": []}}

    chain = {"tier": 2, "text": "Repeated everywhere, sourced once.", "sources": [
        {"name": "Origin Wire"},
        {"name": "Second Paper", "derivedFrom": "Origin Wire"},
        {"name": "Third Paper", "derivedFrom": "Second Paper"},
    ]}
    rep, _ = check_convergence(claimcase(chain))
    results.append(("three citations down one chain count as one source",
                    independent_roots(chain) == 1 and "c" in rep))

    real = {"tier": 2, "text": "Two genuinely separate attestations.", "sources": [
        {"name": "Court Record"},
        {"name": "A Witness"},
    ]}
    rep2, _ = check_convergence(claimcase(real))
    results.append(("two independent citations count as two, and are not flagged",
                    independent_roots(real) == 2 and "c" not in rep2))

    disputed = {"tier": 2, "text": "One account of a disputed fact.",
                "sources": [{"name": "Source A"}],
                "contested": [{"text": "Another account says otherwise.",
                               "sources": [{"name": "Source B"}]}]}
    _, con = check_convergence(claimcase(disputed))
    results.append(("a contested claim is surfaced", "c" in con))

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
