# MAPA DEL CÓDIGO · BioPeat v35 (revisión de datos 23)

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

- L5572 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L5573 constante `AZUCAR_N`
- L5574 constante `USDA_N`
- L5580 constante `FOODS`
- L5582 constante `EXTRA`
- L5583 constante `KEYS`
- L5585 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.
- L5586 constante `MICRO_NOTE`
- L5588 constante `DAYS`
- L5589 constante `FAF`
- L5593 `number(v,min=0,max=1e6)`
- L5599 `decimalInputs(root=document)`
- L5600 `localDate(d=new Date()`
- L5601 `validDate(s)`
- L5606 `shift(s,n)`
- L5614 constante `CONTEXT`
- L5615 `defaults()`
- L5617 `bmr()`
- L5623 constante `DEF_P` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L5624 `targetFor(d)`
- L5640 `cleanNutrients(o,required=false)`
- L5652 `cleanEntry(e)`
- L5657 `cleanPlan(p)`
- L5661 `planEntry(p)`
- L5670 `seedPlan(d,whichDate)`
- L5674 `ensureDay(d=date)`
- L5681 `effectiveEntries(d=day()`
- L5682 `totals(entries=effectiveEntries()`
- L5689 `change(fn,message='Guardado')`
- L5693 `undo()`
- L5700 `toast(text,canUndo=false)`
- L5708 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L5709 `onClick(fn)`
- L5711 `attempt(fn)`
- L5715 `modal(title,body)`
- L5724 `modalRestore()`
- L5734 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L5735 `modalBack()`
- L5736 `goDate(d)`
- L5743 `renderHeader()`
- L5751 `renderRows(entries)`
- L5755 `entryValues(e)`
- L5756 `renderLog()`
- L5763 `fromFood(id,amount,meal)`
- L5769 `pantryId(name)`
- L5771 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L5777 `addEntries(entries,message='Añadido',d=date,opts={})`
- L5785 `recipe(kind)`
- L5791 `summary(entries)`
- L5795 `renderPresetInfo()`
- L5799 `stripCode(raw)`
- L5805 `parseBIO(raw,meal=$('meal-select')`
- L5811 `parseSmart(raw)`
- L5815 constante `COUNT`
- L5818 `nutrientFields(n,prefix='n_')`
- L5819 `readNutrients(form,prefix='n_')`
- L5824 `editEntry(id)`
- L5833 `editFood(id,pending=null)`
- L5838 `usageStats(days=90)`
- L5844 `renderFoods()`
- L5852 `nutrientSources(key)`
- L5859 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L5860 `suppSlot(meal)`
- L5861 `renderSupps()`
- L5876 `editPlan(id)`
- L5883 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L5898 `makePrompt(meal='Comida',note='')`
- L5902 `resetPhoto()`
- L5913 `openPhoto()`
- L5919 `shrinkPhoto(file)`
- L5922 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L5946 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L5953 `cleanFood(id,f)`
- L5957 `migrateBase(o)`
- L5976 `download(name,text,type)`
- L5985 `portable()`
- L6009 `storageStatus()`
- L6015 `idbReadWrite(mode,value)`
- L6016 `openDB()`
- L6017 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L6029 `setQuantity(id,value,msg='Cantidad actualizada')`
- L6033 `niceStep(v)`
- L6034 `stepQuantity(id,dir)`
- L6088 `renderAppInfo()`
- L6103 `init()`

### Corrección de la pauta declarada (revisión 11 de los datos)

- L6121 `planFamily(e)`
- L6133 `correctedPlan(plan)`
- L6139 `syncCorrectedDay(s,dt)`
- L6148 `upgradeTo11(s,o)`

### Navegación: una sola página; la barra inferior solo desplaza

