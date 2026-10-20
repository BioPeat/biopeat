# MAPA DEL CÓDIGO · BioPeat v34 (revisión de datos 23)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (431 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-5546; todo el JavaScript en `<script id="app">` (desde la línea 5547).

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

- L5571 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L5572 constante `AZUCAR_N`
- L5573 constante `USDA_N`
- L5579 constante `FOODS`
- L5581 constante `EXTRA`
- L5582 constante `KEYS`
- L5584 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.
- L5585 constante `MICRO_NOTE`
- L5587 constante `DAYS`
- L5588 constante `FAF`
- L5592 `number(v,min=0,max=1e6)`
- L5598 `decimalInputs(root=document)`
- L5599 `localDate(d=new Date()`
- L5600 `validDate(s)`
- L5605 `shift(s,n)`
- L5613 constante `CONTEXT`
- L5614 `defaults()`
- L5616 `bmr()`
- L5622 constante `DEF_P` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L5623 `targetFor(d)`
- L5639 `cleanNutrients(o,required=false)`
- L5651 `cleanEntry(e)`
- L5656 `cleanPlan(p)`
- L5660 `planEntry(p)`
- L5669 `seedPlan(d,whichDate)`
- L5673 `ensureDay(d=date)`
- L5680 `effectiveEntries(d=day()`
- L5681 `totals(entries=effectiveEntries()`
- L5688 `change(fn,message='Guardado')`
- L5692 `undo()`
- L5699 `toast(text,canUndo=false)`
- L5707 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L5708 `onClick(fn)`
- L5710 `attempt(fn)`
- L5714 `modal(title,body)`
- L5723 `modalRestore()`
- L5733 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L5734 `modalBack()`
- L5735 `goDate(d)`
- L5742 `renderHeader()`
- L5750 `renderRows(entries)`
- L5754 `entryValues(e)`
- L5755 `renderLog()`
- L5762 `fromFood(id,amount,meal)`
- L5768 `pantryId(name)`
- L5770 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L5776 `addEntries(entries,message='Añadido',d=date,opts={})`
- L5784 `recipe(kind)`
- L5790 `summary(entries)`
- L5794 `renderPresetInfo()`
- L5798 `stripCode(raw)`
- L5804 `parseBIO(raw,meal=$('meal-select')`
- L5810 `parseSmart(raw)`
- L5814 constante `COUNT`
- L5817 `nutrientFields(n,prefix='n_')`
- L5818 `readNutrients(form,prefix='n_')`
- L5823 `editEntry(id)`
- L5832 `editFood(id,pending=null)`
- L5837 `usageStats(days=90)`
- L5843 `renderFoods()`
- L5851 `nutrientSources(key)`
- L5858 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L5859 `suppSlot(meal)`
- L5860 `renderSupps()`
- L5875 `editPlan(id)`
- L5882 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L5897 `makePrompt(meal='Comida',note='')`
- L5901 `resetPhoto()`
- L5912 `openPhoto()`
- L5918 `shrinkPhoto(file)`
- L5921 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L5945 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L5952 `cleanFood(id,f)`
- L5956 `migrateBase(o)`
- L5975 `download(name,text,type)`
- L5984 `portable()`
- L6008 `storageStatus()`
- L6014 `idbReadWrite(mode,value)`
- L6015 `openDB()`
- L6016 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L6028 `setQuantity(id,value,msg='Cantidad actualizada')`
- L6032 `niceStep(v)`
- L6033 `stepQuantity(id,dir)`
- L6087 `renderAppInfo()`
- L6102 `init()`

### Corrección de la pauta declarada (revisión 11 de los datos)

- L6120 `planFamily(e)`
- L6132 `correctedPlan(plan)`
- L6138 `syncCorrectedDay(s,dt)`
- L6147 `upgradeTo11(s,o)`

### Navegación: una sola página; la barra inferior solo desplaza

