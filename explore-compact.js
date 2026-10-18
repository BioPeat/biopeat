const fs = require('fs');
let content = fs.readFileSync('index.html', 'utf8');

const s = content.indexOf('body.bp-compact .section-note:not([role=status])');
console.log(content.substring(s, s + 1000));
