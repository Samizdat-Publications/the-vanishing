// The Vanishing v2 -- shared graph engine for the edge-language studies.
// Real entity data from PROJECT.md. Canvas 2D here; production target is WebGPU/WebGL.

export const PALETTE = {
  bg: '#14171c', bg2: '#191d23', panel: '#1e232a', panel2: '#232932',
  line: '#2e353f', line2: '#3b444f',
  text: '#e6e9ee', dim: '#8d97a4', faint: '#5c6672',
  signal: '#5ed4e6',
  dead: '#e8705f', missing: '#efb555',
};
PALETTE.resolved = '#6f7f8c';
PALETTE.transitioned = '#d98a6a';
PALETTE.person = '#c9d2dd';
PALETTE.institution = '#a795e8';
PALETTE.program = '#66d69f';
PALETTE.location = '#7fb4e8';
PALETTE.domain = '#e08ad0';

export const EDGE_TYPES = {
  institutional: { color: '#a795e8', dash: [], label: 'Institutional' },
  geographic:    { color: '#7fb4e8', dash: [6, 4], label: 'Geographic' },
  research:      { color: '#e08ad0', dash: [2, 3], label: 'Research domain' },
  temporal:      { color: '#efb555', dash: [1, 4], label: 'Temporal' },
  behavioral:    { color: '#e8705f', dash: [9, 3, 2, 3], label: 'Behavioral' },
  programmatic:  { color: '#66d69f', dash: [10, 5], label: 'Programmatic' },
  investigative: { color: '#5ed4e6', dash: [4, 3, 1, 3], label: 'Investigative' },
  'witness-chain': { color: '#f0d264', dash: [], label: 'Witness chain' },
};

// Case records. Schema per DESIGN-ADDENDUM-2026-08-07.md, corrected against the
// August 7 2026 research sweep. Everything downstream derives from this array.
// Scores: S = sequence anomaly, P = personal program proximity, I = institutional
// channel. Deliberately NOT summed; a case can be extraordinary on one axis and
// unremarkable on another, and collapsing that destroys the information.

const P_ = (o) => Object.assign({ cls: 'person', leftBehind: [], tookWith: [], domains: [], conflicts: [], unverified: [], sequenceChain: [], claims: [], chronology: [], sources: [], isNonDefense: false, mediaLinkedOnly: false, unexplainedResidual: null }, o);

