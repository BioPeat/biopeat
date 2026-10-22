# MAPA DEL CÓDIGO · BioPeat v42 (revisión de datos 23)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (448 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-5583; todo el JavaScript en `<script id="app">` (desde la línea 5584).

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

- L5616 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L5617 constante `AZUCAR_N`
- L5618 constante `USDA_N`
- L5624 constante `FOODS`
- L5626 constante `EXTRA`
- L5627 constante `KEYS`
- L5629 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.
- L5630 constante `MICRO_NOTE`
- L5632 constante `DAYS`
- L5633 constante `FAF`
- L5637 `number(v,min=0,max=1e6)`
- L5643 `decimalInputs(root=document)`
- L5644 `localDate(d=new Date()`
- L5645 `validDate(s)`
- L5650 `shift(s,n)`
- L5658 constante `CONTEXT`
- L5659 `defaults()`
- L5661 `bmr()`
- L5667 constante `DEF_P` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L5668 `targetFor(d)`
- L5684 `cleanNutrients(o,required=false)`
- L5696 `cleanEntry(e)`
- L5701 `cleanPlan(p)`
- L5705 `planEntry(p)`
- L5714 `seedPlan(d,whichDate)`
- L5718 `ensureDay(d=date)`
- L5725 `effectiveEntries(d=day()`
- L5726 `totals(entries=effectiveEntries()`
- L5733 `change(fn,message='Guardado')`
- L5737 `undo()`
- L5744 `toast(text,canUndo=false)`
- L5752 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L5753 `onClick(fn)`
- L5755 `attempt(fn)`
- L5759 `modal(title,body)`
- L5768 `modalRestore()`
- L5778 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L5779 `modalBack()`
- L5780 `goDate(d)`
- L5787 `renderHeader()`
- L5795 `renderRows(entries)`
- L5799 `entryValues(e)`
- L5800 `renderLog()`
- L5807 `fromFood(id,amount,meal)`
- L5813 `pantryId(name)`
- L5815 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L5821 `addEntries(entries,message='Añadido',d=date,opts={})`
- L5830 `recipe(kind)`
- L5836 `summary(entries)`
- L5840 `renderPresetInfo()`
- L5844 `stripCode(raw)`
- L5850 `parseBIO(raw,meal=$('meal-select')`
- L5856 `parseSmart(raw)`
- L5860 constante `COUNT`
- L5863 `nutrientFields(n,prefix='n_')`
- L5864 `readNutrients(form,prefix='n_')`
- L5869 `editEntry(id)`
- L5878 `editFood(id,pending=null)`
- L5883 `usageStats(days=90)`
- L5889 `renderFoods()`
- L5897 `nutrientSources(key)`
- L5904 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L5905 `suppSlot(meal)`
- L5906 `renderSupps()`
- L5921 `editPlan(id)`
- L5928 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L5947 `makePrompt(meal='Comida',note='')`
- L5952 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L5956 `photoPrompt(meal,note)`
- L5959 `resetPhoto()`
- L5970 `openPhoto()`
- L5976 `shrinkPhoto(file)`
- L5979 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6005 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6012 `cleanFood(id,f)`
- L6016 `migrateBase(o)`
- L6035 `download(name,text,type)`
- L6044 `portable()`
- L6068 `syncAppIcons()`
- L6076 `downloadAppIcons()`
- L6113 `storageStatus()`
- L6119 `idbReadWrite(mode,value)`
- L6120 `openDB()`
- L6121 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L6133 `setQuantity(id,value,msg='Cantidad actualizada')`
- L6137 `niceStep(v)`
- L6138 `stepQuantity(id,dir)`
- L6192 `renderAppInfo()`
- L6207 `init()`

### Corrección de la pauta declarada (revisión 11 de los datos)

- L6225 `planFamily(e)`
- L6237 `correctedPlan(plan)`
- L6243 `syncCorrectedDay(s,dt)`
- L6252 `upgradeTo11(s,o)`

### Navegación: una sola página; la barra inferior solo desplaza

