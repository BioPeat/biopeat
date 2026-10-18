const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf-8');
const lines = content.split('\n');

const startIndex = lines.findIndex(l => l.includes('function editTargetsForm()'));
if (startIndex !== -1) {
    console.log(lines.slice(startIndex, startIndex + 15).join('\n'));
}

const startIndex2 = lines.findIndex(l => l.includes('id="macro-target-form"'));
if (startIndex2 !== -1) {
    console.log(lines.slice(startIndex2, startIndex2 + 5).join('\n'));
}
