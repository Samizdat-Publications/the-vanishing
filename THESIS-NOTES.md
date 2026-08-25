# Thesis notes

**Stewart's analytic frame, recorded 24 August 2026, in his own reasoning.**
This is context for how cases are read. It is not itself a claim the tracker asserts.

---

## The neutralisation frame

The tracker's stated hypothesis has been that a pattern exists in the deaths and
disappearances. Stewart's refinement is that **death is one outcome of the pattern, not the
definition of it.** The object being tracked is not "people who were killed." It is
**people attached to sensitive programmes who fell out of good standing and were
subsequently removed from play**, by whatever means.

In his framing, the mechanism is selected for cost. Killing everyone is expensive and
eventually blows the cover. Discrediting is cheaper and more durable. A researcher who has
had a serious accident and subsequently developed dementia is neutralised more completely
than a dead one, because a dead one becomes a martyr and an incapacitated one becomes
unreliable. Anything she says afterwards about antigravity can be written off by anyone who
wants to write it off, without anyone having to do anything further.

Applied to **Ning Li**: the seven-year gap between the 2014 collision and her 2021 death is
currently treated by this tracker as weakening her case. Under the neutralisation frame the
gap is not exculpatory, because the operative event on that reading is the collision, not
the death. Vehicle collision is a documented assassination method in the historical
literature on US intelligence services, though its use in any specific case here is
unevidenced and should never be asserted.

He also holds a broader suspicion, explicitly beyond what this dataset supports: that
capabilities exist for inducing rare fast-progressing cancers, by analogy to the heart
attack gun disclosed to the Church Committee, alongside more conventional methods.
**Recorded as his working suspicion. Not asserted anywhere in the tracker.**

---

## Why this is analytically serious

It is not a rescue of weak cases. It does three real things.

**It gives the tracker a stated causal model.** A list of anomalies is weaker than a list
plus a mechanism, because a mechanism makes predictions. This one does: it predicts
incapacitation and discrediting events should appear alongside deaths, and that they should
cluster on the same institutional channels.

**It has a documented precedent.** See `PORT-FROM-THE-PROGRAM.md` section 4. Paul Bennewitz,
a physicist beside Kirtland AFB, was fed fabricated material by AFOSI calibrated to what he
already half-believed, was hospitalised in 1988, and the operation was publicly admitted by
one of its participants in 1989. That is neutralisation without death, by a US
counterintelligence organisation, against a private scientist. The Program's own dossier
calls it "the only place in this domain where the state's method is documented rather than
inferred." **A frame with one documented instance is in a different category from a frame
with none.**

**It explains a real selection problem.** If the tracker only counts deaths, it is measuring
the most expensive and least likely tool in the kit and calling that the pattern.

---

## The problem it creates, stated plainly

**The frame is close to unfalsifiable, and that is a real cost, not a quibble.**

If death counts, and incapacitation counts, and discrediting counts, and a career ending
counts, then almost any adverse outcome befalling anyone near a sensitive programme becomes
confirming evidence. A hypothesis that cannot fail is not doing work. Worse, it is exactly
the move a hostile reader expects, and finding it lets them dismiss the strong cases along
with the weak ones.

Stewart's own stated standard is the constraint here: **no fake or specious connections, and
rigor serves the argument rather than opposing it.** The Bennewitz case is usable *because*
it is documented. Applying the same mechanism to a case where nothing is documented does not
inherit that credibility. It borrows its shape.

### The distinction that has to hold

| Legitimate | Not legitimate |
|---|---|
| Widening the **scope of outcomes tracked** so incapacitation is recorded as an event type | Treating "was incapacitated" as evidence that someone *caused* the incapacitation |
| Noting that a documented neutralisation method exists, and citing Bennewitz for it | Inferring that method was used in a case with no supporting record |
| Recording that Ning Li's research line was formally reviewed by DIA, because a document says so | Inferring the 2014 collision was engineered, because nothing says so |

The second column is where this project would lose the argument.

---

## What to actually do about it

**Recommendation: implement the frame as a data field, not as a scoring thumb.**

Add an **outcome type** dimension to the case schema, orthogonal to S / P / I:

