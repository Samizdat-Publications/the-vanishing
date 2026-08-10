# The Vanishing v2 -- Design System

Companion to `CLAUDE-DESIGN-PROMPT.md`. Written for the implementer: every value here is literal, and where a decision was non-obvious there is a one-line reason.

Reference mockup: `The Vanishing v2 - Reference Mockup.dc.html`
Graph engine used by the mockup: `vanishing-graph.js`

Decisions taken with the owner before design started:

| Question | Answer |
|---|---|
| Shell | Workstation: fixed left rail of views, canvas centre, panels dock right |
| Analyst | Bottom command bar expanding upward into a transcript, keyboard-first |
| Edge language | Orthogonal circuit routing, with connection strength encoded |
| Node language | Dossier plate with photo slot |
| Renderer | WebGPU first, WebGL fallback |
| Terminal literalness | Terminal command surface, modern chrome |
| API key | User pastes an Anthropic key into settings, stored in localStorage, direct browser call |

---

## 1. Foundations

### 1.1 Colour

Neutrals are a single cold graphite ramp. Every accent sits at roughly the same lightness and chroma and varies only in hue, so no one category shouts over another.

| Token | Hex | Use |
|---|---|---|
| `--bg` | `#0f1216` | App background, canvas base |
| `--bg-sunk` | `#0d1014` | Inputs, photo slots, wells |
| `--panel` | `#12171d` | Rails and docks |
| `--panel-2` | `#141920` | Cards, top bar, raised surfaces |
| `--panel-3` | `#1a2027` | Hover, selected row |
| `--line` | `#1d242b` | Hairline inside a panel |
| `--line-2` | `#262e36` | Panel boundary |
| `--line-3` | `#333c47` | Input border, chip border |
| `--line-4` | `#3b444f` | Emphasised border, tooltip |
| `--text` | `#e6e9ee` | Primary |
| `--text-2` | `#dfe4ea` | Body copy in cards |
| `--text-3` | `#b9c2cd` | Secondary |
| `--text-dim` | `#8d97a4` | Labels, inactive rail items |
| `--text-faint` | `#5c6672` | Metadata, dot leaders |
| `--text-ghost` | `#4f5964` | Placeholders, counts |

Semantic accents:

| Token | Hex | Meaning |
|---|---|---|
| `--signal` | `#5ed4e6` | System voice: analyst, computed findings, confirmed confidence, active selection |
| `--dead` | `#e8705f` | Status: dead |
| `--missing` | `#efb555` | Status: missing. Also the "claim" confidence level |
| `--transitioned` | `#d98a6a` | Status: was missing, now dead (Casias) |
| `--institution` | `#a795e8` | Node class |
| `--program` | `#66d69f` | Node class. Also analyst action narration |
| `--location` | `#7fb4e8` | Node class |
| `--domain` | `#e08ad0` | Node class |
| `--person` | `#c9d2dd` | Node class fallback |

Rules:

- Status colour appears on exactly two surfaces per person: the plate's left stripe and the status badge. Never as a fill behind text.
- `--signal` is reserved for the system speaking. A user-authored filter chip that happens to be active uses `--signal`; a piece of case data never does.
- Maximum two background tones on screen at once (`--panel` and `--panel-2`).
- Never use hue alone to carry a required distinction; every colour-coded thing also carries a text label. The eight connection types are labelled in the legend and in every connection row.

### 1.2 Typography

One family: **IBM Plex Mono**, weights 400 / 500 / 600. A single mono face across the whole product is the main reason the thing reads as software rather than a page. Fallback `ui-monospace, monospace`.

| Role | Size | Weight | Tracking | Notes |
|---|---|---|---|---|
| Product name | 14px | 600 | 0.01em | Top bar only |
| Panel title | 14.5px | 600 | 0 | Selected entity name |
| Card title | 12px | 600 | 0 | Case cards, cluster headers |
| KPI value | 16px | 600 | 0 | Stats strip |
| Body | 11.5px | 400 | 0 | Analyst transcript, insight copy, card prose. `text-wrap: pretty` |
| UI default | 11px | 400 | 0 | Rail items, inputs |
| Data row | 10.5px | 400 | 0 | Dot-leader rows, connection rows |
| Meta | 10px | 400 | 0 | Dates, secondary lines |
| Micro label | 9px | 400 | 0.10em | Counts, tooltip class line |
| Section eyebrow | 8.5px | 400 | 0.13em | Uppercase. `RECORD`, `CONNECTIONS`, `VIEWS` |
| Plate name (canvas) | 10.5px | 600 | 0 | `SURNAME, I.` |
| Plate date (canvas) | 8.5px | 400 | 0 | `2025.05.04` |

