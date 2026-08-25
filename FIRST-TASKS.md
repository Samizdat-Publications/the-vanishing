# First tasks for the new project, ranked

Ranked by value over effort. Reasoning included so you can disagree with the order.

---

## 0. Read the discovery protocol before doing any research

`DISCOVERY-PROTOCOL.md`, then `LEADS.md`. Not optional, and not a formality.

The old process missed Doty and Bennewitz because it searched **victims and institutions by
name** and had no query pointing at actors, mechanisms or precedents. Any research done
without the six-axis pass will repeat that failure. `LEADS.md` is the queue of things named
but not yet verified, and it must be read at the start of a pass and appended to during it.

## 1. Ning Li: import the DIRD, rescore, rewrite the rationale

**Effort: low. Value: high.**

`DIA-08-1003-013`, "The Role of Superconductors in Gravity Research," 23 March 2010,
Acquisition Threat Support series, produced under the DIA AAWSA programme, FOIA-released,
reviews her work by name. Detail in `PORT-FROM-THE-PROGRAM.md` section 1.

Raise her **I** score, rewrite the retention rationale (it currently says she is kept "for
research continuity to Eskridge rather than for its own anomaly," which is now wrong), and
**leave S and P alone.** The document shows institutional interest in her research line, not
anything happening to her. Keep the seven-year-gap counterargument exactly where it is.

Why first among the substantive items: it is a documentary upgrade rather than an
interpretation, and it fixes a record that currently understates itself.

## 2. Verify James E. McDonald

**Effort: one research pass. Value: potentially high, possibly zero.**

Senior physicist, Institute of Atmospheric Physics, University of Arizona. The most
credentialed public advocate of his era, credibility attacked and collapsed, died 1971.
If the circumstances hold up he is the closest structural analogue to the neutralisation
frame in the entire corpus, and the University of Arizona tie connects to Hicks.

**Verify before asserting anything.** He is currently `unverified` in `LEADS.md` and may
turn out not to belong. That is a legitimate outcome and should be recorded as one.

## 3. McCasland: import the Burlison staff contact

**Effort: low. Value: high.**

Burlison's staff had been trying to reach McCasland about a separate congressional
investigation before he disappeared. Tier 2, sourced, in The Program's
`missing-scientists-probe-2026`. That is a sequence link and belongs on his **S** score.

Also reconcile the institutional record: The Program calls him "former AFRL commander at
Wright-Patterson," this tracker places him at AFRL and the Kirtland Phillips Research Site.
Both can be true across a career. They should not silently disagree.

## 4. Identify the committee's eleven

**Effort: a research sweep. Value: high.**

The Comer-Burlison probe named eleven individuals in nuclear or rocket work since 2022. This
tracker has fifteen. Diffing is the best external curation check available, and it cuts both
ways honestly: a subset is corroboration, a name they have that you do not is a lead, a name
you have that they do not is worth understanding rather than defending.

## 5. Extract the data layer

**Effort: medium. Value: high, and it gates everything structural.**

Per `ARCHITECTURE.md`: pull case records out of `the-vanishing-v2.html` into
`research/cases.json`, stand up `merge.py` and `build_dashboard.py`, and **regenerate the
current HTML byte-for-byte.** That checkpoint proves nothing was lost. Do not change the
schema in the same step as the extraction.

Only after it passes: add per-claim tiering, sources arrays, and the `outcome` field.

## 6. The Snyder docket

**Effort: one phone call, by Stewart not Claude.**

`SNYDER-DOCKET-RETRIEVAL.md`. Criminal Clerk (661) 483-5798, case 26AVCF00232, minute orders
for 5 and 18 June 2026.

## 7. Per-claim tiering, and the discovery checks in verify.py

**Effort: structural. Value: the biggest credibility upgrade available.**

Today a Tier A case can contain an unmarked inference and nothing catches it. Adopt The
Program's 1 / 2 / 3 per-claim tiering with sources arrays.

While building `verify.py`, add the automated discovery checks from `DISCOVERY-PROTOCOL.md`
section 3 **as warnings, not failures**: people named in narratives who are not tracked
nodes, institutions and document numbers mentioned in prose but absent from structured data,
cases missing an expected field, and names appearing in more than one case narrative. That
last one is the aggregate check pointed at discovery instead of at findings.

---

## Three things to be careful about

**The neutralisation frame.** `THESIS-NOTES.md` records it with its falsifiability problem.
Implement it as an `outcome` schema field, not as a thumb on the scores. If death,
incapacitation, discrediting and career-ending all count as confirmation, the hypothesis
loses the ability to fail, and a hostile reader will use that to dismiss the strong cases
along with the weak ones.

**Doty specifically.** Cite him for what he did, never for what he says is true. He has
changed his account repeatedly. The load-bearing inference is narrow: a counterintelligence
officer stated on record that managing the civilian UFO information environment was his
official duty. That survives his unreliability. His claims about anything else do not.

**Importing from The Program.** Copy the claim and its source, never the conclusion. The
Program writes from a stronger premise than this tracker is allowed to use: its voice assumes
the programme exists. The Vanishing does not get to assume its pattern exists, because that
is the thing it is trying to demonstrate.