```
outcome: dead | missing | resolved | incapacitated | discredited | career-terminated
```

That lets the tracker record Ning Li's 2014 collision as an event in its own right, on its
own date, without asserting a cause and without inflating any axis. It makes the
neutralisation frame **visible and checkable** rather than baked silently into scores. A
reader can then look at the distribution of outcome types and judge the mechanism claim for
themselves, which is the same thing the three-axis model does for the anomaly claim.

Do **not** raise S, P or I on the strength of the frame alone. Raise Ning Li's **I** because
of `DIA-08-1003-013`, which is a document. Leave her S alone until something documents the
collision as anomalous.

State the frame explicitly in the analysis view, including this falsifiability problem. A
tracker that names the weakness in its own thesis is much harder to attack than one that
waits for a critic to find it, and this project already applies that logic to its Tier C
cases.

---

## Open research questions this frame generates

| # | Question | Why |
|---|---|---|
| 1 | Which **eleven** individuals did the Comer-Burlison probe name? | An external list to diff against the fifteen. Best available curation check. |
| 2 | Are there incapacitation or discrediting events among people already tracked, that were never recorded because only death was counted? | Directly tests the frame's central prediction. |
| 3 | Does the 2014 Ning Li collision have any documented anomaly at all -- police report, litigation, insurance record? | Currently the frame rests on it with nothing under it. Either something is there or the case stands on the DIRD alone. |
| 4 | Were the 27 April 2026 briefings to Oversight from FBI, Department of War, NASA and DOE ever delivered? | Nobody appears to have followed up. |

---

# Addendum: Doty, and the aggregate problem

Added 24 August 2026, after Stewart's second pass on the Bennewitz material.

## The operator came forward

Bennewitz is stronger than "a documented case" because **the officer who ran the operation
subsequently described it himself, publicly and on the record.**

Richard C. Doty, USAF AFOSI Special Agent 1979-1988, later a New Mexico State Police officer.
The Program carries him as person node `richard-doty`, tier B, C1/A2/D2. Its narrative makes
the point better than a summary would:

> "Doty is the only US counterintelligence officer to have stated on camera and on the record
> that he personally ran disinformation about UFOs against American civilians as part of his
> official duties. [...] Doty's value to this board is not that his statements are reliable --
> they are not, and he has repeatedly changed them -- but that his existence is the proof of
> concept. The United States assigned a counterintelligence officer to manage the UFO
> information environment. He has said so. Whatever else is in dispute, that is not."

Supporting claims on that node:

| Tier | Claim |
|---|---|
| 2 | Doty has stated publicly that he provided false documents and false information to Bennewitz as part of his AFOSI duties |
| 1 | His complete releasable New Mexico State Police personnel file runs to 321 pages, obtained under NMSA 14-2-1 et seq. and published 2021 |
| 2 | He showed Linda Moulton Howe a document at Kirtland in April 1983 that she describes as a briefing paper on retrieved craft and occupants |

Stewart's additional point, recorded as his position: Doty is now broadly pro-disclosure,
describes how badly Bennewitz and others were treated, maintains the underlying phenomenon is
real and non-human, and characterises the practice as routine rather than exceptional.

## The credibility guard that has to travel with him

**Doty is an unreliable narrator and the tracker must say so in the same breath it cites
him.** He has changed his account repeatedly, including altering details of the fabricated
document he passed to Bennewitz, and at one point misattributing the investigating agency.
Some of his later claims are unfalsifiable and some are self-serving.

The load-bearing inference is narrow and survives all of that:

- **Not** "Doty says X, therefore X."
- **But** "a US counterintelligence officer has stated on the record that managing the civilian UFO information environment was his official duty, and the documentary record around Kirtland is consistent with that."

An unreliable witness admitting his own participation in an operation is evidence of the
operation in a way that his claims about anything else are not. **Cite Doty only for what he
did, never for what he says is true.** That distinction is what keeps him usable.

His claim that the practice was widespread and long-running is **his characterisation**, not
a documented finding. Record it as his statement, attributed, tier 2 at best. It is a
research lead, not a conclusion.