Dot leaders: data rows are `KEY` + `.` fill + `VALUE` at a fixed character width, rendered in a `white-space: pre` element. They give a dense two-column read with no table and no alignment CSS. Widths in use: 22 (rail), 37 (connections), 38 (record), 40 (case rows), 46 (geography), 52 (left-behind). Each width is set to the widest leader that fits its container at 10px -- check it when a column width changes, because an over-wide leader clips rather than wraps.

Never below 10px for anything a user must read. 8.5px is permitted only for uppercase eyebrows and counts.

### 1.3 Spacing, shape, elevation

4px base. Steps used: 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 18, 20.

Radius: **0 everywhere**, except 2px on canvas plates and 4px on scrollbar thumbs. Square corners are load-bearing for the instrument feel.

Elevation is borders, not shadows. Three levels:
1. Flush -- `1px solid var(--line)` inside a panel
2. Raised -- `1px solid var(--line-2)` on `--panel-2`
3. Floating -- `1px solid var(--line-4)` plus `0 10px 30px rgba(0,0,0,0.65)`. Tooltips and menus only.

Accent left border marks meaning, never decoration:
- `2px solid var(--signal)` -- computed / confirmed
- `2px dashed var(--missing)` -- claim, or a disputed official finding
- `2px dotted var(--text-dim)` -- open question, or a missing-person record with no determination
- `2px solid var(--program)` at 45% alpha -- analyst action narration

### 1.4 Ambient treatment

Two full-bleed overlays at `z-index: 40`, `pointer-events: none`, above content and below nothing:

1. Scanlines -- `repeating-linear-gradient(180deg, transparent 0 2px, rgba(0,0,0,0.13) 3px, transparent 4px)` at `opacity: 0.5`
2. Vignette -- `inset 0 0 160px rgba(0,0,0,0.6)`

Plus a global `text-shadow: 0 0 7px rgba(94,212,230,0.07)` -- a phosphor bloom weak enough to survive small type.

A 1px cyan sweep line crosses the canvas every 7s. It is the only unprompted motion in the product. Everything else moves in response to the user.

### 1.5 Motion tokens

| Token | Duration | Easing | Applies to |
|---|---|---|---|
| `--t-instant` | 85ms | linear | Tooltip opacity |
| `--t-quick` | 140ms | `cubic-bezier(.4,0,.2,1)` | Hover, chip toggle, row highlight |
| `--t-panel` | 220ms | `cubic-bezier(.2,0,0,1)` | Detail panel, transcript expand |
| `--t-layout` | 620ms | `cubic-bezier(.32,.72,0,1)` | Node repositioning after a filter change |
| `--t-ambient` | 7s | linear, infinite | Canvas sweep |
| `--t-pulse` | 2.6s | `ease-in-out`, infinite | Missing-status pulse, live status dot |
| `--t-caret` | 1.1s | `steps(1)`, infinite | Analyst caret blink |

Nodes never jump. Any filter or layout change interpolates over `--t-layout`.

---

## 2. Layout architecture

Persistent app shell, four rows, never scrolls as a whole:

```
┌─────────────────────────────────────────────── 46px  top bar
├─────────────────────────────────────────────── 46px  stats strip + confidence key
│ 202px  │        1fr         │      306px    │  1fr   body
│  rail  │   view surface     │  detail dock  │
├─────────────────────────────────────────────── auto   analyst
└───────────────────────────────────────────────
```

- The **view surface** is the only thing that changes between views. Rail, stats, dock and analyst are constant. This is why the analyst can drive the whole product: there is one thing to swap.

  Because the surface swaps, leaving NETWORK unmounts the canvas and returning mounts a *new* element. Bind the map controller to the canvas element it was built on and re-mount when that element changes, carrying the current selection and hop count across -- a "have I mounted before" guard leaves the controller drawing into a detached node and the live canvas permanently blank.
- The **detail dock** is one component that handles all five node classes. It never empties into nothing; with no selection it explains what clicking does.
- The **analyst** owns the full width at the bottom so a long answer has room to be read, and so it is never covering the map it is describing.

