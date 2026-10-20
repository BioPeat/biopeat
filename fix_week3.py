import re

with open('index.html', 'r') as f:
    content = f.read()

# Lines to fix:
# 6884: goalsFor(r.dt).ratio.cap -> goalsFor(r.dt).cap
# 6946: goalsFor(dt).ratio.cap -> goalsFor(dt).cap, goalsFor(dt).ratio.pufa -> goalsFor(dt).pufa
# 7066: goalsFor(r.dt).ratio.cap -> goalsFor(r.dt).cap

content = content.replace("goalsFor(r.dt).ratio.cap", "goalsFor(r.dt).cap")
content = content.replace("goalsFor(dt).ratio.cap", "goalsFor(dt).cap")
content = content.replace("goalsFor(dt).ratio.pufa", "goalsFor(dt).pufa")

with open('index.html', 'w') as f:
    f.write(content)
