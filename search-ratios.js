const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');
const searchString = "function renderRatios()";
const idx = content.indexOf(searchString);
console.log(content.substring(idx-100, idx+2000));