- L6258 `setNav(v)`
- L6263 `go(v,focus)`
- L6275 `syncDatePill()`
- L6279 `animateValue(el,to,suffix='%',digits=0)`
- L6288 `tick(now)`
- L6291 `macroCard(key,name,color)`
- L6292 `renderToday()`
- L6315 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L6317 constante `HOME`
- L6319 `coachCandidates()`
- L6325 `coachIdeas(t,g,ref,meal)`
- L6338 `renderCoach()`
- L6355 `coachPrompt()`
- L6363 `nutrientDetailStandard(key)`
- L6376 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L6382 `upgradeTo12(s,o)`
- L6387 `benfotiamineTotals(entries=effectiveEntries()`
- L6396 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L6398 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L6407 `microStat(m,t=totals()`
- L6412 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L6420 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L6421 `ratioInfo(key,t=totals()`
- L6456 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L6473 `ratioBar(i,big=false)`
- L6477 `renderRatios()`
- L6482 `ratioDetail(key)`
- L6492 constante `MICRO_BANDS` — Tarjeta de un nutriente. Límites (máx): verde por debajo. Selenio: banda óptima 100-200 µg.
- L6493 `microCardHTML(m,x,personal)`
- L6503 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L6518 `renderMicroMap()`
- L6522 `nutrientDetailForDay(key)`
- L6527 `editTargetsForm()`
- L6537 `mealData()`
- L6542 `renderMealSegments()`
- L6550 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L6560 constante `FAT_KEYS`
- L6561 constante `FAT_PROFILES`
- L6563 `fatData(entries=effectiveEntries()`
- L6569 `energyData(entries=effectiveEntries()`
- L6573 `segmentedBar(items,total,attr)`
- L6577 `renderMealChart()`
- L6582 `renderFat()`
- L6590 `fatDetail(key)`
- L6595 `energyDetail(key)`
- L6602 `portionCandidates(q='')`
- L6607 `openPortion()`
- L6620 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L6635 `templates()`
- L6639 `renderExtra()`
- L6650 `updateExtra(reset=true)`
- L6662 `addExtra(id,amount)`
- L6678 `shakePreview()`
- L6679 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L6694 constante `LENS`
- L6700 `lensKey(key)`
- L6701 `lensHTML(key)`
- L6705 `appendLens(key)`
- L6714 `weekDates()`

### IA en la página: conexión directa o por servidor

- L6724 constante `MEAL_WORD`
- L6725 `mealOfWord(w)`
- L6726 `mealFromText(raw,fallback)`
- L6730 `canonMeal(v,fallback)`
- L6737 `localMeal(raw,meal)`
- L6743 constante `AI_FALLBACK`
- L6744 `applyAIConfig(raw)`
- L6770 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L6771 `callGemini(model,key,prompt,img,signal,think=true)`
- L6788 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L6820 constante `AI_PREF`
- L6821 `aiConnected()`
- L6822 `syncAI()`
- L6824 `saveAIPrefs()`
- L6825 `loadAIPrefs()`
- L6826 `openAISetup()`
- L6832 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L6839 constante `MACROS`
- L6841 `cleanGoals(o,fallback)`
- L6846 `cleanCompare(o={})`
- L6850 `snapshotDay(d,reference='saved')`
- L6855 `upgradeTo17(s,o)`
- L6860 `entriesFor(d,source=weekSource)`
- L6864 `dayRow(dt,source=weekSource)`
- L6868 `goalsFor(dt)`
- L6874 `metricValue(r,key)`
- L6879 `targetOf(dt,key)`
- L6883 `weekSummary()`
- L6887 `aggregate(key,summary=weekSummary()`
- L6891 `tone(pct,mode='macro')`
- L6898 `pctText(a)`
- L6899 `weekProgress(a,color)`
- L6900 `renderWeekMicros(s)`
- L6924 `ratioAggregate(s,num,den)`
- L6928 `renderWeekRatios(s)`
- L6934 `renderWeekTable(s)`
- L6935 `weeklyDetail(key,oneDate=null)`
- L6943 `weekRatioDetail(key)`
- L6951 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L6957 `openDay(dt)`
- L6995 `withDayGoals(fn)`
- L7000 `renderMicros()`
- L7001 `nutrientDetail(key)`
- L7002 `editTargets()`
- L7003 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L7013 `summaryFor(start)`
- L7017 `ringSVG(pct,color,marker)`
- L7019 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L7023 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L7038 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L7039 `macroTone(p)`
- L7040 `dayMacroPct(dt,k)`
- L7041 `renderWeekly()`
- L7069 `weekDetail(dt,picked)`
- L7077 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L7087 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L7093 `sparkline(pts)`
- L7099 `renderCalendar()`
- L7116 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L7117 `splitMeals(raw)`
- L7127 `localDay(raw,fallback)`
- L7134 `promptDay(raw,fallback)`
- L7135 `analyzeDay(usePhoto=false)`

