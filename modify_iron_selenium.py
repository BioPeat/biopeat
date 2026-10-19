import re
with open('index.html', 'r') as f:
    content = f.read()

lensOrig = """const LENS={pufa:{max:v=>state.profile.pufa*1.1},ca:{min:v=>Math.max(v*.9,v-100)},phos:{max:v=>state.targets.ca||1500},fe:{max:v=>v*1.1}};"""
lensNew = """const LENS={pufa:{max:v=>state.profile.pufa*1.1},ca:{min:v=>Math.max(v*.9,v-100)},phos:{max:v=>state.targets.ca||1500},fe:{max:v=>14},se:{max:v=>250},vitA:{max:v=>3800},i:{max:v=>225}};"""
content = content.replace(lensOrig, lensNew)

limitOrig = """const LIMIT=new Set(['pufa','fe','na']);"""
limitNew = """const LIMIT=new Set(['pufa','fe','na','se','vitA','i']);"""
content = content.replace(limitOrig, limitNew)

with open('index.html', 'w') as f:
    f.write(content)