- L6153 `setNav(v)`
- L6158 `go(v,focus)`
- L6170 `syncDatePill()`
- L6174 `animateValue(el,to,suffix='%',digits=0)`
- L6183 `tick(now)`
- L6186 `macroCard(key,name,color)`
- L6187 `renderToday()`
- L6210 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L6212 constante `HOME`
- L6214 `coachCandidates()`
- L6220 `coachIdeas(t,g,ref,meal)`
- L6233 `renderCoach()`
- L6250 `coachPrompt()`
- L6258 `nutrientDetailStandard(key)`
- L6271 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L6277 `upgradeTo12(s,o)`
- L6282 `benfotiamineTotals(entries=effectiveEntries()`
- L6291 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L6293 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L6302 `microStat(m,t=totals()`
- L6307 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L6315 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L6316 `ratioInfo(key,t=totals()`
- L6351 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L6368 `ratioBar(i,big=false)`
- L6372 `renderRatios()`
- L6377 `ratioDetail(key)`
- L6387 constante `MICRO_BANDS` — Tarjeta de un nutriente. Límites (máx): verde por debajo. Selenio: banda óptima 100-200 µg.
- L6388 `microCardHTML(m,x,personal)`
- L6398 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L6413 `renderMicroMap()`
- L6417 `nutrientDetailForDay(key)`
- L6422 `editTargetsForm()`
- L6432 `mealData()`
- L6437 `renderMealSegments()`
- L6445 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L6455 constante `FAT_KEYS`
- L6456 constante `FAT_PROFILES`
- L6458 `fatData(entries=effectiveEntries()`
- L6464 `energyData(entries=effectiveEntries()`
- L6468 `segmentedBar(items,total,attr)`
- L6472 `renderMealChart()`
- L6477 `renderFat()`
- L6485 `fatDetail(key)`
- L6490 `energyDetail(key)`
- L6497 `portionCandidates(q='')`
- L6502 `openPortion()`
- L6515 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L6530 `templates()`
- L6534 `renderExtra()`
- L6545 `updateExtra(reset=true)`
- L6557 `addExtra(id,amount)`
- L6573 `shakePreview()`
- L6574 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L6589 constante `LENS`
- L6595 `lensKey(key)`
- L6596 `lensHTML(key)`
- L6600 `appendLens(key)`
- L6609 `weekDates()`

### IA en la página: conexión directa o por servidor

- L6619 constante `MEAL_WORD`
- L6620 `mealOfWord(w)`
- L6621 `mealFromText(raw,fallback)`
- L6625 `canonMeal(v,fallback)`
- L6632 `localMeal(raw,meal)`
- L6638 constante `AI_FALLBACK`
- L6639 `applyAIConfig(raw)`
- L6663 `requestAI(prompt,img,signal,modelOverride='')`
- L6676 constante `AI_PREF`
- L6677 `aiConnected()`
- L6678 `syncAI()`
- L6680 `saveAIPrefs()`
- L6681 `loadAIPrefs()`
- L6682 `openAISetup()`
- L6688 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L6695 constante `MACROS`
- L6697 `cleanGoals(o,fallback)`
- L6702 `cleanCompare(o={})`
- L6706 `snapshotDay(d,reference='saved')`
- L6711 `upgradeTo17(s,o)`
- L6716 `entriesFor(d,source=weekSource)`
- L6720 `dayRow(dt,source=weekSource)`
- L6724 `goalsFor(dt)`
- L6730 `metricValue(r,key)`
- L6735 `targetOf(dt,key)`
- L6739 `weekSummary()`
- L6743 `aggregate(key,summary=weekSummary()`
- L6747 `tone(pct,mode='macro')`
- L6754 `pctText(a)`
- L6755 `weekProgress(a,color)`
- L6756 `renderWeekMicros(s)`
- L6780 `ratioAggregate(s,num,den)`
- L6784 `renderWeekRatios(s)`
- L6790 `renderWeekTable(s)`
- L6791 `weeklyDetail(key,oneDate=null)`
- L6799 `weekRatioDetail(key)`
- L6807 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L6813 `openDay(dt)`
- L6851 `withDayGoals(fn)`
- L6856 `renderMicros()`
- L6857 `nutrientDetail(key)`
- L6858 `editTargets()`
- L6859 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L6869 `summaryFor(start)`
- L6873 `ringSVG(pct,color,marker)`
- L6875 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L6879 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L6894 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L6895 `macroTone(p)`
- L6896 `dayMacroPct(dt,k)`
- L6897 `renderWeekly()`
- L6925 `weekDetail(dt,picked)`
- L6933 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L6943 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L6949 `sparkline(pts)`
- L6955 `renderCalendar()`
- L6972 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L6973 `splitMeals(raw)`
- L6983 `localDay(raw,fallback)`
- L6990 `promptDay(raw,fallback)`
- L6991 `analyzeDay(usePhoto=false)`

