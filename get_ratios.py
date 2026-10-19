import re
with open('index.html', 'r') as f:
    content = f.read()

match = re.search(r'function renderRatios\(\)\{.*?\n\}', content, re.DOTALL)
if match:
    print(match.group(0))
else:
    print("Not found")
