# The Vanishing: Research Process

**Version 2, August 7, 2026.** Rewritten to match the three-axis scoring model in `PROJECT.md`. The v1 case schema in this file predated that model and no longer applied.

**Read `PROJECT.md` before running a sweep.** This file is procedure. `PROJECT.md` is the authoritative case record.

---

## Purpose

Keep the tracker current with new cases, updates to existing cases, and institutional developments, and **score every case the same way every time** so that tier assignments are reproducible rather than impressionistic.

The scoring rubric in Section 3 is the part of this document that matters most. Search queries go stale. The rubric is what makes the tracker auditable.

---

## Section 1: Cadence

The August 7, 2026 sweep found **no new cases** in the June 20 to August 7 window, and mainstream coverage has been dormant since early May 2026.

| Mode | When | Scope |
|---|---|---|
| **Monthly sweep** | First Sunday of the month | Full Priority 1-4 |
| **Trigger sweep** | On breaking news | Priority 1 and the affected named cases only |
| **Docket check** | Quarterly | Active legal proceedings only (currently People v. Snyder) |

**Triggers that justify an off-cycle sweep:** a new named death or disappearance in the defense, aerospace, nuclear, or intelligence sector; any House Oversight or Senate action naming a tracked individual; an FBI or agency statement on the review; a medical examiner ruling on any undisclosed cause of death in the file; an NTSB report on the Moffatt crash; any court event in 26AVCF00232.

**Weekly was the v1 cadence and it is no longer justified by the yield.** Moving to monthly is a finding, not a retreat. Log the sweep even when it returns nothing, because a documented empty window is evidence about the pattern's tempo.

### Running it

> "Run the scientist tracker sweep. Read RESEARCH-PROCESS.md in scientist-tracker/ for the procedure, then PROJECT.md for current case state."

Scheduled:

> "Schedule a monthly task, first Sunday at 10am, to run the scientist tracker sweep per RESEARCH-PROCESS.md"

The August 7 sweep ran as **four parallel research agents, one per priority tier.** That worked well and is the recommended pattern. Give each agent the source rules in Section 5 verbatim; agents do not inherit them.

---

## Section 2: Scope

### A) New individuals

Inclusion requires **at least one** of the following, plus a documented death or disappearance since 2021:

| Route | Criterion |
|---|---|
| Personal | US scientist, engineer, or defense/intelligence official in aerospace, propulsion, nuclear, plasma physics, astrophysics, defense research, the intelligence community, or a UAP-adjacent program |
| Institutional | Employed by an institution already in the file, or one meeting the I2/I3 definitions in Section 3 |
| Behavioral | Shares a documented pattern element: personal effects left behind, remote location, cause disputed or undisclosed |
| External | Explicitly linked to the pattern by media, investigators, or a member of Congress |

**A behavioral match alone is not sufficient for Tier A or B.** It gets a case into the file at Tier C pending a P or I score. Behavioral pattern-matching is the weakest inclusion route and the one a hostile reader will attack first.

**Do not pad.** A case that scores S0/P0/I0 does not belong in the file at all. A case that scores low but has a real channel belongs in the file at Tier C, labeled as such. The distinction is the whole point.

### B) Updates on tracked cases

For each of the 15, search for: cause of death or disappearance rulings, legal proceedings, search status, missing-to-found transitions, new witness statements, evidence disclosures, family statements including objections to the framing, and FOIA releases.

**Every update must be re-scored, not just appended.** An update that adds an unexplained fact may move a case up. An update that supplies a conventional explanation may move it down. Section 3 governs both directions.

### C) Institutional and political

House Oversight, Senate Intelligence, any new committee interest; FBI investigation updates; White House statements; PURSUE file releases; DoD, DOE, and NNSA statements; new media investigations; skeptical and debunking coverage; Wikipedia article changes.

**Skeptical coverage is collected as a grading input, not as a rebuttal to answer.** See Section 4.

---

## Section 3: The scoring rubric

Every case carries three independent scores plus a composite tier. **The axes are never summed.** Summing them destroys the information the tracker exists to surface.

### Axis S: Sequence Anomaly

Count the **independently documented, individually unexplained** links in the chain around the event.

| Score | Rule |
|---|---|
| **S3** | Three or more independently documented odd links forming a chain. The sequence is the finding |
| **S2** | Two documented unexplained elements |
| **S1** | One unexplained element |
| **S0** | No anomalous sequence. A conventional account covers the facts |

**Counting rules, applied strictly:**