## The aggregate problem, and what it demands of the analyst

Stewart's framing, and it is the sharpest statement of this project's purpose yet:

> "There's a lot of disconnected evidence that, in a vacuum, has a prosaic explanation but
> when viewed in aggregate shows the broader pattern of how they operate."

This is the same structure as the tracker's founding insight -- an event prosaic in isolation
may not be prosaic in sequence -- generalised from one case's timeline to the whole corpus.
It is also, stated plainly, **the single hardest thing to do honestly**, because "individually
explainable, collectively damning" is the exact shape of both a real intelligence finding and
a conspiracy theory. The difference between them is method, not conviction.

### What this means the analyst has to be built to do

Not "summarise the cases." Surface structure that is invisible per case:

| Capability | Why |
|---|---|
| **Cross-case co-occurrence** -- institutions, geography, programme, timing, method appearing together more than chance would predict | This is the actual claim being made. It has to be computed, not asserted. |
| **State the base rate alongside every aggregate finding** | Without it, any sufficiently large corpus produces striking coincidences. With it, the finding either survives or it does not. |
| **Separate rule-derived links from hand-sourced ones** | The Program already does this and calls it the thing that stops the graph inventing relationships. Adopt it. |
| **Report the negative result when there is one** | An analyst that only ever finds patterns is a pattern generator, not an analyst. If a proposed cluster is no denser than chance, say so, in the interface. |
| **Show which cases carry a finding** | So a reader can check whether an "aggregate pattern" is really two strong cases and eleven passengers. |

### The rule

**An aggregate claim must be reproducible from the data by someone who does not share the
premise.** If the only way to see the pattern is to already believe it, it is not a finding.
Build the analyst so its outputs can be checked, and let the ones that survive checking carry
the argument. That is the same logic that made Tier C cases worth keeping.

---

## The control group, found 25 August 2026

**This is the most useful thing the survey of The Legacy Program Dashboard produced, and it
does not help the pattern. That is why it matters.**

The previous section demands that an aggregate claim be reproducible by someone who does not
share the premise. Doing that requires a denominator, and the tracker has never had one. It
now has a candidate.

### The AAWSAP DIRD author cohort

The 38 Defense Intelligence Reference Documents were produced 2008-2010 under the DIA
Advanced Aerospace Weapon System Applications programme. **Roughly twenty-three of their
authors are individually named, and the membership list is public** at
`https://irp.fas.org/dia/aatip-list.pdf`.

Named: Puthoff, Eric W. Davis (five DIRDs), Kit Green, Friedwardt Winterberg (two), Wil
McCarthy, Claudio Maccone, Vincent Teofilo, William Culbreth (two), George Miley, Ulf
Leonhardt, Bruce Towe (two), Robert M. L. Baker Jr., Marc Millis, Richard Genik (three),
George Hathaway (two), Sergey Macheret, Gerald A. Smith, James Wells, Paul Czysz, John
Cramer, Richard Obousy, J. Albertine, J. Golightly.

**This is a named, closed, documented cohort of scientists formally engaged by a DIA
advanced-aerospace programme.** Their P-axis and I-axis exposure is comparable to, and in
several instances greater than, that of cases already in the tracker. George Hathaway is
already cited in the Ning Li record as the author of `DIA-08-1003-013`.

### Their mortality is unremarkable

Three deaths located, none anomalous: **Vincent Teofilo**, 10 January 2026, aged 81, ordinary
published obituary; **Claudio Maccone**, 2025, aged 77, non-US; **Paul Czysz**, 2013,
pre-window. Nobody has asserted an anomaly about any of them.

### What this obliges the tracker to say

**A group with equal or greater programme proximity, formally contracted to the exact DIA
programme the tracker treats as the institutional channel, shows no elevated rate of death or
disappearance.** That is a real result and it belongs in the argument, stated in the
tracker's own voice rather than waited for from a hostile reader.

It does not refute the thesis. The fifteen are not claimed to be a random sample of
programme-adjacent scientists, and the sequence anomalies in cases like Grillmair and Casias
are facts about those cases regardless of any base rate. But it does remove one move from the
table: **the tracker cannot argue that proximity to this programme is itself predictive**,
because here is a cohort defined by exactly that proximity, and nothing happened to them.

