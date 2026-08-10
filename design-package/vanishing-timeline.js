// Timeline entries for the three-strand chronology view.
// Strand assignment is derived from what the entry IS, not from where it reads well:
//   cases      -- deaths and disappearances
//   oversight  -- what the state said and did, and when
//   skeptical  -- what the published record concluded, and when
// Date precision is rendered rather than smoothed. An entry known only to a
// month says so; nothing is invented to make the axis tidy.

export const PRECEDENT = [
  { date: '1953', precision: 'ranged', label: 'MKULTRA authorised', text: 'CIA mind-control programme runs to 1973. Most records destroyed in 1973 on the director\u2019s order.' },
  { date: '1953', precision: 'year', label: 'Frank Olson', text: 'Army biochemist dies in a fall from a New York hotel window days after being dosed with LSD without his knowledge. Ruled suicide, later settled by the government.' },
  { date: '1975', precision: 'year', label: 'Church Committee', text: 'Senate select committee documents assassination plots and domestic surveillance. Public demonstration of the CIA heart attack gun.' },
  { date: '2026-06-30', precision: 'day', label: 'House Oversight MKULTRA hearing', text: 'Committee holds a hearing on MKULTRA. Verified from the committee\u2019s own hearing calendar.' },
];

export const TIMELINE = [
  { id: 'li', strand: 'cases', date: '2021-07-27', precision: 'day', label: 'Ning Li dies', text: 'UAH gravitomagnetism researcher. Natural causes, seven years after a campus vehicle collision.', tier: 'C', node: 'li' },
  { id: 'eskridge', strand: 'cases', date: '2022-06-11', precision: 'day', label: 'Amy Eskridge dies', text: 'Ruled self-inflicted gunshot. Family supports the ruling.', tier: 'B', node: 'eskridge' },
  { id: 'grusch', strand: 'oversight', date: '2023-07-26', precision: 'day', label: 'Grusch testifies to Congress', text: 'Whistleblower proceedings that later produce the House Oversight letters.', node: 'grusch' },
  { id: 'hicks', strand: 'cases', date: '2023-07-30', precision: 'day', label: 'Michael Hicks dies', text: 'JPL, comets and asteroids. No public cause. Family attributes it to known medical issues.', tier: 'C', node: 'hicks' },
  { id: 'sullivan', strand: 'cases', date: '2024-05-12', precision: 'day', label: 'Matthew Sullivan dies', text: 'USAF intelligence. Accidental drug overdose per PolitiFact.', tier: 'B', node: 'sullivan' },
  { id: 'maiwald', strand: 'cases', date: '2024-07-04', precision: 'day', label: 'Frank Maiwald dies', text: 'JPL. No cause of death disclosed, then or since. Thinnest file in the set.', tier: 'A', node: 'maiwald' },
  { id: 'chavez', strand: 'cases', date: '2025-05-08', precision: 'day', label: 'Anthony Chavez disappears', text: 'Los Alamos. Had no cell phone. Handwritten journal found at the home.', tier: 'A', node: 'chavez' },
  { id: 'reza', strand: 'cases', date: '2025-06-22', precision: 'day', label: 'Monica Reza disappears', text: 'Vanishes within seconds in sight of a companion near Mount Waterman.', tier: 'A', node: 'reza' },
  { id: 'casias', strand: 'cases', date: '2025-06-26', precision: 'day', label: 'Melissa Casias disappears', text: 'LANL administrative assistant. Wallet, keys and factory-reset phones left at home.', tier: 'A', node: 'casias' },
  { id: 'leblanc', strand: 'cases', date: '2025-07-22', precision: 'day', label: 'Joshua LeBlanc dies', text: 'NASA Marshall, DRACO. Four unexplained hours at the airport that morning.', tier: 'A', node: 'leblanc' },
  { id: 'garcia', strand: 'cases', date: '2025-08-28', precision: 'day', label: 'Steven Garcia disappears', text: 'Leaves car, phone, wallet and keys. Takes a handgun and leaves on foot.', tier: 'A', node: 'garcia' },
  { id: 'chavez-closed', strand: 'oversight', date: '2025-10-06', precision: 'day', label: 'Los Alamos PD closes the Chavez case', text: 'Cites no new information, witnesses, or evidence. NM DPS listing stays active.', node: 'chavez' },
  { id: 'thomas', strand: 'cases', date: '2025-12-13', precision: 'day', label: 'Jason Thomas reported missing', text: 'Novartis, non-defense. Body found in Lake Quannapowitt March 17 2026. No foul play.', tier: 'C', node: 'thomas' },
  { id: 'loureiro', strand: 'cases', date: '2025-12-15', precision: 'day', label: 'Nuno Loureiro killed', text: 'MIT plasma physicist. Later resolved: former classmate acted alone.', tier: 'C', node: 'loureiro' },
  { id: 'snyder-report', strand: 'oversight', date: '2025-12-20', precision: 'day', label: 'Grillmair reports Snyder', text: 'Deputies arrest Snyder with a loaded unregistered rifle. Released after three days.', node: 'grillmair' },
  { id: 'charges-dropped', strand: 'oversight', date: '2026-02-05', precision: 'day', label: 'Snyder charges dropped', text: 'Eleven days before the shooting. The single most consequential decision in the file.', node: 'grillmair' },
  { id: 'grillmair', strand: 'cases', date: '2026-02-16', precision: 'day', label: 'Carl Grillmair killed', text: 'Shot on his own porch by the man he had reported for trespassing.', tier: 'A', node: 'grillmair' },
  { id: 'mccasland', strand: 'cases', date: '2026-02-27', precision: 'day', label: 'Neil McCasland disappears', text: 'Retired Maj Gen. Leaves phone, GPS and medication. Takes a revolver and a red backpack.', tier: 'A', node: 'mccasland' },
  { id: 'leavitt', strand: 'oversight', date: '2026-04-15', precision: 'day', label: 'White House podium', text: 'Press secretary addresses the cases. National coverage begins in earnest.', node: 'oversight' },
  { id: 'moffatt', strand: 'cases', date: '2026-04-17', precision: 'day', label: 'James Moffatt dies', text: 'Aircraft accident, four family members killed. Media-linked only, on no mainstream list.', tier: 'C', node: 'moffatt' },
  { id: 'letters', strand: 'oversight', date: '2026-04-20', precision: 'day', label: 'Comer and Burlison letters', text: 'House Oversight requests a staff-level FBI briefing by April 27. No readout has ever been published.', node: 'oversight' },
  { id: 'novella', strand: 'skeptical', date: '2026-04-21', precision: 'day', label: 'Novella base-rate analysis', text: 'Institution-level denominators. JPL and LANL counts run at a small fraction of expected all-cause mortality.', node: 'fbi' },
  { id: 'bartholomew', strand: 'skeptical', date: '2026-04-22', precision: 'day', label: 'Bartholomew on apophenia', text: 'The tendency to see meaningful links in unrelated events, compounded by confirmation bias.' },
  { id: 'engber', strand: 'skeptical', date: '2026-04-22', precision: 'day', label: 'Engber: no mechanism proposed', text: 'Argues the absence of any proposed actor, mechanism or motive is disqualifying. Never answered.' },
  { id: 'families', strand: 'skeptical', date: '2026-04-23', precision: 'day', label: 'Families reject the framing', text: 'BBC and Newsweek collect statements. Every family located rejects or resents the framing.' },
  { id: 'shermer', strand: 'skeptical', date: '2026-04-25', precision: 'day', label: 'Shermer: excluded exceptions', text: 'The narrative examines only the cell of defense-linked scientists who died. Three cells go unexamined.' },
  { id: 'coffindaffer', strand: 'skeptical', date: '2026-04-27', precision: 'day', label: 'Coffindaffer on what they took', text: 'Retired FBI agent: leaving wallet, phone and keys is a recognised signature of suicidal intent, read in the opposite direction.' },
  { id: 'politifact', strand: 'skeptical', date: '2026-04-28', precision: 'day', label: 'PolitiFact and Snopes', text: 'Not all fourteen were scientists. The claim that nearly all worked together is unsupported.' },
  { id: 'fbi-loureiro', strand: 'oversight', date: '2026-04-29', precision: 'day', label: 'FBI closes the Loureiro case', text: 'Former classmate acted alone. No nexus to terrorism.', node: 'loureiro' },
  { id: 'trump-reversal', strand: 'oversight', date: '2026-05-01', precision: 'day', label: 'Trump reverses', text: 'From pretty serious stuff to there is not much of a connection, in sixteen days.' },
  { id: 'sciam', strand: 'skeptical', date: '2026-05-07', precision: 'day', label: 'Scientific American', text: 'David Hand: random events clump if the numbers are big enough. The piece concedes it has no matched denominator.' },
  { id: 'pursue1', strand: 'oversight', date: '2026-05-08', precision: 'day', label: 'PURSUE release 1', text: 'First tranche of declassified UAP files.', node: 'pursue' },
  { id: 'snyder-plea', strand: 'oversight', date: '2026-05-26', precision: 'day', label: 'Snyder pleads not guilty', text: 'Murder, carjacking, first-degree residential burglary. Bail 3.175 million dollars.', node: 'grillmair' },
  { id: 'casias-found', strand: 'cases', date: '2026-05-31', precision: 'day', label: 'Casias remains identified', text: 'Skeletonized. Cause and manner still undetermined.', tier: 'A', node: 'casias' },
  { id: 'chavez-foia', strand: 'oversight', date: '2026-06-26', precision: 'day', label: 'Chavez police reports released', text: 'Public-records request reveals the closed case, the journal and the quantum physics tip.', node: 'chavez' },
  { id: 'bcso', strand: 'oversight', date: '2026-06-26', precision: 'day', label: 'Sheriff corrects the McCasland record', text: 'No Pentagon connection, standard retiree clearance, no known connection to the other cases.', node: 'mccasland' },
  { id: 'mkultra', strand: 'oversight', date: '2026-06-30', precision: 'day', label: 'House Oversight MKULTRA hearing', text: 'The committee held a hearing in this window. Not on the scientists.' },
  { id: 'ndaa', strand: 'oversight', date: '2026-07-22', precision: 'day', label: 'UAP Disclosure Act adopted', text: 'House adopts the Burlison amendment to the FY2027 NDAA. Senate action not verified.' },
  { id: 'casias-gun', strand: 'oversight', date: '2026-08-04', precision: 'day', label: 'Casias handgun identified', text: 'Registered black Springfield. Owner not disclosed. McCasland search confirmed stalled the same day.', node: 'casias' },
  { id: 'pursue5', strand: 'oversight', date: '2026-08-07', precision: 'day', label: 'PURSUE release 5', text: 'Forty-one files spanning 1950 to 2026.', node: 'pursue' },
];

export const STRANDS = [
  { key: 'cases', label: 'CASES', sub: 'deaths and disappearances', color: '#e8705f' },
  { key: 'oversight', label: 'OVERSIGHT & DISCLOSURE', sub: 'what the state said, and when', color: '#66d69f' },
  { key: 'skeptical', label: 'THE SKEPTICAL RECORD', sub: 'what the published analysis concluded', color: '#8d97a4' },
];

export const PRECISION_LABEL = {
  day: 'day-precise', month: 'month-precise', year: 'year-precise', ranged: 'ranged',
};
