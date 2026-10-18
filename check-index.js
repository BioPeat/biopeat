const fs = require('fs');
try {
  let content = fs.readFileSync('index.html', 'utf8');
  if (content.includes('function renderSimulator(type)')) {
    console.log("renderSimulator function exists");
  } else {
    console.log("renderSimulator function missing");
  }
} catch (e) {
  console.log("Error reading index.html: " + e.message);
}
