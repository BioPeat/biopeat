const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');

const chipsIdx = content.indexOf('.bp-chips {');
console.log(content.substring(chipsIdx, chipsIdx + 200));
