# Can the Bennewitz precedent bear the weight the thesis puts on it?

**Asked and answered 25 August 2026.** The question came from `PORT-FROM-THE-PROGRAM.md`
section D item 2: the `paul-bennewitz` node carries the 1988 hospitalisation and the 2003
death in narrative and chronology only, and none of its four listed sources sources either
one. Since Bennewitz is this project's **only documented neutralisation precedent**, both
facts had to be sourced independently before the tracker asserts them.

## Verdict: the precedent splits, and the half the thesis leans on is the weaker half

| Element | Verdict | Strength |
|---|---|---|
| The AFOSI operation existed and was run against him | **Sourceable** | Federal records, plus the operator on record |
| He died 23 June 2003 | **Sourceable, Tier 1** | Primary federal record, verified below |
| Cause of death | **Not sourceable** | No public record found |
| He was hospitalised in 1988 | **Not sourceable to record** | Published book relaying family testimony |
| The operation caused the hospitalisation | **Not sourceable** | Inference, and stated as one by its own sources |

**The operation is documented. Its effect is testimony.** That distinction is the whole
finding, because "neutralisation without death" is a claim about the **effect**.

## What was verified, and how

### The death: primary federal record

Queried the **VA National Gravesite Locator** directly (`gravelocator.cem.va.gov/ngl/`,
POST to `/ngl/result`, 25 Aug 2026). One decedent returned:

| Field | Value |
|---|---|
| Name | BENNEWITZ, PAUL FREDERICK JR |
| Rank and branch | S1C, US COAST GUARD |
| War period | WORLD WAR II |
| Date of birth | 09/30/1927 |
| Date of death | 06/23/2003 |
| Buried at | SANTA FE NATIONAL CEMETERY, Section 12, Site 402 |
| Record id | 7139602 |

This is a US Department of Veterans Affairs record of interment. It is a **Tier 1 documented
claim** and it settles the date of death. It carries **no cause of death**, and VA interment
records never do.

### Two facts the secondary literature does not carry

1. **He was a World War II Coast Guard veteran, Seaman First Class.** Every secondary account
   consulted describes him only as a physicist or electrical engineer running an
   instrumentation company. None mentions military service. This matters practically: it
   means an **Official Military Personnel File exists at the National Personnel Records
   Center**, St. Louis, and OMPFs become archival and publicly requestable 62 years after
   separation. A 1945-46 separation is already past that. Added to `LEADS.md` section D as a
   retrievable instrument.
2. **A date-of-birth conflict.** The federal record says **30 September 1927**. Circulating
   secondary accounts say **29 September 1927**. One day. Logged rather than resolved, per
   the rule on conflicting sources. The federal record is the better authority.

### The 1988 hospitalisation: what actually stands behind it

The chain runs: tracker to Wikipedia to *The Guardian* to Greg Bishop.

- Wikipedia attributes the specific detail (barricading the house with sandbags, admission by
  his family to the mental health unit of Presbyterian Anna Kaseman Hospital, one month under
  observation) to **Steve Rose, "The real Men in Black, Hollywood and the great UFO
  cover-up", The Guardian, 14 August 2014.**
- **That article could not be verified from this environment.** `theguardian.com` refuses this
  agent, and the Wayback Machine holds **no snapshot** at the cited URL. Stated as coverage,
  not as doubt about the article's existence: it was not read.
- The underlying account in every version is **Greg Bishop, *Project Beta: The Story of Paul
  Bennewitz, National Security, and the Creation of a Modern UFO Myth*, Paraview Pocket Books
  (Simon and Schuster), 2005.** That is a real book from a mainstream imprint, and it is a
  legitimate citation. It is also **reconstructed from interviews with family and
  associates**, which is testimony, not record.

There is no medical record, no court record, no commitment docket, and none is obtainable:
psychiatric admission records of a private citizen are not public, and the hospital named has
since been absorbed. **This is not a gap that further searching closes.**

### The operation: this part does hold

Not re-verified in full here, because it was already sourced on the node, but the shape is
worth stating against the weaker elements:

- **FOIA-released AFOSI records** exist and are contemporaneous, including the 28 October 1980
  Multipurpose Internal OSI Form signed by Maj. Thomas Cseh and September 1980 reports signed
  by SA Richard C. Doty.
- **The operator described his own role publicly and on the record**, which is the fact that
  makes this case categorically different from an inferred one.
- **AARO Historical Record Report Volume I** is cited on the node. It **could not be re-checked
  here**: both `aaro.mil` and `media.defense.gov` return **403 to automated requests**. Same
  pattern as the two `esd.whs.mil` URLs already flagged. Added to the browser re-check list
  rather than treated as broken.

## What this changes

`THESIS-NOTES.md` and `PORT-FROM-THE-PROGRAM.md` both compress the precedent into a single
sentence of the form "he was fed fabricated material, and he broke." The first clause is
documented. **The second is a family's account of what happened to their father, relayed
through a book.**

That is not nothing. It is the wrong thing to call documented, and this project's stated
standard is that rigor serves the argument. A precedent described accurately still does its
work: it establishes that a US counterintelligence organisation ran a calibrated
disinformation operation against a private scientist, which is the fact the frame actually
needs. It does not establish, at record strength, what that operation did to him.

**No axis score moves on any of this.** Bennewitz is a precedent, not a tracked case.

## Search coverage

Searched by name across: the VA National Gravesite Locator (**full query, single exact
match, complete record read**); web search for an Albuquerque Journal obituary (**a clipping
is indexed at newspapers.com, id 116778334, dated 29 June 2003, and is paywalled -- HTTP 403,
not read**); Wikipedia's full citation list (**read**); The Guardian (**refused**); the
Wayback Machine for that Guardian URL (**no snapshot**); The Black Vault document archive
(**HTTP 403 to search**); AARO Historical Record Report (**HTTP 403 at two hosts**).

**Not searched:** the National Personnel Records Center, which requires a written request;
New Mexico vital records, which restrict death certificates to family; the text of Bishop's
book, which is not online. The first of those is now a `LEADS.md` instrument.

Sources consulted and **not** cited, per the blocklist and the project's standards:
uapmurders.com, politicalsaucer.substack.com, projectcamelot.org, exopaedia.org,
grokipedia.com, news-nest.com, wikidisc.org, kb42.info, unexplainable.net. Several of these
assert murder. **None offers a record, and the federal interment record contradicts nothing
they claim while supporting none of it.**