### Gimnasio: importación de CSV de HEVY, sesiones y análisis IA

- L7157 `parseCsv(text)`
- L7172 `hevyDate(value,format='auto')`
- L7181 constante `MAP`
- L7182 `hevyMapping()`
- L7183 `renderMapping(parsed)`
- L7190 `optionalNum(v,min=0,max=1e7)`
- L7194 `buildHevy(parsed,map)`
- L7204 `cleanWorkout(s)`
- L7211 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L7226 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L7227 constante `GP_ALIAS`
- L7237 `gpNorm(s)`
- L7238 `gpKey(name)`
- L7242 `gpF(n,d=0)`
- L7243 `gpDate(d,opt)`
- L7244 `gpMonday(d)`
- L7245 constante `GP_GROUPS`
- L7260 constante `GP_COLORS`
- L7261 `gpGroup(name)`
- L7262 `gpWorkSets(s)`
- L7263 `gpModel()`
- L7287 `gpSessionMetrics(e,sets)`
- L7302 constante `GP_METRICS`
- L7307 `gpMetricsFor(e)`
- L7308 `gpRangeHist(e)`
- L7309 `gpPRs(model)`
- L7332 `gpStatus(e)`
- L7350 `gpNext(e)`
- L7358 `gpChart(e)`
- L7386 `gpPointDetail(e)`
- L7392 `gpRepTable(e)`
- L7399 `gpKpis(model)`
- L7407 `gpWeekly(model)`
- L7413 `gpMuscles(model)`
- L7420 `gpHeat(model)`
- L7427 `gpExList(model)`
- L7434 `gpExDetail(model)`
- L7447 `gpDayFood(dt)`
- L7448 `gpNutrition(model)`
- L7455 `gpRecentPRs(model)`
- L7459 `gpSessions(model)`
- L7465 `gpSessionModal(id)`
- L7476 `gpWeekModal(w)`
- L7477 `gpSelect(key)`
- L7478 `gpClick(e)`
- L7490 `renderGym()`
- L7510 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L7519 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L7525 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L7549 `openMoreMenu()` — Menú «Más»: secciones poco frecuentes, sin saturar la barra inferior.
- L7556 `showHelp()`
- L7560 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L7562 `markBackup()`
- L7566 `exportJSON()`
- L7571 `drawBackupReminder()`
- L7581 `applyDensity()`
- L7593 `syncDayComplete()`
- L7596 `drawMeals()` — Comidas del día de un vistazo.
- L7604 `filterLog()` — Buscador de Registro.
- L7617 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L7623 `recentFoods()`
- L7628 `quickChip(e,fav)`
- L7646 `drawQuickFoods()`
- L7675 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L7679 `toggleAddPanel(id)`
- L7691 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L7702 `pasteMessage(text,ok)`
- L7710 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L7721 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L7730 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L7748 `storableState()`

### Render único: actualiza toda la página

- L7756 `nearView(el)`
- L7758 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L7762 `render()`
- L7797 `mealByHour(h=new Date()`
- L7798 `syncMealByHour()`

### Arranque