export const PEOPLE = [
  P_({
    id: 'li', label: 'Ning Li', status: 'dead', date: '2021-07-27', age: 78,
    loc: 'Huntsville, AL', locId: 'l-hsv', instId: 'uah', sub: 'UAH / AC Gravity LLC',
    cluster: 'huntsville', tier: 'C', S: 1, P: 2, I: 2, domains: ['d-prop', 'd-exotic'],
    narrative: 'Chinese-American physicist who emigrated in 1983 and spent two decades at the UAH Center for Space Plasma and Aeronomic Research working on gravitomagnetism, extending the Meissner effect from electromagnetism to gravity. She founded AC Gravity LLC in 1999, won a 448,970 dollar DoD grant in 2001, and moved into classified work at Redstone Arsenal after 2003. She was struck by a car on the UAH campus in 2014 and suffered permanent brain damage; reporting indicates the injury led to an Alzheimer\u2019s diagnosis shortly afterward. She died of natural causes in 2021. The seven-year gap between the collision and her death substantially weakens any suspicious-death framing, and the case is retained for the research continuity to Eskridge rather than for its own anomaly.',
    affiliations: ['UAH Center for Space Plasma and Aeronomic Research (1983-1999)', 'AC Gravity LLC (founder, 1999)', 'Redstone Arsenal / US Army AMCOM (classified, post-2003)'],
    tierRationale: 'A conventional explanation is documented and holds: a 2014 campus vehicle collision, resulting brain damage, and death of natural causes seven years later.',
    chronology: [
      { date: '1983', event: 'Emigrates to the United States, joins UAH', precision: 'year' },
      { date: '1999', event: 'Founds AC Gravity LLC', precision: 'year' },
      { date: '2001', event: 'Wins a 448,970 dollar DoD grant', precision: 'year' },
      { date: '2003', event: 'Work moves to Redstone Arsenal and goes classified', precision: 'year' },
      { date: '2014', event: 'Struck by a car on the UAH campus; permanent brain damage', precision: 'year' },
      { date: '2021-07-27', event: 'Dies at 78 of natural causes', precision: 'day' },
    ],
    claims: [
      { tier: 2, text: 'A May 2003 private email to colleagues claimed an observed 11 kilowatts of output effect during an experiment.', source: 'Reported secondhand' },
      { tier: 2, text: 'Plasma physicist John Brandenburg wrote in April 2026 that he regarded her extension of the Meissner effect to the gravity potential as solid physics.', source: 'X post, April 2026' },
      { tier: 3, text: 'Skeptic magazine presents the 2014 collision and the Alzheimer\u2019s death as unrelated events. The Huntsville Business Journal reporting says the collision caused the brain damage that led to the diagnosis.', source: 'Logged as a skeptic error, not as support for the pattern' },
    ],
    sources: [{ outlet: 'Newsweek', url: 'https://www.newsweek.com/huntsville-mystery-are-two-dead-scientists-same-town-connected-11869617', date: '2026-04-24' }],
  }),
  P_({
    id: 'eskridge', label: 'Amy Eskridge', status: 'dead', date: '2022-06-11', age: 34,
    loc: 'Huntsville, AL', locId: 'l-hsv', instId: 'ies', sub: 'Institute for Exotic Science',
    cluster: 'huntsville', tier: 'B', S: 1, P: 2, I: 1, domains: ['d-prop', 'd-exotic'],
    narrative: 'Anti-gravity and advanced propulsion researcher in Huntsville, ruled a self-inflicted gunshot in June 2022. Before her death she stated on a podcast that she was the target of a psychological war aimed at stopping her anti-gravity work. That is a documented fact about her own stated belief and state of mind; it is not evidence of targeting. The widely circulated text reading that she most definitely did not kill herself, and the directed-energy-weapon claim, are attributed to a friend and to a resurfaced video, not to her family. Her family points the other way: her father, a retired NASA employee, told Newsweek that scientists die also, just like other people, and the family declined to characterize the death as unusual, citing chronic pain.',
    affiliations: ['Institute for Exotic Science', 'Prior NASA-adjacent propulsion work'],
    tierRationale: 'Unresolved in the sense that her own stated fears are documented, but a prosaic explanation exists, is supported by the family, and is not ruled out.',
    conflicts: ['The pattern framing describes a family dispute of the official ruling. The located family statements support the official ruling. The disputing statements come from a friend and a resurfaced video.'],
    chronology: [
      { date: '2022-06-11', event: 'Dies in Huntsville. Ruled self-inflicted gunshot', precision: 'day' },
      { date: '2026-04', event: 'Video resurfaces; case enters national coverage', precision: 'month' },
      { date: '2026-04-24', event: 'Father tells Newsweek scientists die also, just like other people', precision: 'day' },
    ],
    claims: [
      { tier: 1, text: 'Stated on a podcast before her death that she was the target of a psychological war aimed at stopping her anti-gravity work.', source: 'EFE, April 22 2026' },
      { tier: 2, text: 'A friend attributes to her a text reading that she most definitely did not kill herself.', source: 'Attributed to a friend, not to family' },
      { tier: 1, text: 'Retired FBI Special Agent Jennifer Coffindaffer said there is no doubt she took her own life, based on her behavior beforehand.', source: 'Newsweek' },
    ],
    sources: [{ outlet: 'NewsNation', url: 'https://www.newsnationnow.com/missing/amy-eskridge-energy-weapon-attack/', date: '2026-04' }, { outlet: 'Newsweek', url: 'https://www.newsweek.com/amy-eskridge-cause-of-death-investigated-as-new-video-of-scientist-surfaces-11868762', date: '2026-04' }],
  }),
  P_({
    id: 'hicks', label: 'Michael David Hicks', status: 'dead', date: '2023-07-30', age: 59,
    loc: 'Sunland, CA', locId: 'l-sun', instId: 'jpl', sub: 'NASA JPL (1998-2022)',
    cluster: 'california', tier: 'C', S: 0, P: 1, I: 3, domains: ['d-astro'],
    narrative: 'JPL astronomer who studied comets and asteroids, not propulsion or weapons. No cause of death has been publicly disclosed, and the case is listed as natural causes. His daughter said he suffered from known medical issues and that there is no train of logic to follow that would implicate him. His brother said he is going to be remembered for some baloney rather than for his scientific contributions. PolitiFact specifically corrected the record on his research area, which the pattern framing had described as defense-adjacent.',
    affiliations: ['NASA Jet Propulsion Laboratory (1998-2022)'],
    tierRationale: 'A conventional explanation is documented and holds. Family attributes the death to known medical issues. Research area is not defense-adjacent.',
    chronology: [
      { date: '2023-07-30', event: 'Dies at 59. No public cause disclosed', precision: 'day' },
      { date: '2026-04-21', event: 'Daughter and brother publicly reject the pattern framing', precision: 'day' },
    ],
    claims: [
      { tier: 1, text: 'Studied comets and asteroids. The characterization of his work as defense-adjacent is a documented error.', source: 'PolitiFact, April 28 2026' },
    ],
    sources: [{ outlet: 'CNN', url: 'https://www.cnn.com/2026/04/21/us/deaths-disappearances-scientists-investigation', date: '2026-04-21' }],
  }),
  P_({
    id: 'sullivan', label: 'Matthew James Sullivan', status: 'dead', date: '2024-05-12', age: 39,
    loc: 'Falls Church, VA', locId: 'l-fal', instId: 'nsa', sub: 'USAF Intelligence / NSA / NASIC',
    cluster: 'other', tier: 'B', S: 1, P: 3, I: 3, domains: ['d-intel'],
    narrative: 'Air Force intelligence officer with NSA and NASIC ties, and case eleven on the expanded list. PolitiFact characterizes the death as an accidental drug overdose. The framing that he died days before he agreed to testify should not be treated as established: even sympathetic outlets differ on whether it was days, weeks, or months before a scheduled appearance, and most coverage of his case comes from low-reliability outlets. No Congressional hearing, testimony, subpoena, or investigative document from the recent window names him.',
    affiliations: ['US Air Force Intelligence', 'NSA', 'National Air and Space Intelligence Center'],
    tierRationale: 'High personal proximity and a documented intelligence role, but the death has a prosaic explanation that is not ruled out, and the testimony timing is not established.',
    conflicts: ['The tracked record says weeks before testimony. Political.org says months. Other outlets say days. No primary document establishes any of them.'],
    unverified: ['That he had agreed to testify at a specific scheduled proceeding.'],
    chronology: [
      { date: '2024-05-12', event: 'Dies at 39. Accidental drug overdose per PolitiFact', precision: 'day' },
      { date: '2026-04', event: 'Name enters the House Oversight and FBI review', precision: 'month' },
    ],
    claims: [
      { tier: 2, text: 'Described as a source for whistleblower David Grusch.', source: 'Pattern-side coverage; not established in a primary document' },
      { tier: 1, text: 'PolitiFact characterizes the death as an accidental drug overdose.', source: 'PolitiFact, April 28 2026' },
    ],
    sources: [{ outlet: 'NewsNation', url: 'https://www.newsnationnow.com/space/ufo/uap-witness-overdose-death-congress/', date: '2026-04' }],
  }),
  P_({
    id: 'maiwald', label: 'Frank Maiwald', status: 'dead', date: '2024-07-04', age: 61,
    loc: 'Los Angeles, CA', locId: 'l-la', instId: 'jpl', sub: 'NASA JPL',
    cluster: 'california', tier: 'A', S: 1, P: 2, I: 3, domains: ['d-astro'],
    narrative: 'JPL researcher who worked on SWOT and imaging spectroscopy. No cause of death has been publicly disclosed. This is the thinnest file in the set and it is also the one entry where skeptics have offered no specific alternative explanation, only the base rate. That combination is why it holds Tier A despite a low sequence score: there is nothing anomalous in the record, and there is also nothing in the record at all.',
    affiliations: ['NASA Jet Propulsion Laboratory'],
    tierRationale: 'Contains a specific unexplained fact no source accounts for, and sits inside an I3 institution.',
    unexplainedResidual: 'No cause of death has been made public more than two years on, and no skeptic has offered a specific alternative explanation. The rebuttal to this case is the base rate alone.',
    chronology: [
      { date: '2024-07-04', event: 'Dies at 61 in Los Angeles. No public cause disclosed', precision: 'day' },
    ],
    claims: [
      { tier: 1, text: 'No public cause of death, more than two years on.', source: 'Absence of record' },
    ],
    sources: [],
  }),
  P_({
    id: 'chavez', label: 'Anthony Chavez', status: 'missing', date: '2025-05-08', age: 78,
    loc: 'Los Alamos, NM', locId: 'l-los', instId: 'lanl', sub: 'LANL. Occupation disputed',
    cluster: 'new-mexico', tier: 'A', S: 2, P: 1, I: 3, domains: ['d-nuc'],
    leftBehind: ['wallet', 'keys', 'bicycle', 'car'],
    narrative: 'Missing from Los Alamos since May 8 2025. Los Alamos Police closed the investigation on October 6 2025 citing no new information, witnesses, or evidence, while New Mexico DPS still carries him as an active missing-person entry. Police reports obtained by Los Angeles Magazine in June 2026 record a friend telling investigators that Chavez had been working on quantum physics with an unidentified scientist, researching matter existing in two places simultaneously, possibly meeting at the local library. That is a tip recorded in a police report, an allegation rather than a confirmed fact, and Futurism notes explicitly that no evidence connects it to his disappearance. A handwritten journal was found at the home; its contents have not been described. He had no cell phone at all, only a landline, so he cannot be counted in any left-the-phone-behind analysis.',
    affiliations: ['Los Alamos National Laboratory'],
    tierRationale: 'Two independently documented and individually unexplained facts: an agency case closed for lack of evidence that remains open at the state level, and an uncharacterized journal.',
    unexplainedResidual: 'Los Alamos PD closed the case on October 6 2025 for lack of evidence while New Mexico DPS still lists him as an active missing person. Both are true at the same time, and neither agency has reconciled them.',
    conflicts: ['Occupation. Los Angeles Magazine, citing police reports, says retired HVAC technician, age 78. Union Leader and aggregators say construction foreman. PolitiFact says retired construction foreman. The police-report sourcing is stronger.'],
    unverified: ['The widely repeated detail that he was last seen near the Rio Grande does not appear in any primary record located.'],
    sequenceChain: [
      { date: '2025-05-08', event: 'Disappears from Los Alamos. Wallet, keys, bicycle and recently purchased Acura left at the home', isAnomalous: false, source: 'NM DPS record M99969' },
      { date: '2025-05', event: 'Friend tells police Chavez had been working on quantum physics with an unidentified scientist', isAnomalous: true, source: 'Los Alamos PD reports via LA Mag' },
      { date: '2025-05', event: 'Handwritten journal found at the home. Contents never described in the report', isAnomalous: true, source: 'Los Alamos PD reports via LA Mag' },
      { date: '2025-10-06', event: 'Los Alamos PD closes the investigation citing no new information, witnesses, or evidence', isAnomalous: true, source: 'LA Mag public-records request' },
      { date: '2026-06-26', event: 'LA Mag obtains the reports. NM DPS listing still active. No substantive FBI activity reported despite the White House review', isAnomalous: true, source: 'LA Mag' },
    ],
    chronology: [
      { date: '2025-05-08', event: 'Reported missing from Los Alamos', precision: 'day' },
      { date: '2025-10-06', event: 'Los Alamos PD closes the case', precision: 'day' },
      { date: '2026-06-26', event: 'Police reports released under public-records request', precision: 'day' },
    ],
    claims: [
      { tier: 2, text: 'A friend told police he had been researching matter existing in two places simultaneously with an unidentified scientist.', source: 'Police report. An allegation on the record, not a finding' },
      { tier: 1, text: 'He had no cell phone at all. Landline only.', source: 'Friend statement in police report' },
      { tier: 1, text: 'The friend obtained power of attorney, hired a private investigator, and told police he believed the case warranted a homicide investigation.', source: 'LA Mag' },
    ],
    sources: [{ outlet: 'LA Magazine', url: 'https://lamag.com/crimeinla/strange-quantum-physics-lead-emerges-in-missing-los-alamos-anthony-chavezs-case/', date: '2026-06-26' }, { outlet: 'Futurism', url: 'https://futurism.com/future-society/man-vanishes-experiments-quantum-physics', date: '2026-07-03' }, { outlet: 'NM DPS', url: 'https://missingpersons.dps.nm.gov/mpweb/mpdetailreport_serv?id=M99969', date: '2026' }],
  }),
  P_({
    id: 'reza', label: 'Monica Reza', status: 'missing', date: '2025-06-22', age: 60,
    loc: 'Angeles National Forest, CA', locId: 'l-anf', instId: 'boeing', sub: 'Rocketdyne, later Boeing associate technical fellow',
    cluster: 'california', tier: 'A', S: 2, P: 2, I: 2, domains: ['d-prop'],
    narrative: 'Vanished while hiking near Mount Waterman in the Angeles National Forest. She was last seen smiling and waving to a companion roughly thirty feet away and was gone within seconds. The only item recovered in the initial search was a beanie about six hundred feet below the trail. She is a co-inventor of Mondaloy, a nickel-based superalloy developed at Rocketdyne for rocket engines, which is the substantive link to the propulsion thread. Her frequently cited JPL affiliation is unconfirmed: Wikipedia flags it as unverified while Union Leader and solvethecase.org state it as fact.',
    affiliations: ['Rocketdyne (mid-1990s)', 'Boeing associate technical fellow (2004)', 'JPL affiliation unconfirmed'],
    tierRationale: 'The disappearance itself is the unexplained fact. She vanished within seconds inside a companion\u2019s line of sight.',
    unexplainedResidual: 'She vanished within seconds while in sight of a companion roughly thirty feet away. The only item recovered was a beanie about six hundred feet below the trail.',
    conflicts: ['JPL affiliation. Wikipedia flags it unverified; Union Leader and solvethecase.org state it as fact. Treat as unresolved.', 'Age. Priority 4 sourcing gives 60; the earlier tracked estimate was mid-forties.'],
    unverified: ['A Substack claim that she was declared dead four days after she vanished. Not corroborated in any primary or mainstream source.'],
    sequenceChain: [
      { date: '2025-06-22', event: 'Last seen smiling and waving to a companion about thirty feet away near Mount Waterman', isAnomalous: false, source: 'LASD case 2025-56' },
      { date: '2025-06-22', event: 'Vanishes within seconds, inside the companion\u2019s line of sight', isAnomalous: true, source: 'LASD case 2025-56' },
      { date: '2025-06', event: 'Only item recovered is a beanie roughly six hundred feet below the trail', isAnomalous: true, source: 'Solve the Case' },
    ],
    chronology: [
      { date: '2025-06-22', event: 'Disappears near Mount Waterman', precision: 'day' },
      { date: '2026-08-07', event: 'Still missing. No search updates or remains discovery', precision: 'day' },
    ],
    claims: [
      { tier: 1, text: 'Co-inventor of Mondaloy, a nickel-based superalloy for rocket engines developed at Rocketdyne.', source: 'Patent record' },
    ],
    sources: [{ outlet: 'Wikipedia', url: 'https://en.wikipedia.org/wiki/Monica_Reza', date: '2026' }, { outlet: 'Solve the Case', url: 'https://www.solvethecase.org/case/2025-56/monica-reza', date: '2026' }],
  }),
  P_({
    id: 'casias', label: 'Melissa Casias', status: 'dead', date: '2025-06-26', age: null,
    loc: 'Carson National Forest, NM', locId: 'l-carson', instId: 'lanl', sub: 'LANL administrative assistant',
    cluster: 'new-mexico', tier: 'A', S: 3, P: 1, I: 3, domains: ['d-nuc'],
    leftBehind: ['wallet', 'keys', 'phones'],
    narrative: 'Disappeared June 26 2025; remains identified May 31 2026. Cause and manner of death remain undetermined more than a year on, complicated by the remains being skeletonized. She was an administrative assistant at LANL, not a scientist, a correction PolitiFact made explicitly. The case carries the strongest set of evidence-handling problems in the file. Investigators corrected a surveillance timestamp by thirteen hours and fifty-eight minutes with no explanation given. The Mondragon family independently recovered additional evidence at the scene that law enforcement had not collected. A registered black Springfield handgun was found near the remains and police have not disclosed the registered owner or whether she had any connection to it. Sources also conflict on the nature of the disappearance: the family said she ran away of her own volition due to stress, while her wallet, keys, and phones reset to factory settings were found at home, a detail nobody has reconciled with a simple voluntary departure.',
    affiliations: ['Los Alamos National Laboratory, administrative assistant'],
    tierRationale: 'Three independently documented and individually unexplained facts: an unexplained fourteen-hour timestamp correction, evidence the family recovered that police had not, and an undisclosed registered firearm at the scene.',
    unexplainedResidual: 'A surveillance timestamp was corrected by thirteen hours and fifty-eight minutes with no explanation provided, and the family recovered evidence at the scene that investigators had not collected.',
    conflicts: ['Nature of the disappearance. Family and NM State Police lean toward voluntary departure. Wallet, keys and factory-reset phones at the home sit awkwardly with that and have not been reconciled.', 'Discovery date versus identification date. Remains discovered late May 2026, identified May 31 2026. Both may be correct.'],
    unverified: ['A NewsNation report of a security-clearance revocation. Article unreachable; no LANL, NNSA or DOE confirmation found.'],
    sequenceChain: [
      { date: '2025-06-26', event: 'Disappears. Wallet, keys and phones reset to factory settings found at home', isAnomalous: true, source: 'Union Leader' },
      { date: '2025-06-27', event: 'Surveillance timestamp later corrected from June 27 4:16 a.m. to June 26 2:18 p.m., a gap of 13 hours 58 minutes, unexplained', isAnomalous: true, source: 'Police reports via LA Mag' },
      { date: '2026-05-31', event: 'Skeletonized remains identified in Carson National Forest', isAnomalous: false, source: 'NBC News' },
      { date: '2026-06', event: 'Mondragon family independently recovers evidence at the scene that law enforcement had not collected', isAnomalous: true, source: 'LA Mag' },
      { date: '2026-08-04', event: 'Handgun found near remains identified as a registered black Springfield. Owner not disclosed', isAnomalous: true, source: 'LA Mag' },
      { date: '2026-08-07', event: 'Cause and manner of death still undetermined', isAnomalous: true, source: 'NM Office of the Medical Investigator' },
    ],
    chronology: [
      { date: '2025-06-26', event: 'Disappears from the Taos area', precision: 'day' },
      { date: '2026-05-31', event: 'Remains identified', precision: 'day' },
      { date: '2026-07-20', event: 'Investigators state there are no new updates', precision: 'day' },
      { date: '2026-08-04', event: 'Handgun identified as registered. Owner undisclosed', precision: 'day' },
    ],
    claims: [
      { tier: 1, text: 'Administrative assistant at LANL. Early coverage calling her a scientist is inaccurate.', source: 'PolitiFact and Wikipedia' },
      { tier: 1, text: 'Cause and manner of death undetermined more than thirteen months after the disappearance.', source: 'NM OMI' },
    ],
    sources: [{ outlet: 'LA Magazine', url: 'https://lamag.com/crimeinla/melissa-casias-death-still-shrouded-in-mystery-over-one-year-later/', date: '2026-07-17' }, { outlet: 'NBC News', url: 'https://www.nbcnews.com/news/us-news/remains-new-mexico-melissa-casias-vanished-rcna347794', date: '2026-05-31' }],
  }),
  P_({
    id: 'leblanc', label: 'Joshua Kyle LeBlanc', status: 'dead', date: '2025-07-22', age: 29,
    loc: 'Walker County, AL', locId: 'l-walker', instId: 'nasa', sub: 'NASA Marshall, DRACO nuclear propulsion',
    cluster: 'huntsville', tier: 'A', S: 2, P: 3, I: 3, domains: ['d-nuc', 'd-prop'],
    leftBehind: ['phone', 'wallet'],
    narrative: 'Electrical engineer at NASA Marshall Space Flight Center from 2019, working on nuclear propulsion including DRACO, the DARPA and NASA joint program. He left his phone and wallet at home, told no one of any travel plans, and vehicle data showed his Tesla had been parked at Huntsville International Airport for four hours that morning. The burned vehicle was found at 2:45 p.m. on July 22 2025 in Walker County, well outside Huntsville, after a single-vehicle crash into a guardrail and trees. His family reported him missing the morning of the day he was found and had worried he had been abducted. He is the clearest example of the redesign\u2019s purpose: he scores high on all three axes and version one buried him as a routine entry.',
    affiliations: ['NASA Marshall Space Flight Center (2019-2025)', 'DRACO, DARPA and NASA joint program'],
    tierRationale: 'Active nuclear propulsion access at an I3 institution, plus two documented and individually unexplained facts on the day of death.',
    unexplainedResidual: 'Vehicle data places his Tesla at Huntsville International Airport for four unexplained hours that morning. He left his phone and wallet at home and told no one of travel plans.',
    conflicts: ['The Wikipedia overview article summarizes him as found in a lake after disappearing three months prior. That detail belongs to Jason Thomas. Every dedicated source describes the burned-Tesla crash on the same day.'],
    sequenceChain: [
      { date: '2025-07-22', event: 'Leaves phone and wallet at home. Tells no one of travel plans', isAnomalous: true, source: 'Family, via Newsweek' },
      { date: '2025-07-22', event: 'Vehicle data shows the Tesla parked at Huntsville International Airport for four hours that morning', isAnomalous: true, source: 'Fox News' },
      { date: '2025-07-22', event: 'Family reports him missing, fearing abduction', isAnomalous: false, source: '1819 News' },
      { date: '2025-07-22', event: 'Burned vehicle found at 2:45 p.m. in Walker County after a single-vehicle crash into a guardrail and trees', isAnomalous: false, source: 'Newsweek' },
      { date: '2025-07', event: 'Body identified days later by forensic officials', isAnomalous: false, source: 'Wikipedia' },
    ],
    chronology: [
      { date: '2019', event: 'Joins NASA Marshall Space Flight Center', precision: 'year' },
      { date: '2025-07-22', event: 'Dies at 29 in Walker County, Alabama', precision: 'day' },
      { date: '2026-05-25', event: 'Standalone Wikipedia article deleted at AfD as non-notable outside the conspiracy narrative', precision: 'day' },
    ],
    claims: [
      { tier: 1, text: 'Worked on DRACO, a DARPA and NASA joint nuclear propulsion program.', source: 'NASA' },
      { tier: 1, text: 'Four unexplained hours with the vehicle at the airport that morning.', source: 'Vehicle data, via Fox News' },
    ],
    sources: [{ outlet: 'Newsweek', url: 'https://www.newsweek.com/huntsville-mystery-are-two-dead-scientists-same-town-connected-11869617', date: '2026-04-24' }, { outlet: 'Fox News', url: 'https://www.foxnews.com/us/nasa-nuclear-engineer-found-dead-burned-tesla-vanishing-alabama-home-last-year', date: '2026' }],
  }),
  P_({
    id: 'garcia', label: 'Steven Abel Garcia', status: 'missing', date: '2025-08-28', age: 47,
    loc: 'Albuquerque, NM', locId: 'l-abq', instId: 'kcnsc', sub: 'Property custodian, contracted out of KCNSC',
    cluster: 'new-mexico', tier: 'A', S: 2, P: 1, I: 3, domains: ['d-nuc'],
    leftBehind: ['phone', 'wallet', 'keys', 'car'], tookWith: ['handgun'],
    narrative: 'Missing from Albuquerque since August 28 2025, with APD listing and the FBI assisting. He abandoned his car, phone, wallet and keys, took a handgun, and left on foot. The state case carries a Missing Person Other-Caution flag consistent with being armed. His role has been widely mischaracterized: the Santa Fe New Mexican describes him as a property custodian, and the top clearance with nuclear weapons access claim that circulated is not supported by any primary source and has been removed from this record. He is the strongest single case in the left-everything-behind thread precisely because neither reading fully explains him: the abduction reading does not account for the handgun, and the suicidal-intent reading does not account for the car.',
    affiliations: ['Kansas City National Security Campus, contractor', 'Property custodian role per Santa Fe New Mexican'],
    tierRationale: 'A documented combination of departure facts that neither the abduction reading nor the suicide reading accounts for, at an I3 institution.',
    unexplainedResidual: 'He abandoned car, phone, wallet and keys while taking a handgun and leaving on foot. Neither the abduction reading nor the suicidal-intent reading accounts for that combination.',
    conflicts: ['Role. Santa Fe New Mexican says property custodian. Union Leader says government contractor with security clearance. Fox4KC says contracted out of KCNSC.'],
    unverified: ['The top clearance and nuclear weapons access characterization. Not supported by primary sources. Removed from this record.'],
    sequenceChain: [
      { date: '2025-08-28', event: 'Leaves on foot from Albuquerque, abandoning car, phone, wallet and keys', isAnomalous: true, source: 'NM DPS record M101688' },
      { date: '2025-08-28', event: 'Takes a handgun with him', isAnomalous: true, source: 'NM DPS' },
      { date: '2025-08', event: 'State case flagged Missing Person Other-Caution, consistent with being armed', isAnomalous: false, source: 'NM DPS' },
      { date: '2026-04', event: 'FBI assisting. Last substantive reporting', isAnomalous: false, source: 'Santa Fe New Mexican' },
    ],
    chronology: [
      { date: '2025-08-28', event: 'Disappears from Albuquerque at 47', precision: 'day' },
      { date: '2026-04-21', event: 'Named among the four missing New Mexicans in the federal review', precision: 'day' },
    ],
    claims: [
      { tier: 1, text: 'Described as a property custodian by the Santa Fe New Mexican.', source: 'Santa Fe New Mexican, April 21 2026' },
      { tier: 3, text: 'The nuclear weapons access claim originated in aggregator coverage and traces to no primary source.', source: 'Removed from the record' },
    ],
    sources: [{ outlet: 'Santa Fe New Mexican', url: 'https://www.santafenewmexican.com/news/local_news/4-missing-new-mexicans-among-disappearances-deaths-prompting-federal-investigation/article_ed85c2ec-7bb6-433d-9548-dead3a124a78.html', date: '2026-04-21' }, { outlet: 'Cybernews', url: 'https://cybernews.com/news/steven-garcia-ufo-uap-mccasland/', date: '2026' }],
  }),
  P_({
    id: 'thomas', label: 'Jason Thomas', status: 'dead', date: '2025-12-13', age: 45,
    loc: 'Wakefield, MA', locId: 'l-wak', instId: 'novartis', sub: 'Chemical biology, Novartis',
    cluster: 'northeast', tier: 'C', S: 0, P: 0, I: 0, isNonDefense: true, domains: ['d-chem'],
    leftBehind: ['phone', 'wallet', 'watch'],
    narrative: 'Chemical biology researcher and director at Novartis, a pharmaceutical company with no defense connection. Reported missing December 13 2025 from Wakefield, Massachusetts; his body was found in Lake Quannapowitt on March 17 2026. His wife noted he was depressed at the time. The Middlesex County Medical Examiner found no foul play. He is retained in this file deliberately, tagged non-defense, to demonstrate that the list is not curated to fit the thesis. The frequently repeated December 12 death date is wrong; that is the date he was last seen.',
    affiliations: ['Novartis, chemical biology research director'],
    tierRationale: 'A conventional explanation is documented and holds. No defense connection on any axis. Retained for completeness.',
    chronology: [
      { date: '2025-12-13', event: 'Reported missing from Wakefield, Massachusetts', precision: 'day' },
      { date: '2026-03-17', event: 'Body found in Lake Quannapowitt', precision: 'day' },
    ],
    claims: [
      { tier: 1, text: 'Middlesex County Medical Examiner found no foul play.', source: 'Middlesex County ME' },
    ],
    sources: [],
  }),
  P_({
    id: 'loureiro', label: 'Nuno Loureiro', status: 'resolved', date: '2025-12-15', age: 47,
    loc: 'Cambridge, MA', locId: 'l-cam', instId: 'mit', sub: 'MIT Plasma Science and Fusion Center',
    cluster: 'northeast', tier: 'C', S: 0, P: 1, I: 1, domains: ['d-plasma'],
    narrative: 'Fatally shot at his Boston-area home on December 15 2025. On April 29 2026 the FBI and the US Attorney for the District of Massachusetts conclusively determined that Claudio Manuel Neves Valente, a Portuguese national and former classmate, acted alone, with no nexus to terrorism, motivated by personal dissatisfaction and a fixation on Loureiro\u2019s success. Valente is also the Brown University shooting suspect. Investigators released a transcript of videos Valente made. This case is closed in every sense and is no longer an open question.',
    affiliations: ['MIT Plasma Science and Fusion Center'],
    tierRationale: 'Formally resolved by federal investigators. Perpetrator identified, motive established, no terrorism nexus.',
    chronology: [
      { date: '2025-12-15', event: 'Fatally shot at his home at 47', precision: 'day' },
      { date: '2026-04-29', event: 'FBI and US Attorney determine Valente acted alone. Case closed', precision: 'day' },
    ],
    claims: [
      { tier: 1, text: 'Perpetrator identified, acted alone, no nexus to terrorism, personal motive.', source: 'FBI and USAO-Massachusetts, April 29 2026' },
    ],
    sources: [{ outlet: 'Wikipedia', url: 'https://en.wikipedia.org/wiki/Nuno_Loureiro', date: '2026' }],
  }),
  P_({
    id: 'grillmair', label: 'Carl Grillmair', status: 'dead', date: '2026-02-16', age: null,
    loc: 'Llano, CA', locId: 'l-llano', instId: 'ipac', sub: 'Caltech IPAC, dark matter and exoplanets',
    cluster: 'california', tier: 'A', S: 3, P: 1, I: 3, domains: ['d-astro'],
    narrative: 'Shot once in the neck on his own front porch in Llano on February 16 2026. He has the strongest documented sequence in the entire file, and it is a sequence about the criminal justice system rather than about classified work. He reported his eventual killer for trespassing on December 20 2025; deputies found the man carrying a loaded unregistered rifle and arrested him on a felony weapons charge; he was released after three days; prosecutors dropped the charges by February 5 2026; and he killed Grillmair eleven days later. Grillmair studied dark matter and exoplanets and held no documented clearance, while working at Caltech IPAC, inside the institution that manages JPL. All three of those facts have to be visible at once, which is exactly why the three axes are not summed. His widow, Louise Grillmair, rejects the missing-scientists framing as absolute nonsense and says her husband would laugh at those promoting it; she believes he was targeted in a misguided revenge plot.',
    affiliations: ['Caltech Infrared Processing and Analysis Center'],
    tierRationale: 'S3 on the strength of a five-step documented sequence, I3 on the institution, P1 on the research. A single composite grade would either overstate or erase him.',
    unexplainedResidual: 'Charges against the man who killed him were dropped eleven days before the shooting, after deputies had arrested him on Grillmair\u2019s own complaint carrying a loaded unregistered rifle.',
    sequenceChain: [
      { date: '2025-12-20', event: 'Grillmair reports Freddy Snyder for trespassing on his property', isAnomalous: false, source: 'LA County DA' },
      { date: '2025-12-20', event: 'Deputies find Snyder carrying a loaded, unregistered rifle and arrest him on a felony weapons charge', isAnomalous: false, source: 'LA County DA' },
      { date: '2025-12-23', event: 'Snyder released after three days', isAnomalous: true, source: 'LA County DA' },
      { date: '2026-02-02', event: 'Snyder returns to the property with a baseball bat, roughly two weeks before the shooting', isAnomalous: true, source: 'Family statement' },
      { date: '2026-02-05', event: 'Prosecutors drop the felony weapons charges. Eleven days before the shooting', isAnomalous: true, source: 'LA County DA' },
      { date: '2026-02-16', event: 'Snyder arms himself with two rifles, fires into his mother\u2019s ceiling to take her car keys, drives to Llano and shoots Grillmair once in the neck', isAnomalous: false, source: 'LA County DA' },
    ],
    chronology: [
      { date: '2025-12-20', event: 'Reports Snyder for trespassing. Snyder arrested', precision: 'day' },
      { date: '2026-02-05', event: 'Charges dropped', precision: 'day' },
      { date: '2026-02-16', event: 'Killed on his front porch', precision: 'day' },
      { date: '2026-05-26', event: 'Snyder pleads not guilty. Bail 3.175 million dollars', precision: 'day' },
      { date: '2026-06-05', event: 'Preliminary hearing set, Department A2. Outcome not verified', precision: 'day' },
    ],
    claims: [
      { tier: 1, text: 'Case 26AVCF00232. One felony count each of murder, carjacking and first-degree residential burglary, with an allegation of personal use of a rifle.', source: 'LA County DA, May 28 2026' },
      { tier: 1, text: 'Widow Louise Grillmair calls the missing-scientists framing absolute nonsense and believes the motive was a misguided revenge plot.', source: 'BBC News, April 23 2026' },
      { tier: 3, text: 'Snyder claimed he had walked there to go to the post office. Property records indicate the post office was in the opposite direction from his home.', source: 'LA County DA' },
    ],
    sources: [{ outlet: 'LA County DA', url: 'https://da.lacounty.gov/media/news/charged-murderer-pleads-not-guilty-shooting-death-caltech-scientist', date: '2026-05-28' }],
  }),
  P_({
    id: 'mccasland', label: 'Neil McCasland', status: 'missing', date: '2026-02-27', age: null,
    loc: 'Albuquerque, NM', locId: 'l-abq', instId: 'afrl', sub: 'Maj Gen (ret.), former AFRL commander',
    cluster: 'new-mexico', tier: 'A', S: 2, P: 3, I: 3, domains: ['d-prop', 'd-intel'],
    leftBehind: ['Garmin watch', 'GPS devices', 'medication', 'iPhone', 'glasses'],
    tookWith: ['wallet', 'hiking boots', '.38 revolver', 'red backpack'],
    narrative: 'Retired Major General and former AFRL commander, missing from Albuquerque since February 27 2026. The Bernalillo County Sheriff\u2019s Office issued a formal correction set in June 2026 that dismantles most of what circulated about him: there is no Pentagon connection, likely a conflation with Riverside Research, a DoD contractor; he held a standard retiree clearance rather than active operational access; law enforcement emphasized his wife never said he made a desperate attempt to resign; and BCSO states there is no known connection between this case and the other missing-scientist cases. His wife wrote publicly that he had only very commonly held clearances since retiring more than thirteen years earlier, and that it seems quite unlikely he was taken to extract very dated secrets. Investigators confirmed he stepped down from consulting roles citing brain fog, though LA Magazine could not independently verify that in the FOIA documents it obtained. The search has stalled with no confirmed sighting since a store surveillance image on February 26 2026.',
    affiliations: ['Air Force Research Laboratory, former commander', 'Sandia National Laboratories (consulting)', 'Riverside Research (consulting)', 'Kirtland Partnership'],
    tierRationale: 'High personal proximity by career history and a documented departure pattern, tempered heavily by the sheriff\u2019s corrections. Retained at A for the unexplained item split.',
    unexplainedResidual: 'He left his phone, GPS devices, glasses and medication behind and took a revolver, hiking boots and a distinctive red backpack. No confirmed sighting since a store surveillance image on February 26 2026.',
    conflicts: ['Clearance level. A woman who served with him initially claimed top-level clearance, then acknowledged uncertainty. BCSO and his wife say standard retiree clearance.', 'Pentagon connection. Widely circulated, denied by BCSO, likely a conflation with Riverside Research.'],
    unverified: ['The brain fog account. Investigators confirmed it; LA Mag could not verify it in the FOIA documents obtained.'],
    sequenceChain: [
      { date: '2026-02-26', event: 'Captured on REI store surveillance. Last confirmed sighting', isAnomalous: false, source: 'BCSO' },
      { date: '2026-02-27', event: 'Leaves behind iPhone, GPS devices, Garmin watch, medication and glasses', isAnomalous: true, source: 'BCSO inventory' },
      { date: '2026-02-27', event: 'Takes wallet, hiking boots, a .38-caliber revolver with holster, and a distinctive red backpack', isAnomalous: true, source: 'BCSO inventory' },
      { date: '2026-03-06', event: 'Wife states publicly he held only very commonly held clearances since retiring', isAnomalous: false, source: 'Facebook public post' },
      { date: '2026-06-26', event: 'BCSO formally corrects the Pentagon, clearance and resignation claims', isAnomalous: false, source: 'LA Mag' },
      { date: '2026-08-04', event: 'Search stalled. BCSO has no updates for release', isAnomalous: true, source: 'LA Mag' },
    ],
    chronology: [
      { date: '2026-02-27', event: 'Disappears from Albuquerque', precision: 'day' },
      { date: '2026-06-26', event: 'Sheriff pushes back on circulating claims', precision: 'day' },
      { date: '2026-08-04', event: 'Search confirmed stalled', precision: 'day' },
    ],
    claims: [
      { tier: 1, text: 'BCSO: no known connection between this case and human trafficking, gang activity, or other missing scientist cases.', source: 'BCSO, June 26 2026' },
      { tier: 1, text: 'BCSO April statement: no evidence developed establishing that the disappearance is connected to his classified work.', source: 'BCSO' },
    ],
    sources: [{ outlet: 'LA Magazine', url: 'https://lamag.com/crimeinla/exclusive-sheriff-pushes-back-on-reports-surrounding-retired-missing-air-force-general-william-neil-mccasland/', date: '2026-06-26' }, { outlet: 'Newsweek', url: 'https://www.newsweek.com/neil-mccasland-update-sheriff-addresses-speculation-missing-general-11827036', date: '2026-04' }],
  }),
  P_({
    id: 'moffatt', label: 'James Moffatt', status: 'dead', date: '2026-04-17', age: 60,
    loc: 'Union County, SC', locId: 'l-union', instId: 'uah', sub: 'Aerospace engineer, UAH Research Center',
    cluster: 'other', tier: 'C', S: 0, P: 2, I: 2, mediaLinkedOnly: true, domains: ['d-prop'],
    narrative: 'Aerospace and defense engineer, retired Army aviation lieutenant colonel, founder of Moffatt Systems, and director of the Digital Engineering Transformation Lab at the UAH Research Center, with prior NASA work through Johnson Space Center. He died with three family members when his Mooney M20 came down near Union County Airport in South Carolina on April 17 2026. His son Andrew, a research engineer, was also killed. The FAA and NTSB are investigating and no cause has been determined. He is tagged media-linked rather than criteria-linked: he qualifies mainly because Fox News framed the story against the existing pattern, and he appears on no mainstream list, not Wikipedia, not the House Oversight list. Including him without that qualifier would be an instance of the near-enough effect the skeptical literature specifically names.',
    affiliations: ['Moffatt Systems Inc (founder)', 'UAH Research Center, Digital Engineering Transformation Lab', 'US Army aviation (lieutenant colonel, ret. 2008)', 'NASA Johnson Space Center (prior)'],
    tierRationale: 'An aircraft accident under routine NTSB investigation with no determined cause and no family dispute. Qualifies on the media-linkage prong alone.',
    conflicts: ['Inclusion itself is contested. He appears on no mainstream list and was surfaced only by Fox and wire coverage plus advocacy trackers.'],
    chronology: [
      { date: '2026-04-17', event: 'Mooney M20 comes down near Union County Airport. Four family members killed', precision: 'day' },
      { date: '2026-04-21', event: 'Fox News frames the story against the existing pattern', precision: 'day' },
    ],
    claims: [
      { tier: 3, text: 'Appears on no mainstream list. Not on Wikipedia, not on the House Oversight list.', source: 'Verified absence' },
    ],
    sources: [{ outlet: 'Fox News', url: 'https://www.foxnews.com/us/aerospace-defense-engineer-military-veteran-killed-plane-crash-family', date: '2026-04-21' }],
  }),
];

