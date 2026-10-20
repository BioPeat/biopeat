import re

with open('index.html', 'r') as f:
    content = f.read()

# goalsFor returns cleanTarget(t, dt). Let's see what is inside it.
# We set `t.cap = ...; t.pufa = ...` inside targetFor.
# So goalsFor(dt) returns an object with kcal, p, c, f, cap, pufa, and the 25 micros.
# But it NO LONGER has `.macro`, `.ratio`, `.micro` sub-objects.

# targetOf used to do: `return ['kcal','p','c','f'].includes(key)?g.macro[key]:key==='pufa'?g.ratio.pufa:g.micro[key];`
# We already changed it to: `return g[key];`

# Now let's fix dayAssessment.
# It used to do:
# `const capKnown=r.t.known.ca&&r.t.known.phos&&!r.t.missing.ca&&!r.t.missing.phos&&r.t.all.phos>0,puKnown=r.t.known.pufa&&!r.t.missing.pufa;`
# `let ratioKnown=Number(!!capKnown)+Number(!!puKnown),ratioMet=Number(!!capKnown&&r.t.all.ca/r.t.all.phos>=goalsFor(dt).ratio.cap)+Number(!!puKnown&&r.t.all.pufa<=goalsFor(dt).ratio.pufa);`
# It accessed `goalsFor(dt).ratio.cap` and `goalsFor(dt).ratio.pufa`. We need to change to `goalsFor(dt).cap` and `goalsFor(dt).pufa`.

dayAssessment_orig = """let ratioKnown=Number(!!capKnown)+Number(!!puKnown),ratioMet=Number(!!capKnown&&r.t.all.ca/r.t.all.phos>=goalsFor(dt).ratio.cap)+Number(!!puKnown&&r.t.all.pufa<=goalsFor(dt).ratio.pufa);"""
dayAssessment_new = """let ratioKnown=Number(!!capKnown)+Number(!!puKnown),ratioMet=Number(!!capKnown&&r.t.all.ca/r.t.all.phos>=goalsFor(dt).cap)+Number(!!puKnown&&r.t.all.pufa<=goalsFor(dt).pufa);"""

content = content.replace(dayAssessment_orig, dayAssessment_new)

# Also check if there is any other `goalsFor(dt).macro` or `.micro` left in the file.
