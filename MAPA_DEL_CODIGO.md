# MAPA DEL CÓDIGO · BioPeat v34 (revisión de datos 23)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (432 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-5546; todo el JavaScript en `<script id="app">` (desde la línea 5547).

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
- L5804 `recipe(kind)`
- L5810 `summary(entries)`
- L5814 `renderPresetInfo()`
- L5818 `stripCode(raw)`
- L5824 `parseBIO(raw,meal=$('meal-select')`
- L5830 `parseSmart(raw)`
- L5834 constante `COUNT`
- L5837 `nutrientFields(n,prefix='n_')`
- L5838 `readNutrients(form,prefix='n_')`
- L5843 `editEntry(id)`
- L5852 `editFood(id,pending=null)`
- L5857 `usageStats(days=90)`
- L5863 `renderFoods()`
- L5871 `nutrientSources(key)`
- L5878 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L5879 `suppSlot(meal)`
- L5880 `renderSupps()`
- L5895 `editPlan(id)`
- L5902 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L5917 `makePrompt(meal='Comida',note='')`
- L5921 `resetPhoto()`
- L5932 `openPhoto()`
- L5938 `shrinkPhoto(file)`
- L5941 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L5966 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L5973 `cleanFood(id,f)`
- L5977 `migrateBase(o)`
- L5996 `download(name,text,type)`
- L6005 `portable()`
- L6029 `storageStatus()`
- L6035 `idbReadWrite(mode,value)`
- L6036 `openDB()`
- L6037 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L6049 `setQuantity(id,value,msg='Cantidad actualizada')`
- L6053 `niceStep(v)`
- L6054 `stepQuantity(id,dir)`
- L6108 `renderAppInfo()`
- L6123 `init()`

### Corrección de la pauta declarada (revisión 11 de los datos)

- L6141 `planFamily(e)`
- L6153 `correctedPlan(plan)`
- L6159 `syncCorrectedDay(s,dt)`
- L6168 `upgradeTo11(s,o)`

### Navegación: una sola página; la barra inferior solo desplaza

- L6174 `setNav(v)`
- L6179 `go(v,focus)`
- L6191 `syncDatePill()`
- L6195 `animateValue(el,to,suffix='%',digits=0)`
- L6204 `tick(now)`
- L6207 `macroCard(key,name,color)`
- L6208 `renderToday()`
- L6231 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L6233 constante `HOME`
- L6235 `coachCandidates()`
- L6241 `coachIdeas(t,g,ref,meal)`
- L6254 `renderCoach()`
- L6271 `coachPrompt()`
- L6279 `nutrientDetailStandard(key)`
- L6292 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L6298 `upgradeTo12(s,o)`
- L6303 `benfotiamineTotals(entries=effectiveEntries()`
- L6312 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L6314 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L6323 `microStat(m,t=totals()`
- L6328 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L6336 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L6337 `ratioInfo(key,t=totals()`
- L6372 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L6389 `ratioBar(i,big=false)`
- L6393 `renderRatios()`
- L6398 `ratioDetail(key)`
- L6408 constante `MICRO_BANDS` — Tarjeta de un nutriente. Límites (máx): verde por debajo. Selenio: banda óptima 100-200 µg.
- L6409 `microCardHTML(m,x,personal)`
- L6419 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L6434 `renderMicroMap()`
- L6438 `nutrientDetailForDay(key)`
- L6443 `editTargetsForm()`
- L6453 `mealData()`
- L6458 `renderMealSegments()`
- L6466 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L6476 constante `FAT_KEYS`
- L6477 constante `FAT_PROFILES`
- L6479 `fatData(entries=effectiveEntries()`
- L6485 `energyData(entries=effectiveEntries()`
- L6489 `segmentedBar(items,total,attr)`
- L6493 `renderMealChart()`
- L6498 `renderFat()`
- L6506 `fatDetail(key)`
- L6511 `energyDetail(key)`
- L6518 `portionCandidates(q='')`
- L6523 `openPortion()`
- L6536 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L6551 `templates()`
- L6555 `renderExtra()`
- L6566 `updateExtra(reset=true)`
- L6578 `addExtra(id,amount)`
- L6594 `shakePreview()`
- L6595 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L6610 constante `LENS`
- L6616 `lensKey(key)`
- L6617 `lensHTML(key)`
- L6621 `appendLens(key)`
- L6630 `weekDates()`

### IA en la página: conexión directa o por servidor

