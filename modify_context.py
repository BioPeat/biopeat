import re
with open('index.html', 'r') as f:
    content = f.read()

contextOrig = """const CONTEXT="Diego · 77,5 kg · 185 cm · 23 años. Full body lunes, miércoles y sábado; partido el domingo. Objetivo: acercarme a las ideas de Ray Peat y apoyar mi metabolismo, sin atribuir cifras no verificadas.\\nPauta corregida: vitamina E 200 UI y benfotiamina 250 mg en la comida; glicina 5 g en la comida y 5 g antes de dormir; bisglicinato HSN 2 g de polvo en la comida y 2 g antes de dormir. Aspirina: toda la cantidad diaria declarada (500 mg en lunes/miércoles/sábado/domingo; 250 mg martes/jueves/viernes) en la merienda con el batido y la K2. El resto de la pauta se conserva.\\nNo se añaden comidas ficticias. Las tomas automáticas son previstas, no confirmadas. La glicina libre no se suma como proteína completa.";"""
contextNew = """const CONTEXT="Diego · 77,5 kg · 185 cm · 23 años. Full body lunes, miércoles y sábado; partido el domingo. Objetivo: acercarme a las ideas de Ray Peat y apoyar mi metabolismo, sin atribuir cifras no verificadas. Proteína moderada 115-130 g para priorizar glucógeno y conversión T4->T3, grasa 60-65 g con PUFA <= 4 g, C:P 3-4:1, Ca:P >= 1.20, hierro límite <= 14 mg, selenio óptimo 100-200 ug/d, equilibrio A:D y Zn:Cu.\\nPauta corregida: vitamina E 200 UI y benfotiamina 250 mg en la comida; glicina 5 g en la comida y 5 g antes de dormir; bisglicinato HSN 2 g de polvo en la comida y 2 g antes de dormir. Aspirina: toda la cantidad diaria declarada (500 mg en lunes/miércoles/sábado/domingo; 250 mg martes/jueves/viernes) en la merienda con el batido y la K2. El resto de la pauta se conserva.\\nNo se añaden comidas ficticias. Las tomas automáticas son previstas, no confirmadas. La glicina libre no se suma como proteína completa.";"""

content = content.replace(contextOrig, contextNew)
with open('index.html', 'w') as f:
    f.write(content)