1. A link counts only if it is **documented by a source**, not inferred. "The timestamp was corrected by 13h58m" counts. "That seems like a long time to be at an airport" does not.
2. A link counts only if it is **individually unexplained**. If a source offers an explanation and it holds, the link does not count even if it feels odd.
3. Two facts from the same source describing the same event are **one link**, not two.
4. **The absence of information is not a link.** "No cause of death disclosed" is an unexplained residual, which feeds the Tier A test, not the S count.
5. If a link is **contested between sources**, it does not count toward S until resolved. Log it in `conflictingSources`.

**Worked example, Grillmair, S3:** (a) Snyder arrested Dec 20 with a loaded unregistered rifle, (b) released after three days, (c) felony charge dismissed with no explanation ever given, (d) killing eleven days later. Four documented links, none individually explained by any source. Note that "Grillmair reported him" is **not** counted -- his widow disputes it, so under rule 5 it is excluded. **The S3 holds without it.**

### Axis P: Personal Program Proximity

What the individual is **documented** to have held.

| Score | Rule |
|---|---|
| **P3** | Active access to classified, compartmented, nuclear, propulsion, or UAP-adjacent programs at the time of the event |
| **P2** | Former or adjacent access, or work in a sensitive domain without documented program access |
| **P1** | Scientific or technical role with no sensitive access documented |
| **P0** | No defense, aerospace, nuclear, or intelligence nexus of any kind |

**P is the axis most often inflated by aggregator coverage.** Two corrections already made on this axis: Steven Garcia's "top clearance, nuclear weapons access" was unsourced and became P2 with the role recorded as property custodian; Neil McCasland's retiree clearance was confirmed by BCSO as standard, not active operational access, so P2 not P3.

**Rule: a clearance characterization requires a primary or named-official source.** Aggregator assertion is not sufficient. When in doubt, score down and log it.

### Axis I: Institutional Channel

Scored on the **employer**, not the person.

| Score | Rule |
|---|---|
| **I3** | FFRDC, national laboratory, documented JASON / IDA / MITRE / classified-advisory lineage, or direct participation in a DARPA or DoD joint program |
| **I2** | Major research university or NASA center with substantial federal defense or energy funding |
| **I1** | Research institution with no documented classified channel |
| **I0** | Private-sector employer with no government research nexus |

**The I axis establishes plausibility of channel, not evidence of use.** Ten of fifteen cases sit at I3, which cuts both ways: it supports the argument that these people worked inside institutions with real classified channels, and it reflects that FFRDCs and national labs employ tens of thousands, which is the denominator problem the base-rate literature raises. **Never present a high I as evidence of anything having happened.**

### Composite tier

| Tier | Rule |
|---|---|
| **A** | At least one specific unexplained fact that no source has accounted for, **AND** (S2+ or P3 or I3) |
| **B** | Genuinely unresolved, but a prosaic explanation is available and has not been ruled out |
| **C** | A conventional explanation is documented and holds. Retained for completeness |

**The Tier A test has two halves and both are required.** The unexplained residual is the gate. A case can be S3/P3/I3 and still be Tier B if every fact in it has been accounted for by somebody. Conversely a case can be S1 and reach Tier A on a single genuinely unexplained fact plus one high axis, which is exactly Maiwald.

**Removing Tier C cases would weaken the tracker, not strengthen it.** They are the proof the list is not curated.

### Re-scoring discipline

Run this on every update, in this order:

1. Did an update supply an explanation for a previously unexplained link? **Decrement S.**
2. Did an update remove the unexplained residual entirely? **The case leaves Tier A**, regardless of axis scores.
3. Did a primary source contradict a clearance characterization? **Re-score P down and log the correction.**
4. Did a source conflict emerge on a link that was counting toward S? **Stop counting it** and log it in `conflictingSources`.
5. Record the change in the corrections table in `PROJECT.md`. **A tracker that silently fixes its own data is not auditable.**

**Never promote a case on a claim you have not personally traced to a primary source.** The August 7 Sullivan check is the reference case: the promotion condition was "verify the scheduled testimony date," the check found the hearing was announced 180 days after his death and he was not a listed witness, and the case correctly stayed at Tier B. **Failing to promote is a successful outcome.**

---

## Section 4: The skeptical literature as a grading instrument

The counterarguments are not a section to rebut. **They are the instrument that produces the tier assignments.**

| Use | How |
|---|---|
| Base rates | Novella's institution-level analysis supplies matched denominators. Apply it against any cluster or count claim before publishing one |
| Specific alternatives | Where a skeptic offers a concrete alternative explanation and it holds, the affected link stops counting toward S |
| No alternative offered | Where skeptics offer only the base rate and no specific alternative, that is a real signal. **Maiwald is the clean example** and it is why he is Tier A on a thin file |
| Skeptic errors | Log them for accuracy, not as points scored. Shermer compressing the Ning Li facts is logged in `PROJECT.md` and it does not help the pattern case |

