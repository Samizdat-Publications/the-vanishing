# Follow-Up Findings, August 7, 2026

**Scope:** the two open research tasks flagged as highest-value in `SESSION-HANDOFF.md`.

1. Verify Matthew Sullivan's scheduled Congressional testimony date
2. Pull the June 5, 2026 preliminary hearing outcome in People v. Snyder, 26AVCF00232

Both are resolved to the extent open sources permit. **Task 1 resolves against the tracker's prior framing and requires a correction.** Task 2 returns a documented absence plus four corrections to the Grillmair record that were not being sought.

---

## Part 1: Matthew James Sullivan -- the testimony-timing claim does not hold

### Verdict

**The claim that Sullivan died shortly before scheduled Congressional testimony is not supported. He remains Tier B. He does not move to Tier A.**

The tracker was right to flag this as poorly sourced. It is worse than poorly sourced -- the widely circulated version conflates two different events separated by six months, and the surviving kernel is a single undated recollection by a member of Congress speaking roughly two years after the fact.

### What the record actually shows

| Element | Finding | Grade |
|---|---|---|
| Death | Found at his Falls Church, VA home **May 12, 2024**, age 39 | Confirmed |
| Cause | Accidental overdose: alcohol, alprazolam, cyclobenzaprine, imipramine. Northern District Office of the Chief Medical Examiner | Confirmed |
| Was a Congressional hearing scheduled at the time of his death? | **No.** The November 13, 2024 House Oversight hearing was **announced November 8, 2024** -- 180 days after he died | **Confirmed, primary source** |
| Was Sullivan on that hearing's witness list? | **No.** Four witnesses: Gallaudet, Elizondo, Gold, Shellenberger | **Confirmed, primary source** |
| What Burlison actually said | "He was scheduled to come in for an **interview**. Within two weeks, he had suspiciously committed suicide." | Confirmed quote, uncorroborated content |
| What Burlison's April 16, 2026 FBI letter says | Sullivan "was **preparing to provide** testimony to Congress" | Confirmed quote |
| Date of the scheduled interview | **Never stated by anyone, in any source** | Open |
| Documentary corroboration of the interview | **None found.** No Oversight scheduling notice, transcribed-interview record, subpoena, or correspondence names Sullivan | Confirmed absence |

### The three-way conflation

Three distinct things have been collapsed into one claim by downstream outlets:

| The thing | The actual interval from May 12, 2024 | How outlets rendered it |
|---|---|---|
| An informal Congressional **interview** Burlison says was scheduled | "within two weeks," per Burlison, no date given | "days before he was scheduled to testify" |
| Grusch helping him **come forward** as a whistleblower | No date established | "after he agreed to testify" |
| The **November 13, 2024 public hearing** | **Six months**, and it did not exist as a scheduled event until Nov 8, 2024 | "weeks before his testimony" / "months before the hearing" |

This is why sympathetic outlets disagree on days versus weeks versus months. They are not describing the same event.

### Two problems with the surviving kernel

1. **Burlison calls it a suicide.** His quoted characterization is "he had suspiciously committed suicide." The medical examiner ruled **accidental** overdose. Burlison's own account is factually imprecise on the one element that was formally adjudicated, which is a direct reason to discount his recollection of an undated scheduling detail from two years earlier.
2. **An interview is not testimony.** A scheduled member or staff interview is a materially weaker fact than a noticed hearing appearance, and it leaves no public record, which is why it cannot be checked.

### What this is worth to the tracker

It is not a loss. **It is a correction the tracker can make that its critics have not.** PolitiFact flagged Sullivan's death as an accidental overdose but did not take apart the timing claim. Establishing that the November 2024 hearing postdates the death by six months is a checkable, primary-sourced fact that no skeptical outlet has published, and publishing it is exactly the behavior that makes the Tier A entries credible.

### Scoring impact

