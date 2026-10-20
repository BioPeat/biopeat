import re

with open('CONTEXTO_BIOPEAT.md', 'r') as f:
    context = f.read()

# Replace in apartado 5
context = re.sub(
    r"- \*\*PUFA:\*\* límite personal 4,5 g/día \(editable\). Es un \*\*máximo\*\*, no una meta.",
    "- **PUFA:** límite personal <= 4,0 g/día. Es un **máximo**, no una meta.",
    context
)
context = re.sub(
    r"- \*\*Hierro:\*\* es un \*\*límite\*\* \(mejor por debajo\).",
    "- **Hierro:** es un **límite** (mejor por debajo, <= 14 mg).",
    context
)
with open('CONTEXTO_BIOPEAT.md', 'w') as f:
    f.write(context)
