# MAPA DEL CÓDIGO · BioPeat v33 (revisión de datos 23)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (433 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-5453; todo el JavaScript en `<script id="app">` (desde la línea 5454).

## Secciones de la página (id)

- `#view-today` — Resumen del día
- `#day-coach`
- `#balance-card`
- `#view-add` — Añadir comidas
- `#view-log` — Registro de comidas
- `#view-micros` — Micronutrientes
- `#view-supplements` — Suplementos y medicación
- `#weekly`
- `#exercise`
- `#view-settings` — Ajustes y copias

## JavaScript: bloques y funciones (en orden)

- L5477 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L5478 constante `AZUCAR_N`
- L5479 constante `USDA_N`
- L5485 constante `FOODS`
- L5487 constante `EXTRA`
- L5488 constante `KEYS`
- L5490 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.
- L5491 constante `MICRO_NOTE`
- L5493 constante `DAYS`
- L5494 constante `FAF`
- L5498 `number(v,min=0,max=1e6)`
- L5504 `decimalInputs(root=document)`
- L5505 `localDate(d=new Date()`
- L5506 `validDate(s)`
- L5511 `shift(s,n)`
- L5519 constante `CONTEXT`
- L5520 `defaults()`
- L5522 `bmr()`
- L5528 constante `DEF_P` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L5529 `targetFor(d)`
- L5545 `cleanNutrients(o,required=false)`
- L5557 `cleanEntry(e)`
- L5562 `cleanPlan(p)`
- L5566 `planEntry(p)`
- L5575 `seedPlan(d,whichDate)`
- L5579 `ensureDay(d=date)`
- L5586 `effectiveEntries(d=day()`
- L5587 `totals(entries=effectiveEntries()`
- L5594 `change(fn,message='Guardado')`
- L5598 `undo()`
- L5605 `toast(text,canUndo=false)`
- L5613 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L5614 `onClick(fn)`
- L5616 `attempt(fn)`
- L5620 `modal(title,body)`
- L5629 `modalRestore()`
- L5639 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L5640 `modalBack()`
- L5641 `goDate(d)`
- L5648 `renderHeader()`
- L5656 `renderRows(entries)`
- L5660 `entryValues(e)`
- L5661 `renderLog()`
- L5668 `fromFood(id,amount,meal)`
- L5674 `pantryId(name)`
- L5676 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L5682 `addEntries(entries,message='Añadido',d=date,opts={})`
- L5690 `recipe(kind)`
- L5696 `summary(entries)`
- L5700 `renderPresetInfo()`
- L5704 `stripCode(raw)`
- L5710 `parseBIO(raw,meal=$('meal-select')`
- L5716 `parseSmart(raw)`
- L5720 constante `COUNT`
- L5723 `nutrientFields(n,prefix='n_')`
- L5724 `readNutrients(form,prefix='n_')`
- L5729 `editEntry(id)`
- L5738 `editFood(id,pending=null)`
- L5743 `usageStats(days=90)`
- L5749 `renderFoods()`
- L5757 `nutrientSources(key)`
- L5764 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L5765 `suppSlot(meal)`
- L5766 `renderSupps()`
- L5776 `editPlan(id)`
- L5783 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L5798 `makePrompt(meal='Comida',note='')`
- L5802 `resetPhoto()`
- L5813 `openPhoto()`
- L5819 `shrinkPhoto(file)`
- L5822 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L5846 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L5853 `cleanFood(id,f)`
- L5857 `migrateBase(o)`
- L5876 `download(name,text,type)`
- L5885 `portable()`
- L5909 `storageStatus()`
- L5915 `idbReadWrite(mode,value)`
- L5916 `openDB()`
- L5917 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L5929 `setQuantity(id,value,msg='Cantidad actualizada')`
- L5933 `niceStep(v)`
- L5934 `stepQuantity(id,dir)`
- L5991 `renderAppInfo()`
- L6006 `init()`

### Corrección de la pauta declarada (revisión 11 de los datos)

- L6024 `planFamily(e)`
- L6036 `correctedPlan(plan)`
- L6042 `syncCorrectedDay(s,dt)`
- L6051 `upgradeTo11(s,o)`

