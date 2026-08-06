# The Vanishing v2: Creative Design Brief

## For: Claude (next session, Opus 5)
## From: Stewart Gregerson
## Date: August 6, 2026
## Directive: Full creative freedom. Make this extraordinary.

---

## The Ask

Rebuild "The Vanishing" scientist network tracker from the ground up as a visually stunning, deeply interactive, single-page web experience. This is not a simple data table -- it's an investigative visualization tool that should feel like you've accessed a classified intelligence briefing.

**Stewart's exact words:** "I want it as visually advanced as possible and made such that it can call out interesting connections it identifies itself in addition to the standard groupings."

---

## Creative Direction

### Mood & Atmosphere
Think: intelligence analyst's workstation meets investigative journalism meets conspiracy board. Dark, serious, high-tech. The vibe should say "someone is tracking something that matters." Not campy conspiracy-theory corkboard -- more like what the FBI's internal tools *should* look like if they were designed by someone who actually cares about UX.

### Visual References (tone, not literal copy)
- OSINT analysis dashboards
- Network forensics visualization tools
- Intelligence community briefing materials
- Interactive documentary storytelling (NYT, The Pudding, etc.)
- Satellite imagery command centers
- The aesthetic of shows like Devs, Counterpart, or Severance

### Design Principles
1. **Data density without clutter** -- lots of information, elegantly organized
2. **Discovery-driven** -- the interface should reward exploration
3. **Connections are the story** -- the relationships between people, institutions, locations, and timelines ARE the content
4. **Ambient tension** -- subtle animations, pulsing elements, scanning effects that convey "this is live, this is being monitored"
5. **Credibility** -- this tracks real events with real sources. It should feel authoritative, not sensational.

---

## Required Features

### 1. Interactive Network Graph (THE CENTERPIECE)
This is the most important feature. A force-directed or custom-layout network visualization where:

- **Person nodes** show name, status (dead/missing), date, photo placeholder or icon
- **Institution nodes** show name, location, type (government/military/academic/private)
- **Connection edges** show relationship type (employed, researched at, connected to, geographic proximity, shared clearance level, temporal proximity)
- **Clicking a node** highlights all its connections and dims everything else
- **Hovering** shows a tooltip with key details
- **Filtering controls** let you isolate by: status (dead/missing), geographic cluster, institution type, time period, research domain (propulsion, nuclear, astro, intelligence)
- **Auto-identified connections** -- the system should algorithmically surface non-obvious connections. Examples:
  - "3 of these individuals worked on propulsion research within 30 miles of each other"
  - "Sullivan was a source for Grusch, who triggered the Congressional investigation now probing these cases"
  - "5 individuals left their phone/wallet behind before disappearing"
  - "All 4 NM cases are within 150 miles of each other"
  - "The Huntsville 3 all worked on propulsion-adjacent research"
- **Animated transitions** when filtering -- nodes should smoothly rearrange
- **Zoom and pan** for exploring dense areas
- **Edge bundling** or smart routing so connection lines don't become spaghetti
- Consider: D3.js force layout, vis.js, sigma.js, or custom Canvas/WebGL

### 2. Timeline Visualization
- Horizontal or vertical scrollable timeline
- Each event as a node on the timeline
- Color-coded by status
- Clickable to jump to case detail
- Overlay capability: show UAP disclosure events, Congressional actions, media coverage milestones alongside the cases
- Zoom levels: year view, month view, week view
- Animation: timeline should "build" on load or scroll

### 3. Case Detail Cards
- Expandable/collapsible cards for each individual
- Photo placeholder, name, age, date, location, affiliation
- Status badge with appropriate styling
- Key details, cause of death/disappearance
- "Why it matters" section
- Sources with clickable links
- Connection count ("Connected to X other cases via Y pathways")
- Mini network view showing just this person's connections

### 4. Geographic Visualization
- Map view showing all case locations
- Cluster highlighting (CA corridor, NM corridor, Huntsville triangle)
- Distance calculations between cases in same cluster
- Institution locations overlaid
- Heat map or density visualization option

### 5. Analysis & Insights Panel
- Sidebar or overlay panel showing:
  - Pattern analysis (auto-generated observations about the data)
  - Institutional overlap matrix
  - Timeline density analysis (are cases accelerating?)
  - "Left everything behind" pattern tracker
  - Research domain clustering
  - Counterarguments with balanced presentation
- Open questions section