const other = (id, cls, label, cluster, sub) => ({ id, cls, label, cluster, sub });

export const INSTITUTIONS = [
  other('jpl', 'institution', 'NASA JPL', 'california', 'FFRDC'),
  other('ipac', 'institution', 'Caltech IPAC', 'california', 'Academic, manages JPL'),
  other('lanl', 'institution', 'LANL', 'new-mexico', 'National laboratory'),
  other('afrl', 'institution', 'AFRL', 'new-mexico', 'Military research'),
  other('uah', 'institution', 'UAH', 'huntsville', 'Academic'),
  other('ies', 'institution', 'Inst. for Exotic Science', 'huntsville', 'Private'),
  other('nsa', 'institution', 'NSA / NASIC', 'other', 'Intelligence'),
  other('mit', 'institution', 'MIT PSFC', 'northeast', 'Academic'),
  other('kcnsc', 'institution', 'KCNSC', 'new-mexico', 'NNSA campus'),
  other('novartis', 'institution', 'Novartis', 'northeast', 'Pharmaceutical, non-defense'),
  other('boeing', 'institution', 'Boeing / Rocketdyne', 'california', 'Private aerospace'),
  other('nasa', 'institution', 'NASA Marshall', 'huntsville', 'Government'),
];

export const PROGRAMS = [
  other('oversight', 'program', 'House Oversight', 'other', 'Investigation'),
  other('fbi', 'program', 'FBI Review', 'other', 'Investigation'),
  other('pursue', 'program', 'PURSUE Files', 'other', 'Disclosure'),
  other('grusch', 'program', 'Grusch Proceedings', 'other', 'Testimony'),
  other('draco', 'program', 'DRACO', 'other', 'DARPA and NASA nuclear propulsion'),
  other('mondaloy', 'program', 'Mondaloy', 'other', 'Rocketdyne superalloy'),
];

