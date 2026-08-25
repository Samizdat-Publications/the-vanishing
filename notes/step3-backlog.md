# Step 3 backlog

**This file exists so that step 3 work gets written down instead of done.**

`ARCHITECTURE.md:72` names the failure mode directly: extraction and schema change in the
same step is how records get silently mangled. During extraction you will notice real
problems. Every one of them breaks the byte-for-byte checkpoint if fixed now. Add it here
and move on.

Nothing in this file is actioned until `tools/verify.py --idempotent` passes.

---

## Schema cleanups

| Item | Detail |
|---|---|
| Unify the `sources` key name | `PEOPLE` records use `outlet`; `ENTITY_SOURCES` and every other block use `name`. Same concept, two spellings |
| Fold `PHOTOS` into the case record | Adding a case today means editing `PEOPLE` (638-994), `PHOTOS` (2030-2046) and `TIMELINE` (1958-2001), three literals in three conventions, 1,400 lines apart |
| Normalise the `leftBehind` vocabulary | `'phone'`, `'phones'` and `'iPhone'` are three tokens for one concept. The behavioural edge rule at line 1170 is exact string match, so `casias` connects to nobody on `'phones'`. **Do this deliberately, with the edge-count delta reviewed**, currently 10 behavioural edges of 151 |
| `precision` versus date string | `chronology[].precision` partly duplicates what the date string length already encodes. Decide whether it is authored or derived. **Do not derive it during extraction** |
| Extract `COUNTERS` with its surrounding prose | `COUNTERS` (3785-3796) is analytical content, but the "Where the skeptics overreach" table and the "Family positions" paragraph sit inline in `viewCounterargs` (3806-3815) and exist nowhere else. Extracting one without the other splits a single argument across two files |
| Extract the `scriptedReply` prose | 4373-4425 holds the base-rate answer and the hostile-reader answer, hand written, existing nowhere else in the repo |

## Content corrections found during exploration

| Item | Detail |
|---|---|
| "Fifty-two entities" is wrong | Search view copy at line 3838 says fifty-two. `NODES.length` is **54** (15 people, 12 institutions, 6 programmes, 14 locations, 7 domains). Latent, cosmetic, real |
| `PROJECT.md` and the HTML disagree on Ning Li | `the-vanishing-v2.html:643` carries "retained for the research continuity to Eskridge rather than for its own anomaly". `PROJECT.md:152` does not carry that wording at all; it says "The medical chain is documented and covers the facts." **Any rewrite touches two places with different starting text** |

## Decisions that must be made before the schema changes

### 1. Does `outcome` replace `status`, or sit beside it?

`THESIS-NOTES.md:89-101` proposes:

```
outcome: dead | missing | resolved | incapacitated | discredited | career-terminated
```

The current schema has `status: missing | dead | resolved`. The proposal is a strict superset.
**Nobody has written down whether it replaces or supplements**, and the answer changes the
schema. Note the reason the field exists at all: `THESIS-NOTES.md:62` concedes the
neutralisation frame "is close to unfalsifiable, and that is a real cost, not a quibble." The
field is the mechanism that keeps it checkable. Implement it as data, never as a thumb on the
scores.

### 2. Ning Li: claim, not axis move. DECIDED 25 August 2026

**Attach `DIA-08-1003-013` as a Tier 1 claim with its source, and rewrite the retention
rationale. Do not move the I axis.**

`FIRST-TASKS.md` ranks raising her **I** as the top substantive task. That is likely wrong as
specified. `RESEARCH-PROCESS.md:120` scores the I axis **on the employer, not the person**,
and I3 requires FFRDC, national laboratory, or documented JASON / IDA / MITRE lineage. The
DIRD is a DIA review of *her research line*, not a fact about UAH as an employer. Moving UAH
from I2 to I3 on that document repeats the exact error the 10 August adjudication was written
to stop, where seven of eight disagreements were the same error of scoring the person by where
they worked.

The document is real and the upgrade may still be defensible. It needs to be argued on the
employer axis on its own merits, not carried in on a document about the person.

Keep the seven-year-gap counterargument exactly where it is. Leave S and P alone; that is
stated in four separate files.

### 3. McCasland: reconcile before importing

The Program calls him "former AFRL commander at Wright-Patterson". This tracker places him at
AFRL **and** the Kirtland Phillips Research Site. Both can be true across a career. **They
should not silently disagree.** Reconcile first, then consider whether the Burlison staff
contact attempt moves his S score.

## Import queue, gated on the checkpoint

Per `PORT-FROM-THE-PROGRAM.md`, in its stated order. **Governing rule: copy the claim and its
source, never the conclusion.** The Program writes from a stronger premise than this tracker
is allowed to use.

1. Ning Li DIRD, per decision 2 above
2. McCasland Burlison staff contact, after reconciliation
3. Per-claim tiering and sources arrays, described as the single highest-value structural import
4. Kirtland / Wright-Patterson / LANL / Sandia claims as I-axis support. **Do not import the thin ones and pretend they are support**
5. Bennewitz as documented precedent
6. `richard-doty` node, **with The Program's own credibility guard attached. Cite Doty for what he did, never for what he says is true**
