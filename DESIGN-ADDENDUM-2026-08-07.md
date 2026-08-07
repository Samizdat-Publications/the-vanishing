# The Vanishing v2: Design Addendum, August 7, 2026

**Read this alongside `CLAUDE-DESIGN-PROMPT.md` (commit 313ec1a). Where the two conflict, this addendum wins.**

This addendum exists because the August 7 research sweep changed the data model. The visual system, atmosphere, and animation direction in the main brief are unchanged. What changed is the case count, the schema, and the addition of a scoring model that needs its own components.

---

## Change 1: The case count is 15, not 14

One case was added (James "Tony" Moffatt, Apr 17 2026, UAH aerospace engineer). One case is now formally resolved and must display as such (Nuno Loureiro, closed by the FBI Apr 29 2026). One case is tagged non-defense and must be visually distinguishable (Jason Thomas, Novartis).

The design must handle three terminal states, not two:

| State | Meaning |
|---|---|
| **Missing** | 4 cases. Unresolved, person not located. |
| **Dead** | 10 cases. |
| **Resolved** | 1 case. Perpetrator identified, investigation closed. **Needs its own visual treatment** -- not a third status color competing with dead/missing, but a distinct "case closed" marker that reads as settled rather than alarming. |

Additionally, one case (Thomas) carries a **non-defense** tag. It is deliberately retained to demonstrate the list is not curated. The design should let a reader see instantly that it is in a different category, without the treatment reading as an apology.

---

## Change 2: The scoring model (the significant addition)

Every case now carries three independent scores plus a composite tier. **This is the analytical heart of v2 and it needs first-class design treatment, not a badge in a corner.**

### The axes

| Axis | Range | Question it answers |
|---|---|---|
| **S -- Sequence Anomaly** | S0-S3 | How many independently documented, individually unexplained links form a chain around this event? |
| **P -- Personal Program Proximity** | P0-P3 | What sensitive access did this individual personally hold? |
| **I -- Institutional Channel** | I0-I3 | Does the employer have a documented history as a conduit for classified work? |

| Tier | Meaning |
|---|---|
| **A** | 7 cases. Contains a specific unexplained fact no source accounts for, plus S2+ or P3 or I3. |
| **B** | 3 cases. Unresolved, but a prosaic explanation exists and is not ruled out. |
| **C** | 5 cases. A conventional explanation is documented and holds. Retained for completeness. |

### Why three axes and not one number

The axes are deliberately **not** summed. A case can be extraordinary on one axis and unremarkable on another, and collapsing that into a single score destroys the information the tracker exists to surface.

Two worked examples the design must make legible:

- **Carl Grillmair is S3 / P1 / I3.** He has the strongest documented sequence in the entire file: he reported his eventual killer for trespassing in December, that man was arrested with a loaded unregistered rifle, released after three days, had his charges dropped on February 5, and killed him on February 16. Eleven days. But Grillmair studied dark matter and exoplanets and held no documented clearance -- while working at Caltech IPAC, inside the institution that manages JPL. **A reader must be able to see all three of those facts at once.** A single grade would either overstate or erase him.

- **Joshua LeBlanc is S2 / P3 / I3.** Active nuclear propulsion engineer on DRACO, a DARPA-NASA joint program. Four unexplained hours with his Tesla parked at Huntsville International that morning. Phone and wallet left at home. Dead the same day. He scores high on all three axes and **v1 buried him as a routine entry.** Surfacing cases like this is the entire point of the redesign.

### Required components

**1. Score display on the card face.** Tier plus all three axis scores must be visible without expanding the card. This is the most-used piece of information in the interface. Design a compact, scannable treatment -- three small meters, a 3-segment glyph, whatever reads fastest. It must not look like a rating out of 10, because it is not a quality judgment and must never read as one.

**2. The Sequence Chain timeline (highest priority new component).** Any case scoring S2 or higher carries an ordered array of dated, individually sourced steps, each flagged anomalous or not. This is the Grillmair view. It must render as a compact vertical or horizontal chain on the expanded card, with anomalous links visually distinguished from ordinary ones, each link carrying its own source link and date.

This component is the single most important thing in v2. The project's central claim is that events which look ordinary in isolation are not ordinary in sequence. **If a reader cannot see the chain, the claim is invisible.** Design it first.

**3. The S-by-P matrix view.** A scatter or 4x4 matrix plotting sequence anomaly against personal proximity, with institutional channel encoded as node size or fill. Quadrants should be readable at a glance: high-S/high-P is the strong corner, high-S/low-P is the Grillmair corner, low-S/low-P is the completeness corner. This becomes a primary navigation surface alongside the network map.

