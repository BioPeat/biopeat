const fs = require('fs');
let content = fs.readFileSync('index.html', 'utf8');

const s = content.indexOf('function ratioDetail(key)');
console.log(content.substring(s, s + 1500));