A hostile reader will attack the weakest entry to discredit the whole set. **The weakest entries must therefore be labeled as such by the tracker itself.**

---

## Section 5: Source rules

### Blocklist, absolute

Do not cite or rely on: **strangehappen.com, theheartysoul.com, hannahhowell.com, mysterylores.com, frontpagenewspaper.com, headlinereporter.com, factually.co, slaynews.com, vigilantfox.com, ConservativeBrief, Medium reposts.** These recycle identical errors and manufacture timestamps on old material.

**Read-for-framing-only, never cite:** Principia Scientific, planet-today, americanwirenews, Gateway Pundit, shootingnewsweekly, internewscast, patriotnewsalerts, capitalisminstitute, bizpacreview. They are useful for seeing how a claim is being distorted downstream, which is itself diagnostic. They are never a factual source.

### Reliability tiers

| Tier | Sources | Use |
|---|---|---|
| **Primary** | Court records, DA and agency releases, House and Senate documents, congressional press releases, medical examiner findings, obituaries and funeral records, FOIA productions | Can stand alone |
| **Established outlet** | LA Times, Newsweek, CNN, The Guardian, BBC, NY Post, AP, City News Service and its subscribers (Antelope Valley Press, Pasadena Now), LA Magazine, DefenseScoop | Two independent required for a new case |
| **Domain outlet** | NewsNation, Liberation Times, The Debrief | Usable, attribute explicitly, prefer when they quote a primary |
| **Aggregator** | Everything else | Lead generation only. Trace to the original or drop it |

### Verification standard

- A **new case** requires two independent established-outlet sources, or one primary.
- A **score change** requires a primary source or a named official quoted in an established outlet.
- **Record the publication date of every source.** Recycled old material with fresh timestamps is the single most common failure mode in this subject area.
- **Note conflicts rather than resolving them silently.** Several genuine conflicts are logged and they are a credibility feature, not a defect.
- **A documented absence is a finding.** "No source reports the June 5 hearing outcome; here is where I looked" is more valuable than a guess. Record where you looked.

### Never

- Fabricate or imply a connection not supported by a source. **Stewart has been explicit: fake or specious connections defeat the purpose of the project.**
- State an inference as a finding. Label inferences as inferences, in the file, so they are not rediscovered later and mistaken for facts.
- Editorialize against a family. Several families have publicly asked not to have their losses treated as conspiracy material. **Record those statements accurately and do not argue with them.**
- Use an em dash. Double hyphens or restructure.

---

## Section 6: Process flow

| Step | Action |
|---|---|
| **1. Search** | Run Priority 1-4 (Section 7). Four parallel agents, one per tier, works well. Give each agent Section 5 verbatim |
| **2. Triage** | Classify each result: NEW CASE / UPDATE / DEVELOPMENT / SKIP |
| **3. Verify** | Apply Section 5 standards. Cross-reference against `PROJECT.md` for duplicates. Record every URL with its publication date |
| **4. Score** | Apply Section 3 to every new case and **re-score every updated case**, in both directions |
| **5. Snapshot** | Write `scientist-tracker-state-YYYY-MM-DD.md`: sweep date, new cases, updates, developments, score changes with rationale, conflicts, unverified items, and **an explicit list of what was searched and returned nothing** |
| **6. Propagate** | Update `PROJECT.md`: case table, axis tables, corrections log, open questions. **Corrections are logged, never silent** |
| **7. Report** | Brief summary: new case count, key updates, tier changes, developments, decisions needed from Stewart |
| **8. Offer audit** | Ask: **"Do you want to run adversarial review audit?"** Do not run it unless he says yes |

---

## Section 7: Search queries

Refresh the year token each cycle. These go stale; the rubric does not.

### Priority 1: New cases and direct updates

```
"missing scientist" OR "dead scientist" OR "scientist disappear" -fiction -novel -movie
"missing defense" scientist OR engineer OR official 2026
"scientist found dead" (NASA OR JPL OR LANL OR Pentagon OR "Air Force")
site:newsnationnow.com scientist missing OR dead
site:newsweek.com missing scientists
site:cnn.com missing scientists investigation
```

### Priority 2: Named individual updates

```
"Neil McCasland" search OR found OR update
"Steven Garcia" "Kansas City" OR KCNSC
"Monica Reza" "Angeles National Forest" OR "Mount Waterman" OR missing
"Anthony Chavez" "Los Alamos" OR LANL
"Melissa Casias" cause OR manner OR handgun OR "medical examiner"
"Carl Grillmair" OR "Freddy Snyder" trial OR hearing OR arraignment OR 26AVCF00232
"Matthew Sullivan" Grusch OR Burlison OR NASIC
"Amy Eskridge" Huntsville
"Joshua LeBlanc" NASA OR DRACO OR Huntsville
"Frank Maiwald" JPL cause OR "medical examiner"
"Tony Moffatt" OR "Andrew Moffatt" NTSB OR Mooney OR UAH
```

