const fs = require('fs');
let html = fs.readFileSync('index.html', 'utf8');
console.log(html.includes('quick-chips') ? 'Has quick-chips' : 'No quick-chips');
