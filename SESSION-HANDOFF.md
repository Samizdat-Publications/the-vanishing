# Session Handoff: The Vanishing

**Handoff date:** August 24, 2026
**Supersedes:** the August 7, 2026 handoff, which was stale and listed four already-closed items as open.

**If you are a fresh Claude session, read this file first, then `PROJECT.md`, then the latest `scientist-tracker-state-*.md`.**
This file is written to be self-sufficient. You should not need any prior conversation or any Cowork memory to work on this project.

---

## 1. What this project is

Stewart Gregerson's personal research project tracking deaths and disappearances of US
scientists, military officials and defense-connected individuals since 2021. Working title
**"The Vanishing."** Personal research, **not employer work.** No employer branding anywhere.

## 2. Where it lives, and what it is NOT

Git repository. Remote `https://github.com/Samizdat-Publications/the-vanishing.git`
(private, Samizdat-Publications). Branch is **`master`**, not `main`.

**As of 25 August 2026 the project works out of the GitHub repo, not a local folder.**
Sessions run in Claude Code and clone the repo fresh. The former local working copy at
`C:\Users\stewa\OneDrive\Documents\Claude\Cowork files\scientist-tracker\` is no longer
the source of truth. Treat `origin/master` as authoritative and pull before starting work.

**Do not confuse this with The Legacy Program Dashboard.** That is a different project,
a different git repo (`the-legacy-program-dashboard`), and lives at
`...\Claude\Projects\Missing individuals connected to defense contractors\the-program\`.
It is under active development in a separate thread. **Do not touch it.**

The one legitimate crossover: The Program uses `the-vanishing-v2.html` as a frozen build
input at its own `ref/the-vanishing-v2.html`. That is a copy. It is never edited there, and
changes here do not propagate there automatically.

## 3. Current state, August 24 2026

**v2 is built and shipped.** `the-vanishing-v2.html` is a working single-page dashboard,
about 325 KB, 4,741 lines. It supersedes `scientist-network-tracker.html` (v1).

**It is not literally self-contained.** It references `assets/photos/*` by relative path.
Opening the HTML alone, away from the repo, gives you a working board with broken images.
Ship the folder, not the file.

**Local viewing note.** The Chrome tooling cannot open `file://` URLs. To inspect it, serve
the folder and browse to it:

```bash
cd /home/user/the-vanishing
python3 -m http.server 8971
```
Then open `http://127.0.0.1:8971/the-vanishing-v2.html`.

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

| Item | Value |
|---|---|
| Last commit | `b42720b` "Add discovery protocol and leads file after a named recall failure" |
| origin/master | in sync at `b42720b` |
| Uncommitted | none, working tree clean |

**Claude can push now.** That changed with the move to the GitHub repo on 25 August 2026.
Work happens on a feature branch and lands through a pull request, rather than by writing
files to disk for Stewart to commit from PowerShell. Always push with the explicit form:

```bash
git push -u origin <branch-name>
```

The old PowerShell notes are retained only as history. The `index.lock` collisions and the
bare `git push` gotcha were artefacts of the local OneDrive working copy and should not recur.

## 4. What closed since the August 7 handoff

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
- **Monica Reza, S2/P3/I2.** Mondaloy co-inventor (rocket engine superalloy). Vanished within seconds in a companion's sightline.
- **Carl Grillmair, S3/P1/I3.** The model sequence case. Reported a trespasser; that man was arrested with a loaded unregistered rifle, released in three days, had charges dropped, and killed him eleven days later. **Caveat: his widow told the BBC he did not personally call 911. Do not assert he was the caller.**
- **Melissa Casias, S3/P1/I3.** Cause undetermined after 13 months. Registered handgun near remains, owner undisclosed. Surveillance timestamp corrected by 13h58m with no explanation.
- **Frank Maiwald, S1/P2/I3.** No cause of death disclosed and no skeptical source has offered any alternative, only the base rate. The cleanest pure open question.

## 6. Open items

| # | Item | Notes |
|---|---|---|
| 1 | **Snyder docket, LA County case 26AVCF00232** | Was he held to answer on June 5 2026, or continued to June 18? Unreported everywhere. **Resolvable by phone.** Michael D. Antonovich Antelope Valley Courthouse, 42011 4th St West, Lancaster CA 93534. **Criminal Clerk (661) 483-5798.** Ask for the minute orders for June 5 2026 and June 18 2026. Full script in `SNYDER-DOCKET-RETRIEVAL.md`. |
| 2 | Late-December 2025 conduct behind Snyder's first-degree residential burglary count | Charged only after the killing. Sits directly against the "random disturbed neighbor" reading. |
| 3 | Who actually contacted law enforcement about Snyder on December 20 2025 | Sources conflict. The widow says it was not Grillmair. |
| 4 | Was the firearm enhancement amended down between the February complaint and the May arraignment? | Complaint said intentional discharge causing GBI; arraignment said personal use of a rifle. |
| 5 | Frank Maiwald's cause of death | Still undisclosed. |
| 6 | Locate an af.mil or DVIDS original of the Sullivan service portrait | Would move the one likely-federal image from assumed-copyrighted to cleanly public domain. |

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

**Read `THESIS-NOTES.md`.** It records the frame, the documented precedent that supports it
(Bennewitz, hospitalised 1988, method admitted publicly 1989), and, importantly, **the
falsifiability problem it creates and how to keep it honest.** The recommendation there is to
implement the frame as an `outcome` field in the schema rather than as a thumb on the S/P/I
scores. Do not raise axis scores on the strength of the frame alone.

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
