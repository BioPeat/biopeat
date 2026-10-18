const fs = require('fs');
let content = fs.readFileSync('index.html', 'utf8');
const s = content.indexOf('function analyzeDay');
console.log(content.substring(s+2000, s + 3500));
