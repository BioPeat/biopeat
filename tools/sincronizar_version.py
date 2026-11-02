# Mantiene CONTEXTO_BIOPEAT.md al día con index.html. Lo ejecuta GitHub solo en cada subida: no hace falta tocarlo.
#  - «Versión actual» y «revisión de datos» = APP_VERSION y APP_REVISION.
#  - «## 6. Qué hace la app (vNN)» con la versión actual.
#  - «## 10. Historial»: las 8 últimas líneas del «Registro de cambios» de index.html (así lo que haga Gemini o Claude queda apuntado solo).
import re, pathlib
idx = pathlib.Path('index.html').read_text(encoding='utf-8')
ctx_p = pathlib.Path('CONTEXTO_BIOPEAT.md')
ctx = ctx_p.read_text(encoding='utf-8')
v = re.search(r"APP_VERSION\s*=\s*.(v\d+)", idx)
r = re.search(r"APP_REVISION\s*=\s*(\d+)", idx)
if not v:
    print('No encuentro APP_VERSION en index.html'); raise SystemExit(0)
new = re.sub(r"(\*\*Versión actual:\s*)v\d+(\*\*)", lambda m: m.group(1) + v.group(1) + m.group(2), ctx, count=1)
if r:
    new = re.sub(r"(revisión de datos\s*)\d+", lambda m: m.group(1) + r.group(1), new, count=1)
new = re.sub(r"^(#+\s*6\. Qué hace la app \()v\d+(\))", lambda m: m.group(1) + v.group(1) + m.group(2), new, count=1, flags=re.M)
# Historial a partir del registro de cambios del script
a = idx.find('Registro de cambios')
log = []
if a >= 0:
    block = idx[a:idx.find('*/', a)]
    for line in block.split('\n')[1:]:
        m = re.match(r'\s*(v\d+(?:-v\d+)?)\s*·\s*([^·]+?)\s*·\s*(.+)$', line)
        if m:
            log.append(f'- **{m.group(1)} · {m.group(2)}:** {m.group(3).strip()}')
        if len(log) == 8:
            break
if log:
    pat = re.compile(r'(^#+\s*10\. Historial[^\n]*\n)(.*?)(?=^#+\s*11\.)', re.M | re.S)
    new = pat.sub(lambda m: m.group(1) + '\n'.join(log) + '\n\n', new, count=1)
if new != ctx:
    ctx_p.write_text(new, encoding='utf-8')
    print('CONTEXTO actualizado a', v.group(1), '(revisión', (r.group(1) if r else '?') + ')')
else:
    print('CONTEXTO ya estaba en', v.group(1))
