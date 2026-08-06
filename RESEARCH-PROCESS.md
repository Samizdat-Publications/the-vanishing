# The Vanishing: Automated Research Process

## Purpose
Weekly automated research cadence to keep the scientist tracker current with new cases, updates to existing cases, and relevant news/developments.

---

## Research Scope

### A) New Missing Individuals
Search for any NEW deaths or disappearances of scientists, defense officials, military personnel, or intelligence community members that could be connected to the existing pattern. Inclusion criteria:

- US scientist, engineer, or defense/intelligence official
- Died or went missing under unusual circumstances since 2021
- Connected to: aerospace, propulsion, nuclear, plasma physics, astrophysics, defense research, intelligence community, UAP/UFO programs
- OR: connected to institutions already in the tracker (JPL, LANL, AFRL, NASA, NASIC, Caltech, MIT, UAH, KCNSC, Aerojet Rocketdyne)
- OR: shares behavioral patterns (left phone/wallet behind, found in remote area, official cause questioned)
- OR: explicitly linked by media/investigators to the existing pattern

### B) Updates on Existing Individuals
For each of the 14 tracked cases, search for:
- New information about cause of death/disappearance
- Legal proceedings (arraignments, trials, verdicts)
- Search updates (for missing persons)
- Status changes (missing to found, etc.)
- New witness statements or evidence
- Family statements or disputes with official narrative
- FOIA releases mentioning any individual

### C) Institutional/Political Developments
- Congressional actions: House Oversight, Senate Intel, any new committee interest
- FBI investigation updates
- White House statements
- PURSUE file releases (war.gov/UFO)
- DoD/Pentagon statements on missing scientists
- DOE/NNSA statements
- New media investigations (CNN, NewsNation, Newsweek, etc.)
- Skeptic/debunking articles (Scientific American, Skeptic, etc.)
- Wikipedia article changes

---

## Search Queries (Weekly)

Run these searches each week. Group by priority.

### Priority 1: New Cases & Direct Updates
```
"missing scientist" OR "dead scientist" OR "scientist disappear" -fiction -novel -movie
"missing defense" scientist OR engineer OR official 2026
"scientist found dead" (NASA OR JPL OR LANL OR Pentagon OR Air Force)
site:newsnationnow.com scientist missing OR dead
site:newsweek.com missing scientists
site:cnn.com missing scientists investigation
```

### Priority 2: Named Individual Updates
```
"Neil McCasland" -Wikipedia (check for search/status updates)
"Steven Garcia" "Kansas City" OR KCNSC (check for search updates)
"Monica Reza" Lancaster OR missing (check for search updates)
"Anthony Chavez" "Los Alamos" OR LANL (check for search updates)
"Carl Grillmair" OR "Freddy Snyder" trial OR hearing OR arraignment
"Matthew Sullivan" Grusch OR testimony OR Congress
"Amy Eskridge" Huntsville (any new reporting)
"Joshua LeBlanc" NASA OR Huntsville (any new reporting)
```

### Priority 3: Institutional Developments
```
"House Oversight" missing scientists OR dead scientists
"FBI" investigation scientists missing
PURSUE UAP files release OR drop site:defensescoop.com
site:oversight.house.gov scientist OR UAP
"missing scientists" conspiracy OR investigation Congress
```

### Priority 4: Pattern/Analysis
```
"missing scientists" pattern OR cluster OR connection
"missing scientists" "left behind" phone wallet
"missing scientists" propulsion OR nuclear OR plasma
"missing scientists" Huntsville OR "New Mexico" OR JPL
```

---

## Process Flow

### Step 1: Run Searches
Execute all Priority 1-4 search queries using web search tools. Collect all results.

### Step 2: Triage Results
For each result, classify as:
- **NEW CASE**: Previously unknown individual matching inclusion criteria
- **UPDATE**: New information on existing tracked individual
- **DEVELOPMENT**: Institutional/political development
- **SKIP**: Already known, not relevant, or duplicate

### Step 3: Verify & Cross-Reference
For any NEW CASE or significant UPDATE:
- Verify across at least 2 independent sources
- Check against existing tracker data to avoid duplicates
- Note any conflicting information between sources
- Record all source URLs

### Step 4: Update State File
Create a new state snapshot file: `scientist-tracker-state-YYYY-MM-DD.md`
Include:
- Date of research sweep
- New cases found (with full details)
- Updates to existing cases
- Institutional developments
- Sources for all new information
- Any items flagged for manual review

### Step 5: Update Tracker HTML
If new cases or significant updates are found:
- Add new case cards to the HTML tracker
- Update existing cards with new information
- Update stats bar numbers
- Add new timeline entries
- Update network diagram connections
- Add new institution cards if needed
- Update analysis threads
- Add new sources to footer

### Step 6: Report
Generate a brief summary of findings:
- Number of new cases found (if any)
- Key updates to existing cases
- Notable institutional developments
- Any items requiring Stewart's attention/decision

---

## Scheduling

### Recommended Cadence
- **Weekly**: Full research sweep (all 4 priority levels)
- **Day**: Sundays (so findings are ready for Monday review)
- **Notification**: Summary posted in Cowork session

### To Set Up in Cowork
In a new session, ask:
> "Run the weekly scientist tracker research sweep. Read RESEARCH-PROCESS.md in scientist-tracker/ for the full procedure."

Or schedule it:
> "Schedule a weekly task every Sunday at 10am to run the scientist tracker research sweep per RESEARCH-PROCESS.md"

### Manual Trigger
For breaking news or ad-hoc updates:
> "Run the scientist tracker research sweep now -- there may be breaking news about [topic]"

---

## Data Architecture for Updates

When adding a new case to the tracker HTML, use this data structure (placed in the cases array at the top of the rebuilt v2 file):

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
  sources: [
    { name: "Outlet Name", url: "https://..." }
  ],
  dateAdded: "YYYY-MM-DD",
  lastUpdated: "YYYY-MM-DD"
}
```

---

## Quality Standards

- Never fabricate or speculate about connections not supported by sources
- Always include counterarguments and skeptic perspectives
- Note when sources conflict
- Distinguish between confirmed facts and allegations/theories
- Track source reliability (major outlet vs. blog vs. social media)
- Flag any information that could not be independently verified
- Maintain the balanced, investigative tone -- not conspiratorial

---

## File Locations

| File | Purpose |
|------|---------|
| `scientist-tracker/PROJECT.md` | Master project documentation |
| `scientist-tracker/DESIGN-BRIEF.md` | Creative brief for v2 rebuild |
| `scientist-tracker/RESEARCH-PROCESS.md` | This file |
| `scientist-tracker/scientist-network-tracker.html` | Current tracker (v1) |
| `scientist-tracker/scientist-tracker-state-YYYY-MM-DD.md` | State snapshots (one per research sweep) |
