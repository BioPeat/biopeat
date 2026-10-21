# MAPA DEL CÓDIGO · BioPeat v37 (revisión de datos 23)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (438 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-5546; todo el JavaScript en `<script id="app">` (desde la línea 5547).

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

- L5574 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L5575 constante `AZUCAR_N`
- L5576 constante `USDA_N`
- L5582 constante `FOODS`
- L5584 constante `EXTRA`
- L5585 constante `KEYS`
- L5587 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.
- L5588 constante `MICRO_NOTE`
- L5590 constante `DAYS`
- L5591 constante `FAF`
- L5595 `number(v,min=0,max=1e6)`
- L5601 `decimalInputs(root=document)`
- L5602 `localDate(d=new Date()`
- L5603 `validDate(s)`
- L5608 `shift(s,n)`
- L5616 constante `CONTEXT`
- L5617 `defaults()`
- L5619 `bmr()`
- L5625 constante `DEF_P` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L5626 `targetFor(d)`
- L5642 `cleanNutrients(o,required=false)`
- L5654 `cleanEntry(e)`
- L5659 `cleanPlan(p)`
- L5663 `planEntry(p)`
- L5672 `seedPlan(d,whichDate)`
- L5676 `ensureDay(d=date)`
- L5683 `effectiveEntries(d=day()`
- L5684 `totals(entries=effectiveEntries()`
- L5691 `change(fn,message='Guardado')`
- L5695 `undo()`
- L5702 `toast(text,canUndo=false)`
- L5710 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L5711 `onClick(fn)`
- L5713 `attempt(fn)`
- L5717 `modal(title,body)`
- L5726 `modalRestore()`
- L5736 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L5737 `modalBack()`
- L5738 `goDate(d)`
- L5745 `renderHeader()`
- L5753 `renderRows(entries)`
- L5757 `entryValues(e)`
- L5758 `renderLog()`
- L5765 `fromFood(id,amount,meal)`
- L5771 `pantryId(name)`
- L5773 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L5779 `addEntries(entries,message='Añadido',d=date,opts={})`
- L5788 `recipe(kind)`
- L5794 `summary(entries)`
- L5798 `renderPresetInfo()`
- L5802 `stripCode(raw)`
- L5808 `parseBIO(raw,meal=$('meal-select')`
- L5814 `parseSmart(raw)`
- L5818 constante `COUNT`
- L5821 `nutrientFields(n,prefix='n_')`
- L5822 `readNutrients(form,prefix='n_')`
- L5827 `editEntry(id)`
- L5836 `editFood(id,pending=null)`
- L5841 `usageStats(days=90)`
- L5847 `renderFoods()`
- L5855 `nutrientSources(key)`
- L5862 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L5863 `suppSlot(meal)`
- L5864 `renderSupps()`
- L5879 `editPlan(id)`
- L5886 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L5905 `makePrompt(meal='Comida',note='')`
- L5910 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L5914 `photoPrompt(meal,note)`
- L5917 `resetPhoto()`
- L5928 `openPhoto()`
- L5934 `shrinkPhoto(file)`
- L5937 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L5963 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L5970 `cleanFood(id,f)`
- L5974 `migrateBase(o)`
- L5993 `download(name,text,type)`
- L6002 `portable()`
- L6026 `storageStatus()`
- L6032 `idbReadWrite(mode,value)`
- L6033 `openDB()`
- L6034 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L6046 `setQuantity(id,value,msg='Cantidad actualizada')`
- L6050 `niceStep(v)`
- L6051 `stepQuantity(id,dir)`
- L6105 `renderAppInfo()`
- L6120 `init()`

### Corrección de la pauta declarada (revisión 11 de los datos)

- L6138 `planFamily(e)`
- L6150 `correctedPlan(plan)`
- L6156 `syncCorrectedDay(s,dt)`
- L6165 `upgradeTo11(s,o)`

### Navegación: una sola página; la barra inferior solo desplaza

