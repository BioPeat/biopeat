import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Buscamos todos los bloques de script que no tengan src
scripts = re.findall(r'<script\b[^>]*>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)

js_content = ""
for script in scripts:
    # Excluir el sw.js y service workers simples si es necesario, o incluirlos.
    js_content += script + "\n"

with open('extracted.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print("Extracted JS to extracted.js")