export const LOCATIONS = [
  other('l-hsv', 'location', 'Huntsville AL', 'huntsville'),
  other('l-walker', 'location', 'Walker County AL', 'huntsville'),
  other('l-sun', 'location', 'Sunland CA', 'california'),
  other('l-la', 'location', 'Los Angeles CA', 'california'),
  other('l-anf', 'location', 'Angeles Natl Forest CA', 'california'),
  other('l-llano', 'location', 'Llano CA', 'california'),
  other('l-pas', 'location', 'Pasadena CA', 'california'),
  other('l-los', 'location', 'Los Alamos NM', 'new-mexico'),
  other('l-carson', 'location', 'Carson Natl Forest NM', 'new-mexico'),
  other('l-abq', 'location', 'Albuquerque NM', 'new-mexico'),
  other('l-fal', 'location', 'Falls Church VA', 'other'),
  other('l-cam', 'location', 'Cambridge MA', 'northeast'),
  other('l-wak', 'location', 'Wakefield MA', 'northeast'),
  other('l-union', 'location', 'Union County SC', 'other'),
];

export const DOMAINS = [
  other('d-prop', 'domain', 'Propulsion', 'other'),
  other('d-nuc', 'domain', 'Nuclear', 'other'),
  other('d-astro', 'domain', 'Astrophysics', 'other'),
  other('d-intel', 'domain', 'Intelligence', 'other'),
  other('d-plasma', 'domain', 'Plasma', 'other'),
  other('d-exotic', 'domain', 'Exotic materials', 'other'),
  other('d-chem', 'domain', 'Chemical biology', 'other'),
];

