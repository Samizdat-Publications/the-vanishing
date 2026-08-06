# The Vanishing v2: Instructions for Claude Design

## What This Is

You are being asked to produce the complete visual design package for "The Vanishing" -- an interactive single-page web tracker documenting the deaths and disappearances of 14 US scientists, military officials, and defense-connected individuals since 2021. This is a personal research project (NOT corporate work). Your design package will be handed to Claude Code to build the production HTML.

---

## Step 1: Read These Files (in this order)

All files are in this repository:

1. **`PROJECT.md`** -- Master documentation. Contains all 14 cases with details, geographic clusters, institutional connections, analysis threads, counterarguments, source URLs. This is your data source.

2. **`DESIGN-BRIEF.md`** -- The full creative brief with mood, atmosphere, feature requirements, animation specs, and success criteria. Follow this closely.

3. **`scientist-tracker-state-2026-06-20.md`** -- State snapshot from the last research sweep. Contains recent developments (House Oversight, FBI probe, PURSUE releases, Casias found dead, Grillmair suspect arraigned).

4. **`scientist-network-tracker.html`** -- The current v1 tracker (1233 lines). This is what you are redesigning from scratch. Study it to understand the data structure, but do not replicate its design.

5. **`RESEARCH-PROCESS.md`** -- Weekly research cadence spec. Includes the JavaScript data schema for adding new cases. Your design must accommodate this schema.

---

## Step 2: What to Produce

Deliver a **complete design package** containing:

### A. Visual Design System
- **Color palette** with hex values, usage rules, and semantic meaning (status colors for dead/missing, institution types, connection types, backgrounds, text, accents)
- **Typography** -- font families, weights, sizes for all hierarchy levels (H1-H6, body, captions, data labels, monospace for dates/IDs)
- **Spacing system** -- consistent scale
- **Component library specs** for: cards, badges, tooltips, buttons, filter controls, modals/panels, stat counters, timeline nodes, network graph nodes/edges
- **Animation tokens** -- timing functions, durations, easing curves for all interaction states

### B. Layout Architecture
- **Page structure** -- how the sections flow (network graph, timeline, case cards, geographic viz, analysis panel, stats dashboard, search/filter)
- **Responsive breakpoints** -- desktop (primary), tablet, mobile (nice-to-have)
- **Grid system** -- how content is organized within each section
- **Navigation pattern** -- how users move between views/sections

### C. Component Designs (detailed specs for each)

1. **Network Graph** (centerpiece)
   - Node design for persons (dead vs missing states), institutions, and connection types
   - Edge styling for 8 connection types (institutional, geographic, research domain, temporal, behavioral, programmatic, investigative, witness-chain)
   - Hover, selected, dimmed, and filtered states
   - Auto-insight callout design (the system algorithmically surfaces non-obvious connections)
   - Filter control bar design
   - Zoom/pan UI elements

2. **Timeline**
   - Event node design at different zoom levels
   - Color coding scheme
   - Overlay events (UAP disclosure, Congressional actions, media milestones)
   - Scroll/zoom interaction model

3. **Case Cards**
   - Collapsed and expanded states
   - Status badge design
   - Mini-network view showing individual's connections
   - Source link styling
   - Photo placeholder treatment

4. **Geographic View**
   - Map style and overlay design
   - Cluster visualization treatment
   - Distance indicator design
   - Institution pin design

5. **Analysis Panel**
   - Pattern insight card design
   - Counterargument presentation
   - Open questions section
   - Institutional overlap matrix layout

6. **Stats Dashboard**
   - KPI card design (dead, missing, institutions, time span, investigations)
   - Trend indicator styling
   - Last-updated treatment

7. **Search & Filter**
   - Global search bar design
   - Multi-select filter chip design
   - Active filter state indicators

### D. Interaction & Animation Spec
For each of these, specify: trigger, duration, easing, and visual effect.

- Page load sequence (cases appear, network builds)
- Scanning/radar line effect (header)
- Pulse effects (missing persons nodes)
- Connection highlighting on hover (traveling particle effect)
- Filter transitions (nodes rearrange)
- Card expand/collapse
- Section scroll transitions
- Background texture/grid treatment
- Data-loading "incoming intelligence" effect

### E. Reference Mockup
Produce an HTML mockup that demonstrates the design system applied to the actual data. This does not need to be the production build -- it is a visual reference showing colors, typography, layout, component styling, and key interaction states. Claude Code will use this as the definitive visual target.

---

## Creative Direction

### Mood
Intelligence analyst workstation. Investigative journalism. High-tech, serious, dark. The vibe: "someone is tracking something that matters." NOT campy conspiracy corkboard. More like what the FBI's internal analysis tools should look like if designed by someone who cares about UX.

### Visual References (tone, not literal)
- OSINT analysis dashboards
- Network forensics visualization tools
- Intelligence community briefing materials
- Interactive documentary storytelling (NYT, The Pudding)
- The aesthetic of shows like Devs, Counterpart, Severance

### Design Principles
1. Data density without clutter
2. Discovery-driven (reward exploration)
3. Connections are the story
4. Ambient tension (subtle animations, pulsing, scanning)
5. Credibility (real events, real sources, authoritative feel)

---

## Technical Constraints for the Final Build

Your design must be implementable under these constraints:
- Single HTML file, openable locally in a browser
- No server required -- all data embedded
- CDN libraries OK (D3.js, Three.js, GSAP, anime.js, Leaflet)
- 60fps animations on modern hardware
- Target hardware: RTX 5070 Ti, 32GB RAM -- GPU-accelerated effects encouraged
- Responsive (desktop primary, tablet secondary)
- Case data stored in an editable JavaScript array at top of file (per schema in RESEARCH-PROCESS.md)

---

## Hard Rules

- **NO** Bootstrap aesthetic
- **NO** conspiracy-theory corkboard (no red string, no pushpins)
- **NO** employer branding (this is personal, not corporate)
- **NO** em dashes anywhere in text -- use double hyphens (--) or restructure
- **DO** push boundaries of what a single HTML file can do
- **DO** make the network graph genuinely useful for discovering connections
- **DO** include all 14 cases with full data from PROJECT.md
- **DO** maintain balanced credibility (include counterarguments section)
- **DO** add data labels to any charts or statistical visualizations
- **DO** design so new cases can be added by editing the data array

---

## Output Format

Package your deliverables as:
1. A design system document (markdown or HTML) with all specs from Section 2
2. A reference mockup HTML file showing the design applied to real data
3. Any supporting assets (SVG icons, color swatches) as needed

Claude Code will receive this package and build the production v2 tracker from it. Make the specs precise enough that another AI can implement them without ambiguity.