Breakpoints:

| Width | Behaviour |
|---|---|
| ≥1440px | As above. Design target. |
| 1180–1439px | Rail 176px, dock 272px. |
| 900–1179px | Dock becomes an overlay panel sliding from the right over the view surface. Rail collapses to numbers only. |
| <900px | Single column. View surface full width, rail becomes a top tab strip, dock becomes a bottom sheet, analyst collapses to its input row. Tablet secondary, phone nice-to-have. |

---

## 3. The network map

### 3.1 Rendering

WebGPU where available, WebGL2 fallback, and a canvas-2D floor for anything older. The reference mockup is canvas 2D because it only has to prove the visual language; production should not be.

Layer order, back to front:
1. Vertical gradient base, `#161a20` → `#11141a`
2. 44px grid, `rgba(59,68,79,0.18)`, 1px
3. Cluster wells -- radial gradient per named cluster, centred on the mean of its person nodes, radius = furthest member + 120px, stops `0.055 → 0.022 → 0` in the cluster tint. Cluster name at the top of the well at 32% alpha.
4. Edge traces
5. Nodes
6. Insight callout, hop controls, tooltip (DOM, not canvas)

Cluster tints: California `94,212,230` · New Mexico `239,181,85` · Huntsville `167,149,232`.

Layout: force-directed with cluster anchors. Repulsion `3200/d²`, spring constants 0.02 (structural) and 0.006 (temporal/behavioural -- weaker so timing ties do not distort geography), hard minimum separation `radiusA + radiusB + 14`. Alpha decays 0.994 per step to a 0.06 floor. 900 steps run before first paint so the graph opens settled.

Collision radii: person 58 with a photo, 46 without, institution 22, programme 22, location 17, domain 17.

The canvas backing store must track its CSS box exactly (`width = cssWidth × dpr`). Re-assert it **inside the draw loop, every frame**, measuring the canvas element itself -- a `ResizeObserver` alone is not sufficient, because a CSS grid can settle without the observer landing the final height, and a stale buffer scales the canvas non-uniformly so every plate renders wide-and-short. Keep the observer for the re-anchor and settle work, but never let it be the only thing that sizes the buffer. On a real size change, re-anchor and run ~220 settle steps rather than rebuilding the layout.

### 3.2 Node design

**Person -- dossier plate.** 40px tall, 2px radius, `--panel` fill, `--line` border. **100px wide by default; 132px only when a real photograph exists to fill the slot.** An empty slot spends 32px of plate width saying nothing, so it is not drawn -- the absence of a portrait is already carried by the record, and a hatched box repeated fourteen times reads as decoration rather than as information.

```
with photo (132)                     without photo (100)
┌─┬──────┬─────────────────────┐     ┌─┬─────────────────────┐
│▌│ ▓▓▓▓ │ SULLIVAN, M.        │     │▌│ SULLIVAN, M.        │
│▌│ ▓▓▓▓ │ 2024.05.12     DEC  │     │▌│ 2024.05.12     DEC  │
└─┴──────┴─────────────────────┘     └─┴─────────────────────┘
```

- Status stripe: 3px, full height, status colour. The only place status appears as a fill.
- Photo slot (when present): 26×26 at x+9, y+7, `object-fit: cover`, `--line-2` outline. Text block starts at x+43.
- No photo: text block starts at x+11. Collision radius drops from 58 to 46, so the graph tightens up.
- Name: `SURNAME, I.` at 10.5px/600, baseline y+18. Surname-first is what makes 14 plates scannable.
- Date `YYYY.MM.DD` at 8.5px, baseline y+31. Status code right-aligned same baseline: `DEC` · `MIS` · `D←M`.

The same rule applies to the detail dock (56×68) and case cards (42×52): render the image or render nothing. Render it as a `background-image` on the slot div, not as an `<img src>` -- a template-driven `src` fires a network request for the unresolved placeholder string before the value lands, which shows up as a console error on every load. See `COWORK-HANDOFF.md` for which portraits are likely to clear licensing.

**Other classes** are small marks with the label beneath at 9px:

| Class | Mark | Size |
|---|---|---|
| Institution | Square, stroked | 6.5px half-extent |
| Programme | Diamond, stroked | 6px, ×1.3 on the diagonal |
| Location | Circle, stroked | 4.5px radius |
| Research domain | Circle, stroked, with a filled core at 42% radius | 5.5px radius |

