# Discovery protocol

**Written 24 August 2026, after a failure worth naming.**

Stewart: *"if we're missing Doty then we're not doing something right. In fact this seems to
be a pattern, some of the highest value ones I am aware of were not caught by our current
process until I called them out by name."*

He is right, and the failure has a specific and fixable shape.

---

## 1. What actually went wrong

The cross-repo survey searched The Program's dataset for **the fifteen case names** and for
**institution keywords**. That is a victim-centric, entity-name-driven query. Here is what
each finding cost:

| Finding | How it was found | Would the process have found it? |
|---|---|---|
| Ning Li in `DIA-08-1003-013` | Name search | **Yes.** The process worked. |
| McCasland / Oversight probe | Name search | **Yes.** |
| Institution overlap counts | Keyword search | **Yes.** |
| **Bennewitz** | Dumped one `entityInfo` entry **as a formatting sample.** A different sample key and it would have been missed entirely | **No. That was luck, not method.** |
| **Doty** | Only after Stewart named him | **No.** |

**The diagnosis: the search asked "who from our list appears in their data" when it should
also have asked "what in their data is about what we study."**

Those are different questions. The first finds victims and employers. It structurally cannot
find:

- **Actors.** Doty is not a victim and not an institution. He is the person who did the thing. No name-based or institution-based query reaches him.
- **Mechanisms.** How neutralisation is actually performed.
- **Precedents.** Prior documented instances of the pattern.
- **Instruments.** Documents, programmes, dockets, personnel files.

Doty and Bennewitz sit in the actor and precedent categories. The process had no query that
pointed at those categories, so it had a blind spot exactly the width of the most valuable
material.

**Second failure, and the more important one: Stewart is doing recall the system should do.**
He carries domain knowledge -- Doty, the Church Committee heart attack gun, JASON, vehicle
collision as a documented method -- that exists nowhere in the repo. When he happens to
mention it, it lands. When he does not, it is silently absent. That is a knowledge-capture
gap, and it is why the misses feel like a pattern to him. They are one.

**Third: nothing in the process ever asks what is missing.** Every check is a presence check.
There is no negative-space pass.

---

## 2. The fix, as a standing step

Run this **as an explicit step**, not as a vibe. It applies to weekly sweeps, to cross-repo
work, and to any research pass.

### Step A: Query all six axes, not one

For any research target, run the search six ways. Write down which axes returned nothing,
because an empty axis is a finding.

| Axis | Question | Example of what it catches |
|---|---|---|
| **Victims** | Who was harmed? | The current process. Ning Li, McCasland. |
| **Actors** | Who did something, ordered it, ran it, or later admitted it? | **Doty.** Investigating officers, agency personnel, whistleblowers, prosecutors. |
| **Mechanisms** | How is this done? What is the method? | Disinformation tailored to a target's existing beliefs. Vehicle collision. Discrediting. |
| **Precedents** | Has a documented instance of this happened before? | **Bennewitz.** MKULTRA. Church Committee disclosures. |
| **Instruments** | What documents, programmes, dockets, or records exist? | `DIA-08-1003-013`. Doty's 321-page personnel file. Case 26AVCF00232. |
| **Institutions** | What organisation was the conduit? | Partly covered today. Kirtland, AFRL, NASIC, LANL. |

### Step B: Search the corpus, not just the names

When surveying an external dataset, do **both**:

1. Pull the corpus's own index -- entity lists, dossier keys, taxonomy, section headings -- and **read the whole index**, not a sample of it. The Program has 88 `entityInfo` keys and 689 entities. Reading 88 key names takes seconds and would have surfaced `afosi-kirtland-file` by name.
2. Then run targeted name and keyword queries.

**Sampling a large index to "see the shape" is not a search.** It feels like due diligence and
is not. That is precisely the error that made Bennewitz a lucky hit.

### Step C: Check the leads file

`LEADS.md` holds domain knowledge that is not yet in the tracker: names, methods, documents,
precedents, and hunches, each with a status. **Every research pass reads it and every pass
adds to it.** When Stewart mentions something in conversation that is not in the tracker, it
goes in the file immediately, before anything else happens to it.

This is the direct fix for "not caught until I called them out by name." Called out once
should mean captured forever.

### Step D: Negative space pass

Ask, explicitly, and record the answers:

- **What should be here and is not?** Every case has an employer, a jurisdiction, an investigating agency, a coroner or a court. Which of those are missing from the record and why?
- **Which axis came back empty this pass, and is that a real absence or an unasked question?**
- **Who is adjacent to a tracked case and not tracked?** Spouses, co-authors, co-workers, the officer who took the report, the person who found the body.
- **What would a hostile reader say is conspicuously absent?**

### Step E: Name the confidence in the search itself

End every research pass with one line stating **how thoroughly the space was actually
searched**, not just what was found. "Searched by name across four collections" is a very
different claim from "read the full entity index." Say which one it was.

A finding is only as good as the search that produced it, and unreported search coverage is
how a lucky hit gets mistaken for a thorough process.

---

## 3. Build this into the analyst

Steps A and D are largely automatable and should not stay manual:

| Automated check | Output |
|---|---|
| Every person mentioned in any case narrative who is **not** a tracked node | Candidate actor list |
| Every institution, programme, document number or case number mentioned in prose but absent from structured data | Candidate instrument list |
| Cases missing an expected field: investigating agency, jurisdiction, court, employer, cause | Negative-space report |
| Adjacency: named people who appear in more than one case narrative | Cross-case actor candidates |

That last one is the aggregate check from `THESIS-NOTES.md` pointed at discovery instead of
at findings. A person who shows up in two unrelated case narratives is exactly the kind of
thing that is invisible per case and obvious in aggregate.

**Add these to `verify.py` as warnings, not failures.** They are discovery prompts, not
correctness violations. But they should appear on every build so the gap list is never
somebody's memory.

---

## 4. The honest limit

This protocol reduces blind spots. It does not eliminate them, and it should not be sold as
if it does. Two residual risks worth stating:

**It cannot find what the corpus does not contain.** Doty was findable because The Program had
already researched him. A mechanism nobody has written down is not reachable by better
querying.

**Six axes is a heuristic, not a proof of coverage.** The axis list came from analysing two
specific misses. There will be a seventh category, and it will be discovered the same way
these were, by somebody noticing an absence. When that happens, add it here rather than
treating the list as complete.

The realistic goal is that **Stewart's domain knowledge stops being load-bearing** -- that the
things he knows get captured the first time he says them, and that the process reaches
actors, mechanisms and precedents on its own rather than waiting to be told.
