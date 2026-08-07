# The Vanishing v2: Design Brief for Claude Design

**Project:** The Vanishing -- an investigative research tracker documenting the deaths and disappearances of US scientists, defense officials, and defense-connected individuals since 2021.
**Repo:** `Samizdat-Publications/the-vanishing`
**Owner:** Stewart Gregerson (personal research project, not corporate work)
**Your role:** You have virtually full creative control over the visual design. This document defines *what the thing must do* and *what data it holds*. Every visual decision -- color system, typography, layout, component styling, motion language, overall aesthetic -- is yours to make.

---

## 1. What You Are Designing

A single-page web application that lets a researcher explore a network of people, institutions, government programs, locations, and research domains, and discover non-obvious connections between them.

Two things define v2 and both are non-negotiable:

1. **The Network Map is the centerpiece.** It must be the most visually polished and functionally powerful part of the entire application. Everything else supports it.
2. **A built-in AI Analyst drives the whole dashboard.** A user must be able to operate the entire application without clicking anything except the analyst chat input.

Everything else -- which additional sections exist, how they are laid out, how they look -- is your call, informed by the data.

---

## 2. Read These Files First

All in this repository:

| File | What it gives you |
|---|---|
| `PROJECT.md` | Master data source. All 14 cases, institutions, geographic clusters, analysis threads, counterarguments, source URLs. |
| `scientist-tracker-state-2026-06-20.md` | Latest research sweep. Recent developments: House Oversight investigation, FBI probe, PURSUE file releases, Casias found dead, Grillmair suspect arraigned. |
| `RESEARCH-PROCESS.md` | Weekly research cadence and the canonical case data schema (also reproduced in Section 3 below). |
| `DESIGN-BRIEF.md` | Earlier creative brief. Treat as background context and tone reference, not as binding spec. Where it conflicts with this document, this document wins. |
| `scientist-network-tracker.html` | The v1 tracker you are replacing. Study it to understand the data. Do not carry its design forward. |

---

## 3. The Data Model

### 3.1 Case record schema (canonical)

Case data lives in an editable JavaScript array at the top of the built file so Stewart can add cases by editing one array. Your design must accommodate every field.

```javascript
{
  id: "lastname",
  name: "Full Name",
  status: "dead" | "missing",
  date: "Month DD, YYYY",
  age: 00,
  location: "City, State",
  affiliation: "Institution",
  clearance: "public" | "secret" | "top-secret" | "unknown",
  researchDomain: ["propulsion", "nuclear", "astro", "intelligence", "plasma", "exotic"],
  geoCluster: "california" | "new-mexico" | "huntsville" | "other",
  causeOfDeath: "Description or 'N/A'",
  leftBehind: ["phone", "wallet", "keys", "car", "pet"],
  connections: [
    { to: "other-id", type: "institutional" | "geographic" | "research" | "temporal" | "behavioral" | "programmatic" | "investigative" | "witness-chain" }
  ],
  details: "Full case narrative",
  whyItMatters: "Significance to the pattern",
  sources: [ { name: "Outlet Name", url: "https://..." } ],
  dateAdded: "YYYY-MM-DD",
  lastUpdated: "YYYY-MM-DD"
}
```

Note two states the design must handle: `status` can change over the life of a case (Melissa Casias went from Missing to Dead), and `causeOfDeath` is frequently unknown or officially disputed. Design for uncertainty, not just for known values.

### 3.2 Entity types in the network

The network is **not** just people and institutions. It has five node classes, and **every node of every class must be clickable**:

| Node class | Examples from the data | Notes |
|---|---|---|
| **Person** | The 14 tracked individuals | Two states: dead, missing. Plus a transitioned state (was missing, now dead). |
| **Institution** | NASA JPL, Caltech IPAC, LANL, AFRL, UAH, Institute for Exotic Science, NSA, NASIC, MIT, KCNSC, Novartis, Aerojet Rocketdyne | Sub-types: government, military, academic, private, national lab. |
| **Government program / investigation** | House Oversight investigation, FBI probe, PURSUE UAP file releases, Grusch whistleblower proceedings, Wright-Patterson AFRL programs | These are first-class nodes, not annotations. |
| **Geographic location** | Huntsville AL, Pasadena CA, Lancaster CA, Altadena CA, Pearblossom CA, Los Alamos NM, Espanola NM, Albuquerque NM, Taos/Carson NF NM, Falls Church VA, Cambridge MA, Wakefield MA | Roll up into three named clusters: California/JPL corridor, New Mexico, Huntsville triangle. |
| **Research domain** | propulsion, nuclear, astro, intelligence, plasma, exotic materials | Lets a user see domain convergence across geography and institution. |