- L6171 `setNav(v)`
- L6176 `go(v,focus)`
- L6188 `syncDatePill()`
- L6192 `animateValue(el,to,suffix='%',digits=0)`
- L6201 `tick(now)`
- L6204 `macroCard(key,name,color)`
- L6205 `renderToday()`
- L6228 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L6230 constante `HOME`
- L6232 `coachCandidates()`
- L6238 `coachIdeas(t,g,ref,meal)`
- L6251 `renderCoach()`
- L6268 `coachPrompt()`
- L6276 `nutrientDetailStandard(key)`
- L6289 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L6295 `upgradeTo12(s,o)`
- L6300 `benfotiamineTotals(entries=effectiveEntries()`
- L6309 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L6311 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L6320 `microStat(m,t=totals()`
- L6325 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L6333 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L6334 `ratioInfo(key,t=totals()`
- L6369 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L6386 `ratioBar(i,big=false)`
- L6390 `renderRatios()`
- L6395 `ratioDetail(key)`
- L6405 constante `MICRO_BANDS` — Tarjeta de un nutriente. Límites (máx): verde por debajo. Selenio: banda óptima 100-200 µg.
- L6406 `microCardHTML(m,x,personal)`
- L6416 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L6431 `renderMicroMap()`
- L6435 `nutrientDetailForDay(key)`
- L6440 `editTargetsForm()`
- L6450 `mealData()`
- L6455 `renderMealSegments()`
- L6463 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L6473 constante `FAT_KEYS`
- L6474 constante `FAT_PROFILES`
- L6476 `fatData(entries=effectiveEntries()`
- L6482 `energyData(entries=effectiveEntries()`
- L6486 `segmentedBar(items,total,attr)`
- L6490 `renderMealChart()`
- L6495 `renderFat()`
- L6503 `fatDetail(key)`
- L6508 `energyDetail(key)`
- L6515 `portionCandidates(q='')`
- L6520 `openPortion()`
- L6533 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L6548 `templates()`
- L6552 `renderExtra()`
- L6563 `updateExtra(reset=true)`
- L6575 `addExtra(id,amount)`
- L6591 `shakePreview()`
- L6592 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L6607 constante `LENS`
- L6613 `lensKey(key)`
- L6614 `lensHTML(key)`
- L6618 `appendLens(key)`
- L6627 `weekDates()`

### IA en la página: conexión directa o por servidor

- L6637 constante `MEAL_WORD`
- L6638 `mealOfWord(w)`
- L6639 `mealFromText(raw,fallback)`
- L6643 `canonMeal(v,fallback)`
- L6650 `localMeal(raw,meal)`
- L6656 constante `AI_FALLBACK`
- L6657 `applyAIConfig(raw)`
- L6683 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L6684 `callGemini(model,key,prompt,img,signal,think=true)`
- L6701 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L6733 constante `AI_PREF`
- L6734 `aiConnected()`
- L6735 `syncAI()`
- L6737 `saveAIPrefs()`
- L6738 `loadAIPrefs()`
- L6739 `openAISetup()`
- L6745 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L6752 constante `MACROS`
- L6754 `cleanGoals(o,fallback)`
- L6759 `cleanCompare(o={})`
- L6763 `snapshotDay(d,reference='saved')`
- L6768 `upgradeTo17(s,o)`
- L6773 `entriesFor(d,source=weekSource)`
- L6777 `dayRow(dt,source=weekSource)`
- L6781 `goalsFor(dt)`
- L6787 `metricValue(r,key)`
- L6792 `targetOf(dt,key)`
- L6796 `weekSummary()`
- L6800 `aggregate(key,summary=weekSummary()`
- L6804 `tone(pct,mode='macro')`
- L6811 `pctText(a)`
- L6812 `weekProgress(a,color)`
- L6813 `renderWeekMicros(s)`
- L6837 `ratioAggregate(s,num,den)`
- L6841 `renderWeekRatios(s)`
- L6847 `renderWeekTable(s)`
- L6848 `weeklyDetail(key,oneDate=null)`
- L6856 `weekRatioDetail(key)`
- L6864 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L6870 `openDay(dt)`
- L6908 `withDayGoals(fn)`
- L6913 `renderMicros()`
- L6914 `nutrientDetail(key)`
- L6915 `editTargets()`
- L6916 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L6926 `summaryFor(start)`
- L6930 `ringSVG(pct,color,marker)`
- L6932 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L6936 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L6951 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L6952 `macroTone(p)`
- L6953 `dayMacroPct(dt,k)`
- L6954 `renderWeekly()`
- L6982 `weekDetail(dt,picked)`
- L6990 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L7000 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L7006 `sparkline(pts)`
- L7012 `renderCalendar()`
- L7029 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L7030 `splitMeals(raw)`
- L7040 `localDay(raw,fallback)`
- L7047 `promptDay(raw,fallback)`
- L7048 `analyzeDay(usePhoto=false)`

