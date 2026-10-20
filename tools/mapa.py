#!/usr/bin/env python3
"""Regenera MAPA_DEL_CODIGO.md a partir de index.html (no editar el mapa a mano).
Uso: python tools/mapa.py
"""
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
html = (ROOT / 'index.html').read_text(encoding='utf-8')
lines = html.split('\n')
ver = re.search(r"APP_VERSION='(v\d+)'", html).group(1)
rev = re.search(r"APP_REVISION=(\d+)", html).group(1)
start = next(i for i, l in enumerate(lines) if '<script id="app">' in l)
out = [f'# MAPA DEL CÓDIGO · BioPeat {ver} (revisión de datos {rev})', '',
       'Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.', '',
       f'`index.html` ({len(html)//1024} KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-{start}; todo el JavaScript en `<script id="app">` (desde la línea {start+1}).', '',
       '## Secciones de la página (id)', '']
for m in re.finditer(r'<section([^>]*)>', html):
    a = m.group(1)
    sid = re.search(r'id="([^"]+)"', a); lab = re.search(r'aria-label="([^"]+)"', a)
    if sid: out.append(f'- `#{sid.group(1)}`' + (f' — {lab.group(1)}' if lab else ''))
out += ['', '## JavaScript: bloques y funciones (en orden)', '']
pending = ''
for i in range(start, len(lines)):
    l = lines[i].strip()
    if l.startswith('// ====='):
        out += ['', '### ' + l.strip('/ =').strip(), '']; pending = ''; continue
    if l.startswith('//'):
        pending = l[2:].strip(); continue
    m = re.match(r'(?:async\s+)?function\s+([\w$]+)\s*\(([^)]*)\)', l) or re.match(r'const\s+([A-Z][A-Z0-9_]+)\s*=', l)
    if m:
        name = m.group(1); args = m.group(2) if m.lastindex and m.lastindex >= 2 else None
        sig = f'`{name}({args})`' if args is not None else f'constante `{name}`'
        out.append(f'- L{i+1} {sig}' + (f' — {pending}' if pending else ''))
    pending = ''
(ROOT / 'MAPA_DEL_CODIGO.md').write_text('\n'.join(out) + '\n', encoding='utf-8')
print('MAPA_DEL_CODIGO.md actualizado:', len(out), 'líneas')
