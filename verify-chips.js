const fs = require('fs');
let content = fs.readFileSync('index.html', 'utf8');

console.log(content.substring(content.indexOf('function drawQuickFoods'), content.indexOf('function drawQuickFoods') + 1000));
