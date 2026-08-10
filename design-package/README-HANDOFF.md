# The Vanishing v2 -- Design Handoff

Prepared 7 August 2026, against `DESIGN-ADDENDUM-2026-08-07.md` and the August 7 state snapshot.

Hand this whole folder back to Claude Cowork. Start it with the prompt in `COWORK-HANDOFF.md`.

## What is in here

| File | What it is |
|---|---|
| `The Vanishing v2 - Reference Mockup.dc.html` | **The definitive visual target.** Open it in a browser. All seven views work, the graph is live, the dossier is real, the analyst drives the dashboard, the settings panel stores a key. |
| `DESIGN-SYSTEM.md` | **The binding spec.** Every colour, size, motion token, node and edge treatment, the scoring model, the confidence system, the command surface, the credential flow. Read this before writing code. |
| `The Vanishing v2 - Design System.dc.html` | Interactive companion to the spec. Live swatches, live node states, the strength ramp drawn by the production renderer. |
| `vanishing-graph.js` | Working engine: case records, edge derivation, strength aggregation, force layout, node and edge renderers, the left-behind membership rule. Port it, do not reinvent it. |
| `vanishing-timeline.js` | Three-strand chronology entries and the precedent set. |
| `COWORK-HANDOFF.md` | The implementation prompt, including the photograph sourcing instructions. |
| `github.md` | Repo association and screen map. |
| `Edge Study A-D` | The four edge languages prototyped before circuit routing was chosen. Reference only. |
| `Shell A / Shell B` | Literal terminal versus modern chrome. Shell B won and became the mockup. |

## The decisions this package locks in

| Question | Answer | Where |
|---|---|---|
| Shell | Workstation: fixed left rail, canvas centre, dock right, analyst across the bottom | Spec 2 |
| Edge language | Orthogonal circuit routing, strength encoded, directional flow particles | Spec 3.3 |
| Node language | Dossier plate, 100x40, widening to 132 only when a real photograph exists | Spec 3.2 |
| Scoring | Three unsummed axes (S, P, I) plus tier A/B/C | Spec 3.6 |
| Timeline | Vertical, three strands, year gutter, rendered date precision | Spec 6.4 |
| Dossier | Four tabs, second most important surface in the product | Spec 6.2 |
| Analyst | Bottom command bar, full command surface, scripted fallback with no key | Spec 4 |
| Model | claude-sonnet-5, balanced reasoning effort, user-supplied Console key | Spec 4.6 |
| Renderer | WebGPU first, WebGL2 fallback, canvas-2D floor | Spec 3.1 |

## The five rules worth not breaking

1. **The axes are never summed.** Grillmair is S3/P1/I3 and LeBlanc is S2/P3/I3. A single grade would erase one of them.
2. **Derived connections stay separate from editorial ones** in the data layer, so the map cannot invent a relationship.
3. **Every claim carries a confidence treatment.** Solid signal for computed, dashed amber for reported, dotted grey for open.
4. **Absence is printed as absence.** `NOT REPORTED`, `NOTHING RECORDED`, `No attributed source on file`. Never blank, never zero.
5. **No em dashes in any string.** Non-negotiable, per the addendum.

## Known open items for the implementer

- **Photographs.** None of the 15 records carry one. `COWORK-HANDOFF.md` has the licence-first sourcing instructions. Where nothing clears, render nothing: the plate narrows and the layout closes up.
- **Axis scores.** Grillmair and LeBlanc match the addendum's worked examples exactly. The other thirteen are the design's reading of the rubric and want Stewart's review.
- **Moffatt** is included and tagged `MEDIA-LINKED ONLY`. He is on no mainstream list. Inclusion is a live editorial decision.
- **Not yet built:** the S-by-P matrix view (addendum priority 4), per-axis filtering, the Historical Precedent section as a full view rather than the timeline strip, and `frameNodes` / `highlightPath` / timeline zoom on the command surface.
