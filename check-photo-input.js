const fs = require('fs');
let content = fs.readFileSync('index.html', 'utf8');
const p = content.indexOf('function resetPhoto()');
console.log(content.substring(p-100, p + 500));
