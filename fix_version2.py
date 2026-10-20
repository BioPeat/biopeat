import re

with open('index.html', 'r') as f:
    content = f.read()

# Update version
new_ver = 33
match = re.search(r"const APP_VERSION='v(\d+)';", content)
if match:
    old_ver = int(match.group(1))
    new_ver = old_ver + 1
    content = content.replace(f"const APP_VERSION='v{old_ver}';", f"const APP_VERSION='v{new_ver}';")

# Append to changelog in index.html
changelog_add = f"""        <li><b>v{new_ver}:</b> Arreglos críticos (v30-v32). Perfil Prometabólico a 145P/75F y 130P/65F, verificación más estricta de errores en vistas.</li>"""

# Find changelog
content = re.sub(r'(<ul id="changelog-list">)', r'\1\n' + changelog_add, content)

with open('index.html', 'w') as f:
    f.write(content)
