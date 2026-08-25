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
