const fs = require('fs');

const content = fs.readFileSync('index.html', 'utf8');

const chipsCSSIdx = content.indexOf('.bp-chips {');
console.log(content.substring(chipsCSSIdx-50, chipsCSSIdx+300));
