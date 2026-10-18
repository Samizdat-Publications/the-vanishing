# Session Handoff: The Vanishing

**Handoff date:** August 25, 2026
**Supersedes:** the August 7, 2026 handoff, which was stale and listed four already-closed items as open.

**If you are a fresh Claude session, read this file first, then `PROJECT.md`, then the latest `scientist-tracker-state-*.md`.**
This file is written to be self-sufficient. You should not need any prior conversation or any Cowork memory to work on this project.

---

## 1. What this project is

Stewart Gregerson's personal research project tracking deaths and disappearances of US
scientists, military officials and defense-connected individuals since 2021. Working title
**"The Vanishing."** Personal research, **not work-related.** No employer branding anywhere.

## 2. Where it lives, and what it is NOT

Git repository. Remote `https://github.com/Samizdat-Publications/the-vanishing.git`
(private, Samizdat-Publications). Branch is **`master`**, not `main`.

**Two environments, one repo.** As of 25 August 2026 the project is worked on from both a
cloud Claude Code session, which clones the repo fresh and can push, and Stewart's local
machine at `C:\Users\stewa\Documents\Claude\Cowork files\scientist-tracker\`.
Both are live. Neither working tree sees the other's uncommitted work.

**`origin/master` is the only source of truth. Always pull before starting and push when
done.** Do not assume the working tree reflects everything that exists.

**Do not confuse this with The Legacy Program Dashboard.** That is a different project,
a different git repo (`the-legacy-program-dashboard`), and lives at
`...\Claude\Projects\Missing individuals connected to defense contractors\the-program\`.
It is under active development in a separate thread. **Do not touch it.**

The one legitimate crossover: The Program uses `the-vanishing-v2.html` as a frozen build
input at its own `ref/the-vanishing-v2.html`. That is a copy. It is never edited there, and
changes here do not propagate there automatically.

## 3. Current state, August 25 2026

**The rebuild is done through step 4, and the first import has landed.** The dashboard is
**built from data**, not hand edited. Case records live in `research/*.json`.

```bash
cd /home/user/the-vanishing
python3 tools/merge.py && python3 tools/build_dashboard.py
python3 tools/verify.py --idempotent
python3 -m http.server 8971
```
Then open `http://127.0.0.1:8971/dist/the-vanishing.html`. On Stewart's machine use `python`.
`file://` will not work. The build copies `assets/` into `dist/` so the photographs resolve.

**`verify.py` passing is the definition of shippable**, and every check is itself tested
against input it must reject (`--self-test`). Same for `discovery_checks.py`.

```bash
cd /home/user/the-vanishing
python3 tools/verify.py --self-test            # 5 gates proven to reject bad input
python3 tools/discovery_checks.py --self-test  # 21 checks proven to fire
node tools/test_claim_sources.js && node tools/test_source_render.js
```

**Two things about the gates worth knowing before you edit data.**

**A claim cannot be removed silently.** The semantic gate requires every baseline claim text
to still be present. To retire one deliberately, write it out verbatim in
`RETIRED_CLAIM_TEXTS` in `tools/semantic_diff.py` with the reason. An undeclared removal
fails, and that is proven by a self-test. New claims are declared the same way in
`NEW_CLAIM_TEXTS`.

**The negative-space check has three states, not two.** Answered, **documented absence**
(the record says plainly that no such fact is public), and gap (the record says nothing
either way). Before 25 August 2026 a negation read as coverage, so writing "no investigating
agency has ever been named" silenced that record's gap. The distinction is substantive:
Maiwald's Tier A rests on there being nothing in the record at all, which only means
something if the tracker can tell "we looked and found nothing" from "we did not look."

**`the-vanishing-v2.html` is now the frozen historical reference and must not be edited.**
It is what `data/baseline.json` was extracted from, and `verify.py` asserts its hash so the
semantic gate keeps its anchor. It is no longer the build target.

**What the gates are.** Step 2 proved the extraction lossless by regenerating the original
HTML byte for byte. That gate retired when step 3 changed the schema on purpose;
`data/baseline.json` and `tools/semantic_diff.py` replace it. **Every content change must now
be declared in `EXPECTED_CHANGES` with a reason**, which is the audit trail
`RESEARCH-PROCESS.md` asks for. Claim texts have their own allowlist, so a
collection-level declaration cannot become a blank cheque.

**Step 5 is partially done.** Ning Li and McCasland imports landed with no axis moves. The
rest of `PORT-FROM-THE-PROGRAM.md` is not started.

### Case counts

| Metric | Value |
|---|---|
| Cases | 15 |
| Tier A | 8 |
| Tier B | 2 |
| Tier C | 5 (retained deliberately, to prove the list is not curated) |
| Dead | 10 |
| Missing | 4 |
| Resolved | 1 |
| I3 institutional channel | 10 |
| P3 personal program proximity | 2 (Sullivan, LeBlanc) |
| Photographs | **15 of 15. Zero placeholders.** |

### Git state

The dashboard is built from `research/*.json`, so **the authoritative counts are whatever
`python3 tools/merge.py` reports**, not this table. It prints the case, node and timeline
counts on every run.

**Claude can push.** Work happens on a feature branch and lands through a pull request.
Always push with the explicit form:

```bash
git push -u origin <branch-name>
```

The old PowerShell notes are history. The `index.lock` collisions and the bare `git push`
gotcha were artefacts of the local OneDrive working copy and should not recur.

## 4. What closed before the rebuild

All four "immediate next steps" from the previous handoff are **done**. Do not re-open them.

| Item | Outcome |
|---|---|
| Delete `_to_delete\`, commit the three pending files | Done, plus 11 further commits building v2 |
| Update `RESEARCH-PROCESS.md` for the three-axis model | Done. Grew from 7.6 KB to 21.4 KB |
| Verify Matthew Sullivan's testimony timing | **Checked and it failed.** The Nov 13 2024 hearing was announced after his May 12 2024 death. The "died before testifying" framing is not supportable on that hearing. He stays Tier B. This was the highest-value open item and it resolved against the hypothesis. Record it that way. |
| LA County docket 26AVCF00232, June 5 prelim outcome | **Confirmed unreported in open sources.** Still genuinely unknown. See section 6. |

Also landed since: `SCORING-DISCREPANCIES.md` (axis conflicts adjudicated),
`PHOTOS.md` (licence research plus the Aug 24 addendum), photograph integration,
data export, analyst charts and reports, map pan and zoom, and an adversarial review pass.

## 5. The three-axis scoring model

Every case carries three independent scores plus a composite tier. **The axes are never summed.**

| Axis | Range | Question |
|---|---|---|
| **S** Sequence Anomaly | 0-3 | How many independently documented, individually unexplained links form a chain? |
| **P** Personal Program Proximity | 0-3 | What sensitive access did this person personally hold? |
| **I** Institutional Channel | 0-3 | Does the employer have documented history as a conduit for classified work? |

Tier A = an unexplained fact no source accounts for, plus (S2+ or P3 or I3).

### The cases that carry the argument

- **Joshua LeBlanc, S2/P3/I3.** Active DRACO nuclear propulsion engineer at NASA Marshall. Four unexplained hours with his Tesla at Huntsville International that morning. Phone and wallet left at home. Dead the same day. High on all three axes; v1 buried him.
- **Monica Reza, S2/P2/I2.** Mondaloy co-inventor (rocket engine superalloy). Vanished within seconds in a companion's sightline. **Corrected 25 Aug 2026: this file previously read P3, contradicting both the adjudicated value in `SCORING-DISCREPANCIES.md` and its own counts table above.**
- **Carl Grillmair, S3/P1/I3.** The model sequence case. Reported a trespasser; that man was arrested with a loaded unregistered rifle, released in three days, had charges dropped, and killed him eleven days later. **Caveat: his widow told the BBC he did not personally call 911. Do not assert he was the caller.**
- **Melissa Casias, S3/P1/I3.** Cause undetermined after 13 months. Registered handgun near remains, owner undisclosed. Surveillance timestamp corrected by 13h58m with no explanation.
- **Frank Maiwald, S1/P2/I3.** No cause of death disclosed and no skeptical source has offered any alternative, only the base rate. The cleanest pure open question.

### Eskridge, and how to hold it

**Stewart's position, 25 August 2026: he believes the case is ultimately real, and he
accepted every specific correction made to it.** Those are not in tension, and a future
session should not treat the corrections as grounds to downgrade the case.

What the 25 August pass actually did was make the record **better documented, not weaker**:

- **Added** a real affiliation the tracker never had. She was **CEO and co-founder of
  HoloChron LLC**, a father-daughter gravity-modification company, per her own slide deck.
- **Removed an unsupported claim.** "Prior NASA-adjacent propulsion work" appears to have
  been her father's record attributed to her. Moved to `unverified`, not deleted.
- **Held I at 1**, now argued from the corporate record and from her own stated preference
  for independence from government funding, rather than assumed from "small private institute".

**Untouched by any of it:** her documented statement that she believed she was the target of
a "psychological war" to stop her anti-gravity work, which is a fact about what she said and
is not affected by any of the above. Tier B stands. Her family's position stands as recorded,
and the tracker does not argue with it.

## 6. Open items

**Note on item 1.** It would close four questions at once, but **Stewart decided on 25 August
2026 that he will probably not make the call, and asked that it stay on file as a want.**
It is recorded, not scheduled. **Do not keep raising it.** The correct standing position on
the Grillmair tail is "confirmed unreported", which is honest.

| # | Item | Notes |
|---|---|---|
| 1 | **Snyder docket, LA County case 26AVCF00232** | **On file as a want, not scheduled.** Was he held to answer on June 5 2026, or continued to June 18? Unreported everywhere and obtainable only by phone: Antelope Valley Courthouse, Criminal Clerk **(661) 483-5798**. Script in `SNYDER-DOCKET-RETRIEVAL.md`. Would close items 1 through 4. **Until then the tracker says confirmed unreported, and that is the correct answer rather than a placeholder.** |
| 2 | Late-December 2025 conduct behind Snyder's burglary count | Charged only after the killing. Sits against the "random disturbed neighbour" reading |
| 3 | Who contacted law enforcement about Snyder on December 20 2025 | Sources conflict. The widow says it was not Grillmair |
| 4 | Was the firearm enhancement amended down between the February complaint and the May arraignment? | |
| 5 | Frank Maiwald's cause of death | Still undisclosed, and now **recorded as a documented absence rather than left silent**: no investigating agency has ever been publicly named either. Checked 25 Aug 2026 against the PolitiFact fact-check, which names him and offers **no alternative explanation at all**. His Tier A rests on the absence of skeptical engagement, so that absence is now verified rather than assumed |
| 6 | Source "Prior NASA-adjacent propulsion work" on Amy Eskridge, or leave it unverified | **Stewart reviewed and agreed with the correction on 25 Aug 2026. It stays in her `unverified` array until something sources it.** Her own December 2018 deck calls her "Chemist, Entrepreneur" and names her father separately as "Retired NASA Engineer, Scientist". **Open only in the sense that a source could still turn up. Not a live doubt about the case.** See the Eskridge note in section 5 |
| 7 | Is the Institute for Exotic Science registered in any state? | No Alabama registration exists. Delaware not searched, its name search is CAPTCHA-gated. **An open question, not a finding of impropriety** |
| 8 | Retrieve the USPTO file wrapper for application 15/141,270 | Contains Examiner Bonzell's rejection in his own words. The highest-value document outstanding on the Pais thread. **Attempted 25 Aug 2026 and blocked, not for want of trying: the Open Data Portal API returns 401 without a key, PEDS is retired and unreachable, and Patent Center returns 405 to every public method.** The unblock is a **free ODP API key** from `data.uspto.gov`, which needs a browser. See `LEADS.md` section D for the four routes and how each failed |
| 9 | Re-check two `esd.whs.mil` URLs from a browser | They underpin the SAP cover-mechanism citation and return 403 to automated requests |
| 10 | **A long-form Richard Doty interview transcript** | **A want, recorded 26 Aug 2026.** Roughly three hours of the operator describing method, including a loaned-out dirty-tricks capability. **The episode is not yet identified:** Stewart recalls Danny Jones and is unsure; that could not be confirmed, and a confirmed long-form alternative exists (Rebelliously Curious RC 80). Identify first, then transcribe. **The rule does not bend for volume: cite Doty for what he did, never for what he says is true.** Three hours of detail is three hours of unverified assertion by a self-described disinformation officer, and the transcript is one source, not many. See `LEADS.md` section D |

### Closed since the last handoff

| Item | Outcome |
|---|---|
| Locate an af.mil or DVIDS original of the Sullivan portrait | **Closed as a negative.** Exhaustive search, no federal original exists in any public repository. The credit string no longer asserts USAF authorship |
| PROJECT.md open question 15, the Sullivan interview date | **Closed as a negative.** Exact-phrase search of oversight.house.gov returns no posts |
| Identify the Comer-Burlison eleven | **Obtained, and it devalued itself.** 11 of 11 already tracked, zero theirs-only. But all four letters footnote their enumeration to Daily Mail and NY Post, so **it is not an independent check and must never be described as one** |
| Verify James E. McDonald | **Rejected as an analogue.** The campaign was real but privately authored by Philip Klass. Retained as a mechanism citation only |
| Were the 27 April 2026 briefings delivered? | **No public record from any of the four agencies**, and none on record refusing |
| Holocron Engineering | **Resolved to HoloChron LLC.** She was CEO and co-founder, not a lecturer. Channel question closed as a negative |
| **Can the Bennewitz precedent bear its weight?** | **Answered 25 Aug 2026, and it splits.** Death sourced Tier 1 to a federal interment record; hospitalisation is testimony, not record. See section B |
| **The five negative-space record gaps** | **All five closed.** LeBlanc to ALEA and the Alabama Department of Forensic Sciences; Reza to LASD Homicide Bureau Missing Persons Unit; Hicks and Maiwald recorded as documented absences; Thomas turned out to be **a wrong Tier 1 claim**, corrected |
| **PolitiFact, 28 Apr 2026** | **Read in full.** Three things attached that the tracker did not carry, including McCasland's wife's account of his UFO-community association as consulting on a fiction book |
| **The cc'd minority, Garcia and Frost** | **Checked, clean negative.** Both own release indexes read directly across the full window. Zero mentions. Both published on days around the deadline and did not raise it |
| **What the Oversight enumeration rests on** | **Confirmed by reading the FBI letter itself.** All eight footnotes are press: two Daily Mail, three NY Post, two The Hill. The Committee calls its own basis "unconfirmed public reporting" |

## 7. Research cadence

**Weekly sweeps, retained.** Stewart's decision on Aug 24 2026: keep weekly through
development, revisit and probably move to monthly once the build is final.
Spec is in `RESEARCH-PROCESS.md`, Priority 1-4. The Aug 7 sweep ran as four parallel
research agents, one per priority tier, which worked well. Story has been dormant in
mainstream coverage since early May 2026.

## 8. Working rules

- **No em dashes** anywhere: generated text, UI copy, documentation. Use double hyphens or restructure. Verified on every file delivered so far. Keep it that way.
- Tables preferred over bullet lists for comparative content. Charts get data labels.
- Terminal commands include the `cd` so they are copy-pasteable.
- **Never fabricate connections.** Always carry counterarguments. Distinguish confirmed fact from allegation from open question. Flag anything unverifiable. Note where sources conflict, and several genuine conflicts are logged.
- **Never fabricate URLs, case numbers or document numbers.** If a URL cannot be verified to resolve, say so.
- Do not cite: strangehappen.com, theheartysoul.com, hannahhowell.com, mysterylores.com, frontpagenewspaper.com, headlinereporter.com, factually.co, slaynews.com, vigilantfox.com, ConservativeBrief, Medium reposts. These recycle identical errors and manufacture timestamps on old material.
- These are real deaths and real missing people. Several families have publicly asked not to have their losses treated as conspiracy material. The tracker records those statements accurately and does not argue with them.

### Editorial stance

Built on the working hypothesis that **a pattern exists**, for an audience receptive to that
framing. The core analytical insight: **an event prosaic in isolation may not be prosaic in
sequence.** Civilian academics at major institutions are in scope even without documented
clearances, on the JASON precedent. What Stewart explicitly does **not** want is fake or
specious connections; the rigor serves the argument rather than opposing it. Skeptical
literature is used as a **grading instrument**, not a rebuttal section.

### Photograph rights posture (set Aug 24 2026)

Publicly findable images are used, with per-image credit. Licence grading in `PHOTOS.md` is
information, not a gate. Stewart has acknowledged and accepted the risk on the basis that
this is personal research for a small private audience. **Do not re-litigate this.**

### Adversarial review protocol

At the end of any deliverable that feels final, ask: **"Do you want to run adversarial
review audit?"** Only run it when he says yes, because it consumes context. When running it,
act as his managers, the management he presents to. Pick apart anything that looks odd or
does not parse at first glance, and actually inspect the rendered output.

---

# ADDENDUM: 24 August 2026, later the same day

Three decisions and one survey landed after the body of this handoff was written.
**Where this addendum and the sections above disagree, the addendum wins.**

## A. The single-file HTML constraint is dropped

Stewart's call. `the-vanishing-v2.html` is 4,741 lines and already fails its own constraint,
because it loads photos by relative path. The project moves to a normal multi-file structure
with a data layer, a build pipeline and a verification gate, mirroring The Legacy Program
Dashboard, which was itself built on this project's engine.

**Read `ARCHITECTURE.md`.** It has the target layout, the migration order, and the one rule
that must come with it: regenerating the current HTML byte-for-byte from extracted data is
the checkpoint that proves nothing was lost. Do not change the schema and extract in the
same step.

`the-vanishing-v2.html` stays in the repo as the reference output until that checkpoint passes.

## B. The neutralisation frame is recorded

Stewart's analytic refinement: **death is one outcome of the pattern, not the definition of
it.** The object tracked is people attached to sensitive programmes who fell out of good
standing and were removed from play, by whatever means, because discrediting is cheaper and
more durable than killing.

**Read `THESIS-NOTES.md`.** It records the frame, the precedent that supports it, and,
importantly, **the falsifiability problem it creates and how to keep it honest.** The
recommendation there is to implement the frame as an `outcome` field in the schema rather
than as a thumb on the S/P/I scores. Do not raise axis scores on the strength of the frame
alone.

**The precedent was sourced on 25 August 2026 and it splits. Know this before citing it.**

| Element | Strength |
|---|---|
| The AFOSI operation existed and was run against Bennewitz | **Documented.** Federal records, plus the operator on the record |
| He died 23 June 2003 | **Tier 1.** VA National Gravesite Locator record 7139602, queried directly |
| Cause of death | No public record found |
| He was hospitalised in 1988 | **Testimony.** Family and associate accounts relayed in Greg Bishop, *Project Beta*, 2005 |
| The operation caused the hospitalisation | Inference, and stated as one by its own sources |

**The operation is documented. Its effect is testimony.** Since "neutralisation without
death" is a claim about the effect, **cite the operation and do not cite the breakdown as
documented.** No further searching closes this: psychiatric admission records of a private
citizen are not public. Full brief: `notes/research/2026-08-25-bennewitz.md`.

## C. Cross-repo survey against The Legacy Program Dashboard

**Read `PORT-FROM-THE-PROGRAM.md`.** Read-only survey, nothing imported yet. Headlines:

| Finding | Impact |
|---|---|
| **Ning Li is named in a released DIA document.** DIA-08-1003-013, "The Role of Superconductors in Gravity Research," 23 March 2010, Acquisition Threat Support series, produced under the DIA AAWSA programme, FOIA-released. It reviews her work by name. | Her retention rationale here ("retained for research continuity to Eskridge rather than for its own anomaly") is now **too weak and wrong on documentary grounds.** Raise her **I** score. Leave S and P alone -- the document shows institutional interest in her research line, not anything happening to her. |
| **The Comer-Burlison probe covers eleven people.** This tracker has fifteen. | Best available external curation check. Identifying the eleven and diffing is a high-value research task. |
| **Burlison's staff had been trying to reach McCasland about a separate congressional investigation before he vanished.** | Sequence-anomaly fact for McCasland's **S** score. Sourced. |
| Briefings were demanded of FBI, Department of War, NASA and DOE by 27 April 2026 | Deadline has passed. Nobody appears to have followed up. Open question. |
| **Amy Eskridge appears zero times in The Program's dataset.** | The long-standing note in this project and in Claude's memory that Eskridge is the overlap point between the two projects is **wrong.** The real overlap is Ning Li, McCasland and the Oversight probe. |
| The two schemas are already compatible | Same record shape. This tracker scores S/P/I, The Program scores C/A/D. Porting is mechanical. |

**Governing rule for any import: copy the claim and its source, never the conclusion.**
The Program writes from a stronger premise than this tracker is allowed to use. Its voice
assumes the programme exists. The Vanishing does not get to assume its pattern exists,
because that is the thing it is trying to demonstrate.

## D. Updated file list

| File | Purpose |
|---|---|
| `ARCHITECTURE.md` | The multi-file rebuild plan and migration order |
| `THESIS-NOTES.md` | The neutralisation frame, its precedent, its falsifiability problem |
| `PORT-FROM-THE-PROGRAM.md` | What ports from the sibling repo, ranked, with the honest limits on each |
| `SNYDER-DOCKET-RETRIEVAL.md` | Manual retrieval script for the one open court record |
| `README.md` | Repo entry point |
| `CLAUDE.md` | Loads automatically at session start. The rules, condensed, so they do not depend on anyone thinking to read this file |
| `FIRST-TASKS.md` | Ranked opening moves with reasoning |

## E. Discovery protocol, added after a named failure

Stewart, 24 August 2026: *"if we're missing Doty then we're not doing something right. In
fact this seems to be a pattern, some of the highest value ones I am aware of were not caught
by our current process until I called them out by name."*

**He is right. Read `DISCOVERY-PROTOCOL.md` and treat it as a required step, not a
suggestion.**

The diagnosis in one line: **the search was victim-centric and entity-name-driven**, so it
structurally could not reach actors, mechanisms or precedents. Doty is not a victim and not
an institution, so no query in the old process pointed anywhere near him. Bennewitz was found
by luck, not method -- he surfaced only because one `entityInfo` entry was dumped as a
formatting sample.

The protocol adds five things: query six axes (victims, **actors**, **mechanisms**,
**precedents**, **instruments**, institutions); read a corpus index in full rather than
sampling it; check `LEADS.md`; run an explicit negative-space pass; and state how thoroughly
the space was actually searched, not just what was found.

**`LEADS.md` is the direct fix for the recall problem.** Anything Stewart names in
conversation that is not in the tracker goes in that file immediately. Called out once
should mean captured forever. Every research pass reads it and adds to it.

### Running the corrected protocol once already paid for itself

Reading The Program's full 279-person list, rather than searching it by the fifteen case
names, surfaced candidates the old process could never have found:

| Found | Axis | Why it matters |
|---|---|---|
| **James E. McDonald**, senior physicist, Institute of Atmospheric Physics, **University of Arizona**, died 1971 after his scientific credibility collapsed | Analogue case | Near-exact structural analogue of the neutralisation frame. Also a University of Arizona tie, which connects to Hicks. **Unverified. Verify the circumstances before asserting anything.** |
| **John B. Alexander**, US Army Col (ret.), **Los Alamos non-lethal weapons programme** | Actor and mechanism | Sits at the intersection of the LANL cluster (Chavez, Casias) and the mechanism question |
| **William L. Moore**, **Linda Moulton Howe** | Actor, witness | The rest of the Bennewitz disinformation cluster |
| **Capt. Uyrangê Hollanda Lima**, **Betty Cash** | Analogue cases | Pattern instances outside the tracker's current scope |

All of these are in `LEADS.md` as **unverified**. They are a queue, not findings.

**Also noted, for the other project and not actioned here:** The Program lists Nick Pope with
status `dead`. He appears to be alive. Looks like a data error in `the-program.json`. Raise it
in that project's own thread. The Program was not modified by any of this work.