export const NODES = [...PEOPLE, ...INSTITUTIONS, ...PROGRAMS, ...LOCATIONS, ...DOMAINS];

const E = (a, b, type) => ({ a, b, type });

// Explicit programme and investigation ties. Editorial: they come from the
// reporting, not from a rule, so they stay hand-written and sourced.
const PROGRAM_EDGES = [
  E('sullivan', 'grusch', 'witness-chain'), E('grusch', 'oversight', 'witness-chain'),
  E('oversight', 'fbi', 'witness-chain'),
  E('leblanc', 'draco', 'programmatic'), E('draco', 'nasa', 'programmatic'),
  E('reza', 'mondaloy', 'programmatic'), E('mondaloy', 'boeing', 'programmatic'),
  E('mccasland', 'afrl', 'institutional'), E('sullivan', 'afrl', 'programmatic'),
  E('pursue', 'oversight', 'programmatic'),
];

const IN_FBI = ['chavez', 'reza', 'casias', 'garcia', 'mccasland', 'leblanc', 'li', 'eskridge', 'loureiro'];
const IN_OVERSIGHT = ['li', 'eskridge', 'leblanc', 'garcia', 'mccasland', 'chavez', 'sullivan'];

const INSTITUTION_PLACES = [
  ['jpl', 'l-pas'], ['ipac', 'l-pas'], ['lanl', 'l-los'], ['uah', 'l-hsv'], ['ies', 'l-hsv'],
  ['boeing', 'l-anf'], ['kcnsc', 'l-abq'], ['mit', 'l-cam'], ['novartis', 'l-wak'],
  ['nasa', 'l-hsv'], ['afrl', 'l-abq'],
];

const TEMPORAL_WINDOW_DAYS = 60;
const days = (a, b) => Math.abs(new Date(a) - new Date(b)) / 86400000;

function deriveEdges() {
  const out = [];
  for (const p of PEOPLE) {
    if (p.instId) out.push(E(p.id, p.instId, 'institutional'));
    if (p.locId) out.push(E(p.id, p.locId, 'geographic'));
    for (const d of p.domains) out.push(E(p.id, d, 'research'));
  }
  for (const [inst, place] of INSTITUTION_PLACES) out.push(E(inst, place, 'geographic'));
  for (const id of IN_FBI) out.push(E(id, 'fbi', 'investigative'));
  for (const id of IN_OVERSIGHT) out.push(E(id, 'oversight', 'investigative'));

  for (let i = 0; i < PEOPLE.length; i++) {
    for (let j = i + 1; j < PEOPLE.length; j++) {
      const a = PEOPLE[i], b = PEOPLE[j];
      if (a.instId && a.instId === b.instId) out.push(E(a.id, b.id, 'institutional'));
      if (a.cluster === b.cluster && a.cluster !== 'other') out.push(E(a.id, b.id, 'geographic'));
      if (a.domains.some(d => b.domains.includes(d))) out.push(E(a.id, b.id, 'research'));
      if (days(a.date, b.date) <= TEMPORAL_WINDOW_DAYS) out.push(E(a.id, b.id, 'temporal'));
      if (a.leftBehind.some(x => b.leftBehind.includes(x))) out.push(E(a.id, b.id, 'behavioral'));
    }
  }
  return [...out, ...PROGRAM_EDGES];
}

export const EDGES = deriveEdges();

// Sourcing now lives on each case record (record.sources). This map covers the
// non-person nodes only. Absence is meaningful: the UI must say "no attributed
// source on file" rather than imply one exists.
export const SOURCES = {
  oversight: [{ name: 'House Oversight', url: 'https://oversight.house.gov/release/comer-burlison-seek-information-on-missing-nuclear-and-rocket-scientists/' }],
  fbi: [{ name: 'CNN', url: 'https://www.cnn.com/2026/04/21/us/deaths-disappearances-scientists-investigation' }],
  pursue: [{ name: 'DefenseScoop', url: 'https://defensescoop.com/2026/05/14/uap-trump-first-pursue-ufo-file-drop/' }],
};

export const CLUSTERS = {
  california: { label: 'California / JPL corridor' },
  'new-mexico': { label: 'New Mexico' },
  huntsville: { label: 'Huntsville triangle' },
  northeast: { label: 'Northeast' },
  other: { label: 'Unclustered' },
};

export const TIERS = {
  A: { label: 'Tier A', color: '#5ed4e6', note: 'Contains a specific unexplained fact no source accounts for' },
  B: { label: 'Tier B', color: '#efb555', note: 'Unresolved, but a prosaic explanation exists and is not ruled out' },
  C: { label: 'Tier C', color: '#8d97a4', note: 'A conventional explanation is documented and holds' },
};

export const AXES = [
  { key: 'S', label: 'Sequence anomaly', question: 'How many independently documented, individually unexplained links form a chain around this event?' },
  { key: 'P', label: 'Program proximity', question: 'What sensitive access did this individual personally hold?' },
  { key: 'I', label: 'Institutional channel', question: 'Does the employer have a documented history as a conduit for classified work?' },
];

export const STATUS_LABEL = {
  dead: 'DEAD', missing: 'MISSING', resolved: 'RESOLVED',
};

// Why two entities are linked, in a sentence. The map colours the edge; this is
// what the dossier prints next to it.
export function explainEdge(type, a, b) {
  const other = (n) => (n.cls === 'person' ? n.label : n.label);
  switch (type) {
    case 'institutional':
      return a.cls === 'person' && b.cls === 'person'
        ? 'Both employed by the same institution.'
        : 'Employment or formal affiliation.';
    case 'geographic':
      return a.cls === 'person' && b.cls === 'person'
        ? 'Both fall inside the same geographic cluster.'
        : 'Physical location of record.';
    case 'research':
      return a.cls === 'person' && b.cls === 'person'
        ? 'Overlapping research domain.'
        : 'Documented research area.';
    case 'temporal':
      return 'Dates fall within sixty days of each other.';
    case 'behavioral':
      return 'Both left the same category of personal item behind.';
    case 'programmatic':
      return 'Named on the same government programme or product.';
    case 'investigative':
      return 'Named in the same federal review.';
    case 'witness-chain':
      return 'Sourced testimony chain.';
    default:
      return 'Connected.';
  }
}