| Field | Was | Now | Basis |
|---|---|---|---|
| Tier | B | **B (unchanged, now for a stated reason)** | The condition for promotion was documentary corroboration of tight timing. It does not exist |
| S | S1 | **S1, re-based** | The single anomalous element is no longer "died before testifying." It is "a member of Congress states an interview was scheduled two weeks prior, undated and uncorroborated" |
| P | P3 | **P3 unchanged** | NASIC, NSA, AFIA service is documented and independent of the timing claim |
| I | I3 | **I3 unchanged** | Intelligence community |

**Sullivan's P3 was never dependent on the timing claim and survives it intact.** He is still the highest personal program proximity in the file. What changes is that the tracker can no longer present the timing as an anomaly, only as an unverified assertion.

### Corroborating detail worth keeping

Major General David Abba -- Director of Special Programs and head of the DoD Special Access Program Central Office, 2021 to 2024, and Sullivan's former supervisor at Langley AFB -- **spoke at Sullivan's funeral**, describing him as carrying "the burden that a select few in this nation have of truly understanding what's going on." This is a documented, attributable fact from a named senior SAP official and it independently supports the P3 score. It is stronger evidence of program proximity than anything in the timing claim.

---

## Part 2: People v. Snyder, 26AVCF00232 -- documented absence

### Verdict

**The June 5, 2026 preliminary hearing outcome is not publicly reported anywhere.** This is a confirmed absence, not a research failure. Log it as such.

| # | Question | Finding |
|---|---|---|
| 1 | June 5 prelim outcome | **Not found.** No outlet, DA release, or accessible court record states whether Snyder was held to answer, or whether the hearing went forward |
| 1b | Last documented court event | A **June 18, 2026** court date, referenced in passing by Los Angeles magazine |
| 2 | Status as of August 2026 | **Not found.** No arraignment on information, trial date, plea change, or charge amendment reported |
| 3 | Charges | One felony count each: murder, carjacking, first-degree residential burglary, plus an allegation he personally used a rifle. **PC section numbers appear in no public source** |
| 4 | DA explanation for the dropped December weapons charge | **None exists.** DA declined comment to LA Magazine. LASD **denied** LA Magazine's CPRA request on May 5, 2026 |
| 5 | In custody | Yes as of June 18, 2026, Twin Towers, $3.175M bail. **August status unverified** |

Media coverage stops entirely after June 18, 2026.

### Why the docket could not be pulled remotely

| Barrier | Detail |
|---|---|
| LASC portal | lacourt.org criminal case access now redirects to media.lacourt.org/lascmediaproxy, which is **reCAPTCHA-gated 7:00 a.m. to 7:00 p.m. daily** by court policy. Direct API probes returned SPA fallbacks or HTTP 500 |
| LASD inmate locator | app4.lasd.org and inmatelocator.lasd.org were **DNS-unreachable** from the research environment |
| LA Times | On the fetch blocklist. Only secondary characterizations of the Feb 19 and Feb 26 LAT stories were available |

**All three are resolvable by a human in one pass.** The court clerk at the Antelope Valley courthouse, Dept. A2, can answer items 1, 2, 3, and 5 by phone.

### Do not script the inference

Under PC 739 and 1382 an information must be filed within 15 days of a holding order. June 5 plus 15 is June 20, so a June 18 court date is **consistent with** Snyder having been held to answer on June 5 and arraigned on the information on June 18. It is **equally consistent** with the June 5 hearing having been continued to June 18. Nothing in the record distinguishes these. This inference is recorded here so it is not rediscovered and mistaken for a finding.

---

## Part 3: Four corrections to the Grillmair record

These surfaced while chasing the docket and were not being sought. All four affect text currently in `PROJECT.md`.

