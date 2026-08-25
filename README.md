# The Vanishing

A tracker of deaths and disappearances of US scientists, military officials and
defense-connected individuals since 2021.

**15 cases. 8 Tier A, 2 Tier B, 5 Tier C. 57 months of span. Three axes, never summed.**

Serve the folder and open `the-vanishing-v2.html`:

```powershell
cd "C:\Users\stewa\OneDrive\Documents\Claude\Cowork files\scientist-tracker"
python -m http.server 8971
```
Then browse to `http://127.0.0.1:8971/the-vanishing-v2.html`.

The dashboard is a single HTML file but it is **not** self-contained: it loads
`assets/photos/*` by relative path. Ship the folder, not the file.

---

## What it is

A research instrument built on the working hypothesis that a pattern exists. Its purpose is
to document that pattern and surface connections invisible at the individual case level.

The core analytical claim: **an event prosaic in isolation may not be prosaic in sequence.**
A scientist shot by a disturbed neighbor is a crime story. A scientist shot by a neighbor
who had been reported, arrested with a loaded unregistered rifle, released after three days,
and had his charges dropped eleven days before the killing, is a different object. Nothing
in that chain is invented. It only becomes visible when reconstructed.

**Tier C cases are retained deliberately.** Five of the fifteen have a conventional
explanation that holds. Removing them would weaken this tracker rather than strengthen it,
because a hostile reader attacks the weakest entry to discredit the whole set. The tracker
labels its own weakest entries.

Skeptical literature is used as a **grading instrument**, not a rebuttal section.

## Scoring

Three axes, 0 to 3, **never summed.** A case can be extraordinary on one axis and wholly
unremarkable on another, and collapsing that into one number destroys the information.

| Axis | Question |
|---|---|
| **S** Sequence Anomaly | How many independently documented, individually unexplained links form a chain? |
| **P** Personal Program Proximity | What sensitive access did this person personally hold? |
| **I** Institutional Channel | Does the employer have documented history as a conduit for classified work? |

Tier A requires an unexplained fact that no published source accounts for, **plus**
S2 or higher, or P3, or I3.

## Files

| File | Purpose |
|---|---|
| `SESSION-HANDOFF.md` | **Start here.** Current state, open items, working rules. Written to be self-sufficient. |
| `PROJECT.md` | Master documentation. All cases, institutions, clusters, analysis threads, counterarguments, sources. |
| `scientist-tracker-state-YYYY-MM-DD.md` | Research sweep snapshots. The latest is authoritative on case facts. |
| `RESEARCH-PROCESS.md` | Weekly sweep spec and the canonical case data schema. |
| `PHOTOS.md` | Per-image licence research and provenance for all 15 photographs. |
| `SCORING-DISCREPANCIES.md` | Axis conflicts and how they were adjudicated. |
| `SNYDER-DOCKET-RETRIEVAL.md` | Manual retrieval instructions for the one open court record. |
| `the-vanishing-v2.html` | The current dashboard. |
| `scientist-network-tracker.html` | v1. Superseded, retained for reference. |
| `CLAUDE-DESIGN-PROMPT.md`, `DESIGN-ADDENDUM-2026-08-07.md`, `DESIGN-BRIEF.md` | Design briefs. The addendum is the most recent. |

## Standards

**Nothing here is invented.** No fabricated sources, URLs, document numbers or quotes.
Counterarguments are always carried. Confirmed fact, allegation and open question are
distinguished. Source conflicts are logged rather than resolved by preference.

These are real deaths and real missing people. Several families have publicly asked not to
have their losses treated as conspiracy material. The tracker records those statements
accurately and does not argue with them. The research standard is high for that reason, not
only for accuracy.

## Not to be confused with

**The Legacy Program Dashboard**, a companion board on a different subject
(`github.com/Samizdat-Publications/the-legacy-program-dashboard`). It shares this project's
engine, schema and design system, and uses `the-vanishing-v2.html` as a frozen build input.
The two projects overlap at exactly one node, Amy Eskridge. They are not merged.

## Licence

Not chosen. Photographs are credited individually and are mostly **not** public domain; see
`PHOTOS.md`.
