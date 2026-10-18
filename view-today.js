const fs = require('fs');
let content = fs.readFileSync('index.html', 'utf8');

const s = content.indexOf('id="view-today"');
console.log(content.substring(s, s + 1000));