| # | Tracker currently says | Sources say | Grade |
|---|---|---|---|
| 1 | Killed in **Pearblossom** | Every source says **Llano** (street detail deliberately not reproduced here). The Dec 20 arrest was in **Palmdale** | **Confirmed error. Correct it** |
| 2 | **Grillmair reported** Snyder for trespassing | NY Post and LA Times say Grillmair called. LA Magazine says **neighbors** reported a possible trespasser. **Louise Grillmair told the BBC her husband did not call 911** and believes Snyder wrongly blamed him for the police contact | **Genuine conflict. Do not state either version as fact** |
| 3 | Shot once in the **neck** | DA and most outlets say neck. **The LA County Medical Examiner reported a single wound to the torso** (via The Guardian); NY Post described deputies finding him bleeding from the torso | **Genuine conflict. Flag it** |
| 4 | Dismissal by **Feb 5, 2026** | Newsweek and NY Post say Feb 5 citing court records; LA Magazine says **Feb 6**. Also unresolved: LA Magazine says "Judge Osman Abbasi **and prosecutors** dropped the charge," NY Post says "**prosecutors moved** to drop." Under PC 1385 the court orders the dismissal, so the moving party matters and is unsettled | One-day conflict, minor. Moving-party conflict, material |

### Correction 2 is the one that matters

The sequence chain currently opens with "Grillmair reported Freddy Snyder for trespassing." **His widow says he did not.** That is the single most load-bearing link in the S3 sequence, and it is contested by the closest available witness, who has separately rejected the pattern framing entirely.

The chain does not collapse -- Snyder was still arrested with a loaded unregistered rifle on Dec 20, still released after three days, still had charges dropped, still killed Grillmair eleven days later. **The institutional-failure sequence is intact regardless of who placed the call.** But the causal framing "he reported the man who killed him" is not established and must not be asserted.

### Two new threads the docket search opened

| Thread | Why it matters |
|---|---|
| **The burglary count is not from Feb 16.** City News Service and Antelope Valley Press both state the first-degree residential burglary was "allegedly committed in **late December**." Prosecutors charged Snyder with a late-December offense, but only **after** the killing | This sits directly against the dropped December weapons case. If there was chargeable December conduct, the dismissal question sharpens considerably. **Likely the most productive open thread in the Grillmair case** |
| **The firearm enhancement appears to have softened.** The February complaint alleged "personal and intentional discharge of a firearm causing great bodily injury." The May 28 DA release alleges only that he "personally used a rifle" | Either the DA release is loose language, or the enhancement was amended down between filing and arraignment. Only the charging documents settle it |

---

## Net effect on the case file

| Case | Change |
|---|---|
| **Sullivan** | Tier B confirmed, not promoted. S1 re-based onto a named but uncorroborated assertion. P3 and I3 intact and independently strengthened by the Abba funeral remarks |
| **Grillmair** | Location corrected. Three factual conflicts newly flagged, one of them (who called police) material to the S3 chain. Two new investigative threads opened. **Tier A and S3 both hold** -- the sequence does not depend on the contested link |

**No case changes tier as a result of this work.** One inflated claim was removed, and the strongest sequence case gained two threads and lost none.

---

## Open questions added

| # | Question |
|---|---|
| A | On what date was Sullivan's Congressional interview scheduled, and does any Oversight record corroborate it? |
| B | Was Snyder held to answer on June 5, 2026, or was the hearing continued to June 18? |
| C | What late-December conduct supports the first-degree residential burglary count, and why was it charged only after the killing? |
| D | Was the firearm enhancement amended down between the February complaint and the May arraignment? |
| E | Who actually contacted law enforcement about Snyder on December 20, 2025? |
| F | Neck or torso? The DA and the Medical Examiner do not agree on the wound location |

---

## Sources

### Sullivan