**4. Per-axis filtering.** Users must be able to filter and sort on each axis independently, not just by composite tier. "Show me every I3 case with an undisclosed cause of death" is a real query this tracker should answer.

---

## Change 3: Schema

```js
{
  id: string,
  name: string,
  status: "missing" | "dead" | "resolved",
  isNonDefense: boolean,

  tier: "A" | "B" | "C",
  sequenceScore: 0 | 1 | 2 | 3,
  significanceScore: 0 | 1 | 2 | 3,
  channelScore: 0 | 1 | 2 | 3,
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

`sequenceChain` is required for any case with `sequenceScore >= 2`. `unexplainedResidual` is the specific fact no published source accounts for, and it should have a distinct visual treatment wherever it appears -- it is the load-bearing content of a Tier A case.

`conflictingSources` and `unverified` are not decorative. Several cases have genuinely contradictory reporting (Anthony Chavez is described as both a retired HVAC technician and a construction foreman by different sources, one citing police records directly). **The design must have a treatment for "sources disagree" that is visible but not alarmist.** This is a credibility feature.

---

## Change 4: Two new content sections

**Historical Precedent.** A section covering MKULTRA, the Church Committee, the 1975 heart attack gun demonstration, Frank Olson, the JASON advisory group, and the June 30 2026 House Oversight MKULTRA hearing. This is documented declassified history and it establishes that the mechanism the project hypothesizes has precedent. Design it to read as **archival and sober** -- closer to a document exhibit than to the case cards. It should feel like evidence, not like atmosphere.

**The Skeptical Case as grading instrument.** The counterarguments are no longer a defensive section at the bottom. They are the instrument that produced the tier assignments, and the design should present them that way -- integrated with the scoring model rather than quarantined. Where a specific counterargument determined a specific score, the interface should be able to show that link.

Two constraints here. Family statements must be presented with restraint; several families have publicly objected to this framing and the design must not editorialize against them. And the geographic cluster sections must carry their statistical caveat inline, because the base-rate argument cuts directly against the cluster thesis and burying that would be the fastest way to lose a skeptical reader.

---

## Change 5: Data corrections affecting display

Eight case records were corrected. The ones that change what appears on screen:

| Case | Correction |
|---|---|
| Chavez | May 8 2025 (not May 4), Los Alamos (not Espanola). **Had no cell phone at all** -- he must be removed from any "left phone behind" visualization. |
| Reza | Angeles National Forest / Mount Waterman (not Lancaster). Age 60. **JPL affiliation is unconfirmed and must display as such.** |
| Garcia | Age 47. **The "top clearance / nuclear weapons access" claim was unsourced and is removed.** |
| Casias | Remains identified May 31 2026. Role: administrative assistant, not scientist. |
| LeBlanc | Walker County AL (not Florence). Single-vehicle crash. |
| Loureiro | Resolved. Age 47. |
| Thomas | Missing Dec 13 2025, found Mar 17 2026. Non-defense. |
| Ning Li | 2014 campus vehicle collision caused the brain damage leading to Alzheimer's; died 2021 of natural causes. |

The **"Left Everything Behind"** thread needs rework. It now has 4 clean members, not 5+, and it must carry the counterargument inline: retired FBI Special Agent Jennifer Coffindaffer argues this is a recognized signature of suicidal intent read in the opposite direction. The thread's strongest single case is Steven Garcia, who abandoned car, phone, wallet and keys while taking a handgun and leaving on foot -- which neither reading fully explains.

---

## Unchanged from the main brief

Everything in `CLAUDE-DESIGN-PROMPT.md` not contradicted above still stands, specifically:

- The **WebGL/WebGPU network map** as centerpiece, with five node classes and eight edge types
- The **built-in AI Analyst** driving the full dashboard, with a documented command surface
- All visual system, typography, spacing, animation, and atmosphere direction
- Responsive behavior and accessibility requirements
- Single-file HTML output constraint

The network map now has additional edge material worth using: the institutional channel scores create a real, defensible clustering by FFRDC and national laboratory that the map should be able to express.

---

## Priority order

1. **Sequence Chain component** -- without it the project's central claim is invisible
2. Score display on card face
3. Network map (as already specified)
4. S-by-P matrix view
5. AI Analyst (as already specified)
6. Everything else

---

## Non-negotiable

**No em dashes anywhere in generated text or UI copy.** Use double hyphens or restructure the sentence. This applies to every string in the interface, every label, and every piece of documentation you produce.
