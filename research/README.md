# research/

Hand-editable source of truth for the case data, extracted from `the-vanishing-v2.html`
by `tools/extract.py`.

**Until the byte-for-byte checkpoint passes, these files are an extraction artefact, not
yet the live source.** The dashboard still ships from `the-vanishing-v2.html`. See
`ARCHITECTURE.md` migration order.

## Rules for editing these files

- **Key order is data, not style.** The source file's key order is authorial. `grillmair`
  writes its keys in a different order from the other 14 cases, an artefact of the
  August 7 follow-up appending two keys after the fact. Reordering it changes the output.
  **Never run a formatter over these files, and never `sort_keys`.**
- **Array order is load bearing.** `cases.json` is an ordered array, not a keyed object.
  `NODES` index seeds the force layout, and `deriveEdges` iterates pairwise, so
  reordering changes both the emitted edge order and the initial graph.
- **Absent means default.** A key absent from a record takes its value from
  `case_defaults.json`, which mirrors the `P_` factory. Writing a key whose value equals
  its default changes the output. The rule was verified exception-free across all 15
  records and all 13 default keys.
- **Do not normalise strings.** `leftBehind` contains `'phone'`, `'phones'` and
  `'iPhone'` as three distinct tokens. The behavioural edge rule is exact string match,
  so tidying them silently adds edges. Logged in `notes/step3-backlog.md`.
- **Dates are strings of variable precision.** `'1953'`, `'2026-04'` and `'2026-08-04'`
  all occur. Never coerce to a date type.

## What is extracted

| File | Blocks | Contents |
|---|---|---|
| `cases.json` | `PEOPLE` | 15 case records, date ascending |
| `entities.json` | `INSTITUTIONS`, `PROGRAMS`, `LOCATIONS`, `DOMAINS`, `ENTITY_INFO`, `ENTITY_SOURCES`, `SOURCES` | 39 non-person nodes plus their dossiers and bibliographies |
| `timeline.json` | `TIMELINE`, `PRECEDENT` | 42 timeline entries, 4 historical precedents |
| `graph.json` | `PROGRAM_EDGES`, `IN_FBI`, `IN_OVERSIGHT`, `INSTITUTION_PLACES`, `TEMPORAL_WINDOW_DAYS` | The hand-authored editorial edges and membership lists |
| `photos.json` | `PHOTOS` | 15 image paths with per-image credit |
| `taxonomy.json` | `CLUSTERS`, `TIERS`, `AXES`, `STRANDS`, `STATUS_LABEL`, `PRECISION_LABEL` | Scoring and display taxonomy |
| `case_defaults.json` | the `P_` factory | Mirror of the defaults. `verify.py` asserts it still matches the shell |

**Derived, never extracted:** `NODES`, `EDGES` and `deriveEdges()`. They are computed from
the above. The source comment at line 596 is a design constraint worth repeating: the first
five connection types are computed from the records, the last three are editorial and hand
sourced. **Do not merge them.**

## What is deliberately left in the shell, and why

The checkpoint only proves what it covers, so this boundary is a commitment rather than a
convenience.

| Block | Reason |
|---|---|
| `PALETTE`, `EDGE_TYPES` | Design system. Changes when the design changes, not when a case does |
| `COUNTERS` | Analytical content, and by the case-facing test it belongs here. But the "Where the skeptics overreach" table and the "Family positions" paragraph sit inline in `viewCounterargs` (3806-3815) and exist nowhere else in the repo. Extracting one without the other splits a single argument across two files. Both move together in step 3 |
| `MODELS`, `EFFORTS`, `MODEL_CAPS`, `SUGGESTIONS`, `SYSTEM_PROMPT` | Analyst config, coupled to the Anthropic API. Belongs with the code that calls it |
| `VIEW_LABEL`, `FILTER_GROUPS`, `TYPE_PRIORITY`, `STRENGTH_RAMP`, shaders | Renderer internals |

Also not in any data block, and therefore not yet under the gate: the hand-written
analytical prose in `scriptedReply` (4373-4425), which holds the base-rate answer and the
hostile-reader answer. Logged for step 3.

## Provenance

Extracted from `the-vanishing-v2.html`, sha256
`2dfc55e324b7535fbeea223e6b8699bf788ef60d9220417a81bf14bbff3d910a`, 324,923 bytes.

**Never extract from `design-package/vanishing-graph.js` or `vanishing-timeline.js`.**
They are pre-August-7 ancestors differing by three adjudicated axis scores: `li` S0 not S1,
`loureiro` I3 not I1, `mccasland` P2 not P3. The declaration differs by one word
(`export const PEOPLE` versus `const PEOPLE`), so the mistake would be silent.
`tools/extract.py` refuses any path under `design-package/`.
