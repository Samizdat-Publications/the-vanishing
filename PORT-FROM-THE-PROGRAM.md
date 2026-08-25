# What ports from The Legacy Program Dashboard

**Written 24 August 2026.** Read-only survey of `the-program/data/the-program.json`
(279 people, 689 entities, 2,160 edges, 858 timeline events, 88 entityInfo dossiers).
Nothing in The Program was modified. Nothing has been imported yet. This is the shopping list.

**Bottom line: four things port, and one of them is a Tier 1 primary document that
materially upgrades a case this tracker currently treats as filler.**

---

## 1. Ning Li is named in a released DIA document

**This is the find.** The Vanishing currently says of Ning Li that "the seven-year gap
between the collision and her death substantially weakens any suspicious-death framing, and
the case is retained for the research continuity to Eskridge rather than for its own
anomaly." That framing is now too weak, and it is too weak on documentary grounds, not
interpretive ones.

The Program holds entity `dird-the-role-of-superconductors-in-gravity` with these **Tier 1**
claims:

| Field | Value |
|---|---|
| Title | "The Role of Superconductors in Gravity Research" |
| Document number | **DIA-08-1003-013** |
| Series | Acquisition Threat Support |
| Published | 23 March 2010, ICOD 1 December 2010 |
| Programme | Inside cover: "produced in FY 2009 under the Defense Intelligence Agency [redacted b(3) 10 USC 424] Advanced Aerospace Weapon System Applications (AAWSA) Program" |
| Release | Released by DIA under FOIA, posted in the DIA FOIA reading room |
| Author of record | Dr George Hathaway, Hathaway Consulting, per the DIA letter of 9 January 2018, item 10. The released cover redacts the author under (b)(6). |

And this **Tier 2** claim:

> "The paper reviews the rotating-superconductor gravity-modification claims associated with
> Evgeny Podkletnov and the work of Ning Li."

### What this establishes, precisely

**It establishes that Ning Li's research line was inside AAWSAP's field of view and was
formally reviewed under a DIA advanced-aerospace programme.** That is an **I-axis**
(institutional channel) fact of a quality this tracker rarely gets: a numbered, FOIA-released
government document, in a named programme, reviewing her work by name.

### What it does not establish, and must not be stretched to mean

- It does **not** show DIA funded, employed, tasked, or endorsed her.
- The review was **commissioned from a skeptic of the effect.** Hathaway ran a Podkletnov replication between 1996 and 2003 and got null results. DIA went to the man with a documented record of failing to reproduce the phenomenon.
- The Program's own analyst note makes this point against the grain of its own thesis: "DIA commissioned a review of gravity modification from the one person in the field with a documented history of failing to replicate it. That is not the commissioning behaviour of a programme buying a predetermined conclusion."

**So the honest reading is: the government was seriously enough interested in her research
line to pay for an adversarial technical review of it inside a black-budget aerospace
programme.** That is a real institutional channel. It is not evidence of anything happening
to her. Score it on I, leave S and P alone, and say so explicitly in the record so no
reader mistakes the one for the other.

### Recommended action

Raise Ning Li's **I** score and rewrite her retention rationale. She is no longer retained
"for research continuity to Eskridge." She is retained because a DIA programme document
reviews her work by name. Keep the seven-year-gap counterargument exactly where it is.

---

## 2. The House Oversight probe, with facts this tracker does not have

The Program holds a **Tier A** timeline node `ch-2026-04-21` and entity
`missing-scientists-probe-2026`. Three items here are new to The Vanishing or sharper than
what it carries.

| Fact | Tier | Why it matters here |
|---|---|---|
| The probe covers **eleven** individuals in nuclear or rocket technology who died or vanished since 2022 | 2 | **This tracker has fifteen. Which eleven did the committee pick?** That is an external validation check against a congressional list, and it is the single best available answer to "is this list curated?" If the committee's eleven are a subset of the fifteen, that is strong. If they include someone not tracked here, that is a research lead. |
| **Burlison's staff had been attempting to contact Gen. McCasland regarding a separate congressional investigation before his disappearance** | 2 | Directly relevant to McCasland's **S score**. A man congressional staff were trying to reach about an unrelated investigation vanishes. That is a sequence link, and it is sourced. |
| Briefings demanded from the FBI, the Department of War, NASA and the Department of Energy by **27 April 2026** | 2 | Gives the probe a deadline that has now passed. **Open question: were those briefings delivered?** Nobody appears to have followed up. |

Also available: Burlison's quotation, "How many people walk out their front door without
their phone, their wallet, their keys, or anything? I don't go anywhere without my phone."
That is a congressman making this tracker's own sequence argument on the record, which is
worth having in the counterarguments view.

The Program describes McCasland as "former AFRL commander at Wright-Patterson." This tracker
places him at AFRL and the Kirtland Phillips Research Site. **Reconcile before importing.**
Both can be true across a career, but the records should not silently disagree.

---

## 3. Institution dossiers are ready-made I-axis evidence

The **I** axis asks: does the employer have documented history as a conduit for classified
work? The Program has spent 4,108 tiered claims answering exactly that question about
largely the same institutions.

Mention counts in The Program's dataset for institutions this tracker also uses:

| Institution | Mentions in The Program | Used in The Vanishing by |
|---|---|---|
| Kirtland AFB | 62 | McCasland |
| Wright-Patterson AFB | 60 | Sullivan (NASIC), McCasland (AFRL) |
| Sandia | 43 | context |
| Los Alamos / LANL | 38 / 21 | Chavez, Casias |
| NASIC | 16 | Sullivan |
| AFRL | 9 | McCasland |
| JPL | 3 | Maiwald, Hicks |
| NASA Marshall | 2 | LeBlanc |
| UAH | 2 | Ning Li, Moffatt |