### 6. Stats Dashboard
- Key metrics at a glance (dead, missing, institutions, time span)
- Trend indicators
- Last updated timestamp
- Case resolution rate

### 7. Search & Filter System
- Global search across all case data
- Multi-select filters: status, location, institution, research domain, date range
- Filter combinations should update all visualizations simultaneously
- Save/share filter states via URL parameters

---

## Animation & Interaction Requirements

Stewart wants this to feel alive. Specific animation ideas:

- **On load:** Cases appear sequentially on timeline, network graph builds connection by connection
- **Scanning line:** Subtle horizontal scanning effect across the header (like radar)
- **Pulse effects:** Missing persons nodes gently pulse. Dead nodes have a subtle flatline effect.
- **Connection highlighting:** When hovering a node, connected edges light up with a traveling particle effect along the line
- **Status transitions:** When Casias changed from Missing to Dead, show that transition capability
- **Parallax scrolling:** Subtle depth effects as you scroll through sections
- **Data loading effect:** When new data would come in (from weekly updates), show an "incoming intelligence" animation
- **Background texture:** Subtle grid or topographic lines, very faint, suggesting a technical/military aesthetic
- **Cursor effects:** Custom cursor or subtle trail effect in the network graph area

---

## Technical Constraints

- **Single HTML file** (or very few files) -- must be openable locally in a browser
- **No server required** -- all data embedded in the file
- **CDN libraries OK** -- D3.js, Three.js, GSAP, anime.js, Leaflet, etc.
- **Performance matters** -- smooth 60fps animations on modern hardware
- **Responsive** -- should work on desktop and tablet (phone is nice-to-have)
- Stewart has: ASUS ROG Zephyrus G16, Intel Core Ultra 9, RTX 5070 Ti, 32GB RAM -- so don't hold back on GPU-accelerated effects

---

## Data Structure

All 14 cases and their connections are documented in `PROJECT.md` in this folder. The full current tracker HTML is at `scientist-network-tracker.html`. The state snapshot with all case details, sources, and analysis threads is at `scientist-tracker-state-2026-06-20.md`.

Read all three files to get the complete data set before building.

### Connection Types to Visualize
1. **Institutional** -- worked at same institution
2. **Geographic** -- in same geographic cluster
3. **Research domain** -- same field (propulsion, nuclear, astro, intelligence, plasma)
4. **Temporal** -- died/disappeared within X months of each other
5. **Behavioral** -- shared the "left everything behind" pattern
6. **Programmatic** -- connected to same government program (AFRL, NASIC, etc.)
7. **Investigative** -- connected through the same investigation (FBI probe, House Oversight)
8. **Witness chain** -- Sullivan -> Grusch -> Congressional testimony -> House investigation

---

## What Success Looks Like

Stewart opens this file in Chrome and says "holy shit." He can:
1. Immediately see the full scope of the pattern at a glance
2. Click into the network graph and discover connections he hadn't noticed
3. Filter to just Huntsville cases and see the propulsion cluster light up
4. Hover over Sullivan and see the chain to Congressional oversight
5. Scroll through a timeline that overlays UAP disclosure events
6. Read detailed case information with sources
7. See auto-generated insights calling out patterns
8. Share a screenshot that makes people want to know more

---

## Available Design Themes

Stewart has 57 TypeUI design themes installed. Consider using one as a starting point, or create something entirely custom. Some that might fit the mood: `typeui-cosmic`, `typeui-dramatic`, `typeui-dashboard`, `typeui-agentic`, `typeui-midnight` (if it exists). But you have full creative freedom -- if none of these fit, build your own design system.

Theme index: `.claude/skills/typeui-index/SKILL.md`
Individual themes: `.claude/skills/typeui-{name}/SKILL.md`

---

## DO NOT

- Make it look like a generic Bootstrap dashboard
- Use campy conspiracy-theory aesthetics (no red string, no corkboard)
- Sacrifice readability for style
- Use employer branding (this is personal, not work)
- Include em dashes in any text (Stewart's preference)

## DO

- Push the boundaries of what a single HTML file can do
- Make the network graph genuinely useful for discovering connections
- Include smooth, purposeful animations everywhere
- Make it feel like a tool, not a presentation
- Include all 14 cases with full data
- Maintain balanced credibility (include counterarguments)
- Add data labels to any charts
- Build it so new cases can be added by editing a data array at the top of the file
