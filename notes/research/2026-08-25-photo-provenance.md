# Staged: federal image provenance, Sullivan and the wider set

**Run 25 August 2026. STAGED, NOT MERGED.** Do not edit PHOTOS.md until the checkpoint passes.

---

## Sullivan portrait: NOT FOUND. Clean, well-supported negative.

No af.mil, DVIDS or other federal original exists in public repositories.

Tried: eight distinct DVIDS queries including branch-facet narrowing; a full read of the
152-result NASIC image corpus; the complete nasic.af.mil biography index (four entries, all
senior leadership, no Sullivan); af.mil Biographies (general officers and SES only);
domain-restricted searches across af.mil, nasic.af.mil, wpafb.af.mil, dvidshub.net,
defense.gov, spaceforce.mil, nsa.gov.

**Correction to the existing PHOTOS.md record.** PHOTOS.md states DVIDS returned "No
results" for the Sullivan queries. That is accurate only for the *combined* name-plus-NASIC
queries. The bare-name query `"Matthew Sullivan"` had not been run, and it does return 27
image hits, all unrelated. The conclusion is unchanged but the stated basis was too strong.
**Worth fixing so the negative is recorded honestly.**

**Two reasons the resemblance does not carry legal weight, and both matter:**
1. Official personnel portraits are produced for records and promotion boards. They are
   **not** public affairs products and are structurally not released through DVIDS or unit
   sites. The absence is what you would expect even if the photo is genuinely federal, so it
   neither confirms nor refutes authorship.
2. Base photo studios are in some cases **contractor-operated**. Contractor works are not
   covered by 17 U.S.C. 105, so even "this is a real official portrait" would not settle it.

**Recommendation: keep as assumed copyrighted, change the status from open question to
closed negative.** Further searching is not worthwhile. The only remaining routes are human
actions: a request to NASIC or AFIA Public Affairs, an AFPC records request, or the family.

**One substantive flag.** The current build credit reads `US Air Force service portrait via
family obituary`. That string asserts USAF authorship, which is exactly what is not
established, in a project whose rules forbid unverifiable attribution. Suggested:
`Service portrait, via family obituary (Dignity Memorial)`. Flagged, not changed.

NY Post (25 Apr 2026) carries three Sullivan photographs; every `<figure>` credit string on
the page is `Dignity Memorial` and nothing else. No .mil, no DVIDS, no USAF credit.

## McCasland: CONFIRMED, federal original stands

| Field | Value |
|---|---|
| Page | `https://www.af.mil/About-Us/Biographies/Display/article/104776/major-general-william-n-mccasland/` |
| Image | `https://media.defense.gov/2013/Apr/09/2000060253/700/700/0/130409-F-JZ004-207.JPG` |
| Identifier | VIRIN `130409-F-JZ004-207` (2013-04-09, F = Air Force, JZ004 unit code, 207 sequence) |
| Photographer | **None stated on the page. Do not invent one** |

Precision note: PHOTOS.md records the full-resolution `-1/-1/0` variant. The URL confirmed
embedded in the live page is the `700/700/0` variant. The `-1/-1/0` form is the standard
DIMOC full-size path and almost certainly resolves, but media.defense.gov returned 403 to
direct requests, so it was not independently re-verified this pass.

## LeBlanc: NOT FOUND, clean negative

NASA Image and Video Library API: `Joshua LeBlanc` 0 hits, `LeBlanc DRACO` 0, `LeBlanc
Marshall` 0. DVIDS `"Joshua LeBlanc"` returned 5 results, all Marine Division and Air
Refueling Wing, none related. NASA imagery is generally public domain, so this would have
been the easy win. It is simply not there. He was a civil servant engineer, not a public
affairs subject.

## Everyone else: zero

NASA image library API run across every remaining federal-adjacent name (Ning Li, Eskridge,
Moffatt, Maiwald, Reza, Hicks) returned **zero total hits** in all cases. DVIDS
`"Moffatt" NASA` returned no results.

Moffatt was the most promising untested candidate given NASA JSC payload and flight crew
support across 14 Shuttle and ISS missions. Nothing in either repository.

**No new federal original was found for any image in the set. The existing five clears
remain the five clears.** Recommend no further repository passes; the productive remaining
work is direct agency and family requests.

**Worth recording as a finding in its own right:** four subjects with substantial federal
careers (Sullivan at NASIC/NSA/AFIA, LeBlanc at NASA Marshall, Moffatt at NASA JSC, Maiwald
at JPL) have **zero** agency-published photographs. For LeBlanc and Moffatt that is genuinely
notable. For Sullivan it is fully explained by intelligence-unit imagery practice, so it
should not be treated as anomalous.

## Search coverage

Eight DVIDS HTML queries with branch-facet narrowing, full read of the 152-result NASIC
image corpus, complete nasic.af.mil biography index, two domain-restricted searches across
seven .mil domains, thirteen NASA Image and Video Library API queries across all twelve
federal-adjacent names, and direct HTML parsing of the NY Post article to extract every
per-figure credit string. **Not reached:** the DVIDS API (no key), the Dignity Memorial
obituary page (403), NewsNation (403), web.archive.org (unfetchable). **No reverse image
search was run**, and that is the one technique that could still surface a .mil copy.