- L6640 constante `MEAL_WORD`
- L6641 `mealOfWord(w)`
- L6642 `mealFromText(raw,fallback)`
- L6646 `canonMeal(v,fallback)`
- L6653 `localMeal(raw,meal)`
- L6659 constante `AI_FALLBACK`
- L6660 `applyAIConfig(raw)`
- L6684 `requestAI(prompt,img,signal,modelOverride='')`
- L6698 constante `AI_PREF`
- L6699 `aiConnected()`
- L6700 `syncAI()`
- L6702 `saveAIPrefs()`
- L6703 `loadAIPrefs()`
- L6704 `openAISetup()`
- L6710 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L6717 constante `MACROS`
- L6719 `cleanGoals(o,fallback)`
- L6724 `cleanCompare(o={})`
- L6728 `snapshotDay(d,reference='saved')`
- L6733 `upgradeTo17(s,o)`
- L6738 `entriesFor(d,source=weekSource)`
- L6742 `dayRow(dt,source=weekSource)`
- L6746 `goalsFor(dt)`
- L6752 `metricValue(r,key)`
- L6757 `targetOf(dt,key)`
- L6761 `weekSummary()`
- L6765 `aggregate(key,summary=weekSummary()`
- L6769 `tone(pct,mode='macro')`
- L6776 `pctText(a)`
- L6777 `weekProgress(a,color)`
- L6778 `renderWeekMicros(s)`
- L6802 `ratioAggregate(s,num,den)`
- L6806 `renderWeekRatios(s)`
- L6812 `renderWeekTable(s)`
- L6813 `weeklyDetail(key,oneDate=null)`
- L6821 `weekRatioDetail(key)`
- L6829 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L6835 `openDay(dt)`
- L6873 `withDayGoals(fn)`
- L6878 `renderMicros()`
- L6879 `nutrientDetail(key)`
- L6880 `editTargets()`
- L6881 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L6891 `summaryFor(start)`
- L6895 `ringSVG(pct,color,marker)`
- L6897 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L6901 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L6916 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L6917 `macroTone(p)`
- L6918 `dayMacroPct(dt,k)`
- L6919 `renderWeekly()`
- L6947 `weekDetail(dt,picked)`
- L6955 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L6965 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L6971 `sparkline(pts)`
- L6977 `renderCalendar()`
- L6994 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L6995 `splitMeals(raw)`
- L7005 `localDay(raw,fallback)`
- L7012 `promptDay(raw,fallback)`
- L7013 `analyzeDay(usePhoto=false)`

### Gimnasio: importación de CSV de HEVY, sesiones y análisis IA

- L7019 `parseCsv(text)`
- L7034 `hevyDate(value,format='auto')`
- L7043 constante `MAP`
- L7044 `hevyMapping()`
- L7045 `renderMapping(parsed)`
- L7052 `optionalNum(v,min=0,max=1e7)`
- L7056 `buildHevy(parsed,map)`
- L7066 `cleanWorkout(s)`
- L7073 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L7088 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L7089 constante `GP_ALIAS`
- L7099 `gpNorm(s)`
- L7100 `gpKey(name)`
- L7104 `gpF(n,d=0)`
- L7105 `gpDate(d,opt)`
- L7106 `gpMonday(d)`
- L7107 constante `GP_GROUPS`
- L7122 constante `GP_COLORS`
- L7123 `gpGroup(name)`
- L7124 `gpWorkSets(s)`
- L7125 `gpModel()`
- L7149 `gpSessionMetrics(e,sets)`
- L7164 constante `GP_METRICS`
- L7169 `gpMetricsFor(e)`
- L7170 `gpRangeHist(e)`
- L7171 `gpPRs(model)`
- L7194 `gpStatus(e)`
- L7212 `gpNext(e)`
- L7220 `gpChart(e)`
- L7248 `gpPointDetail(e)`
- L7254 `gpRepTable(e)`
- L7261 `gpKpis(model)`
- L7269 `gpWeekly(model)`
- L7275 `gpMuscles(model)`
- L7282 `gpHeat(model)`
- L7289 `gpExList(model)`
- L7296 `gpExDetail(model)`
- L7309 `gpDayFood(dt)`
- L7310 `gpNutrition(model)`
- L7317 `gpRecentPRs(model)`
- L7321 `gpSessions(model)`
- L7327 `gpSessionModal(id)`
- L7338 `gpWeekModal(w)`
- L7339 `gpSelect(key)`
- L7340 `gpClick(e)`
- L7352 `renderGym()`
- L7372 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L7381 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L7387 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L7411 `openMoreMenu()` — Menú «Más»: secciones poco frecuentes, sin saturar la barra inferior.
- L7418 `showHelp()`
- L7422 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L7424 `markBackup()`
- L7428 `exportJSON()`
- L7433 `drawBackupReminder()`
- L7443 `applyDensity()`
- L7455 `syncDayComplete()`
- L7458 `drawMeals()` — Comidas del día de un vistazo.
- L7466 `filterLog()` — Buscador de Registro.
- L7479 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L7485 `recentFoods()`
- L7490 `quickChip(e,fav)`
- L7508 `drawQuickFoods()`
- L7537 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L7541 `toggleAddPanel(id)`
- L7553 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L7564 `pasteMessage(text,ok)`
- L7572 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L7583 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L7592 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L7610 `storableState()`

### Render único: actualiza toda la página

- L7618 `nearView(el)`
- L7620 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L7624 `render()`
- L7659 `mealByHour(h=new Date()`
- L7660 `syncMealByHour()`

### Arranque

