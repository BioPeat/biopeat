# MAPA DEL CÓDIGO · BioPeat v43 (revisión de datos 23)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (453 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-5587; todo el JavaScript en `<script id="app">` (desde la línea 5588).

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

- L5621 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L5622 constante `AZUCAR_N`
- L5623 constante `USDA_N`
- L5629 constante `FOODS`
- L5631 constante `EXTRA`
- L5632 constante `KEYS`
- L5634 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.
- L5635 constante `MICRO_NOTE`
- L5637 constante `DAYS`
- L5638 constante `FAF`
- L5642 `number(v,min=0,max=1e6)`
- L5648 `decimalInputs(root=document)`
- L5649 `localDate(d=new Date()`
- L5650 `validDate(s)`
- L5655 `shift(s,n)`
- L5663 constante `CONTEXT`
- L5664 `defaults()`
- L5666 `bmr()`
- L5672 constante `DEF_P` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L5673 `targetFor(d)`
- L5689 `cleanNutrients(o,required=false)`
- L5701 `cleanEntry(e)`
- L5706 `cleanPlan(p)`
- L5710 `planEntry(p)`
- L5719 `seedPlan(d,whichDate)`
- L5723 `ensureDay(d=date)`
- L5730 `effectiveEntries(d=day()`
- L5731 `totals(entries=effectiveEntries()`
- L5738 `change(fn,message='Guardado')`
- L5742 `undo()`
- L5749 `toast(text,canUndo=false)`
- L5757 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L5758 `onClick(fn)`
- L5760 `attempt(fn)`
- L5764 `modal(title,body)`
- L5773 `modalRestore()`
- L5783 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L5784 `modalBack()`
- L5785 `goDate(d)`
- L5792 `renderHeader()`
- L5800 `renderRows(entries)`
- L5804 `entryValues(e)`
- L5805 `renderLog()`
- L5812 `fromFood(id,amount,meal)`
- L5818 `pantryId(name)`
- L5820 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L5826 `addEntries(entries,message='Añadido',d=date,opts={})`
- L5835 `recipe(kind)`
- L5841 `summary(entries)`
- L5845 `renderPresetInfo()`
- L5849 `stripCode(raw)`
- L5855 `parseBIO(raw,meal=$('meal-select')`
- L5861 `parseSmart(raw)`
- L5865 constante `COUNT`
- L5868 `nutrientFields(n,prefix='n_')`
- L5869 `readNutrients(form,prefix='n_')`
- L5874 `editEntry(id)`
- L5883 `editFood(id,pending=null)`
- L5888 `usageStats(days=90)`
- L5894 `renderFoods()`
- L5902 `nutrientSources(key)`
- L5909 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L5910 `suppSlot(meal)`
- L5911 `renderSupps()`
- L5926 `editPlan(id)`
- L5933 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L5952 `makePrompt(meal='Comida',note='')`
- L5957 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L5961 `photoPrompt(meal,note)`
- L5964 `resetPhoto()`
- L5975 `openPhoto()`
- L5981 `shrinkPhoto(file)`
- L5984 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6010 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6017 `cleanFood(id,f)`
- L6021 `migrateBase(o)`
- L6040 `download(name,text,type)`
- L6049 `portable()`
- L6073 `syncAppIcons()`
- L6081 `downloadAppIcons()`
- L6118 `storageStatus()`
- L6124 `idbReadWrite(mode,value)`
- L6125 `openDB()`
- L6126 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L6138 `setQuantity(id,value,msg='Cantidad actualizada')`
- L6142 `niceStep(v)`
- L6143 `stepQuantity(id,dir)`
- L6197 `renderAppInfo()`
- L6212 `init()`

### Corrección de la pauta declarada (revisión 11 de los datos)

- L6230 `planFamily(e)`
- L6242 `correctedPlan(plan)`
- L6248 `syncCorrectedDay(s,dt)`
- L6257 `upgradeTo11(s,o)`

### Navegación: una sola página; la barra inferior solo desplaza