The heavy end of that table is directly reusable. The light end is not: The Program has
almost nothing on JPL, NASA Marshall or UAH, because those are not its subject. **Do not
import the thin ones and pretend they are support.**

Not present in The Program at all, so nothing to port: **DRACO, Mondaloy, AC Gravity LLC,
and Amy Eskridge.** The long-held belief that Eskridge is the overlap point between the two
projects is **wrong as of this dataset** -- she appears zero times in `the-program.json`.
The actual overlap is Ning Li, McCasland and the Oversight probe.

---

## 4. The Bennewitz precedent, and why it matters to the thesis

The Program's `afosi-kirtland-file` dossier opens with a line worth reading twice:

> "The Bennewitz operation is the only place in this domain where the state's method is
> documented rather than inferred."

The documented sequence: 1979, Paul Bennewitz, a physicist running a USAF-supplying
instrumentation company on the edge of Kirtland AFB, records lights and emissions over the
Manzano Weapons Storage Area and reports them in writing to the Air Force. 10 November 1980,
AFOSI generates a record confirming Kirtland security police had themselves observed
unexplained objects in Coyote Canyon. From 1981, rather than investigate its own security
police reports, AFOSI, through Special Agent Richard Doty and the civilian researcher Bill
Moore, begins supplying Bennewitz with fabricated material about underground bases, treaties
and biological experimentation, tailored to what he already half-believed. 1988, Bennewitz
is hospitalised. July 1989, Moore stands up at a MUFON conference and admits the whole thing.

**Nobody killed Paul Bennewitz.** He was fed material calibrated to discredit him, and the
discrediting worked, and he broke. That is a documented instance of neutralisation without
death, run by a US counterintelligence organisation, against a private physicist, adjacent to
a facility that appears in this tracker.

**And the officer who ran it came forward.** The Program carries person node `richard-doty`
(tier B, C1/A2/D2): USAF AFOSI Special Agent 1979-1988, "the only US counterintelligence
officer to have stated on camera and on the record that he personally ran disinformation
about UFOs against American civilians as part of his official duties." Tier 1 supporting
record: his 321-page New Mexico State Police personnel file, obtained under NMSA 14-2-1 et
seq. and published 2021.

Port the node **with The Program's own credibility guard attached**, which is the reason it
is usable: Doty's value "is not that his statements are reliable -- they are not, and he has
repeatedly changed them -- but that his existence is the proof of concept." **Cite Doty for
what he did, never for what he says is true.** See `THESIS-NOTES.md` addendum.

This is the strongest available support for the analytic frame described in
`THESIS-NOTES.md`. It is also the reason that frame has to be handled carefully rather than
enthusiastically: the Bennewitz case is usable **because** it is documented. An inferred
version of the same mechanism, applied to a case where nothing is documented, is not
evidence, it is the shape of evidence. See `THESIS-NOTES.md` for the falsifiability problem
this creates and how to keep it honest.

---

## 5. The two schemas are already compatible

The Program's person record and The Vanishing's are the same shape, because The Program was
built on this project's engine:

```
id, cls, label, status, date, age, loc, locId, instId, sub, cluster, tier,
<three axis scores>, domains[], narrative, claims[], chronology[]
```

The Vanishing scores **S / P / I**. The Program scores **C / A / D** (custody proximity,
access level, disclosure role). Both are 0 to 3 and both are never summed. Everything else
matches.

**Two things The Program has that this tracker should adopt when it goes multi-file:**

1. **Per-claim tiering.** Every claim carries `tier: 1 | 2 | 3` -- documented / sourced claim / stated inference. The Vanishing tiers whole cases but not individual claims, which means a Tier A case can contain an unmarked inference. Per-claim tiering fixes that and it is the single highest-value structural import.
2. **Sources arrays on claims rather than a bibliography at the bottom.** Makes every assertion individually auditable and makes an automated verification gate possible.

The Program's `tools/verify.py` pattern is worth copying too: it asserts facts, fails the
build, and **every check is itself tested** against input it must reject. Three of its first
eight checks were born broken and silently passing, which is exactly the failure mode a
research project cannot afford.

---

## Import order, if and when

| # | Item | Effort | Value |
|---|---|---|---|
| 1 | Ning Li DIRD, rescore I, rewrite retention rationale | Low | **High** |
| 2 | McCasland: Burlison staff contact attempt, probe details | Low | **High** |
| 3 | Identify the committee's eleven and diff against the fifteen | Research task, not an import | **High** |
| 4 | Per-claim tiering and sources arrays | Structural, do it during the multi-file rebuild | High |
| 5 | Kirtland / Wright-Patterson / LANL / Sandia institution claims as I-axis support | Medium | Medium |
| 6 | Bennewitz as a documented precedent in the analysis view | Low | Medium, handle per `THESIS-NOTES.md` |
| 7 | `richard-doty` node, **with its credibility guard**, as the operator testimony behind Bennewitz | Low | Medium. Cite him for what he did, never for what he says is true. |

**Analyst requirements note.** Stewart's aggregate framing -- disconnected evidence that is
prosaic in a vacuum but shows a pattern in aggregate -- is a build requirement, not just a
thesis. It means the analyst has to compute cross-case co-occurrence, state base rates
alongside findings, separate rule-derived links from hand-sourced ones, report negative
results, and show which cases carry each finding. The rule: **an aggregate claim must be
reproducible from the data by someone who does not share the premise.** Full spec in the
`THESIS-NOTES.md` addendum.

**Rule for all of the above: copy the claim and its source, not the conclusion.** The
Program is written from a stronger premise than this tracker uses. Its narrative voice
assumes the programme exists. The Vanishing's does not get to assume its pattern exists,
because that is the thing it is trying to demonstrate.
