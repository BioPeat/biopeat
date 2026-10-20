import re

# UPDATE CONTEXTO_BIOPEAT.md
with open('CONTEXTO_BIOPEAT.md', 'r') as f:
    context = f.read()

# "actualiza la tabla del apartado 2 (145P/75F en L/X/S/D y 130P/65F en M/J/V), el apartado 5 y 6"
context = re.sub(
    r"\| Días de entreno \(L/X/S/D\) \|.*?\n",
    "| Días de entreno (L/X/S/D) | 145 g | 75 g | 450+ g (resto de kcal para ratio C:P >= 3.0) |\n",
    context
)
context = re.sub(
    r"\| Días de descanso \(M/J/V\) \|.*?\n",
    "| Días de descanso (M/J/V)  | 130 g | 65 g | 390+ g (resto de kcal para ratio C:P >= 3.0) |\n",
    context
)
# Make sure we hit apartado 5 and 6 if needed (though the user says "el apartado 5 y 6", let's check what they say)
with open('CONTEXTO_BIOPEAT.md', 'w') as f:
    f.write(context)

# MAPA_DEL_CODIGO.md
# "regenera el listado real de funciones y líneas en MAPA_DEL_CODIGO.md"
