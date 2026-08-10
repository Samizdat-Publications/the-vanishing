# GitHub

repo: Samizdat-Publications/the-vanishing
branch: master

## Last sync

date: 2026-08-07T21:40:00Z

### Updated in this project
- Rebuilt the data layer against `DESIGN-ADDENDUM-2026-08-07.md` and the August 7 state snapshot: 15 cases, three-axis scoring (S/P/I) plus tier, sequence chains, resolved status, non-defense and media-linked tags, and the eight record corrections.
- Rebuilt the timeline as a vertical three-strand chronology (cases, oversight, skeptical record) with a year gutter and rendered date precision. Replaces the horizontal axis, which could not carry 40 labelled entries.
- Built the full dossier panel: narrative, assessment meters, unexplained residual, and four tabs (dossier, chain, links, sources).
- Circuit-routing edges now encode connection strength and carry directional flow particles.

## Screen map

| Screen / artefact | Built from |
|---|---|
| The Vanishing v2 - Reference Mockup.dc.html | DESIGN-ADDENDUM-2026-08-07.md (scoring, chains, statuses), scientist-tracker-state-2026-08-07.md (all 15 records, corrections, skeptical case, family statements), CLAUDE-DESIGN-PROMPT.md |
| vanishing-graph.js | Case records, edge derivation, strength aggregation, force layout, node and edge renderers |
| vanishing-timeline.js | Three-strand chronology and precedent entries |
| DESIGN-SYSTEM.md | CLAUDE-DESIGN-PROMPT.md section 11, extended for the addendum |
| The Vanishing v2 - Design System.dc.html | Interactive companion to the markdown spec |
| COWORK-HANDOFF.md | Implementation prompt, including the photo-sourcing instructions |

## Sync history

- 2026-08-07T19:40:00Z first pass. Built from the v2 brief before the August 7 addendum landed. 14 cases, no scoring model.