Node states:

| State | Treatment |
|---|---|
| Default | As above |
| Hover | Border → class colour, `shadowBlur 11` in class colour, label → `--text` |
| Selected | Border 1.5px class colour, fill `--panel-2`, `shadowBlur 24` |
| Connected to selection | Border → `#56616e`. No glow. Legibility, not celebration. |
| Dimmed | `globalAlpha 0.16` |
| Filtered out | Animates to `globalAlpha 0` over `--t-layout`, then stops being hit-tested |

Level of detail: below scale 0.5, plates collapse to a 5px status dot; non-person labels drop below scale 0.62. Selected and hovered nodes always render at full detail regardless of scale.

### 3.3 Edge design -- circuit routing with strength

**Geometry.** One trace per *pair*, right-angled, with a single mitred corner. The corner sits at `min(|dx|,|dy|) × 0.55` along the shorter axis; the long axis runs first. `lineJoin: miter`, `lineCap: butt`. Right angles keep 200+ traces separable in a way curves do not at this density.

**Strength.** Edges are aggregated by pair, and weight is *the number of independent connection types tying that pair together*. One shared employer is weak evidence. Employer plus geography plus domain plus timing is the thing a reader should look at first. This is the answer to "let me see the strong connections at a glance", and it is computed, not authored.

| Weight | Label | Idle colour | Width | Extra |
|---|---|---|---|---|
| 1 | Single link | `#4d5a66` | 0.9px | -- |
| 2 | Corroborated | `#6e8b9c` | 1.8px | -- |
| 3 | Strong | `#5ed4e6` | 2.8px | Glow `blur 12`, 3 tick marks at the corner |
| 4 | Very strong | `#8ee6f0` | 3.8px | Glow `blur 15`, 4 ticks |
| 5 | Maximal | `#d7f6fa` | 4.8px | Glow `blur 17`, 5 ticks |

Idle alpha `0.30 + (weight − 1) × 0.15`. Traces draw weakest-first so strong ones land on top. Tick marks are 2.2px squares stacked at the corner on a 3.4px pitch, one per link type -- the exact weight is countable, not just felt.

**Idle vs selected.** At rest, hue carries *strength* and the eight types are not individually distinguishable -- that is deliberate, because at rest the question is "where should I look". Inside a selection, hue switches to the **dominant type colour** so the categories become readable, at alpha 0.95, with everything outside the selection at 0.045.

Dominant type precedence: witness-chain → investigative → programmatic → behavioural → institutional → research → geographic → temporal.

Connection type colours, used inside selections, in legends, and on every connection row:

| Type | Colour | Derivation |
|---|---|---|
| Institutional | `#a795e8` | Same `instId` |
| Geographic | `#7fb4e8` | Same `geoCluster` (excluding `other`) |
| Research domain | `#e08ad0` | Shared entry in `researchDomain` |
| Temporal | `#efb555` | Dates within 60 days |
| Behavioural | `#e8705f` | Shared entry in `leftBehind` |
| Programmatic | `#66d69f` | Hand-authored, sourced |
| Investigative | `#5ed4e6` | Hand-authored, sourced |
| Witness chain | `#f0d264` | Hand-authored, sourced |

The first five are **derived by rule** from the case records, so adding a case creates its connections automatically. The last three are **editorial** and stay hand-written, because they come from reporting rather than from a rule. Keep that split; it is what stops the graph inventing relationships.

### 3.4 Controls and tooltip

Hop buttons sit top-left of the canvas: `1 hop` / `2 hops` / `3 hops` / `clear`. Active is `rgba(94,212,230,0.12)` on a `--signal` border.

Tooltip is three lines, `white-space: pre`, floating elevation, offset +15/+15 from the cursor, 85ms opacity:

```
[PERSON] Anthony Chavez
LANL (construction foreman) / Espanola, NM
strongest: Melissa Casias (4 link types)
```

The third line is the point: hovering tells you where to click next.

### 3.5 Algorithmic pattern discovery

Callout, bottom-left of the canvas, `--panel-2` at 96%, `--signal` left border, 372px. Eyebrow states its provenance: `STRONGEST PAIR · COMPUTED`. Two actions: **Show me on the map** (drives the map to the entities described) and **Next pattern**. Dismiss `×` top right.

Deterministic on the client -- no model needed, and therefore always available:

| Pattern | Computation |
|---|---|
| Strongest pair | `max(weight)` over aggregated pairs |
| Temporal clustering | Case count per rolling 8-month window |
| Behavioural signature | Count of records with a non-empty `leftBehind`, and how many states they span |
| Institutional overlap | Case count per institution, against headcount where known |
| Domain convergence | Domain sets intersected with cluster membership |
| Structural | Betweenness for bridge nodes; shortest path between any two entities; connected components inside a named cluster |

Send to a model only for interpretation -- phrasing a finding, judging whether an overlap is meaningful against base rate, answering an open-ended question. **Never** to decide whether a connection exists. The graph is the authority on what is connected; the model is only allowed to talk about it.

---

## 3.6 The scoring model

Every case carries three independent scores plus a composite tier. The axes are deliberately **not summed**. A case can be extraordinary on one axis and unremarkable on another, and collapsing that into one number destroys the information the tracker exists to surface.

| Axis | Range | Question |
|---|---|---|
| **S** Sequence anomaly | 0-3 | How many independently documented, individually unexplained links form a chain around this event? |
| **P** Program proximity | 0-3 | What sensitive access did this individual personally hold? |
| **I** Institutional channel | 0-3 | Does the employer have a documented history as a conduit for classified work? |

| Tier | Colour | Meaning |
|---|---|---|
| **A** | `--signal` | Contains a specific unexplained fact no source accounts for |
| **B** | `--missing` | Unresolved, but a prosaic explanation exists and is not ruled out |
| **C** | `--text-dim` | A conventional explanation is documented and holds. Retained for completeness |

The two cases that prove why three axes are needed:

- **Carl Grillmair, S3 / P1 / I3.** The strongest documented sequence in the file: he reported his eventual killer for trespassing, the man was arrested with a loaded unregistered rifle, released after three days, had charges dropped on February 5, and killed him on February 16. Eleven days. But he studied dark matter and exoplanets and held no documented clearance, while working inside the institution that manages JPL. A reader has to see all three of those at once. A single grade would either overstate or erase him.
- **Joshua LeBlanc, S2 / P3 / I3.** Active nuclear propulsion engineer on DRACO. Four unexplained hours with his car at the airport. Phone and wallet at home. Dead the same day. High on all three axes, and version one buried him as a routine entry.

**Rendering.** Three 3-pip meters, filled in the tier colour. Never a bar out of ten, never a star rating, never summed into one figure. On the card face they are a compact inline row; in the dossier they are labelled rows with the axis name.

Three terminal states, not two: **missing** (4), **dead** (10), **resolved** (1). Resolved gets `#6f7f8c`, a settled grey that reads as closed rather than as a third alarm colour. Two cases carry tags that are visible without being apologetic: `NON-DEFENSE` (Jason Thomas, Novartis) and `MEDIA-LINKED ONLY` (James Moffatt, on no mainstream list). Both are retained deliberately to show the list is not curated.

## 4. The AI Analyst

### 4.1 Layout

Bottom command bar, full width, three stacked parts:

1. **Header row**, 7px/14px padding -- `ANALYST` eyebrow in `--signal`, then live status, then a Collapse/Expand affordance.
2. **Transcript**, `max-height: 208px`, scrolls. Each turn is a 66px role gutter plus content.
3. **Suggestion chips**, then the **input row** -- blinking caret, input, `SEND`.

Collapsed, only the header and input row remain. The dashboard never loses its command line.

### 4.2 Conversation states

| State | Treatment |
|---|---|
| Idle | Status `ready · key stored locally · <model>` in `--program`. Caret blinking. |
| Receiving input | Input border → `--signal`. |
| Thinking | Status → `thinking`, three dots cycling at `--t-pulse`. Transcript shows the role gutter with an empty content block, so the layout does not jump when text arrives. |
| Executing actions | Action lines stream in *before* the prose. The user sees the map move and the reason for it in the same beat. |
| Streaming | Text appends. No typewriter effect on already-settled text. |
| Error | Status → `--dead`, message inline in the transcript as an analyst turn, retry affordance. |
| Rate limited | Status → `--missing`, states the wait. Input stays enabled; queued send. |
| No API key | Status → `--missing`: *no API key configured -- running scripted replies. The dashboard stays fully usable by hand.* This is a first-class state, not an error. |

### 4.3 Action narration

Every dashboard action the analyst takes is printed in the transcript, in the same beat as the answer:

```
:: selectNode("sullivan")
:: highlightPath("sullivan","oversight",hops=3)
:: setEdgeFilter(["witness-chain","programmatic"])
```

9.5px, `--program`, `rgba(102,214,159,0.05)` background, 2px left border at 45% alpha, `white-space: pre`. Verbatim function calls, not prose descriptions -- the user learns the command surface by watching it used, and can retype any line.

### 4.4 Citation and traceability

Every factual claim traces to a case record. Citations render as clickable chips below the turn: 9px, `--line-3` border, `--text-dim`. Clicking drives the map to the cited entity. A claim with no attributable source in `SOURCES` must not get a chip -- the record says *No attributed source on file for this entity* instead. Absence of sourcing is information.

### 4.5 Suggested questions

Four chips above the input, contextual to the current view and selection. Pill-free: 1px `--line-3` border, square, hover to `--signal`. They are phrased as the owner would actually ask, including the ones with uncomfortable answers ("Is the JPL overlap meaningful or just base rate?").

### 4.6 Credentials and model settings

The top bar carries a single affordance reading `Set API key`, which becomes `API key set` once one exists. Clicking it opens a settings panel anchored under the button.

**Do not build this as a centred modal.** The app root is taller than the viewport and sits inside a transformed ancestor, so `position: fixed` computes as `absolute` and a centred overlay puts the card below the fold. The panel is `position: absolute; top: 46px; right: 15px`, with `max-height: calc(100% - 120px)` and its own scroll.

Three sections:

1. **Anthropic API key.** A password-type field, Save and Remove actions, and a live state line. Save validates the `sk-ant-` prefix before writing. Copy states plainly that the key is stored in this browser only, sent directly to api.anthropic.com, and that a Console key with credits is required because a Pro or Max subscription does not carry API access.
2. **Model.** Three options as selectable rows, each with a one-line reason to pick it. Default **claude-sonnet-5**: fast enough for conversational use, strong enough to reason across the whole case file. Haiku 4.5 for lookups, Opus 4.6 for genuinely hard comparative questions.
3. **Reasoning effort.** Instant / Balanced / Deep, with the selected option's rationale printed below. Default **Balanced**: a short thinking budget on questions that need it and none on map commands, which keeps driving the interface instant while still reasoning properly across cases.

Persistence is exactly three localStorage entries, `vanishing.apiKey`, `vanishing.model`, `vanishing.effort`, all reads and writes wrapped in try/catch so a browser with storage blocked still runs. Nothing else in storage is touched.

The analyst status line reflects all three: with a key it reads `ready · key stored in this browser · claude-sonnet-5 · balanced`. Without one it states that scripted replies are running and the dashboard stays fully usable by hand. That is a first-class state, not an error.

## 5. The dashboard command surface

One namespace both the UI and the analyst call. No component mutates state directly. Implement exactly these names.

| Action | Parameters | Effect |
|---|---|---|
| `selectNode` | `id: string` | Selects any node of any class, recomputes the active neighbourhood, opens the detail dock, switches to NETWORK if elsewhere |
| `clearSelection` | -- | Drops selection, restores the full network |
| `setHops` | `n: 1\|2\|3` | Re-expands the active neighbourhood around the current selection |
| `highlightPath` | `from: id, to: id, hops?: n` | Highlights the shortest path between two entities, dims the rest |
| `setView` | `v: 'NETWORK'\|'TIMELINE'\|'GEOGRAPHY'\|'CASES'\|'ANALYSIS'\|'COUNTERARGS'\|'SEARCH'` | Swaps the view surface |
| `toggleFilter` | `key: string` | Toggles one status / cluster / domain / clearance filter. Filters compose |
| `setEdgeFilter` | `types: string[]` | Restricts which of the eight connection types render |
| `clearFilters` | -- | Resets every filter |
| `focusCluster` | `c: 'california'\|'new-mexico'\|'huntsville'` | Frames and selects into a named cluster |
| `frameNodes` | `ids: string[]` | Zooms and pans so exactly these nodes fill the canvas |
| `expandCase` | `id: string` | Switches to CASES and expands one card |
| `search` | `q: string` | Switches to SEARCH and runs the query |
| `showInsight` | `i: number` | Surfaces a specific computed pattern in the callout |
| `dismissInsight` | -- | Hides the callout |
| `setTimelineZoom` | `z: 'year'\|'quarter'\|'month'` | Timeline granularity |
| `toggleTimelineOverlay` | `track: 'congress'\|'fbi'\|'pursue'\|'media'` | Shows or hides a context track |