- Rep. Tim Burchett, "House Oversight Committee announces UAP hearing," **November 8, 2024** -- https://burchett.house.gov/media/press-releases/house-oversight-committee-announces-uap-hearing (primary; establishes the hearing was announced 180 days after Sullivan's death, with a four-name witness list not including him)
- U.S. House Committee Repository, "Unidentified Anomalous Phenomena: Exposing the Truth," Nov 13, 2024 -- https://docs.house.gov/Committee/Calendar/ByEvent.aspx?EventId=117722
- House Oversight Committee hearing page -- https://oversight.house.gov/hearing/unidentified-anomalous-phenomena-exposing-the-truth
- Congress.gov event record, 118th Congress -- https://www.congress.gov/event/118th-congress/house-event/LC73681/text
- Christopher Sharp, "Late Air Force Officer Linked To Alleged Legacy UFO Program," Liberation Times, **April 24, 2026** -- https://www.liberationtimes.com/home/late-air-force-officer-linked-to-alleged-legacy-ufo-program (source of the verbatim Burlison "interview / within two weeks" quote and the Maj. Gen. Abba funeral remarks)
- Matthew Sullivan funeral webcast, Maj. Gen. David Abba remarks -- https://client.tribucast.com/tcid/c24053175552014
- NewsNation, "UAP witness Matthew James Sullivan died of accidental OD before meeting with Congress" -- https://www.newsnationnow.com/space/ufo/uap-witness-overdose-death-congress/ (note the careful wording: "**meeting with** Congress," not testifying)
- Political.org, April 26, 2026 -- https://political.org/2026/04/26/air-force-veteran-set-to-testify-on-ufo-programs-died-of-overdose-months-before-hearing-adding-to-list-of-13-deceased-or-missing-aerospace-figures/ (the "months before hearing" framing, consistent with the Nov 2024 date)

### Snyder / Grillmair

- LA County District Attorney, "Charged Murderer Pleads Not Guilty in Shooting Death of Caltech Scientist," May 28, 2026 -- https://da.lacounty.gov/media/news/charged-murderer-pleads-not-guilty-shooting-death-caltech-scientist
- LA County DA June 2026 release index, both pages, no Snyder item -- https://da.lacounty.gov/media/news/2026-6
- Lauren Conlin, "Who Is Freddy Snyder?", Los Angeles magazine, **June 18, 2026** -- https://lamag.com/crimeinla/who-is-freddy-snyder-what-we-know-about-the-man-accused-of-killing-caltechs-carl-grillmair/ (last documented court date; LASD CPRA denial letter of May 5, 2026 quoted here)
- Lauren Conlin, "Caltech Astrophysicist Murder Suspect Pleads Not Guilty," Los Angeles magazine, June 2, 2026 -- https://lamag.com/crimeinla/caltech-astrophysicist-murder-suspect-pleads-not-guilty/
- Antelope Valley Press / City News Service, "Llano shooting suspect had prior gun arrest," Feb 2026 -- https://www.avpress.com/news/llano-shooting-suspect-had-prior-gun-arrest/article_9ee90e7c-9050-4b41-aab5-81eb90c81da8.html
- Antelope Valley Press / City News Service, "Suspect pleads not guilty in death of renowned scientist," May 26, 2026 -- https://www.avpress.com/news/suspect-pleads-not-guilty-in-death-of-renowned-scientist/article_b5fc367b-68d8-491c-9a5f-4f8a93600992.html
- Pasadena Now / City News Service, Feb 21, 2026 -- https://pasadenanow.com/main/man-charged-with-killing-caltech-scientist-had-been-released-after-loaded-gun-arrest
- Newsweek, Jenna Sundel, Feb 24, 2026 -- https://www.newsweek.com/man-allegedly-killed-scientist-released-from-jail-weeks-earlier-11574228
- Wikipedia, "Carl Grillmair," retrieved Aug 7, 2026 (cites The Guardian Feb 20, 2026 for the torso finding and the BBC for Louise Grillmair's account) -- https://en.wikipedia.org/wiki/Carl_Grillmair

### Excluded

No source on the project blocklist was used for any factual claim. Principia Scientific, planet-today, vigilantfox, americanwirenews, Gateway Pundit, shootingnewsweekly, internewscast, patriotnewsalerts, capitalisminstitute, and bizpacreview all surfaced in search results and were **read for framing only, never cited**. Every one of them renders the Sullivan timing claim in a form the primary sources do not support.
