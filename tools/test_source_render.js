// Regression test for a bug that shipped in v2: sourcesHtml read s.outlet, but entity
// nodes carry `name` from ENTITY_SOURCES, so every entity's source list rendered
// "undefined" as its link text. Case records happened to use `outlet` and looked fine,
// which is why it survived. The data now uses `name` everywhere and the renderer accepts
// both, so this exercises every source-bearing record in the dataset.
const fs = require('fs');
const html = fs.readFileSync('dist/the-vanishing.html', 'utf8');
const start = html.indexOf('function sourcesHtml(p){');
const end = html.indexOf('/* --- 6.6 ANALYSIS');
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const sourcesHtml = new Function('esc', html.slice(start, end) + '; return sourcesHtml;')(esc);
const data = JSON.parse(fs.readFileSync('data/dataset.json', 'utf8'));

let checked = 0, undef = 0, unattributed = 0;
const bad = [];
function check(id, rec) {
  if (!rec.sources || !rec.sources.length) return;
  checked++;
  const out = sourcesHtml(rec);
  if (out.includes('undefined')) { undef++; bad.push(id + ' renders undefined'); }
  if (out.includes('Unattributed')) { unattributed++; bad.push(id + ' has a source with no name'); }
}
for (const c of data.cases) check('case:' + c.id, c);
for (const [k, v] of Object.entries(data.entities.ENTITY_SOURCES)) check('entity:' + k, { sources: v });
for (const [k, v] of Object.entries(data.entities.SOURCES)) check('source:' + k, { sources: v });

console.log('records with sources :', checked);
console.log('rendering "undefined":', undef, undef === 0 ? 'OK' : 'REGRESSION');
console.log('unnamed sources      :', unattributed, unattributed === 0 ? 'OK' : 'CHECK');
bad.forEach(b => console.log('   ' + b));

// The empty case must still say so rather than rendering a blank block.
const empty = sourcesHtml({ sources: [] });
console.log('\nempty case           :', empty.includes('No attributed source on file') ? 'OK' : 'BAD');
// Legacy shape must still work, so a pre-migration record never renders undefined.
const legacy = sourcesHtml({ sources: [{ outlet: 'CNN', url: 'https://x.test', date: '2026-04-21' }] });
console.log('legacy outlet shape  :', legacy.includes('CNN') ? 'OK' : 'BAD');
process.exit(undef === 0 ? 0 : 2);