### 3.3 Connection (edge) types

Eight types. Each needs a visually distinct treatment that survives being drawn hundreds of times at once:

1. **Institutional** -- worked at or was funded by the same institution
2. **Geographic** -- same geographic cluster or within a stated distance
3. **Research domain** -- same field
4. **Temporal** -- died or disappeared within a window of each other
5. **Behavioral** -- shared the "left everything behind" pattern (phone, wallet, keys, car, pet)
6. **Programmatic** -- tied to the same government program
7. **Investigative** -- swept up in the same investigation (FBI probe, House Oversight)
8. **Witness chain** -- Sullivan to Grusch to Congressional testimony to House investigation

### 3.4 Scale

14 person nodes, 12+ institutions, roughly 6 program/investigation nodes, roughly 12 location nodes, 6 domain nodes. Call it 50 nodes and several hundred edges today, growing over time as Stewart adds cases. Design for the graph to stay legible at 3x that size.

---

## 4. Required Capability: The Network Map

This is the centerpiece. Treat it as the product.

### 4.1 Rendering technology

Use the current state of the art for browser-based visualization. WebGL or WebGPU rendering, GPU-accelerated particle systems, GPU-computed force layouts, instanced rendering, custom shaders -- push what is possible in a browser in 2026. SVG-only or DOM-only rendering is not sufficient for the quality bar here.

Target hardware is an RTX 5070 Ti with 32GB RAM. Do not hold back on GPU effects. Do specify a graceful degradation path for machines without WebGPU.

### 4.2 Required behaviors

- **Every node is clickable.** Person, institution, program, location, domain -- all of them.
- **Clicking a node highlights all of its connections across the entire network** and dims everything else. Multi-hop highlighting (show me what this node reaches in 2 hops) should be available.
- **Clicking opens a detail panel** containing everything known about that entity. For a person that means the full case record: narrative, why it matters, cause of death or disappearance, what they left behind, clearance, all sources as clickable links, connection inventory. For an institution, program, location, or domain it means every entity attached to it and why.
- **Hover** gives a fast, lightweight preview without committing to selection.
- **Filtering** by status, geographic cluster, institution type, time period, research domain, connection type, and clearance level. Filters compose. Nodes animate smoothly into new positions rather than snapping.
- **Zoom and pan**, with level-of-detail behavior so the map is readable both at full-network scale and when zoomed into a cluster.
- **Edge legibility at density.** Edge bundling, curvature, or another approach so the map does not degrade into spaghetti. This is a design problem worth solving well.

### 4.3 Algorithmic pattern discovery

The network must surface connections, clusters, and trends the user has not asked for. This is a stated core requirement, not a nice-to-have. Categories of pattern the system should compute and surface:

- **Temporal clustering** -- are cases accelerating? Are there date collisions?
- **Geographic proximity** -- how close are cases in a cluster to each other, in miles?
- **Institutional overlap** -- shared employers, shared funders, shared program affiliations
- **Behavioral patterns** -- the "left everything behind" signature across 5+ cases
- **Research domain convergence** -- propulsion research clustering inside a 30-mile radius
- **Structural graph patterns** -- bridge nodes, unexpectedly short paths between distant entities, tightly connected subgraphs the named clusters do not capture

Real examples from this data that the system should be capable of surfacing:

> "Three of these individuals worked on propulsion research within 30 miles of each other."
> "Sullivan was a source for Grusch, who triggered the Congressional investigation now probing these cases."
> "Five individuals left their phone or wallet behind before disappearing."
> "All four New Mexico cases are within 150 miles of each other."

Design how these insights appear: as callouts, as a panel, as ambient annotations on the map, as something else. Your call. They must be dismissible, they must be traceable back to the underlying nodes, and clicking one must drive the map to show what it is describing.

An LLM reasoning component is permitted and encouraged as part of this architecture where deterministic graph analysis is not enough. Specify where the boundary sits: what the client computes deterministically versus what gets sent to a model for interpretation.

---

