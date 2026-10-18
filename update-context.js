const fs = require('fs');
let content = fs.readFileSync('CONTEXTO_BIOPEAT.md', 'utf8');

const titleStr = 'BIOPEAT: EL REGISTRO DE DIEGO';
content = content.replace(titleStr, titleStr + '\n\n**v29:** Botón de foto automático, "Tus rápidos" y Modo Resumen compactados, y simulador en vivo de ratios.');

fs.writeFileSync('CONTEXTO_BIOPEAT.md', content);
console.log("CONTEXTO_BIOPEAT.md updated");