- L6154 `setNav(v)`
- L6159 `go(v,focus)`
- L6171 `syncDatePill()`
- L6175 `animateValue(el,to,suffix='%',digits=0)`
- L6184 `tick(now)`
- L6187 `macroCard(key,name,color)`
- L6188 `renderToday()`
- L6211 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L6213 constante `HOME`
- L6215 `coachCandidates()`
- L6221 `coachIdeas(t,g,ref,meal)`
- L6234 `renderCoach()`
- L6251 `coachPrompt()`
- L6259 `nutrientDetailStandard(key)`
- L6272 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L6278 `upgradeTo12(s,o)`
- L6283 `benfotiamineTotals(entries=effectiveEntries()`
- L6292 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L6294 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L6303 `microStat(m,t=totals()`
- L6308 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L6316 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L6317 `ratioInfo(key,t=totals()`
- L6352 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L6369 `ratioBar(i,big=false)`
- L6373 `renderRatios()`
- L6378 `ratioDetail(key)`
- L6388 constante `MICRO_BANDS` — Tarjeta de un nutriente. Límites (máx): verde por debajo. Selenio: banda óptima 100-200 µg.
- L6389 `microCardHTML(m,x,personal)`
- L6399 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L6414 `renderMicroMap()`
- L6418 `nutrientDetailForDay(key)`
- L6423 `editTargetsForm()`
- L6433 `mealData()`
- L6438 `renderMealSegments()`
- L6446 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L6456 constante `FAT_KEYS`
- L6457 constante `FAT_PROFILES`
- L6459 `fatData(entries=effectiveEntries()`
- L6465 `energyData(entries=effectiveEntries()`
- L6469 `segmentedBar(items,total,attr)`
- L6473 `renderMealChart()`
- L6478 `renderFat()`
- L6486 `fatDetail(key)`
- L6491 `energyDetail(key)`
- L6498 `portionCandidates(q='')`
- L6503 `openPortion()`
- L6516 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L6531 `templates()`
- L6535 `renderExtra()`
- L6546 `updateExtra(reset=true)`
- L6558 `addExtra(id,amount)`
- L6574 `shakePreview()`
- L6575 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L6590 constante `LENS`
- L6596 `lensKey(key)`
- L6597 `lensHTML(key)`
- L6601 `appendLens(key)`
- L6610 `weekDates()`

### IA en la página: conexión directa o por servidor

- L6620 constante `MEAL_WORD`
- L6621 `mealOfWord(w)`
- L6622 `mealFromText(raw,fallback)`
- L6626 `canonMeal(v,fallback)`
- L6633 `localMeal(raw,meal)`
- L6639 constante `AI_FALLBACK`
- L6640 `applyAIConfig(raw)`
- L6664 `requestAI(prompt,img,signal,modelOverride='')`
- L6677 constante `AI_PREF`
- L6678 `aiConnected()`
- L6679 `syncAI()`
- L6681 `saveAIPrefs()`
- L6682 `loadAIPrefs()`
- L6683 `openAISetup()`
- L6689 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L6696 constante `MACROS`
- L6698 `cleanGoals(o,fallback)`
- L6703 `cleanCompare(o={})`
- L6707 `snapshotDay(d,reference='saved')`
- L6712 `upgradeTo17(s,o)`
- L6717 `entriesFor(d,source=weekSource)`
- L6721 `dayRow(dt,source=weekSource)`
- L6725 `goalsFor(dt)`
- L6731 `metricValue(r,key)`
- L6736 `targetOf(dt,key)`
- L6740 `weekSummary()`
- L6744 `aggregate(key,summary=weekSummary()`
- L6748 `tone(pct,mode='macro')`
- L6755 `pctText(a)`
- L6756 `weekProgress(a,color)`
- L6757 `renderWeekMicros(s)`
- L6781 `ratioAggregate(s,num,den)`
- L6785 `renderWeekRatios(s)`
- L6791 `renderWeekTable(s)`
- L6792 `weeklyDetail(key,oneDate=null)`
- L6800 `weekRatioDetail(key)`
- L6808 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L6814 `openDay(dt)`
- L6852 `withDayGoals(fn)`
- L6857 `renderMicros()`
- L6858 `nutrientDetail(key)`
- L6859 `editTargets()`
- L6860 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L6870 `summaryFor(start)`
- L6874 `ringSVG(pct,color,marker)`
- L6876 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L6880 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L6895 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L6896 `macroTone(p)`
- L6897 `dayMacroPct(dt,k)`
- L6898 `renderWeekly()`
- L6926 `weekDetail(dt,picked)`
- L6934 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L6944 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L6950 `sparkline(pts)`
- L6956 `renderCalendar()`
- L6973 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L6974 `splitMeals(raw)`
- L6984 `localDay(raw,fallback)`
- L6991 `promptDay(raw,fallback)`
- L6992 `analyzeDay(usePhoto=false)`