## 5. Required Capability: The Built-In AI Analyst

**This is the second defining feature of v2 and it is absent from the previous version of this brief. Read this section carefully.**

The application ships with a built-in chatbot that acts as an intelligence analyst. It is not a help widget and it is not a search box. It is a second, complete way to operate the entire dashboard.

### 5.1 The requirement, stated plainly

A user must be able to use the entire application without clicking or interacting with anything except the analyst. Every action a manual user can take, the analyst can take on their behalf.

### 5.2 What the analyst can do

The analyst has full control of the dashboard. At minimum it can:

- Select and deselect nodes of any class
- Highlight connections and connection paths between entities
- Apply, combine, and clear filters
- Navigate between views and sections
- Zoom into and frame specific clusters or subgraphs
- Open case detail panels and specific sections within them
- Run searches
- Toggle timeline overlays and change timeline zoom level
- Trigger and dismiss pattern-discovery insights

Design implication: the dashboard needs a **command surface** -- a documented internal API of dashboard actions that both the UI controls and the analyst call into. Specify this command surface as part of your deliverable. Name the actions, name their parameters. Claude Code will implement against your spec, so it needs to be unambiguous.

### 5.3 What the analyst can reason about

The analyst answers questions that require reasoning across the data, not just lookup. Representative questions Stewart will actually ask:

> "Show me all the propulsion researchers."
> "What connects Sullivan to the Congressional investigation?"
> "Are there any temporal patterns I'm missing?"
> "Which institution shows up in the most cases and is that meaningful or is it just base rate?"
> "Show me every case where the official cause of death was disputed by family."
> "What is the weakest link in the New Mexico cluster?"

Note the last two. The analyst must be able to handle questions where the honest answer is "the data does not support that" or "that pattern is probably coincidence." It should not manufacture connections. See Section 8 on credibility.

### 5.4 What you need to design

- **The analyst panel itself.** Docked, floating, overlay, full-takeover mode -- your call. It has to coexist with a dense network map without covering the thing the user is looking at.
- **Conversation states:** idle, receiving input, thinking, executing dashboard actions, streaming an answer, error, rate-limited, no-API-key-configured.
- **Action narration.** When the analyst drives the dashboard, the user needs to see what it did. Design how actions are announced -- inline in the transcript, as a transient action log, as visible cursor-equivalent feedback on the map, or a combination.
- **Citation and traceability.** Every factual claim the analyst makes should be traceable to a case record and its sources. Design that affordance.
- **Suggested questions.** Entry points for a user who does not know what to ask. Contextual to what is on screen.
- **Transcript design.** Long analytical answers with embedded entity references that are themselves clickable and drive the map.
- **The API key path.** The core dashboard runs with no server. The analyst needs a model API. Design the configuration flow for a user supplying their own key, and design the degraded state where no key is present -- the dashboard must remain fully usable manually.

---

## 6. Everything Else

Beyond the network map and the analyst, **which sections exist is your decision**, based on what this data supports. Candidates the data clearly justifies:

- **Timeline** -- 14 events across ~60 months, with overlay tracks for UAP disclosure events, Congressional actions, FBI probe milestones, and media coverage. Multiple zoom levels.
- **Geographic view** -- three named clusters, distances between cases, institution pins, density treatment.
- **Case detail cards** -- collapsed and expanded, status badges, mini-network of that person's connections, source links, photo placeholder treatment.
- **Analysis panel** -- pattern insights, institutional overlap matrix, timeline density, the "left everything behind" tracker, research domain clustering.
- **Stats dashboard** -- dead, missing, institutions, time span, active investigations, last updated.
- **Search and filter** -- global search, multi-select filter chips, active filter state, shareable filter state via URL.
- **Counterarguments** -- see Section 8.

Add, merge, or drop these as you see fit. Justify structural decisions briefly so Claude Code understands intent.

Every section should be heavily animated and interactive. The whole thing should feel alive.

---

## 7. Creative Direction

### Mood
Intelligence analyst workstation. Serious, high-tech, data-dense, dark. The feeling should be "someone is tracking something that matters." Think about what the FBI's internal analysis tooling would look like if it were designed by someone who cared about UX.

### Reference points (tone, not literal copy)
- OSINT analysis dashboards
- Network forensics visualization tools
- Intelligence community briefing materials
- Interactive documentary storytelling (NYT, The Pudding)
- The visual language of Devs, Counterpart, Severance

