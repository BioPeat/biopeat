# Pone en CONTEXTO_BIOPEAT.md la misma versión y revisión de datos que tiene index.html
# (APP_VERSION y APP_REVISION). Lo ejecuta GitHub solo en cada subida. No hace falta tocarlo.
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
if new != ctx:
    ctx_p.write_text(new, encoding='utf-8')
    print('CONTEXTO actualizado a', v.group(1), '(revisión', (r.group(1) if r else '?') + ')')
else:
    print('CONTEXTO ya estaba en', v.group(1))