// The "left everything behind" thread has a definition, and it is narrower than
// "the leftBehind array is non-empty". A member left BOTH the phone and the
// wallet and did not carry a departure kit. That rule excludes Chavez, who owned
// no cell phone, and McCasland, who deliberately took wallet, boots, a revolver
// and a backpack. Four clean members, per DESIGN-ADDENDUM-2026-08-07 change 5.
export function leftEverythingBehind() {
  const has = (arr, word) => arr.some(x => x.toLowerCase().indexOf(word) > -1);
  return PEOPLE.filter(p =>
    has(p.leftBehind, 'phone') && has(p.leftBehind, 'wallet') && !has(p.tookWith, 'wallet'));
}

export function nodeColor(n) {
  if (n.cls === 'person') return PALETTE[n.status] || PALETTE.person;
  return PALETTE[n.cls] || PALETTE.person;
}

// ---- layout -------------------------------------------------------------

const DEFAULT_INSET = { l: 84, r: 84, t: 34, b: 40 };

export function anchorsFor(w, h, inset) {
  const i = inset || DEFAULT_INSET;
  const x = i.l, y = i.t, uw = w - i.l - i.r, uh = h - i.t - i.b;
  return {
    california: [x + uw * 0.14, y + uh * 0.42],
    'new-mexico': [x + uw * 0.82, y + uh * 0.40],
    huntsville: [x + uw * 0.30, y + uh * 0.90],
    other: [x + uw * 0.56, y + uh * 0.06],
    domains: [x + uw * 0.84, y + uh * 0.92],
  };
}

function anchorKey(n) { return n.cls === 'domain' ? 'domains' : n.cluster; }

export function initLayout(nodes, w, h, inset) {
  const anchors = anchorsFor(w, h, inset);
  let i = 0;
  for (const n of nodes) {
    const [ax, ay] = anchors[anchorKey(n)] || anchors.other;
    const a = (i * 2.399963) % (Math.PI * 2);
    const r = 40 + ((i * 37) % 130);
    n.x = ax + Math.cos(a) * r;
    n.y = ay + Math.sin(a) * r * 0.7;
    n.vx = 0; n.vy = 0;
    if (n.cls === 'person') {
      const parts = n.label.split(' ');
      n.short = (parts[parts.length - 1] + ', ' + parts[0][0] + '.').toUpperCase();
    }
    n.w = n.cls === 'person' ? (n.photo ? 132 : 100) : 0;
    n.h = n.cls === 'person' ? 40 : 0;
    n.rad = n.cls === 'person' ? (n.photo ? 58 : 46) : n.cls === 'institution' ? 22 : n.cls === 'program' ? 22 : 17;
    i++;
  }
  return anchors;
}

export function makeSim(nodes, edges, w, h, inset) {
  const ins = inset || DEFAULT_INSET;
  const byId = new Map(nodes.map(n => [n.id, n]));
  const links = edges.map(e => ({ s: byId.get(e.a), t: byId.get(e.b), type: e.type }))
    .filter(l => l.s && l.t);
  const anchors = anchorsFor(w, h, ins);
  const deg = new Map();
  for (const l of links) {
    deg.set(l.s.id, (deg.get(l.s.id) || 0) + 1);
    deg.set(l.t.id, (deg.get(l.t.id) || 0) + 1);
  }
  for (const n of nodes) n.deg = deg.get(n.id) || 0;

  let alpha = 1;
  function step() {
    alpha = Math.max(alpha * 0.994, 0.06);
    for (const n of nodes) {
      const [ax, ay] = anchors[anchorKey(n)] || anchors.other;
      n.vx += (ax - n.x) * 0.0022 * alpha * 6;
      n.vy += (ay - n.y) * 0.0022 * alpha * 6;
    }
    for (let i = 0; i < nodes.length; i++) {
      const a = nodes[i];
      for (let j = i + 1; j < nodes.length; j++) {
        const b = nodes[j];
        let dx = b.x - a.x, dy = b.y - a.y;
        let d2 = dx * dx + dy * dy;
        if (d2 < 1) { d2 = 1; dx = (i - j) * 0.5; dy = 0.5; }
        const min = (a.rad + b.rad + 14);
        const d = Math.sqrt(d2);
        const f = (3200 * alpha) / d2;
        dx /= d; dy /= d;
        a.vx -= dx * f; a.vy -= dy * f;
        b.vx += dx * f; b.vy += dy * f;
        if (d < min) {
          const push = (min - d) * 0.40;
          a.vx -= dx * push; a.vy -= dy * push;
          b.vx += dx * push; b.vy += dy * push;
        }
      }
    }
    for (const l of links) {
      const dx = l.t.x - l.s.x, dy = l.t.y - l.s.y;
      const d = Math.max(Math.sqrt(dx * dx + dy * dy), 0.01);
      const rest = l.type === 'geographic' ? 118 : l.type === 'institutional' ? 132 : 190;
      const k = (l.type === 'temporal' || l.type === 'behavioral') ? 0.006 : 0.02;
      const f = (d - rest) * k * alpha * 4;
      const ux = (dx / d) * f, uy = (dy / d) * f;
      l.s.vx += ux; l.s.vy += uy;
      l.t.vx -= ux; l.t.vy -= uy;
    }
    for (const n of nodes) {
      n.vx *= 0.82; n.vy *= 0.82;
      n.x += Math.max(-9, Math.min(9, n.vx));
      n.y += Math.max(-9, Math.min(9, n.vy));
      n.x = Math.max(ins.l, Math.min(w - ins.r, n.x));
      n.y = Math.max(ins.t, Math.min(h - ins.b, n.y));
    }
  }
  return { step, links, byId, anchors, get alpha() { return alpha; } };
}

// ---- drawing primitives -------------------------------------------------

export function roundRect(ctx, x, y, w, h, r) {
  ctx.beginPath();
  ctx.moveTo(x + r, y);
  ctx.arcTo(x + w, y, x + w, y + h, r);
  ctx.arcTo(x + w, y + h, x, y + h, r);
  ctx.arcTo(x, y + h, x, y, r);
  ctx.arcTo(x, y, x + w, y, r);
  ctx.closePath();
}

function hatch(ctx, x, y, w, h, color, gap = 4) {
  ctx.save();
  ctx.beginPath(); ctx.rect(x, y, w, h); ctx.clip();
  ctx.strokeStyle = color; ctx.lineWidth = 0.7;
  ctx.beginPath();
  for (let i = -h; i < w + h; i += gap) { ctx.moveTo(x + i, y + h); ctx.lineTo(x + i + h, y); }
  ctx.stroke();
  ctx.restore();
}

// Dossier plate: photo slot + name + status stripe. LOD collapses to a mark.
export function drawNode(ctx, n, st) {
  const { scale = 1, state = 'default' } = st || {};
  const col = nodeColor(n);
  const dim = state === 'dimmed';
  const sel = state === 'selected';
  const near = state === 'connected';
  const hov = state === 'hover';
  ctx.globalAlpha = dim ? 0.16 : 1;

  if (n.cls !== 'person') {
    const r = n.cls === 'institution' ? 6.5 : n.cls === 'program' ? 6 : n.cls === 'domain' ? 5.5 : 4.5;
    // class shape: institution = square, program = diamond, location = ring, domain = dot
    ctx.lineWidth = sel || hov ? 1.8 : 1.1;
    ctx.strokeStyle = col;
    ctx.fillStyle = PALETTE.bg2;
    ctx.beginPath();
    if (n.cls === 'institution') { ctx.rect(n.x - r, n.y - r, r * 2, r * 2); }
    else if (n.cls === 'program') {
      ctx.moveTo(n.x, n.y - r * 1.3); ctx.lineTo(n.x + r * 1.3, n.y);
      ctx.lineTo(n.x, n.y + r * 1.3); ctx.lineTo(n.x - r * 1.3, n.y); ctx.closePath();
    } else { ctx.arc(n.x, n.y, r, 0, Math.PI * 2); }
    ctx.fill();
    if (sel || near || hov) { ctx.save(); ctx.shadowColor = col; ctx.shadowBlur = 10; ctx.stroke(); ctx.restore(); }
    ctx.stroke();
    if (n.cls === 'domain') { ctx.fillStyle = col; ctx.beginPath(); ctx.arc(n.x, n.y, r * 0.42, 0, Math.PI * 2); ctx.fill(); }
    if (scale > 0.62 || sel || hov) {
      ctx.fillStyle = dim ? PALETTE.faint : (sel || hov ? PALETTE.text : PALETTE.dim);
      ctx.font = `${sel || hov ? 600 : 400} 9px "IBM Plex Mono", monospace`;
      ctx.textAlign = 'center'; ctx.textBaseline = 'top';
      ctx.fillText(n.label.toUpperCase(), n.x, n.y + r + 5);
    }
    ctx.globalAlpha = 1;
    return;
  }

  // person plate. The photo slot only exists when there is a photo to put in it;
  // an empty slot would spend 35px of plate width saying nothing.
  const hasPhoto = !!n.photo;
  const w = hasPhoto ? 132 : 100, h = 40, x = n.x - w / 2, y = n.y - h / 2;
  if (scale < 0.5 && !sel && !hov) {
    ctx.fillStyle = col;
    ctx.beginPath(); ctx.arc(n.x, n.y, 5, 0, Math.PI * 2); ctx.fill();
    ctx.globalAlpha = 1; return;
  }
  if (sel || hov) {
    ctx.save(); ctx.shadowColor = col; ctx.shadowBlur = sel ? 24 : 11;
    ctx.fillStyle = PALETTE.panel; roundRect(ctx, x, y, w, h, 2); ctx.fill(); ctx.restore();
  }
  ctx.fillStyle = sel ? PALETTE.panel2 : PALETTE.panel;
  roundRect(ctx, x, y, w, h, 2); ctx.fill();
  ctx.strokeStyle = sel || hov ? col : (near ? '#56616e' : PALETTE.line);
  ctx.lineWidth = sel ? 1.5 : 1;
  roundRect(ctx, x, y, w, h, 2); ctx.stroke();

  // status stripe
  ctx.fillStyle = col;
  ctx.fillRect(x, y, 3, h);

  let tx = x + 11;
  if (hasPhoto) {
    const px = x + 9, py = y + 7, pw = 26, ph = h - 14;
    ctx.fillStyle = PALETTE.bg;
    ctx.fillRect(px, py, pw, ph);
    if (n.photoImg && n.photoImg.complete) {
      ctx.save();
      ctx.beginPath(); ctx.rect(px, py, pw, ph); ctx.clip();
      ctx.drawImage(n.photoImg, px, py, pw, ph);
      ctx.restore();
    }
    ctx.strokeStyle = PALETTE.line2; ctx.lineWidth = 0.7;
    ctx.strokeRect(px + 0.5, py + 0.5, pw - 1, ph - 1);
    tx = px + pw + 8;
  }

  ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
  ctx.fillStyle = sel || hov ? PALETTE.text : '#cfd6df';
  ctx.font = '600 10.5px "IBM Plex Mono", monospace';
  ctx.fillText(n.short || n.label.toUpperCase(), tx, y + 18);
  ctx.fillStyle = PALETTE.faint;
  ctx.font = '400 8.5px "IBM Plex Mono", monospace';
  ctx.fillText(n.date.replace(/-/g, '.'), tx, y + 31);
  ctx.fillStyle = col;
  ctx.font = '600 8px "IBM Plex Mono", monospace';
  ctx.textAlign = 'right';
  ctx.fillText(n.status === 'resolved' ? 'CLD' : n.status === 'dead' ? 'DEC' : 'MIS', x + w - 8, y + 31);
  ctx.globalAlpha = 1;
}