**Recommended use.** Build the cohort out as a comparison population and report it beside the
fifteen. It is worth more to the argument as a denominator than any additional case would be
as a numerator, because it is the thing that makes the numerator legible. It is also the
single best answer to Novella's base-rate objection, which the tracker currently logs as
unanswered.

**Recommended against.** Do not add these people as cases. Do not describe the cohort as
"also at risk". Do not go looking for an anomaly among them, which is how a control group
stops being one.

## Two suspected mechanisms, searched for and not found

`LEADS.md` section C records two of Stewart's suspicions: **vehicle collision as an
assassination method**, and **induced rare fast-progressing cancer** by analogy to the heart
attack gun disclosed to the Church Committee in 1975.

The 25 August 2026 survey looked for both across The Program's entire corpus: 279 people, 689
entities, 858 timeline events, 88 dossiers. **Neither is supported at any tier.**

Literal string searches returned: **"Church Committee" zero occurrences. "heart attack gun"
zero. "MKULTRA" nineteen, every one attached to a single House Oversight Task Force hearing
of 30 June 2026, none with any operational detail.** There is nothing anywhere in that corpus
on staged accidents, poisoning, induced illness, or vehicle collision as method.

**Recorded as a documented absence, which is a finding.** The corpus most likely to contain
such material does not contain it. Both suspicions stay in `LEADS.md` as suspicions, now with
a stated search behind the absence rather than an untested assumption. Neither may be
asserted about any tracked case.

## Documented institutional interest, and the line it does not cross

Verified 25 August 2026 from primary sources. **This section exists to hold a real finding
and its limit in the same place, because the limit is the part that gets dropped.**

Three dated instances of the US government pursuing the rotating-superconductor and
gravity-modification research line:

| When | What | Status |
|---|---|---|
| 2001 | DoD grant to Ning Li's AC Gravity LLC | Already in the tracker |
| 2008-2010 | DIA AAWSAP commissions `DIA-08-1003-013`, reviewing the rotating-superconductor claims associated with Podkletnov and Li's work | Imported 25 Aug 2026 |
| 2015-2019 | Navy files six patent applications by a NAWCAD engineer covering inertial mass reduction, high-frequency gravitational waves, room-temperature superconductivity and plasma compression fusion, all assigned to the Secretary of the Navy | Verified from USPTO PDFs |

**That is roughly two decades of documented, funded, agency-level interest in one research
area.** It is the strongest available support for the proposition that this subject matter
attracts real institutional attention, and none of it requires believing anything about the
phenomenon itself.

### The three things that must travel with it

**1. Every one of those efforts ended in a negative or an abandonment.** NAWCAD spent
$508,000 across three fiscal years and concluded the effect could not be proven. The
superconductor and fusion applications were abandoned for failure to respond to an office
action, the cheapest way to let a filing die. Both flagship granted patents were allowed to
lapse for non-payment of maintenance fees in 2023. The DIRD itself was **commissioned from a
researcher with a documented record of failing to replicate the effect.**

**2. The documents do not connect to each other through Ning Li.** The complete reference
lists of all three granted Pais patents were read in full. Neither Li, nor Podkletnov, nor
Hathaway, nor `DIA-08-1003-013` appears in any of them. The link runs through **Puthoff**.
**The overlap with her case is thematic, at the level of subject area, and must be written in
exactly those words.**

**3. There is no victim anywhere in this thread.** Salvatore Pais is alive. James Sheehy,
Philip Bonzell and the rest are people who did their jobs, and one of them, Bonzell, is the
documented internal objection: a federal examiner who said no in writing and was overridden
by rank. **He is worth more to this tracker's credibility than the patents are**, because he
shows the institution containing its own friction.

**The move this forecloses.** It is tempting to run the sequence 2001 grant, 2010 DIRD, 2015
patents, and land on a tracked person. Nothing in the documents supports that step, and
taking it would be the specious connection the project's editorial stance exists to prevent.
**Institutional interest in a subject is not evidence about a person who worked on it.**
