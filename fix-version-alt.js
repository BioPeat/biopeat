const fs = require('fs');
let content = fs.readFileSync('index.html', 'utf8');

const vMatch = content.match(/const VERSION='v(\d+)'/);
if (vMatch) {
    const oldV = parseInt(vMatch[1]);
    const newV = oldV + 1;
    content = content.replace(`const VERSION='v${oldV}'`, `const VERSION='v${newV}'`);

    // Add changelog entry
    const changelogMark = '<h1>¿Qué hay de nuevo?</h1>';
    const newChangelog = `<h1>¿Qué hay de nuevo?</h1>\n<p><b>v${newV}</b> · Botón de foto automático, listado de comidas rápidas compactado, Modo resumen simplificado en Hoy, y simulador en vivo de ratios Ca:P y C:P.</p>`;
    content = content.replace(changelogMark, newChangelog);

    fs.writeFileSync('index.html', content);
    console.log(`Updated to v${newV} and added changelog.`);
} else {
    console.log("Could not find VERSION");
}
