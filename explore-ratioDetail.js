const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');

const s = content.indexOf('function ratioDetail');
console.log(content.substring(s-50, s+1500));