### Gimnasio: importación de CSV de HEVY, sesiones y análisis IA

- L6997 `parseCsv(text)`
- L7012 `hevyDate(value,format='auto')`
- L7021 constante `MAP`
- L7022 `hevyMapping()`
- L7023 `renderMapping(parsed)`
- L7030 `optionalNum(v,min=0,max=1e7)`
- L7034 `buildHevy(parsed,map)`
- L7044 `cleanWorkout(s)`
- L7051 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L7066 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L7067 constante `GP_ALIAS`
- L7077 `gpNorm(s)`
- L7078 `gpKey(name)`
- L7082 `gpF(n,d=0)`
- L7083 `gpDate(d,opt)`
- L7084 `gpMonday(d)`
- L7085 constante `GP_GROUPS`
- L7100 constante `GP_COLORS`
- L7101 `gpGroup(name)`
- L7102 `gpWorkSets(s)`
- L7103 `gpModel()`
- L7127 `gpSessionMetrics(e,sets)`
- L7142 constante `GP_METRICS`
- L7147 `gpMetricsFor(e)`
- L7148 `gpRangeHist(e)`
- L7149 `gpPRs(model)`
- L7172 `gpStatus(e)`
- L7190 `gpNext(e)`
- L7198 `gpChart(e)`
- L7226 `gpPointDetail(e)`
- L7232 `gpRepTable(e)`
- L7239 `gpKpis(model)`
- L7247 `gpWeekly(model)`
- L7253 `gpMuscles(model)`
- L7260 `gpHeat(model)`
- L7267 `gpExList(model)`
- L7274 `gpExDetail(model)`
- L7287 `gpDayFood(dt)`
- L7288 `gpNutrition(model)`
- L7295 `gpRecentPRs(model)`
- L7299 `gpSessions(model)`
- L7305 `gpSessionModal(id)`
- L7316 `gpWeekModal(w)`
- L7317 `gpSelect(key)`
- L7318 `gpClick(e)`
- L7330 `renderGym()`
- L7350 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L7359 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L7365 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L7389 `openMoreMenu()` — Menú «Más»: secciones poco frecuentes, sin saturar la barra inferior.
- L7396 `showHelp()`
- L7400 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L7402 `markBackup()`
- L7406 `exportJSON()`
- L7411 `drawBackupReminder()`
- L7421 `applyDensity()`
- L7433 `syncDayComplete()`
- L7436 `drawMeals()` — Comidas del día de un vistazo.
- L7444 `filterLog()` — Buscador de Registro.
- L7457 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L7463 `recentFoods()`
- L7468 `quickChip(e,fav)`
- L7486 `drawQuickFoods()`
- L7515 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L7519 `toggleAddPanel(id)`
- L7531 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L7542 `pasteMessage(text,ok)`
- L7550 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L7561 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L7570 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L7588 `storableState()`

### Render único: actualiza toda la página

- L7596 `nearView(el)`
- L7598 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L7602 `render()`
- L7637 `mealByHour(h=new Date()`
- L7638 `syncMealByHour()`

### Arranque

