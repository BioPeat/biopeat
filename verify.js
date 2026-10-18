const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');
const idRatio = content.indexOf('function renderRatios()');
console.log(content.substring(idRatio - 50, idRatio + 500));
