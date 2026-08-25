# The Vanishing -- instructions for Claude

Personal research project of Stewart Gregerson tracking deaths and disappearances of US
scientists, military officials and defense-connected individuals since 2021.
**Personal research. Not employer work. No employer branding in any output.**

## Read these first, in this order

1. `SESSION-HANDOFF.md` -- current state, open items, working rules. Self-sufficient by design.
2. `FIRST-TASKS.md` -- ranked opening moves with reasoning.
3. `DISCOVERY-PROTOCOL.md` -- **required before any research pass.**
4. `LEADS.md` -- the unverified queue. Read at the start of a pass, append during it.
5. `ARCHITECTURE.md`, `THESIS-NOTES.md`, `PORT-FROM-THE-PROGRAM.md` as the task requires.

`PROJECT.md` is the master case documentation. The latest `scientist-tracker-state-*.md` is
authoritative on case facts.

## Repository

Branch is **`master`**, not `main`. Probing `origin/main` returns exit 128; that is expected
and is not an error worth investigating.

## Serving the dashboard

`the-vanishing-v2.html` is one file but it is **not** self-contained: it loads
`assets/photos/*` by relative path. Ship the folder, not the file. `file://` will not work,
so serve it:

```bash
cd /home/user/the-vanishing
python3 -m http.server 8971
```
Then open `http://127.0.0.1:8971/the-vanishing-v2.html`. On Stewart's machine, `cd` to the
local path in "Two environments, one repo" below and use `python` instead of `python3`.

## Rebuild in progress

The single-file constraint is dropped. `ARCHITECTURE.md` has the target layout and the
migration order. **Do not do step 3 before step 2.** Extracting the case records and changing
the schema in the same step is how records get silently mangled, and regenerating the current
HTML byte-for-byte from extracted data is the checkpoint that proves nothing was lost.
`the-vanishing-v2.html` stays in the repo as the reference output until that checkpoint passes.

**FROZEN while the rebuild is in progress.** Do not edit `the-vanishing-v2.html` from either
environment until `python3 tools/verify.py --idempotent` passes. It is the target the
regenerator has to reproduce exactly, so an edit mid-rebuild silently moves the goalposts and
the checkpoint stops meaning anything. Land case corrections in `notes/step3-backlog.md`
instead. Pinned reference:

```
sha256 2dfc55e324b7535fbeea223e6b8699bf788ef60d9220417a81bf14bbff3d910a
324923 bytes
```

**Never extract from `design-package/vanishing-graph.js` or `vanishing-timeline.js`.** They
are pre-August-7 ancestors that differ by three adjudicated axis scores: `li` S0 not S1,
`loureiro` I3 not I1, `mccasland` P2 not P3. The declaration differs by one word
(`export const PEOPLE` versus `const PEOPLE`), so a mixup is easy and silent.

## Output rules

- **No em dashes.** Anywhere. Generated text, UI copy, documentation, commit messages. Use double hyphens or restructure.
- Tables over bullet lists for comparative content. Charts get data labels.
- Terminal commands include the `cd`, so they are copy-pasteable.
- Be concise. Remove words that do not change the meaning.

## Research rules

- **Never fabricate connections, sources, URLs, case numbers or document numbers.** If a URL cannot be verified to resolve, say so.
- Always carry counterarguments. Distinguish confirmed fact from allegation from open question. Flag anything unverifiable. Note where sources conflict, and several genuine conflicts are logged.
- **State search coverage, not just findings.** "Searched by name across four collections" is a very different claim from "read the full entity index." Say which one it was.
- Do not cite: strangehappen.com, theheartysoul.com, hannahhowell.com, mysterylores.com, frontpagenewspaper.com, headlinereporter.com, factually.co, slaynews.com, vigilantfox.com, ConservativeBrief, Medium reposts.
- These are real deaths and real missing people. Several families have publicly asked not to have their losses treated as conspiracy material. The tracker records those statements accurately and does not argue with them.

## Editorial stance

Built on the working hypothesis that a pattern **exists**, for an audience receptive to that
framing. Core insight: **an event prosaic in isolation may not be prosaic in sequence.**
Civilian academics count even without documented clearances, on the JASON precedent.

**Stewart explicitly does not want fake or specious connections. The rigor serves the
argument rather than opposing it.** Skeptical literature is a grading instrument, not a
rebuttal section. Tier C cases are retained deliberately, to prove the list is not curated.

## Scoring

Three axes, 0 to 3, **never summed.** S sequence anomaly, P personal program proximity,
I institutional channel. Tier A requires an unexplained fact no published source accounts
for, plus S2 or higher, or P3, or I3.

## Photograph rights

Publicly findable images are used, with per-image credit. Stewart has acknowledged and
accepted the risk; it is personal research for a small private audience. **Do not
re-litigate this.** See `PHOTOS.md`.

## Adversarial review protocol

At the end of any deliverable that feels final, ask: **"Do you want to run adversarial review
audit?"** Run it only on an explicit yes, because it consumes context. When running it, act
as his managers, the management Stewart presents to. Pick apart anything that looks odd or
does not parse at first glance, and actually inspect the rendered output rather than
reasoning about it.

## Two environments, one repo

This repo is worked on from both a **cloud Claude Code session** (GitHub-attached) and
**Stewart's local machine** at
`C:\Users\stewa\OneDrive\Documents\Claude\Cowork files\scientist-tracker\`.

**Always `git pull` before starting work, and push when done.** A cloud session cannot see
uncommitted local work and vice versa. Do not assume the working tree reflects everything
that exists.

## Do not touch

**The Legacy Program Dashboard** is a separate project, separate repo
(`the-legacy-program-dashboard`), under active development in its own thread. It consumes
this project's built dashboard as a frozen build input at its own `ref/the-vanishing-v2.html`.
That is a pinned copy. Changes here do not propagate there, and nothing here should modify it.