Every one of these is reachable by clicking too. If a control exists that has no entry here, the analyst cannot operate it, and the "operate the whole app from the chat input" requirement is broken.

---

## 6. Other components

### 6.1 Stats strip

Six KPI cells, 46px, each `1px solid --line` on the right: 8.5px eyebrow over a 16px/600 value with a 9px unit. Values coloured only where status colour applies (dead red, missing amber, investigations green). Right end carries the confidence key permanently, so the three levels are legible on every view.

### 6.2 Detail dock: the dossier

**This is the second most important surface in the product after the map itself.** A click on any node opens a full dossier, not a demographic summary. Fixed header plus four tabs.

Header, always visible:
1. Class eyebrow, non-defense or media-linked flag, status badge (`DEAD` / `MISSING` / `RESOLVED`)
2. Portrait (56x68, omitted entirely when there is no photograph), name, affiliation, location and date
3. **Assessment block**: tier badge plus the three axes as 3-pip meters (S, P, I), each labelled, plus the tier rationale in one sentence. Pips are filled in the tier colour and empty in `#232b34`. Three separate meters, never a sum, never a rating out of ten.
4. **Unexplained residual**, when present: the specific fact no published source accounts for, on a solid `--signal` border. This is the load-bearing content of a Tier A case and it sits above the tabs so it cannot be missed.

| Tab | Contents |
|---|---|
| **DOSSIER** | Narrative prose (the story, several sentences, written to be read). Affiliations list. Record dot-leaders. `SOURCES DISAGREE` blocks on dashed amber. `UNVERIFIED, NOT PROPAGATED` blocks on dotted grey. |
| **CHAIN** | The sequence chain as a vertical connector: filled cyan node for an unexplained step, hollow grey for an ordinary one, each with date, event, and its own source. Then the full chronology. When no chain exists, the panel says why that is a finding rather than a gap. |
| **LINKS** | Every connection, strongest first, each with a plain-language sentence explaining *why* the two are linked, not just the type name. Weight and dominant type on the right. |
| **SOURCES** | Claims grouped by evidence level (Tier 1 documented, Tier 2 sourced claim, Tier 3 inference), each with its attribution, then the source list. |

Missing values render as `NOT REPORTED` / `NOTHING RECORDED` / `NONE RECORDED` in `--text-faint`, never blank, never zero.

### 6.3 Case cards

Collapsed card face carries: status stripe, portrait (only if one exists), name, affiliation, status badge, **tier badge**, date, and the **three axis meters**. The scores are the most-used piece of information in the interface and they are visible without expanding.

Expanded adds the full narrative, the unexplained residual, record dot-leaders, the **sequence chain** as a compact vertical connector with unexplained steps marked, any source conflicts, the source list, and an `Open on map` action. Grid is `repeat(auto-fill, minmax(268px, 1fr))`.

### 6.4 Timeline: three strands, one axis

Vertical, not horizontal. Forty labelled entries cannot be read on a horizontal axis without rotated text, collision, or sideways scrolling; all three were tried and all three failed. The axis runs down the page and the entries read as prose.

Layout: a year gutter (62px, right-aligned, sticky, printed only when the year changes) plus three strand columns.

| Strand | Contents | Accent |
|---|---|---|
| CASES | Deaths and disappearances | Tier colour of that case |
| OVERSIGHT & DISCLOSURE | What the state said and did, and when | `--program` |
| THE SKEPTICAL RECORD | What the published analysis concluded | `--text-dim`, dashed border |

The three-column arrangement IS the argument: the cases cluster through 2025, the state arrives in April 2026, and the published analysis reverses it inside eleven days. Read as one list, that relationship disappears.

Each entry is a card: title, one sentence of substance, and a stamp reading the formatted date plus its **precision** (`day-precise`, `month-precise`, `year-precise`, `ranged`). Precision is rendered, never smoothed. Case cards carry their tier badge and are clickable through to the map.

Below the axis: the reporting-attention caveat as an open-question card, then **Precedent**, a set of documented declassified items outside the window (MKULTRA, Frank Olson, the Church Committee, the June 30 2026 MKULTRA hearing). Precedent is styled as an archival exhibit, plainer than the case cards, because it is establishing that a mechanism has history rather than making a claim about these cases.

