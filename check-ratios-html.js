const fs = require('fs');
let content = fs.readFileSync('index.html', 'utf8');

const s = content.indexOf('function ratioGauge(o)');
console.log(content.substring(s, s + 1000));
