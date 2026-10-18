const fs = require('fs');

const content = fs.readFileSync('index.html', 'utf8');

console.log("----- #view-add -----");
const viewAddIdx = content.indexOf('id="view-add"');
console.log("Starts at: " + content.substring(viewAddIdx-50, viewAddIdx+150));