**Responsive:** below 820px of surface width the three columns stack into one and each entry carries its strand as a chip instead. Measured with a `ResizeObserver` on the view surface, queried by `[data-surface]`.

### 6.5 Geography

Three cluster cards. Header: tint swatch, name, case count. Body: dot-leader member rows. Footer: the distance claim on a dashed amber border, because those figures come from reporting rather than from coordinates. A closing dotted card says so explicitly. If real geodata is added later, that footer becomes a solid confirmed border and the caveat card goes.

### 6.6 Analysis

Four pattern cards, each tagged with provenance (`CONFIRMED · COMPUTED`, `CLAIM · REPORTED`, `OPEN QUESTION`) and carrying a `show →` that drives the map. Then the institutional overlap bar chart -- labelled with counts, bars in `--institution` at 2+ cases and `#4d5a66` below. Then the left-behind tracker as dot-leader rows.

Every chart carries data labels.

### 6.7 Counterarguments

Same card grammar as Analysis, same density, dashed amber borders. Five entries: Scientific American, Skeptic Magazine, Bartholomew, PolitiFact, NeuroLogica. Opens with one line stating why the view exists. It must never read as an appendix; equal weight is a design requirement, not a disclaimer.

### 6.8 Search

Full-width input, result rows of `class · label · meta`, class in its node colour. Empty state shows the first nine of 52 entities rather than nothing. Filter state and query belong in the URL so a view is shareable.

---

## 7. Interaction and animation

| Trigger | Duration | Easing | Effect |
|---|---|---|---|
| App load | 0–900ms | -- | Chrome paints immediately; force layout runs 900 steps off-screen; nodes fade up over 400ms in weight order, weakest traces last |
| Node hover | 85ms | linear | Tooltip in; border and glow up |
| Node click | 220ms | `--t-panel` | Neighbourhood computed, non-members to `alpha 0.16`, dock slides in, edge hue switches from strength to type |
| Hop change | 620ms | `--t-layout` | Neighbourhood grows outward one ring at a time |
| Filter toggle | 620ms | `--t-layout` | Removed nodes fade to 0 and stop being hit-tested; remaining nodes re-run the layout and interpolate. Never snap |
| View switch | 220ms | `--t-panel` | View surface cross-fades. Rail, stats, dock and analyst do not move |
| Card expand | 220ms | `--t-panel` | Height auto-animates; `+` becomes `−` |
| Analyst send | -- | -- | User turn appends immediately; thinking state within 100ms |
| Analyst actions | 140ms apart | `--t-quick` | Action lines stream one at a time, each firing its dashboard change as it prints |
| Insight surface | 220ms | `--t-panel` | Callout rises 8px and fades in |
| Ambient sweep | 7s | linear | 1px cyan gradient line crosses the canvas |
| Missing pulse | 2.6s | `ease-in-out` | Missing-status nodes breathe between 0.3 and 1 alpha on their stripe only |

`prefers-reduced-motion`: drop the sweep, the pulse and the caret blink; keep state transitions but cut them to 100ms.

---

## 8. Credibility rules the design enforces

1. Three confidence levels, three border treatments, applied everywhere a claim appears. No claim renders without one.
2. Counterarguments get a top-level view with the same card grammar and density as Analysis.
3. Unsourced entities say so. `No attributed source on file for this entity.`
4. Derived connections are separated from editorial ones in the data layer, so the map cannot quietly invent a relationship.
5. Distance and proximity claims are labelled as reported, not measured, until real geodata exists.
6. The analyst is designed to say the data does not support a reading, and three of the four shipped suggested questions have answers that push back.
7. Absent values are printed as absent, never as zero.

---

## 9. Data layer

Case records follow `RESEARCH-PROCESS.md` §3.1, extended with the fields the map needs: `instId`, `locId`, `clearance`, `leftBehind`, `cause`. Everything downstream derives from one array -- nodes, edges, strengths, filters, stats, timeline, geography, analysis. Adding a case is editing that array and nothing else.

Five node classes, all clickable: person (14), institution (12), programme (6), location (14), research domain (6) -- 52 today, and the layout is tuned to stay legible at 3×.

`vanishing-graph.js` in this repo is the working implementation of the derivation, the layout, the strength aggregation and all four edge languages that were prototyped. Production should port it to WebGPU and keep the derivation as-is.
