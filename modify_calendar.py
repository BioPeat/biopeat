import re
with open('index.html', 'r') as f:
    content = f.read()

calendarHTMLOrig = """<section aria-label="Calendario y comparación" class="view" id="view-calendar"><div class="card"><div class="row between"><h2 class="m-0">Mapa del mes</h2><input id="calendar-month" type="month"/></div><div class="calendar-controls"><div class="row"><button class="btn btn-slate btn-small" data-calmetric="macro" aria-pressed="true">Ver cumplimiento de macros</button><button class="btn btn-slate btn-small" data-calmetric="pufa" aria-pressed="false">Ver límite de poliinsaturadas</button><button class="btn btn-slate btn-small" data-calmetric="cap" aria-pressed="false">Ver ratio calcio : fósforo</button></div></div><div class="calendar-grid" id="calendar-grid"></div><div class="calendar-legend"><span class="legend-color macro-over"></span> Exceso calorico<span class="legend-color macro-ok"></span> Macros en verde<span class="legend-color macro-under"></span> Déficit o vacío</div><p class="section-note" id="calendar-caption"></p>"""

calendarHTMLNew = """<section aria-label="Calendario y comparación" class="view" id="view-calendar"><div class="card"><div class="row between"><h2 class="m-0">Mapa del mes</h2><input id="calendar-month" type="month"/></div><div class="calendar-controls"><div class="row"><button class="btn btn-slate btn-small" data-calmetric="peat" aria-pressed="true">🔥 Semáforo Peat</button><button class="btn btn-slate btn-small" data-calmetric="macro" aria-pressed="false">🎯 Macros y Kcal</button><button class="btn btn-slate btn-small" data-calmetric="gym" aria-pressed="false">🏋️ Entreno y Pauta</button></div></div><div class="calendar-grid" id="calendar-grid"></div><div class="calendar-legend"><span class="legend-color macro-over"></span> Exceso calorico<span class="legend-color macro-ok"></span> Macros en verde<span class="legend-color macro-under"></span> Déficit o vacío</div><p class="section-note" id="calendar-caption"></p>"""
content = content.replace(calendarHTMLOrig, calendarHTMLNew)

with open('index.html', 'w') as f:
    f.write(content)