### Gimnasio: importación de CSV de HEVY, sesiones y análisis IA

- L7070 `parseCsv(text)`
- L7085 `hevyDate(value,format='auto')`
- L7094 constante `MAP`
- L7095 `hevyMapping()`
- L7096 `renderMapping(parsed)`
- L7103 `optionalNum(v,min=0,max=1e7)`
- L7107 `buildHevy(parsed,map)`
- L7117 `cleanWorkout(s)`
- L7124 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L7139 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L7140 constante `GP_ALIAS`
- L7150 `gpNorm(s)`
- L7151 `gpKey(name)`
- L7155 `gpF(n,d=0)`
- L7156 `gpDate(d,opt)`
- L7157 `gpMonday(d)`
- L7158 constante `GP_GROUPS`
- L7173 constante `GP_COLORS`
- L7174 `gpGroup(name)`
- L7175 `gpWorkSets(s)`
- L7176 `gpModel()`
- L7200 `gpSessionMetrics(e,sets)`
- L7215 constante `GP_METRICS`
- L7220 `gpMetricsFor(e)`
- L7221 `gpRangeHist(e)`
- L7222 `gpPRs(model)`
- L7245 `gpStatus(e)`
- L7263 `gpNext(e)`
- L7271 `gpChart(e)`
- L7299 `gpPointDetail(e)`
- L7305 `gpRepTable(e)`
- L7312 `gpKpis(model)`
- L7320 `gpWeekly(model)`
- L7326 `gpMuscles(model)`
- L7333 `gpHeat(model)`
- L7340 `gpExList(model)`
- L7347 `gpExDetail(model)`
- L7360 `gpDayFood(dt)`
- L7361 `gpNutrition(model)`
- L7368 `gpRecentPRs(model)`
- L7372 `gpSessions(model)`
- L7378 `gpSessionModal(id)`
- L7389 `gpWeekModal(w)`
- L7390 `gpSelect(key)`
- L7391 `gpClick(e)`
- L7403 `renderGym()`
- L7423 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L7432 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L7438 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L7462 `openMoreMenu()` — Menú «Más»: secciones poco frecuentes, sin saturar la barra inferior.
- L7469 `showHelp()`
- L7473 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L7475 `markBackup()`
- L7479 `exportJSON()`
- L7484 `drawBackupReminder()`
- L7494 `applyDensity()`
- L7506 `syncDayComplete()`
- L7509 `drawMeals()` — Comidas del día de un vistazo.
- L7517 `filterLog()` — Buscador de Registro.
- L7530 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L7536 `recentFoods()`
- L7541 `quickChip(e,fav)`
- L7559 `drawQuickFoods()`
- L7588 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L7592 `toggleAddPanel(id)`
- L7604 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L7615 `pasteMessage(text,ok)`
- L7623 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L7634 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L7643 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L7661 `storableState()`

### Render único: actualiza toda la página

- L7669 `nearView(el)`
- L7671 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L7675 `render()`
- L7710 `mealByHour(h=new Date()`
- L7711 `syncMealByHour()`

### Arranque

