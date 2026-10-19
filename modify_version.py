import re
with open('index.html', 'r') as f:
    content = f.read()
content = re.sub(r"const APP_VERSION='v30';", "const APP_VERSION='v31';", content)
with open('index.html', 'w') as f:
    f.write(content)
