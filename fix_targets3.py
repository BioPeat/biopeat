import re

with open('index.html', 'r') as f:
    content = f.read()

targetOf_orig = """function targetOf(dt,key){
  const g=goalsFor(dt);
  return ['kcal','p','c','f'].includes(key)?g.macro[key]:key==='pufa'?g.ratio.pufa:g.micro[key];
}"""

targetOf_new = """function targetOf(dt,key){
  const g=goalsFor(dt);
  return g[key];
}"""

content = content.replace(targetOf_orig, targetOf_new)

with open('index.html', 'w') as f:
    f.write(content)
