import sys
import re

def update_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # insert the new changelog entry at the top of the changelog list
    new_entry = "   v30 · Jules · Implementado el guardado de metas global/split, control total IA, Perfil Prometabólico Peat/Dinkov, y auto-completar del día anterior.\n"
    content = content.replace(" Registro de cambios (versión · autor · resumen):\n", " Registro de cambios (versión · autor · resumen):\n" + new_entry)

    with open(filename, 'w') as f:
        f.write(content)

update_file("index.html")
