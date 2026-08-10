# Handoff prompt for Cowork / Claude Code

Paste the block below. It assumes this design package sits in the repo alongside `PROJECT.md`.

---

## The prompt

Build the production v2 of The Vanishing from the design package in this repo.

**Note:** this package was rebuilt against `DESIGN-ADDENDUM-2026-08-07.md` and the August 7 state snapshot. It carries 15 cases, the three-axis scoring model, sequence chains, the resolved status, and the eight data corrections. No em dashes appear in any UI string; keep it that way.

**Read first, in this order:**
1. `DESIGN-SYSTEM.md` -- the binding spec. Every colour, size, motion token, node and edge treatment, the confidence system, and the full command surface.
2. `The Vanishing v2 - Reference Mockup.dc.html` -- the definitive visual target. Open it in a browser. All seven views work, the graph is live, the analyst drives the dashboard.
3. `vanishing-graph.js` -- a working implementation of the record schema, the edge derivation, the strength aggregation, the force layout, and the node and edge renderers. Port it; do not reinvent it. The derivation rules in particular are load-bearing.
4. `PROJECT.md`, `DESIGN-ADDENDUM-2026-08-07.md` and `scientist-tracker-state-2026-08-07.md` -- the data. The addendum wins where it conflicts with the main brief.
5. `CLAUDE-DESIGN-PROMPT.md` -- the original brief, for intent.

**Build target:** single HTML file, openable locally, no server, all case data in one editable JavaScript array at the top matching `RESEARCH-PROCESS.md` §3.1 extended with `instId`, `locId`, `clearance`, `leftBehind`, `cause`.

**Where to spend effort beyond the mockup:**
- Port the network map to **WebGPU** with a WebGL2 fallback and the canvas-2D floor. The mockup is canvas 2D only because it had to prove the visual language. Target 60fps on an RTX 5070 Ti with 50 nodes today and 150 later.
- Implement the **command surface** in `DESIGN-SYSTEM.md` §5 exactly as named. Nothing in the UI may mutate state directly; every control calls the same functions the analyst calls. This is what makes the "operate the whole app from the chat input" requirement true rather than aspirational.
- Wire the **analyst** to the real Anthropic API with the user-supplied key flow in §4.6. Keep the no-key state fully functional.
- Add `setEdgeFilter`, `frameNodes`, `highlightPath`, and the timeline zoom and overlay actions, which the mockup specifies but only partially implements.
- Put filter and selection state in the URL so a view is shareable.

**Do not change without asking:** the strength encoding (weight = number of independent connection types), the derived-versus-editorial split in the edge data, the three-level confidence system, or the counterarguments view's weight.

---

## Photographs for the dossier slots

The person node and the detail dock both carry a hatched photo slot sized for a real portrait: 26×26 on the canvas plate, 42×52 on the case card, 56×68 in the detail dock. Try to fill them. Instructions:

Research whether a usable photograph exists for each of the 14 individuals, and **sort what you find by licence, not by availability**:

1. **Public-domain official portraits first.** Several of these people were US government employees, and works produced by US federal employees in the course of their duties are generally public domain:
   - Neil McCasland -- retired Major General, former AFRL commander. An official USAF portrait almost certainly exists and is public domain.
   - Matthew Sullivan -- USAF intelligence. Check for an official service photo.
   - Michael Hicks, Frank Maiwald, Joshua LeBlanc -- NASA / JPL. NASA imagery is generally public domain; check JPL and NASA image libraries and mission pages, including Deep Space 1 and DART team photos for Hicks.
   - Anthony Chavez, Melissa Casias -- LANL. Lab and DOE imagery may be public domain; verify per image.
   - Steven Garcia -- KCNSC / NNSA.
   - Carl Grillmair -- Caltech IPAC. Academic staff pages are usually institutionally owned, not public domain. Check anyway; ask before using.
   - Nuno Loureiro -- MIT PSFC faculty page. Same caveat.
   - Ning Li -- UAH. Academic or archival; verify.
2. **Missing-person flyers and law-enforcement releases.** Photos released by police for the purpose of public circulation are intended to be redistributed. This likely covers Chavez, Reza, Garcia and McCasland. Note the releasing agency as the source.
3. **News outlet photographs -- do not embed.** These are copyrighted, usually licensed from wire services or supplied by families. Link to the article instead. Do not hotlink the image either.
4. **Family-supplied photographs -- do not use without permission.** Four of these families are dealing with an open case. Do not scrape social media.

For each of the 14, record in a new `PHOTOS.md`: whether an image was found, the source URL, the licence or rationale, and the attribution string to display. Then:

- If an image clears (1) or (2), save it to `assets/photos/<id>.jpg`, add a `photo` and `photoCredit` field to that case record, and render it in the slot with the credit visible in the detail dock's sources section.
- If nothing clears, **render nothing**. The plate, the case card and the detail dock all omit the image element entirely when `photo` is null -- the plate narrows from 132px to 100px and the layout closes up. Do not substitute a generic silhouette, do not draw an empty placeholder box, and do not generate anything. Absence is already carried by the record.

Expect a partial result. My estimate is that the government and law-enforcement routes will cover roughly half the list, and that is a good outcome. A design where six plates carry real faces and eight carry none is better than one that fakes uniformity -- the plates without photographs are simply narrower, and the graph tightens up around them.
