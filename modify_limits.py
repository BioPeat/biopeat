import re
with open('index.html', 'r') as f:
    content = f.read()

limitOrig = """const DEPOSIT=new Set(['vitA','vitD','vitE','b12','b9','se','i','cu','fe']),LIMIT=new Set(['fe']);"""
limitNew = """const DEPOSIT=new Set(['vitA','vitD','vitE','b12','b9','se','i','cu','fe']),LIMIT=new Set(['fe','se','vitA','i']);"""
content = content.replace(limitOrig, limitNew)

with open('index.html', 'w') as f:
    f.write(content)
