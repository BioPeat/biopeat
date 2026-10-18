const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');
const p = content.indexOf('function drawQuickFoods');
console.log(content.substring(p-100, p + 500));
const bpChipsIdx = content.indexOf('id="bp-chips"');
console.log("\n--- bp-chips HTML ---\n");
console.log(content.substring(bpChipsIdx-200, bpChipsIdx + 300));