### Priority 3: Institutional developments

```
"House Oversight" missing scientists OR dead scientists
FBI investigation scientists missing review
PURSUE UAP files release site:defensescoop.com
site:oversight.house.gov scientist OR UAP
site:burlison.house.gov UAP OR whistleblower
"missing scientists" Congress briefing OR subpoena OR hearing
```

### Priority 4: Pattern and skeptical analysis

```
"missing scientists" pattern OR cluster OR connection
"missing scientists" "left behind" phone wallet
"missing scientists" propulsion OR nuclear OR plasma
"missing scientists" Huntsville OR "New Mexico" OR JPL
"missing scientists" debunk OR "base rate" OR statistics
site:skeptic.com OR site:sciencebasedmedicine.org missing scientists
```

---

## Section 8: Case schema (v2)

Matches `DESIGN-ADDENDUM-2026-08-07.md`. **This replaces the v1 structure that was in this file.**

```js
{
  id: string,
  name: string,
  status: "missing" | "dead" | "resolved",
  isNonDefense: boolean,

  tier: "A" | "B" | "C",
  sequenceScore: 0 | 1 | 2 | 3,       // S
  significanceScore: 0 | 1 | 2 | 3,   // P
  channelScore: 0 | 1 | 2 | 3,        // I
  tierRationale: string,
  unexplainedResidual: string | null,

  sequenceChain: [
    { date: string, event: string, sourceUrl: string, isAnomalous: boolean }
  ],

  date: string,
  age: number | null,
  location: string,
  affiliation: string,
  institution: string,
  keyDetail: string,
  leftBehind: string[],
  tookWith: string[],
  sources: [{ outlet: string, url: string, date: string }],
  conflictingSources: string[],
  unverified: string[]
}
```

**Field rules:**

| Field | Rule |
|---|---|
| `sequenceChain` | **Required** when `sequenceScore >= 2`. Each link needs its own date and source URL. Links excluded under counting rule 5 do not appear here; they go in `conflictingSources` |
| `unexplainedResidual` | The specific fact no published source accounts for. **Null means the case cannot be Tier A.** This field is the Tier A gate |
| `conflictingSources` | Not decorative. Genuine contradictions between reputable sources. A credibility feature |
| `unverified` | Anything that could not be independently confirmed, including documented absences and where you looked |
| `significanceScore` | Legacy field name for the P axis. Kept for schema compatibility with the design brief |

---

## Section 9: Adversarial review

**Standing instruction. Offer it at the end of any deliverable that feels final. Do not run it until Stewart says yes**, because it consumes context.

The ask: **"Do you want to run adversarial review audit?"**

When running it, act as **his managers** -- the management Stewart presents to. The audit must be robust:

| Check | What it means |
|---|---|
| First-glance parse | Pick apart anything that looks odd or does not read cleanly on first pass. If a reasonable person would stumble, it fails |
| Rendered output | **Actually inspect the output.** If it is a slide or a page, verify nothing overlaps, misaligns, or truncates. Do not audit the source and assume the render |
| Score defensibility | For each tier assignment, ask what a hostile reader attacks first. Every S link must survive Section 3's counting rules |
| Source trace | Spot-check that every load-bearing claim traces to a source at the required reliability tier, with a date |
| Internal consistency | Case table against axis tables against corrections log against open questions. They drift |
| Em dashes | Grep for them. Zero tolerance |

**The weakest entry in any deliverable is the one that gets attacked to discredit the whole set. Find it before his managers do.**

---

## Section 10: File locations

| File | Purpose |
|---|---|
| `PROJECT.md` | **Master. Authoritative on case facts and scores** |
| `RESEARCH-PROCESS.md` | This file. Procedure and scoring rubric |
| `SESSION-HANDOFF.md` | Cross-session context |
| `FINDINGS-YYYY-MM-DD-*.md` | Targeted research on a specific open question |
| `scientist-tracker-state-YYYY-MM-DD.md` | Sweep snapshots, one per sweep |
| `CLAUDE-DESIGN-PROMPT.md` | v2 design brief for Claude Design |
| `DESIGN-ADDENDUM-2026-08-07.md` | Schema and component changes. **Wins over the design prompt where they conflict** |
| `scientist-network-tracker.html` | v1 tracker, being replaced |
| `DESIGN-BRIEF.md` | Superseded by `CLAUDE-DESIGN-PROMPT.md` |
| `scientist-tracker-state-2026-06-20.md` | Superseded by the Aug 7 snapshot |

Repository: `https://github.com/Samizdat-Publications/the-vanishing.git`, branch **`master`**.