// ---- four edge languages ------------------------------------------------
// Each: (ctx, links, opts) where opts = { t, active:Set|null, scale }

function alphaFor(l, active, base) {
  if (!active) return base;
  return active.has(l.s.id) && active.has(l.t.id) ? 1 : 0.05;
}

function bundleCtrl(l, anchors) {
  const [ax, ay] = anchors[l.s.cls === 'domain' ? 'domains' : l.s.cluster] || anchors.other;
  const [bx, by] = anchors[l.t.cls === 'domain' ? 'domains' : l.t.cluster] || anchors.other;
  const mx = (l.s.x + l.t.x) / 2, my = (l.s.y + l.t.y) / 2;
  const hx = (ax + bx) / 2, hy = (ay + by) / 2;
  const b = l.s.cluster === l.t.cluster ? 0.18 : 0.42;
  return [mx + (hx - mx) * b, my + (hy - my) * b];
}

export function drawEdgesBundled(ctx, links, o) {
  const { active, anchors, t } = o;
  ctx.lineCap = 'round';
  for (const l of links) {
    const a = alphaFor(l, active, 0.30);
    const et = EDGE_TYPES[l.type];
    const [cx, cy] = bundleCtrl(l, anchors);
    ctx.globalAlpha = a;
    ctx.strokeStyle = et.color;
    ctx.lineWidth = active && a > 0.5 ? 1.5 : 0.75;
    ctx.beginPath();
    ctx.moveTo(l.s.x, l.s.y);
    ctx.quadraticCurveTo(cx, cy, l.t.x, l.t.y);
    ctx.stroke();
  }
  // travelling particles on the active set only
  if (active) {
    for (const l of links) {
      if (!(active.has(l.s.id) && active.has(l.t.id))) continue;
      const et = EDGE_TYPES[l.type];
      const [cx, cy] = bundleCtrl(l, anchors);
      for (let k = 0; k < 2; k++) {
        const u = ((t * 0.00022 + k * 0.5 + (l.s.x % 97) / 97) % 1);
        const iv = 1 - u;
        const px = iv * iv * l.s.x + 2 * iv * u * cx + u * u * l.t.x;
        const py = iv * iv * l.s.y + 2 * iv * u * cy + u * u * l.t.y;
        ctx.globalAlpha = Math.sin(u * Math.PI) * 0.95;
        ctx.fillStyle = et.color;
        ctx.save(); ctx.shadowColor = et.color; ctx.shadowBlur = 8;
        ctx.beginPath(); ctx.arc(px, py, 1.9, 0, Math.PI * 2); ctx.fill(); ctx.restore();
      }
    }
  }
  ctx.globalAlpha = 1;
}

export function drawEdgesArcs(ctx, links, o) {
  const { active } = o;
  for (const l of links) {
    const a = alphaFor(l, active, 0.34);
    const et = EDGE_TYPES[l.type];
    const dx = l.t.x - l.s.x, dy = l.t.y - l.s.y;
    const mx = (l.s.x + l.t.x) / 2, my = (l.s.y + l.t.y) / 2;
    const len = Math.sqrt(dx * dx + dy * dy) || 1;
    const off = Math.min(len * 0.13, 46);
    const cx = mx + (-dy / len) * off, cy = my + (dx / len) * off;
    ctx.globalAlpha = a;
    ctx.strokeStyle = et.color;
    ctx.lineWidth = active && a > 0.5 ? 1.6 : 0.8;
    ctx.setLineDash(et.dash);
    ctx.beginPath();
    ctx.moveTo(l.s.x, l.s.y);
    ctx.quadraticCurveTo(cx, cy, l.t.x, l.t.y);
    ctx.stroke();
  }
  ctx.setLineDash([]);
  ctx.globalAlpha = 1;
}

export function drawEdgesField(ctx, links, o) {
  const { active, anchors } = o;
  // Pass 1: broad faint glow, weight by endpoint degree -- reads as a density field.
  ctx.globalCompositeOperation = 'lighter';
  for (const pass of [0, 1, 2]) {
    for (const l of links) {
      const a = alphaFor(l, active, 0.055 - pass * 0.014);
      if (a <= 0.02) continue;
      const et = EDGE_TYPES[l.type];
      const [cx, cy] = bundleCtrl(l, anchors);
      const wgt = Math.min((l.s.deg + l.t.deg) / 22, 2.4);
      ctx.globalAlpha = a;
      ctx.strokeStyle = et.color;
      ctx.lineWidth = (14 - pass * 5) * (0.5 + wgt * 0.4);
      ctx.beginPath();
      ctx.moveTo(l.s.x, l.s.y);
      ctx.quadraticCurveTo(cx, cy, l.t.x, l.t.y);
      ctx.stroke();
    }
  }
  ctx.globalCompositeOperation = 'source-over';
  // Pass 2: crisp cores, only where selected
  if (active) {
    for (const l of links) {
      if (!(active.has(l.s.id) && active.has(l.t.id))) continue;
      const et = EDGE_TYPES[l.type];
      const [cx, cy] = bundleCtrl(l, anchors);
      ctx.globalAlpha = 0.95;
      ctx.strokeStyle = et.color;
      ctx.lineWidth = 1.2;
      ctx.beginPath();
      ctx.moveTo(l.s.x, l.s.y);
      ctx.quadraticCurveTo(cx, cy, l.t.x, l.t.y);
      ctx.stroke();
    }
  }
  ctx.globalAlpha = 1;
}

// Strength = how many INDEPENDENT connection types tie the same pair together.
// One shared employer is weak evidence; employer + geography + domain + timing +
// the left-behind signature is the thing worth looking at. Aggregating by pair is
// what lets the map say that at a glance.
const TYPE_PRIORITY = ['witness-chain', 'investigative', 'programmatic', 'behavioral', 'institutional', 'research', 'geographic', 'temporal'];

export const STRENGTH_RAMP = [
  { weight: 1, label: 'Single link', color: '#4d5a66', width: 0.9 },
  { weight: 2, label: 'Corroborated', color: '#6e8b9c', width: 1.8 },
  { weight: 3, label: 'Strong', color: '#5ed4e6', width: 2.8 },
  { weight: 4, label: 'Very strong', color: '#8ee6f0', width: 3.8 },
  { weight: 5, label: 'Maximal', color: '#d7f6fa', width: 4.8 },
];

export function strengthStyle(weight) {
  return STRENGTH_RAMP[Math.min(weight, STRENGTH_RAMP.length) - 1];
}

export function aggregatePairs(links) {
  const map = new Map();
  for (const l of links) {
    const key = l.s.id < l.t.id ? l.s.id + '|' + l.t.id : l.t.id + '|' + l.s.id;
    let rec = map.get(key);
    if (!rec) { rec = { s: l.s, t: l.t, types: [] }; map.set(key, rec); }
    if (!rec.types.includes(l.type)) rec.types.push(l.type);
  }
  const pairs = [...map.values()];
  for (const p of pairs) {
    p.weight = p.types.length;
    p.dominant = TYPE_PRIORITY.find(t => p.types.includes(t)) || p.types[0];
    // Flow direction carries meaning: between two people it runs earlier date to
    // later date, so the animation reads as the sequence of events. Everywhere
    // else it runs from the person outward to the thing they were attached to.
    p.flip = false;
    if (p.s.date && p.t.date) p.flip = new Date(p.s.date) > new Date(p.t.date);
    else if (p.t.cls === 'person' && p.s.cls !== 'person') p.flip = true;
    // Deterministic per-pair phase offset so particles do not march in lockstep.
    p.phase = ((p.s.id.charCodeAt(0) * 31 + p.t.id.charCodeAt(0) * 17) % 100) / 100;
  }
  // Weakest first so strong traces draw on top.
  pairs.sort((a, b) => a.weight - b.weight);
  return pairs;
}

// Orthogonal route as a point list, so particles can walk it by arc length.
function circuitPoints(p) {
  const dx = p.t.x - p.s.x, dy = p.t.y - p.s.y;
  const k = Math.min(Math.abs(dx), Math.abs(dy)) * 0.55;
  const sx = Math.sign(dx) || 1, sy = Math.sign(dy) || 1;
  if (Math.abs(dx) > Math.abs(dy)) {
    return [
      [p.s.x, p.s.y],
      [p.s.x + (Math.abs(dx) - k) * sx, p.s.y],
      [p.t.x, p.s.y + k * sy],
      [p.t.x, p.t.y],
    ];
  }
  return [
    [p.s.x, p.s.y],
    [p.s.x, p.s.y + (Math.abs(dy) - k) * sy],
    [p.s.x + k * sx, p.t.y],
    [p.t.x, p.t.y],
  ];
}

function walk(pts, u) {
  const segs = [];
  let total = 0;
  for (let i = 1; i < pts.length; i++) {
    const d = Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]);
    segs.push(d); total += d;
  }
  if (total < 1) return pts[0];
  let want = u * total;
  for (let i = 0; i < segs.length; i++) {
    if (want <= segs[i] || i === segs.length - 1) {
      const f = segs[i] < 0.001 ? 0 : Math.min(want / segs[i], 1);
      return [
        pts[i][0] + (pts[i + 1][0] - pts[i][0]) * f,
        pts[i][1] + (pts[i + 1][1] - pts[i][1]) * f,
      ];
    }
    want -= segs[i];
  }
  return pts[pts.length - 1];
}

