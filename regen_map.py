import re

with open('extracted.js', 'r') as f:
    js_content = f.readlines()

functions = []
for i, line in enumerate(js_content):
    match = re.match(r'^(?:async )?function\s+([a-zA-Z0-9_]+)\(', line)
    if match:
        functions.append(f"- L{i+1} `{match.group(1)}()`")
    else:
        match2 = re.match(r'^(?:export )?(?:const|let|var)\s+([a-zA-Z0-9_]+)\s*=\s*(?:async )?(?:\([^)]*\)|[a-zA-Z0-9_]+)\s*=>', line)
        if match2:
            functions.append(f"- L{i+1} `{match2.group(1)}()`")
        else:
            match3 = re.match(r'^(?:const|let|var)\s+([A-Z0-9_]+)\s*=', line)
            if match3:
                functions.append(f"- L{i+1} constante `{match3.group(1)}`")

with open('MAPA_DEL_CODIGO.md', 'r') as f:
    map_content = f.read()

# Replace the functions list in MAPA_DEL_CODIGO.md
start_idx = map_content.find('## 3. Listado de funciones')
if start_idx != -1:
    end_idx = map_content.find('## 4. Notas arquitectónicas', start_idx)
    if end_idx != -1:
        new_list = "## 3. Listado de funciones y constantes por línea\n" + "\n".join(functions) + "\n\n"
        map_content = map_content[:start_idx] + new_list + map_content[end_idx:]

with open('MAPA_DEL_CODIGO.md', 'w') as f:
    f.write(map_content)