- L6263 `setNav(v)`
- L6268 `go(v,focus)`
- L6280 `syncDatePill()`
- L6284 `animateValue(el,to,suffix='%',digits=0)`
- L6293 `tick(now)`
- L6296 `macroCard(key,name,color)`
- L6297 `renderToday()`
- L6320 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L6322 constante `HOME`
- L6324 `coachCandidates()`
- L6330 `coachIdeas(t,g,ref,meal)`
- L6343 `renderCoach()`
- L6360 `coachPrompt()`
- L6368 `nutrientDetailStandard(key)`
- L6381 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L6387 `upgradeTo12(s,o)`
- L6392 `benfotiamineTotals(entries=effectiveEntries()`
- L6401 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L6403 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L6412 `microStat(m,t=totals()`
- L6417 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L6425 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L6426 `ratioInfo(key,t=totals()`
- L6461 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L6478 `ratioBar(i,big=false)`
- L6482 `renderRatios()`
- L6487 `ratioDetail(key)`
- L6497 constante `MICRO_BANDS` — Tarjeta de un nutriente. Límites (máx): verde por debajo. Selenio: banda óptima 100-200 µg.
- L6498 `microCardHTML(m,x,personal)`
- L6508 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L6523 `renderMicroMap()`
- L6527 `nutrientDetailForDay(key)`
- L6532 `editTargetsForm()`
- L6542 `mealData()`
- L6547 `renderMealSegments()`
- L6555 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L6565 constante `FAT_KEYS`
- L6566 constante `FAT_PROFILES`
- L6568 `fatData(entries=effectiveEntries()`
- L6574 `energyData(entries=effectiveEntries()`
- L6578 `segmentedBar(items,total,attr)`
- L6582 `renderMealChart()`
- L6587 `renderFat()`
- L6595 `fatDetail(key)`
- L6600 `energyDetail(key)`
- L6607 `portionCandidates(q='')`
- L6612 `openPortion()`
- L6625 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L6640 `templates()`
- L6644 `renderExtra()`
- L6655 `updateExtra(reset=true)`
- L6667 `addExtra(id,amount)`
- L6683 `shakePreview()`
- L6684 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L6699 constante `LENS`
- L6705 `lensKey(key)`
- L6706 `lensHTML(key)`
- L6710 `appendLens(key)`
- L6719 `weekDates()`

### IA en la página: conexión directa o por servidor

- L6729 constante `MEAL_WORD`
- L6730 `mealOfWord(w)`
- L6731 `mealFromText(raw,fallback)`
- L6735 `canonMeal(v,fallback)`
- L6742 `localMeal(raw,meal)`
- L6748 constante `AI_FALLBACK`
- L6749 `applyAIConfig(raw)`
- L6775 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L6776 `callGemini(model,key,prompt,img,signal,think=true)`
- L6793 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L6825 constante `AI_PREF`
- L6826 `aiConnected()`
- L6827 `syncAI()`
- L6829 `saveAIPrefs()`
- L6830 `loadAIPrefs()`
- L6831 `openAISetup()`
- L6837 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L6844 constante `MACROS`
- L6846 `cleanGoals(o,fallback)`
- L6851 `cleanCompare(o={})`
- L6855 `snapshotDay(d,reference='saved')`
- L6860 `upgradeTo17(s,o)`
- L6865 `entriesFor(d,source=weekSource)`
- L6869 `dayRow(dt,source=weekSource)`
- L6873 `goalsFor(dt)`
- L6879 `metricValue(r,key)`
- L6884 `targetOf(dt,key)`
- L6888 `weekSummary()`
- L6892 `aggregate(key,summary=weekSummary()`
- L6896 `tone(pct,mode='macro')`
- L6903 `pctText(a)`
- L6904 `weekProgress(a,color)`
- L6905 `renderWeekMicros(s)`
- L6929 `ratioAggregate(s,num,den)`
- L6933 `renderWeekRatios(s)`
- L6939 `renderWeekTable(s)`
- L6940 `weeklyDetail(key,oneDate=null)`
- L6948 `weekRatioDetail(key)`
- L6956 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L6962 `openDay(dt)`
- L7000 `withDayGoals(fn)`
- L7005 `renderMicros()`
- L7006 `nutrientDetail(key)`
- L7007 `editTargets()`
- L7008 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L7018 `summaryFor(start)`
- L7022 `ringSVG(pct,color,marker)`
- L7024 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L7028 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L7043 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L7044 `macroTone(p)`
- L7045 `dayMacroPct(dt,k)`
- L7046 `renderWeekly()`
- L7074 `weekDetail(dt,picked)`
- L7082 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L7092 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L7098 `sparkline(pts)`
- L7104 `renderCalendar()`
- L7121 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L7122 `splitMeals(raw)`
- L7132 `localDay(raw,fallback)`
- L7139 `promptDay(raw,fallback)`
- L7140 `analyzeDay(usePhoto=false)`