export function drawEdgesCircuit(ctx, links, o) {
  const { active } = o;
  const t = o.t || 0;
  const pairs = o.pairs || aggregatePairs(links);
  ctx.lineJoin = 'miter';
  ctx.lineCap = 'butt';
  const flowing = [];
  for (const p of pairs) {
    const on = !active || (active.has(p.s.id) && active.has(p.t.id));
    const ramp = strengthStyle(p.weight);
    const et = EDGE_TYPES[p.dominant];
    // Idle: strength drives width and lightness. Selected: dominant type takes
    // over the hue so the eight categories stay readable inside a selection.
    ctx.globalAlpha = on ? (active ? 0.95 : 0.30 + (p.weight - 1) * 0.15) : 0.045;
    ctx.strokeStyle = active && on ? et.color : ramp.color;
    ctx.lineWidth = ramp.width * (active && on ? 1.15 : 1);
    const pts = circuitPoints(p);
    const path = new Path2D();
    path.moveTo(pts[0][0], pts[0][1]);
    for (let i = 1; i < pts.length; i++) path.lineTo(pts[i][0], pts[i][1]);
    if (p.weight >= 3 && on) {
      ctx.save();
      ctx.shadowColor = active ? et.color : ramp.color;
      ctx.shadowBlur = 5 + p.weight * 2.5;
      ctx.stroke(path);
      ctx.restore();
    }
    ctx.stroke(path);

    // Weight tick marks at the corner: one notch per independent link type.
    if (p.weight >= 3 && on) {
      const c = pts[2];
      ctx.fillStyle = active && on ? et.color : ramp.color;
      for (let i = 0; i < p.weight; i++) ctx.fillRect(c[0] - 1.1, c[1] - 6 + i * 3.4, 2.2, 2.2);
    }

    // Idle keeps only corroborated pairs alive, so the resting map reads as
    // signal rather than noise. A selection animates everything inside it.
    if (on && (active || p.weight >= 2)) flowing.push({ p, pts, color: active ? et.color : ramp.color, on });
  }

  // Particles last, so they sit above every trace.
  for (const f of flowing) {
    const { p, pts } = f;
    const count = active ? Math.max(2, p.weight) : p.weight;
    for (let i = 0; i < count; i++) {
      let u = (t * 0.000115 + p.phase + i / count) % 1;
      if (p.flip) u = 1 - u;
      const [px, py] = walk(pts, u);
      const fade = Math.sin(Math.min(u, 1 - u) * Math.PI) * 1.35;
      ctx.globalAlpha = Math.min(1, (active ? 0.95 : 0.62) * Math.max(fade, 0.18));
      ctx.fillStyle = f.color;
      ctx.save();
      ctx.shadowColor = f.color;
      ctx.shadowBlur = active ? 9 : 6;
      ctx.beginPath();
      ctx.arc(px, py, active ? 2 : 1.5, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
    }
  }
  ctx.globalAlpha = 1;
}

export const RENDERERS = {
  bundled: drawEdgesBundled,
  arcs: drawEdgesArcs,
  field: drawEdgesField,
  circuit: drawEdgesCircuit,
};

export function neighborhood(links, id, hops = 1) {
  const set = new Set([id]);
  let frontier = [id];
  for (let h = 0; h < hops; h++) {
    const next = [];
    for (const l of links) {
      if (frontier.includes(l.s.id) && !set.has(l.t.id)) { set.add(l.t.id); next.push(l.t.id); }
      if (frontier.includes(l.t.id) && !set.has(l.s.id)) { set.add(l.s.id); next.push(l.s.id); }
    }
    frontier = next;
  }
  return set;
}

// ---- mountable map controller -------------------------------------------
// Owns sizing, layout, the draw loop and hit testing so a shell only has to
// supply a canvas and react to callbacks.
export function mountMap(canvas, opts = {}) {
  const variant = opts.variant || 'bundled';
  const inset = opts.inset || { l: 96, r: 96, t: 44, b: 44 };
  const onHover = opts.onHover || (() => {});
  const onSelect = opts.onSelect || (() => {});
  const nodes = NODES.map(n => ({ ...n }));
  let W = 0, H = 0, dpr = 1, sim = null, active = null, selected = null, hover = null;
  let raf = null, fallback = null, frames = 0, t0 = performance.now(), dead = false, pairs = [];

  function measure() {
    const b = canvas.getBoundingClientRect();
    const pb = canvas.parentElement.getBoundingClientRect();
    const nw = Math.max(b.width || pb.width, 320), nh = Math.max(b.height || pb.height, 240);
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    const bw = Math.round(nw * dpr), bh = Math.round(nh * dpr);
    if (canvas.width !== bw || canvas.height !== bh) { canvas.width = bw; canvas.height = bh; }
    const changed = Math.abs(nw - W) > 1 || Math.abs(nh - H) > 1;
    W = nw; H = nh;
    return changed;
  }

  function reflow() {
    const changed = measure();
    if (!changed || !sim) return;
    // Re-anchor to the new box and let the layout settle into it.
    Object.assign(sim.anchors, anchorsFor(W, H, inset));
    for (let i = 0; i < 220; i++) sim.step();
    pairs = aggregatePairs(sim.links);
  }

  function build() {
    measure();
    initLayout(nodes, W, H, inset);
    sim = makeSim(nodes, EDGES, W, H, inset);
    for (let i = 0; i < 900; i++) sim.step();
    pairs = aggregatePairs(sim.links);
  }

  function hitTest(mx, my) {
    let best = null, bd = 1e9;
    for (const n of nodes) {
      if (n.cls === 'person') {
        const hw = (n.photo ? 132 : 100) / 2 + 2;
        if (Math.abs(mx - n.x) < hw && Math.abs(my - n.y) < 20) return n;
      } else {
        const d = (mx - n.x) ** 2 + (my - n.y) ** 2;
        if (d < 260 && d < bd) { bd = d; best = n; }
      }
    }
    return best;
  }

  function draw() {
    const ctx = canvas.getContext('2d');
    const t = performance.now() - t0;
    // Re-assert the backing store every frame. The observer and resize paths can
    // both miss the final settle of a CSS grid; a stale buffer scales the canvas
    // non-uniformly and every plate renders wide-and-short.
    const b = canvas.getBoundingClientRect();
    if (b.width > 0) {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      const bw = Math.round(b.width * dpr), bh = Math.round(b.height * dpr);
      if (canvas.width !== bw || canvas.height !== bh) {
        canvas.width = bw; canvas.height = bh;
        W = b.width; H = b.height;
      }
    }
    if (sim.alpha > 0.061) sim.step();
    ctx.save();
    ctx.scale(dpr, dpr);
    ctx.clearRect(0, 0, W, H);
    const g = ctx.createLinearGradient(0, 0, 0, H);
    g.addColorStop(0, '#161a20'); g.addColorStop(1, '#11141a');
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    ctx.strokeStyle = 'rgba(59,68,79,0.18)'; ctx.lineWidth = 1;
    ctx.beginPath();
    for (let x = 0; x < W; x += 44) { ctx.moveTo(x, 0); ctx.lineTo(x, H); }
    for (let y = 0; y < H; y += 44) { ctx.moveTo(0, y); ctx.lineTo(W, y); }
    ctx.stroke();

    const tints = { california: '94,212,230', 'new-mexico': '239,181,85', huntsville: '167,149,232' };
    for (const [key, tint] of Object.entries(tints)) {
      const pts = nodes.filter(n => n.cluster === key && n.cls === 'person');
      if (!pts.length) continue;
      const cx = pts.reduce((s, p) => s + p.x, 0) / pts.length;
      const cy = pts.reduce((s, p) => s + p.y, 0) / pts.length;
      const rad = Math.max(...pts.map(p => Math.hypot(p.x - cx, p.y - cy))) + 120;
      const rg = ctx.createRadialGradient(cx, cy, 0, cx, cy, rad);
      rg.addColorStop(0, 'rgba(' + tint + ',0.055)');
      rg.addColorStop(0.62, 'rgba(' + tint + ',0.022)');
      rg.addColorStop(1, 'rgba(' + tint + ',0)');
      ctx.fillStyle = rg;
      ctx.beginPath(); ctx.arc(cx, cy, rad, 0, Math.PI * 2); ctx.fill();
      ctx.font = '600 9.5px "IBM Plex Mono", monospace';
      ctx.fillStyle = 'rgba(' + tint + ',0.32)';
      ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      ctx.fillText(CLUSTERS[key].label.toUpperCase(), cx, cy - rad + 22);
    }

    (RENDERERS[variant] || RENDERERS.bundled)(ctx, sim.links, { t, active, anchors: sim.anchors, scale: 1, pairs });

    const order = [...nodes].sort((a, b) => (a.cls === 'person' ? 1 : 0) - (b.cls === 'person' ? 1 : 0));
    for (const n of order) {
      let st = 'default';
      if (active) st = n.id === selected ? 'selected' : (active.has(n.id) ? 'connected' : 'dimmed');
      if (hover && hover.id === n.id && st !== 'selected') st = 'hover';
      drawNode(ctx, n, { scale: 1, state: st });
    }
    ctx.restore();
  }

  function tick() { frames++; try { draw(); } catch (e) { /* keep the loop alive */ } }
  function loop() {
    if (dead) return;
    if (fallback) { clearInterval(fallback); fallback = null; }
    tick();
    raf = requestAnimationFrame(loop);
  }

  const onMove = (e) => {
    const r = canvas.getBoundingClientRect();
    const mx = e.clientX - r.left, my = e.clientY - r.top;
    hover = hitTest(mx, my);
    onHover(hover, mx, my);
  };
  const onLeave = () => { hover = null; onHover(null, 0, 0); };
  const onClick = (e) => {
    const r = canvas.getBoundingClientRect();
    const n = hitTest(e.clientX - r.left, e.clientY - r.top);
    api.select(n ? n.id : null);
  };
  const onResize = () => reflow();

  canvas.addEventListener('mousemove', onMove);
  canvas.addEventListener('mouseleave', onLeave);
  canvas.addEventListener('click', onClick);
  window.addEventListener('resize', onResize);
  // The parent is laid out by a grid that settles after mount, so a window
  // resize listener alone misses the size change that actually matters.
  let ro = null;
  if (typeof ResizeObserver !== 'undefined') {
    ro = new ResizeObserver(() => { try { reflow(); } catch (e) { /* keep observing */ } });
    ro.observe(canvas.parentElement);
    ro.observe(canvas);
  }

  const api = {
    nodes,
    get links() { return sim.links; },
    get pairs() { return pairs; },
    strongestFor(id) {
      return pairs.filter(p => p.s.id === id || p.t.id === id).sort((a, b) => b.weight - a.weight);
    },
    select(id, hops = 1) {
      selected = id;
      active = id ? neighborhood(sim.links, id, hops) : null;
      const node = id ? nodes.find(n => n.id === id) : null;
      onSelect(node, active);
      return node;
    },
    byId(id) { return nodes.find(n => n.id === id); },
    destroy() {
      dead = true;
      cancelAnimationFrame(raf);
      if (fallback) clearInterval(fallback);
      if (ro) ro.disconnect();
      canvas.removeEventListener('mousemove', onMove);
      canvas.removeEventListener('mouseleave', onLeave);
      canvas.removeEventListener('click', onClick);
      window.removeEventListener('resize', onResize);
    },
  };

  build();
  tick();
  raf = requestAnimationFrame(loop);
  setTimeout(() => { if (frames < 2 && !fallback && !dead) fallback = setInterval(tick, 40); }, 350);
  return api;
}
