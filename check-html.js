const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');
const photoPanelIdx = content.indexOf('id="photo-panel"');
console.log(content.substring(photoPanelIdx, photoPanelIdx + 1000));
