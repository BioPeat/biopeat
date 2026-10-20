import re

with open('index.html', 'r') as f:
    content = f.read()

render_today_orig = """  if($('macro-progress-grid') && !$('macro-progress-grid').children.length)$('macro-progress-grid').innerHTML=macroCard('c','Carbohidratos','#38bdf8')+macroCard('p','Proteína','#10b981')+macroCard('f','Grasa','#fbbf24');"""
render_today_new = """  if($('macro-progress-grid') && !$('macro-progress-grid').children?.length)$('macro-progress-grid').innerHTML=macroCard('c','Carbohidratos','#38bdf8')+macroCard('p','Proteína','#10b981')+macroCard('f','Grasa','#fbbf24');"""

content = content.replace(render_today_orig, render_today_new)

with open('index.html', 'w') as f:
    f.write(content)