### Design principles
1. Data density without clutter
2. Discovery-driven -- the interface rewards exploration
3. Connections are the story
4. Ambient tension -- subtle motion, pulsing, scanning, a sense of something live
5. Credibility -- these are real events with real sources and real families

---

## 8. Credibility Requirements

This project tracks real deaths and real missing people. Several cases have official explanations, one has a suspect awaiting trial, and credible skeptics have published statistical rebuttals of the pattern claim. The design must hold this honestly.

- A **counterarguments section is required**, presented with the same visual weight and quality as the pattern analysis. Scientific American, Skeptic Magazine, Robert Bartholomew's apophenia argument, PolitiFact, and NeuroLogica are all in `PROJECT.md`.
- Design a visual distinction between **confirmed fact**, **allegation or claim**, and **open question**. Do not let the design flatten these into one confidence level.
- The AI Analyst must be designed to say "the data does not support that."
- Sources must be visible and clickable everywhere a claim appears.

This is what separates a research tool from a conspiracy board. It is a design requirement, not a disclaimer.

---

## 9. Technical Constraints

- **Single HTML file**, or a minimal file set, openable locally in a browser
- **No server required** for the core dashboard. All case data embedded. LLM features may make outbound API calls.
- **CDN libraries are fine** -- D3.js, Three.js, GSAP, deck.gl, regl, sigma.js, Leaflet, whatever fits
- **60fps** animation target
- **Target hardware:** RTX 5070 Ti, 32GB RAM. GPU-heavy effects encouraged. Provide a degradation path.
- **Responsive:** desktop primary, tablet secondary, mobile nice-to-have
- **Case data in an editable JavaScript array at the top of the file**, matching the schema in Section 3.1

---

## 10. Hard Rules

- **NO** Bootstrap aesthetic or generic dashboard look
- **NO** conspiracy corkboard -- no red string, no pushpins, no cork texture, no ransom-note typography
- **NO** employer branding. This is personal, not corporate.
- **NO** em dashes in any generated text. Use double hyphens (--) or restructure the sentence.
- **DO** make the network map genuinely useful for discovering connections, not just pretty
- **DO** include all 14 cases with full data from `PROJECT.md`
- **DO** add data labels to any chart or statistical visualization
- **DO** design so new cases are added by editing one array
- **DO** keep readability ahead of style when they conflict

---

## 11. What to Deliver

### A. Visual design system
Color palette with hex values, usage rules, and semantic assignments (status, node class, edge type, confidence level, background, text, accent). Typography with families, weights, and a full scale. Spacing scale. Elevation and depth. Motion tokens -- durations, easing curves, and which token applies to which interaction class.

### B. Layout architecture
Page or app structure, how sections relate, navigation model, responsive breakpoints, grid system. If the network map is a persistent canvas with panels over it rather than a scrolling page, say so and design accordingly.

### C. Component specifications
Precise enough that another AI implements them without guessing. At minimum:

1. **Network map** -- node design per class and per state (default, hover, selected, connected-to-selection, dimmed, filtered out), edge design per the 8 types, cluster treatment, insight callout design, filter bar, zoom and pan controls, level-of-detail rules, empty and loading states
2. **AI Analyst** -- panel design, all conversation states from Section 5.4, action narration, citation affordance, suggested questions, transcript with clickable entity references, API key configuration flow, no-key degraded state
3. **The dashboard command surface** -- the named list of actions the analyst can invoke, with parameters
4. **Detail panel** -- one design that handles all five node classes, or a documented set of variants
5. Whatever additional components your Section 6 decisions require

### D. Interaction and animation specification
For each: trigger, duration, easing, and visual effect. Cover at minimum the page load sequence, network graph build-in, filter transitions, node selection and connection highlighting, panel open and close, analyst action narration, timeline scrub, section transitions, and the ambient background treatment.

### E. Reference mockup
An HTML mockup demonstrating the design system applied to the **real data** from `PROJECT.md`. It does not need to be the production build. It needs to be a definitive visual target -- colors, typography, layout, component styling, and key interaction states. Claude Code will build against it.

---

## 12. Downstream

Your package goes to Claude Code, which builds the production single-file tracker from it. Write specs precise enough that an implementer never has to guess your intent. Where you make a non-obvious design decision, say why in one line.
