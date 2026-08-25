# The Vanishing -- project instructions

Personal research project of Stewart Gregerson. Tracks deaths and disappearances of US
scientists, military officials and defense-connected individuals since 2021.

**This is not employer work. No employer branding anywhere.**

## Read order for a fresh session

1. `SESSION-HANDOFF.md` -- current state, open items, working rules. Read this first.
2. `PROJECT.md` -- the case records and the full argument.
3. The latest `scientist-tracker-state-*.md`.
4. `ARCHITECTURE.md` before any structural work. `THESIS-NOTES.md` before any scoring work.
5. `DISCOVERY-PROTOCOL.md` and `LEADS.md` before any research sweep. Both are required steps,
   not suggestions.

## Repository facts

| Item | Value |
|---|---|
| Remote | `https://github.com/Samizdat-Publications/the-vanishing` (private) |
| Default branch | **`master`**, not `main` |
| Entry point | `the-vanishing-v2.html`, served from the repo root |

Do not confuse this with **The Legacy Program Dashboard**
(`Samizdat-Publications/the-legacy-program-dashboard`). Different project, different repo.
The only crossover is that The Program pins a frozen copy of `the-vanishing-v2.html`
at its own `ref/`. Changes here do not propagate there, and that copy is never edited.

## Serving the dashboard

The HTML is one file but it is **not** self-contained: it loads `assets/photos/*` by relative
path. Ship the folder, not the file.

```bash
cd /home/user/the-vanishing
python3 -m http.server 8971
```
Then open `http://127.0.0.1:8971/the-vanishing-v2.html`.

## Writing rules

- **No em dashes.** Not in generated text, UI copy, documentation or commit messages.
  Use double hyphens or restructure. This has been held on every file so far. Keep it that way.
- Tables over bullet lists for comparative content. Charts get data labels.
- Terminal commands include the `cd`, so they are copy-pasteable.

## Research rules

- **Never fabricate connections.** Always carry counterarguments. Distinguish confirmed fact
  from allegation from open question. Flag anything unverifiable. Note where sources conflict.
- **Never fabricate URLs, case numbers or document numbers.** If a URL cannot be verified to
  resolve, say so.
- Anything Stewart names in conversation that is not already tracked goes into `LEADS.md`
  immediately, marked unverified. Called out once should mean captured forever.
- Do not cite: strangehappen.com, theheartysoul.com, hannahhowell.com, mysterylores.com,
  frontpagenewspaper.com, headlinereporter.com, factually.co, slaynews.com, vigilantfox.com,
  ConservativeBrief, Medium reposts. These recycle identical errors and manufacture
  timestamps on old material.
- These are real deaths and real missing people. Several families have publicly asked not to
  have their losses treated as conspiracy material. The tracker records those statements
  accurately and does not argue with them.

## Scoring

Three independent axes plus a composite tier. **The axes are never summed.**

| Axis | Range | Question |
|---|---|---|
| **S** Sequence Anomaly | 0-3 | How many independently documented, individually unexplained links form a chain? |
| **P** Personal Program Proximity | 0-3 | What sensitive access did this person personally hold? |
| **I** Institutional Channel | 0-3 | Does the employer have documented history as a conduit for classified work? |

Tier A = an unexplained fact no source accounts for, plus (S2+ or P3 or I3).

Do not raise axis scores on the strength of the neutralisation frame alone. See
`THESIS-NOTES.md`, which records the frame and the falsifiability problem it creates.

## Settled decisions -- do not re-litigate

- **Photograph rights.** Publicly findable images are used with per-image credit. The licence
  grading in `PHOTOS.md` is information, not a gate. Stewart has accepted the risk on the
  basis that this is personal research for a small private audience.
- **Tier C cases are retained deliberately**, to prove the list is not curated.
- **The single-file HTML constraint is dropped.** See `ARCHITECTURE.md` for the migration
  order, and do not do step 3 before step 2.

## Adversarial review

At the end of any deliverable that feels final, ask: **"Do you want to run adversarial review
audit?"** Only run it when he says yes, because it consumes context. When running it, act as
his managers, the management he presents to. Pick apart anything that looks odd or does not
parse at first glance, and actually inspect the rendered output.
