const fs = require('fs');
let content = fs.readFileSync('CONTEXTO_BIOPEAT.md', 'utf8');

const titleStr = '**v29:** Botón de foto automático, "Tus rápidos" y Modo Resumen compactados, y simulador en vivo de ratios.';
content = content.replace(titleStr, titleStr + '\n**v30:** Perfil Prometabólico, macros split, hierro límite estricto, Apply AI Config.');

fs.writeFileSync('CONTEXTO_BIOPEAT.md', content);
console.log("CONTEXTO_BIOPEAT.md updated v30");
