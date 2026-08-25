const fs = require('fs');
const html = fs.readFileSync('dist/the-vanishing.html', 'utf8');

// Pull the real claimSources implementation out of the built page and exercise it
// against the real records, rather than trusting a UI click to have exercised it.
const start = html.indexOf('function claimSources(c){');
const end = html.indexOf('function tabSources(p){');
const src = html.slice(start, end);
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const claimSources = new Function('esc', src + '; return claimSources;')(esc);

const data = JSON.parse(fs.readFileSync('data/dataset.json', 'utf8'));
let total = 0, falseAbsence = 0, empty = 0;
const samples = [];
for (const c of data.cases) {
  for (const cl of (c.claims || [])) {
    total++;
    const out = claimSources(cl);
    if (out === 'No attributed source on file') falseAbsence++;
    if (!out) empty++;
    if (samples.length < 4) samples.push(c.id + ': ' + out);
  }
}
console.log('claims rendered      :', total);
console.log('false "no source"    :', falseAbsence, falseAbsence === 0 ? 'OK' : 'REGRESSION');
console.log('empty output         :', empty, empty === 0 ? 'OK' : 'BAD');
console.log('\nsamples:');
samples.forEach(s => console.log('  ' + s));

// Legacy shape must still work, so a pre-migration record never renders as sourceless.
console.log('\nlegacy string shape  :', claimSources({ source: 'PolitiFact, April 28 2026' }));
console.log('genuinely empty      :', claimSources({}));
console.log('with url             :', claimSources({ sources: [{ name: 'CNN', url: 'https://x.test', date: '2026-04-21' }] }));
