# Scoring Discrepancies: PROJECT.md versus the v2 data layer

**Raised August 10, 2026, during the v2 build. Needs your adjudication. I have not silently changed any score.**

Claude Design's `vanishing-graph.js` carries axis scores that differ from `PROJECT.md` on eight of fifteen records, and on one composite tier. Its own README flags this: *"Grillmair and LeBlanc match the addendum's worked examples exactly. The other thirteen are the design's reading of the rubric and want Stewart's review."*

The built app reads from the data layer, so **the running dashboard currently shows 8 Tier A cases and 9 at I3, while `PROJECT.md` says 7 and 10.** Every count in the UI now derives from the data rather than from hardcoded copy, so nothing can drift silently, but the two documents still disagree and one of them is wrong.

---

## The one that changes a tier

| Case | PROJECT.md | v2 data | What turns on it |
|---|---|---|---|
| **Anthony Chavez** | **Tier B**, S2/P2/I3 | **Tier A**, S2/P1/I3 | The headline Tier A count, 7 versus 8 |

**The argument for A.** Chavez clears the S2+ half of the gate. The residual question is whether he carries a specific unexplained fact no source accounts for. Candidates: the handwritten journal whose contents were never disclosed, and Los Alamos PD closing the case on October 6 2025 while NM DPS still lists it active. Both are documented, and neither has been accounted for by anybody.

**The argument for B.** A prosaic explanation is available and not ruled out: a 78-year-old man walked away and has not been found. The journal being undisclosed is not the same as being unexplained. And the design simultaneously dropped him to **P1**, which sits oddly next to promoting him -- if his personal proximity is lower than PROJECT.md says, the case for A is weaker, not stronger.

**My read, offered not applied:** the agency-disagreement fact is the stronger residual, and it is genuinely unaccounted for. But the P1/A combination in the design data is internally inconsistent and should not stand as-is either way.

---

## Personal proximity, P axis

| Case | PROJECT.md | v2 data | Note |
|---|---|---|---|
| Monica Reza | **P3** | P2 | Mondaloy co-inventor. Real propulsion IP, but is co-inventing a superalloy *active access to a sensitive program*, or work in a sensitive domain without documented program access? The rubric's P2 language fits the second reading. **The design may be right here.** |
| Anthony Chavez | **P2** | P1 | Retired. Occupation itself is an unresolved conflict in the record (HVAC technician per police reports, construction foreman per aggregators). P1 is defensible on "no sensitive access documented". |
| Steven Garcia | **P2** | P1 | Role recorded as property custodian at an NNSA production facility. The August 7 correction already removed the unsourced clearance claim. P1 or P2 both arguable. |
| Neil McCasland | **P2** | **P3** | **This one runs against you.** PROJECT.md dropped him to P2 specifically because BCSO confirmed a standard retiree clearance, not active operational access, and no Pentagon connection. The design has him back at P3. **PROJECT.md is right and the data is wrong.** |
| Nuno Loureiro | P2 | P1 | Resolved case. Low stakes either way. |

---

## Institutional channel, I axis

| Case | PROJECT.md | v2 data |
|---|---|---|
| Nuno Loureiro | **I3** (MIT Lincoln Laboratory FFRDC, documented JASON lineage) | **I1** |

This is the whole 10-versus-9 difference at I3. PROJECT.md's basis is explicit and correct: MIT PSFC sits inside the institution that runs Lincoln Laboratory, an FFRDC, and MIT has documented JASON lineage. **I3 is right.** The case is resolved and Tier C regardless, so this changes a count and not a conclusion.

---

## Sequence anomaly, S axis

| Case | PROJECT.md | v2 data | Note |
|---|---|---|---|
| Ning Li | **S0** | S1 | PROJECT.md says the medical chain covers the facts, which is S0 by the rubric. The design found one element it read as unexplained. |
| Jason Thomas | **S1** | S0 | Non-defense, ME found no foul play. S0 fits. **The design is probably right.** |

---

## What I recommend

| Action | Why |
|---|---|
| **Fix McCasland to P2 in the data** | Not a judgment call. A named BCSO correction is on the record and PROJECT.md already applied it. The data reverts a correction you already made. |
| **Fix Loureiro to I3 in the data** | The FFRDC and JASON basis is documented in PROJECT.md and the design gives no counter-reason. |
| **Decide Chavez deliberately** | This is the only one that moves a headline number. Whichever way it goes, S, P and tier need to agree with each other. |
| **Accept Reza P2 and Thomas S0** | The design's readings look better than PROJECT.md's on both. |
| **Then re-sync `PROJECT.md` and the data layer in the same commit** | Two sources of truth on the scores is exactly the condition the corrections log exists to prevent. |

Nothing here is applied. Tell me which way on each and I will make both documents agree in one pass.
