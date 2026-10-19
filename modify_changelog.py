import re
with open('index.html', 'r') as f:
    content = f.read()

changelogOrig = """ Registro de cambios (versión · autor · resumen):
   v30 · Jules · Implementado el guardado de metas global/split, control total IA, Perfil Prometabólico Peat/Dinkov, y auto-completar del día anterior."""

changelogNew = """ Registro de cambios (versión · autor · resumen):
   v31 · Jules · Actualización total Perfil Prometabólico Peat/Dinkov en vivo, Epley 1RM, nuevo Calendario y Accesos rápidos.
   v30 · Jules · Implementado el guardado de metas global/split, control total IA, Perfil Prometabólico Peat/Dinkov, y auto-completar del día anterior."""

content = content.replace(changelogOrig, changelogNew)
with open('index.html', 'w') as f:
    f.write(content)