### Gimnasio: importación de CSV de HEVY, sesiones y análisis IA

- L6998 `parseCsv(text)`
- L7013 `hevyDate(value,format='auto')`
- L7022 constante `MAP`
- L7023 `hevyMapping()`
- L7024 `renderMapping(parsed)`
- L7031 `optionalNum(v,min=0,max=1e7)`
- L7035 `buildHevy(parsed,map)`
- L7045 `cleanWorkout(s)`
- L7052 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L7067 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L7068 constante `GP_ALIAS`
- L7078 `gpNorm(s)`
- L7079 `gpKey(name)`
- L7083 `gpF(n,d=0)`
- L7084 `gpDate(d,opt)`
- L7085 `gpMonday(d)`
- L7086 constante `GP_GROUPS`
- L7101 constante `GP_COLORS`
- L7102 `gpGroup(name)`
- L7103 `gpWorkSets(s)`
- L7104 `gpModel()`
- L7128 `gpSessionMetrics(e,sets)`
- L7143 constante `GP_METRICS`
- L7148 `gpMetricsFor(e)`
- L7149 `gpRangeHist(e)`
- L7150 `gpPRs(model)`
- L7173 `gpStatus(e)`
- L7191 `gpNext(e)`
- L7199 `gpChart(e)`
- L7227 `gpPointDetail(e)`
- L7233 `gpRepTable(e)`
- L7240 `gpKpis(model)`
- L7248 `gpWeekly(model)`
- L7254 `gpMuscles(model)`
- L7261 `gpHeat(model)`
- L7268 `gpExList(model)`
- L7275 `gpExDetail(model)`
- L7288 `gpDayFood(dt)`
- L7289 `gpNutrition(model)`
- L7296 `gpRecentPRs(model)`
- L7300 `gpSessions(model)`
- L7306 `gpSessionModal(id)`
- L7317 `gpWeekModal(w)`
- L7318 `gpSelect(key)`
- L7319 `gpClick(e)`
- L7331 `renderGym()`
- L7351 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L7360 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L7366 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L7390 `openMoreMenu()` — Menú «Más»: secciones poco frecuentes, sin saturar la barra inferior.
- L7397 `showHelp()`
- L7401 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L7403 `markBackup()`
- L7407 `exportJSON()`
- L7412 `drawBackupReminder()`
- L7422 `applyDensity()`
- L7434 `syncDayComplete()`
- L7437 `drawMeals()` — Comidas del día de un vistazo.
- L7445 `filterLog()` — Buscador de Registro.
- L7458 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L7464 `recentFoods()`
- L7469 `quickChip(e,fav)`
- L7487 `drawQuickFoods()`
- L7516 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L7520 `toggleAddPanel(id)`
- L7532 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L7543 `pasteMessage(text,ok)`
- L7551 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L7562 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L7571 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L7589 `storableState()`

### Render único: actualiza toda la página

- L7597 `nearView(el)`
- L7599 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L7603 `render()`
- L7638 `mealByHour(h=new Date()`
- L7639 `syncMealByHour()`

### Arranque

