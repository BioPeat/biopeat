const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');

const regex = /<div class="quick-chips"[^>]+>.*?<\/div>/;

if (regex.test(html)) {
  html = html.replace(regex, `
<div class="quick-chips" style="overflow-x:auto;white-space:nowrap;padding:8px 12px;background:#1e293b;scrollbar-width:none;-webkit-overflow-scrolling:touch;">
  <button class="filter-pill" style="margin-right:6px;" onclick="document.getElementById('balance-card').scrollIntoView({behavior:'smooth'})">⚖️ Equilibrio Peat</button>
  <button class="filter-pill" style="margin-right:6px;" onclick="document.getElementById('micros-section').scrollIntoView({behavior:'smooth'})">🧬 25 Micros</button>
  <button class="filter-pill" style="margin-right:6px;" onclick="document.getElementById('plan-grid').scrollIntoView({behavior:'smooth'})">💊 Tu Pauta</button>
  <button class="filter-pill" style="margin-right:6px;" onclick="document.getElementById('btn-calendar').click(); setTimeout(()=>document.getElementById('view-calendar').scrollIntoView({behavior:'smooth'}),100)">📅 Calendario</button>
  <button class="filter-pill" onclick="document.getElementById('btn-settings').click(); setTimeout(()=>document.getElementById('ai-notes').scrollIntoView({behavior:'smooth'}),100)">🤖 Notas IA</button>
</div>`.trim().replace(/\n/g, ''));
  fs.writeFileSync('index.html', html);
  console.log('Fixed chips formatting.');
} else {
  console.log('Chips container not found.');
}