### Gimnasio: importación de CSV de HEVY, sesiones y análisis IA

- L7162 `parseCsv(text)`
- L7177 `hevyDate(value,format='auto')`
- L7186 constante `MAP`
- L7187 `hevyMapping()`
- L7188 `renderMapping(parsed)`
- L7195 `optionalNum(v,min=0,max=1e7)`
- L7199 `buildHevy(parsed,map)`
- L7209 `cleanWorkout(s)`
- L7216 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L7231 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L7232 constante `GP_ALIAS`
- L7242 `gpNorm(s)`
- L7243 `gpKey(name)`
- L7247 `gpF(n,d=0)`
- L7248 `gpDate(d,opt)`
- L7249 `gpMonday(d)`
- L7250 constante `GP_GROUPS`
- L7265 constante `GP_COLORS`
- L7266 `gpGroup(name)`
- L7267 `gpWorkSets(s)`
- L7268 `gpModel()`
- L7292 `gpSessionMetrics(e,sets)`
- L7307 constante `GP_METRICS`
- L7312 `gpMetricsFor(e)`
- L7313 `gpRangeHist(e)`
- L7314 `gpPRs(model)`
- L7337 `gpStatus(e)`
- L7355 `gpNext(e)`
- L7363 `gpChart(e)`
- L7391 `gpPointDetail(e)`
- L7397 `gpRepTable(e)`
- L7404 `gpKpis(model)`
- L7412 `gpWeekly(model)`
- L7418 `gpMuscles(model)`
- L7425 `gpHeat(model)`
- L7432 `gpExList(model)`
- L7439 `gpExDetail(model)`
- L7452 `gpDayFood(dt)`
- L7453 `gpNutrition(model)`
- L7460 `gpRecentPRs(model)`
- L7464 `gpSessions(model)`
- L7470 `gpSessionModal(id)`
- L7481 `gpWeekModal(w)`
- L7482 `gpSelect(key)`
- L7483 `gpClick(e)`
- L7495 `renderGym()`
- L7515 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L7524 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L7530 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L7554 `openMoreMenu()` — Menú «Más»: secciones poco frecuentes, sin saturar la barra inferior.
- L7561 `showHelp()`
- L7565 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L7567 `markBackup()`
- L7571 `exportJSON()`
- L7576 `drawBackupReminder()`
- L7586 `applyDensity()`
- L7598 `syncDayComplete()`
- L7601 `drawMeals()` — Comidas del día de un vistazo.
- L7609 `filterLog()` — Buscador de Registro.
- L7622 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L7628 `recentFoods()`
- L7633 `quickChip(e,fav)`
- L7651 `drawQuickFoods()`
- L7680 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L7684 `toggleAddPanel(id)`
- L7696 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L7707 `pasteMessage(text,ok)`
- L7715 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L7726 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L7735 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L7753 `storableState()`

### Render único: actualiza toda la página

- L7761 `nearView(el)`
- L7763 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L7767 `render()`
- L7802 `mealByHour(h=new Date()`
- L7803 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L7813 `dataSummary(s)`
- L7817 `confirmImport(next,name)`
- L7824 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L7830 `checkUpdate()`
- L7835 `showUpdate(v)`

### Arranque