### Navegación: una sola página; la barra inferior solo desplaza

- L6057 `setNav(v)`
- L6062 `go(v,focus)`
- L6074 `syncDatePill()`
- L6078 `animateValue(el,to,suffix='%',digits=0)`
- L6087 `tick(now)`
- L6090 `macroCard(key,name,color)`
- L6091 `renderToday()`
- L6114 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L6116 constante `HOME`
- L6118 `coachCandidates()`
- L6124 `coachIdeas(t,g,ref,meal)`
- L6137 `renderCoach()`
- L6154 `coachPrompt()`
- L6162 `nutrientDetailStandard(key)`
- L6175 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L6182 `upgradeTo12(s,o)`
- L6187 `benfotiamineTotals(entries=effectiveEntries()`
- L6196 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L6198 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L6207 `microStat(m,t=totals()`
- L6212 `metric(m)`
- L6217 `ratioGauge(o)`
- L6222 `renderRatios()`
- L6237 constante `MICRO_BANDS` — Tarjeta de un nutriente. Límites (máx): verde por debajo. Selenio: banda óptima 100-200 µg.
- L6238 `microCardHTML(m,x,personal)`
- L6248 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L6263 `renderMicroMap()`
- L6267 `nutrientDetailForDay(key)`
- L6272 `editTargetsForm()`
- L6282 `mealData()`
- L6287 `renderMealSegments()`
- L6295 `mealDetail(index)`
- L6301 `renderSimulator(type)`
- L6329 `ratioDetail(key)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L6340 constante `FAT_KEYS`
- L6341 constante `FAT_PROFILES`
- L6343 `fatData(entries=effectiveEntries()`
- L6349 `energyData(entries=effectiveEntries()`
- L6353 `segmentedBar(items,total,attr)`
- L6357 `renderMealChart()`
- L6362 `renderFat()`
- L6370 `fatDetail(key)`
- L6375 `energyDetail(key)`
- L6382 `portionCandidates(q='')`
- L6387 `openPortion()`
- L6400 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L6415 `templates()`
- L6419 `renderExtra()`
- L6430 `updateExtra(reset=true)`
- L6442 `addExtra(id,amount)`
- L6458 `shakePreview()`
- L6459 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L6474 constante `LENS`
- L6480 `lensKey(key)`
- L6481 `lensHTML(key)`
- L6485 `appendLens(key)`
- L6494 `weekDates()`

### IA en la página: conexión directa o por servidor

- L6505 constante `MEAL_WORD`
- L6506 `mealOfWord(w)`
- L6507 `mealFromText(raw,fallback)`
- L6511 `canonMeal(v,fallback)`
- L6518 `localMeal(raw,meal)`
- L6524 constante `AI_FALLBACK`
- L6525 `applyAIConfig(raw)`
- L6549 `requestAI(prompt,img,signal,modelOverride='')`
- L6562 constante `AI_PREF`
- L6563 `aiConnected()`
- L6564 `syncAI()`
- L6566 `saveAIPrefs()`
- L6567 `loadAIPrefs()`
- L6568 `openAISetup()`
- L6574 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L6581 constante `MACROS`
- L6583 `cleanGoals(o,fallback)`
- L6588 `cleanCompare(o={})`
- L6592 `snapshotDay(d,reference='saved')`
- L6597 `upgradeTo17(s,o)`
- L6602 `entriesFor(d,source=weekSource)`
- L6606 `dayRow(dt,source=weekSource)`
- L6610 `goalsFor(dt)`
- L6616 `metricValue(r,key)`
- L6621 `targetOf(dt,key)`
- L6625 `weekSummary()`
- L6629 `aggregate(key,summary=weekSummary()`
- L6633 `tone(pct,mode='macro')`
- L6640 `pctText(a)`
- L6641 `weekProgress(a,color)`
- L6642 `renderWeekTotals()`
- L6657 `renderWeekChart(s)`
- L6664 `renderWeekMicros(s)`
- L6688 `ratioAggregate(s,num,den)`
- L6692 `renderWeekRatios(s)`
- L6698 `renderWeekTable(s)`
- L6699 `weeklyDetail(key,oneDate=null)`
- L6707 `weekRatioDetail(key)`
- L6715 `dayAssessment(dt)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L6727 `calendarCell(dt)`
- L6734 `renderCalendar()`
- L6743 `renderCalendarDetail()`
- L6747 `shiftMonth(n)`
- L6753 `weekDetail(dt)`
- L6761 `openDay(dt)`
- L6802 `withDayGoals(fn)`
- L6807 `renderMicros()`
- L6808 `nutrientDetail(key)`
- L6809 `editTargets()`
- L6810 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L6821 `summaryFor(start)`
- L6825 `overviewData(start=weekDates()`
- L6830 `ringSVG(pct,color,marker)`
- L6832 `renderWeekVisual(d)` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L6841 `renderOverview()`
- L6860 `trendData()`
- L6864 `renderTrends()`
- L6877 `renderWeekly()`
- L6883 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L6884 `splitMeals(raw)`
- L6894 `localDay(raw,fallback)`
- L6901 `promptDay(raw,fallback)`
- L6902 `analyzeDay(usePhoto=false)`

### Gimnasio: importación de CSV de HEVY, sesiones y análisis IA

- L6908 `parseCsv(text)`
- L6923 `hevyDate(value,format='auto')`
- L6932 constante `MAP`
- L6933 `hevyMapping()`
- L6934 `renderMapping(parsed)`
- L6941 `optionalNum(v,min=0,max=1e7)`
- L6945 `buildHevy(parsed,map)`
- L6955 `cleanWorkout(s)`
- L6962 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L6977 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L6978 constante `GP_ALIAS`
- L6988 `gpNorm(s)`
- L6989 `gpKey(name)`
- L6993 `gpF(n,d=0)`
- L6994 `gpDate(d,opt)`
- L6995 `gpMonday(d)`
- L6996 constante `GP_GROUPS`
- L7011 constante `GP_COLORS`
- L7012 `gpGroup(name)`
- L7013 `gpWorkSets(s)`
- L7014 `gpModel()`
- L7038 `gpSessionMetrics(e,sets)`
- L7053 constante `GP_METRICS`
- L7058 `gpMetricsFor(e)`
- L7059 `gpRangeHist(e)`
- L7060 `gpPRs(model)`
- L7083 `gpStatus(e)`
- L7101 `gpNext(e)`
- L7109 `gpChart(e)`
- L7137 `gpPointDetail(e)`
- L7143 `gpRepTable(e)`
- L7150 `gpKpis(model)`
- L7158 `gpWeekly(model)`
- L7164 `gpMuscles(model)`
- L7171 `gpHeat(model)`
- L7178 `gpExList(model)`
- L7185 `gpExDetail(model)`
- L7198 `gpDayFood(dt)`
- L7199 `gpNutrition(model)`
- L7206 `gpRecentPRs(model)`
- L7210 `gpSessions(model)`
- L7216 `gpSessionModal(id)`
- L7227 `gpWeekModal(w)`
- L7228 `gpSelect(key)`
- L7229 `gpClick(e)`
- L7241 `renderGym()`
- L7261 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L7270 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L7276 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L7300 `openMoreMenu()` — Menú «Más»: secciones poco frecuentes, sin saturar la barra inferior.
- L7307 `showHelp()`
- L7311 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L7313 `markBackup()`
- L7317 `exportJSON()`
- L7322 `drawBackupReminder()`
- L7332 `applyDensity()`
- L7344 `syncDayComplete()`
- L7347 `drawMeals()` — Comidas del día de un vistazo.
- L7355 `filterLog()` — Buscador de Registro.
- L7368 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L7374 `recentFoods()`
- L7379 `quickChip(e,fav)`
- L7397 `drawQuickFoods()`
- L7426 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L7430 `toggleAddPanel(id)`
- L7442 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L7453 `pasteMessage(text,ok)`
- L7461 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L7472 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L7481 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L7499 `storableState()`

### Render único: actualiza toda la página

- L7507 `nearView(el)`
- L7509 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L7513 `render()`
- L7548 `mealByHour(h=new Date()`
- L7549 `syncMealByHour()`

### Arranque

