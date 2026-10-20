import re

with open('index.html', 'r') as f:
    content = f.read()

renderWeekVisual_orig = """  const capRef=d.s.rows.reduce((s,r)=>s+goalsFor(r.dt).ratio.cap,0)/7"""
renderWeekVisual_new = """  const capRef=d.s.rows.reduce((s,r)=>s+(goalsFor(r.dt)?.cap ?? 1.2),0)/7"""

content = content.replace(renderWeekVisual_orig, renderWeekVisual_new)

with open('index.html', 'w') as f:
    f.write(content)
