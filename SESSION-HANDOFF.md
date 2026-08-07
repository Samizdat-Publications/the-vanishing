# Session Handoff: The Vanishing

**Handoff date:** August 7, 2026
**From:** Cowork cloud session
**To:** Cowork local session (running on Stewart's computer)

**If you are a fresh Claude session picking this up, read this file first, then `PROJECT.md`.**

---

## Where everything lives

```
C:\Users\stewa\OneDrive\Documents\Claude\Cowork files\scientist-tracker\
```

That directory is the canonical project. It is a git repository with remote `https://github.com/Samizdat-Publications/the-vanishing.git` (private, Samizdat-Publications). Branch is **`master`**, not `main`. Claude Design has read access to the repo.

There is a second, nearly empty folder at `...\Claude\Projects\Missing individuals connected to defense contractors\` containing only a `README.md` pointer and a snapshot copy. That is deliberate, to avoid two sources of truth. **Do not move the project into it.**

### File inventory (verified Aug 7, 2026)

| File | Bytes | Status |
|---|---|---|
| `PROJECT.md` | 42,321 | **Master doc. Rewritten Aug 7. Authoritative.** |
| `scientist-tracker-state-2026-08-07.md` | 59,877 | **Latest research sweep. Authoritative on case facts.** |
| `DESIGN-ADDENDUM-2026-08-07.md` | 10,707 | Schema and component changes for Claude Design |
| `CLAUDE-DESIGN-PROMPT.md` | 20,069 | v2 design brief. Pushed as commit `313ec1a`. |
| `RESEARCH-PROCESS.md` | 7,623 | Weekly sweep spec and case schema. **Needs updating for the 3-axis model.** |
| `scientist-network-tracker.html` | 84,420 | v1 tracker being replaced |
| `scientist-tracker-state-2026-06-20.md` | 16,505 | Prior sweep, superseded |
| `DESIGN-BRIEF.md` | 9,764 | Earlier creative brief, superseded |

**Housekeeping:** there is a `_to_delete\` folder in the repo containing two zero-byte stale git lock files. The cloud session could not delete files on the local disk, only move them. **A local session can and should just delete that folder.** Do not commit it.

---

## Git state

| Item | Value |
|---|---|
| Local HEAD | `313ec1a` (Rewrite v2 brief) |
| origin/master | `313ec1a` -- **in sync as of the last push** |
| Uncommitted | `PROJECT.md`, `DESIGN-ADDENDUM-2026-08-07.md`, `scientist-tracker-state-2026-08-07.md` |

**Next commit needed:**
```
git add PROJECT.md DESIGN-ADDENDUM-2026-08-07.md scientist-tracker-state-2026-08-07.md
git commit -m "Aug 7 sweep: three-axis scoring model, 15 cases, data corrections"
git push origin master
```

**Two git lessons from the cloud session, both now moot locally but worth knowing:**

1. `git push` alone silently failed; `git push origin master` worked. If a push reports "Everything up-to-date" when you know it shouldn't, check `.git\refs\remotes\origin\master` against `.git\refs\heads\master` before believing it.
2. The cloud session's `device_bash` could create `.git\index.lock` but not remove it, which blocked Stewart's own git commands twice. **A local session has real shell access and does not have this problem.** This was the main reason for moving local.

OneDrive syncing the `.git` folder is a plausible contributor to lock issues. Consider excluding the repo from OneDrive sync.

---

## What this project is

Stewart Gregerson's personal research project tracking deaths and disappearances of US scientists, military officials, and defense-connected individuals since 2021. Working title **"The Vanishing."** Personal research, **not employer work** -- no employer branding anywhere.

There is a **separate** project in this same Cowork workspace on targeted individuals and directed-energy-weapon claims. The two overlap (Amy Eskridge appears in both) but are distinct. Do not merge them.

---

## Editorial stance (important -- read before writing anything)

Stewart has been explicit about this. The tracker is built on the working hypothesis that **a pattern exists**, for an audience receptive to that framing. Its purpose is to document the pattern and surface connections invisible at the individual case level.

His core analytical insight, which drove the whole redesign: **an event that looks prosaic in isolation may not be prosaic in sequence.** A scientist shot by a disturbed neighbor is a crime story. A scientist shot by a neighbor he had reported, who was arrested with a loaded unregistered rifle, released after three days, and had his charges dropped eleven days before the killing, is a different object. Nothing in that chain is invented; it only becomes visible when reconstructed.

He also holds, correctly and with historical support, that **civilian academic scientists at major institutions belong in scope** even without documented clearances, because the government has recruited university scientists into classified advisory work for sixty years (JASON, formed 1960) and because absence of a public clearance record is weak evidence of absence of sensitive work.

**What he explicitly does not want:** fake or specious connections. He said so directly. Padding the list with weak cases defeats his purpose. The rigor is in service of the argument, not opposed to it.

**How the skeptical literature is used:** as a **grading instrument**, not a rebuttal section. The statistical arguments are what separate cases that survive hostile scrutiny from ones that do not. This is not hedging -- a hostile reader will attack the weakest entry to discredit the whole set, so the weakest entries must be labeled as such by the tracker itself.

---

## The three-axis scoring model (the core of v2)

Every case carries three independent scores plus a composite tier. **The axes are deliberately not summed.**

| Axis | Range | Question |
|---|---|---|
| **S** Sequence Anomaly | 0-3 | How many independently documented, individually unexplained links form a chain? |
| **P** Personal Program Proximity | 0-3 | What sensitive access did this person personally hold? |
| **I** Institutional Channel | 0-3 | Does the employer have documented history as a conduit for classified work? |

Tier A = an unexplained fact no source accounts for, plus (S2+ or P3 or I3). **7 cases.**
Tier B = unresolved, prosaic explanation available. **3 cases.**
Tier C = conventional explanation documented and holds. **5 cases.** Retained to prove the list is not curated.

### The cases that matter most

- **Joshua LeBlanc, S2/P3/I3.** Active DRACO nuclear propulsion engineer at NASA Marshall. Four unexplained hours with his Tesla at Huntsville International that morning. Phone and wallet left at home. Dead the same day. **High on all three axes and v1 buried him.**
- **Monica Reza, S2/P3/I2.** Mondaloy co-inventor (rocket engine superalloy). Vanished within seconds in a companion's sightline.
- **Carl Grillmair, S3/P1/I3.** The model sequence case, described above. Dark matter and exoplanets, no documented clearance, Caltech IPAC.
- **Melissa Casias, S3/P1/I3.** Cause undetermined after 13 months. Registered handgun near remains, owner undisclosed. Surveillance timestamp corrected by 13h58m with no explanation. Family recovered evidence police had not collected.
- **Frank Maiwald, S1/P2/I3.** No cause of death disclosed and **no skeptical source has offered any alternative** -- only the base rate. Cleanest pure open question.

---

## Immediate next steps

1. **Delete `_to_delete\`**, then commit and push the three uncommitted files.
2. **Update `RESEARCH-PROCESS.md`** -- its case schema predates the three-axis model and no longer matches `PROJECT.md`. This is the most obvious loose end.
3. **Verify Matthew Sullivan's scheduled Congressional testimony date.** He is P3/I3, the highest program proximity in the file, and the "died before testifying" claim is the most load-bearing unsourced item in the project. Outlets say days, weeks, and months; most coverage is low-reliability. If it resolves tight against his May 12 2024 death, he moves to Tier A. If it doesn't, better to know before a critic finds it. **Highest-value open research task.**
4. **Pull the LA County Superior Court docket on case 26AVCF00232** for the June 5 2026 preliminary hearing outcome in People v. Snyder. Media went quiet after May 28.
5. Claude Design is working from `CLAUDE-DESIGN-PROMPT.md` plus `DESIGN-ADDENDUM-2026-08-07.md`. Its output goes to Claude Code to build.
6. **Adversarial review of the Aug 7 snapshot and PROJECT.md is offered but not yet run.** Stewart runs these on request only, because they consume context. See below.

---

## Working rules

- **No em dashes** in any generated text, UI copy, or documentation. Use double hyphens or restructure. This has been verified on every file delivered so far and must stay that way.
- Tables preferred over bullet lists for comparative content. Charts get data labels.
- **Never fabricate connections.** Always carry counterarguments. Distinguish confirmed fact from allegation from open question. Flag anything unverifiable. Note where sources conflict, and there are several genuine conflicts logged in the Aug 7 snapshot.
- Do not cite: strangehappen.com, theheartysoul.com, hannahhowell.com, mysterylores.com, frontpagenewspaper.com, headlinereporter.com, factually.co, slaynews.com, vigilantfox.com, ConservativeBrief, Medium reposts. These recycle identical errors and manufacture timestamps on old material.
- These are real deaths and real missing people. Several families have publicly asked not to have their losses treated as conspiracy material, and the tracker records those statements accurately without arguing with them.

### Adversarial review protocol (Stewart's standing instruction)

At the end of any deliverable that feels final, ask: **"Do you want to run adversarial review audit?"** Only run it when he says yes, because it consumes context. When running it, act as his managers -- the management he presents to. Pick apart anything that looks odd or doesn't parse at first glance, audit thoroughly, and actually inspect the rendered output (if it's a slide, verify nothing overlaps or misaligns). The audit must be robust and should be built into any skill or process produced.

---

## Research cadence

Weekly sweeps per `RESEARCH-PROCESS.md`, Priority 1-4. The Aug 7 sweep found **no new cases** in the June 20 to August 7 window and the story has been dormant in mainstream coverage since early May. **Consider moving to monthly with breaking-news triggers.** Last sweep ran as four parallel research agents, one per priority tier, which worked well.
