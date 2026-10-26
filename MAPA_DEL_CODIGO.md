# MAPA DEL CÓDIGO · BioPeat v52 (revisión de datos 23)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (538 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-5789; todo el JavaScript en `<script id="app">` (desde la línea 5790).

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

- L5832 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L5833 constante `AZUCAR_N`
- L5834 constante `USDA_N`
- L5840 constante `FOODS`
- L5842 constante `BASE_FAT_FIX`
- L5845 constante `EXTRA`
- L5846 constante `KEYS`
- L5848 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L5850 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L5854 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L5855 constante `OPT`
- L5873 constante `LIMIT`
- L5874 `optInfo(k,goal)`
- L5879 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L5887 `optLine(k,goal,unit)`
- L5894 `optRefHTML(k,goal,unit)`
- L5896 constante `DAYS`
- L5897 constante `FAF`
- L5901 `number(v,min=0,max=1e6)`
- L5907 `decimalInputs(root=document)`
- L5908 `localDate(d=new Date()`
- L5909 `validDate(s)`
- L5914 `shift(s,n)`
- L5922 constante `CONTEXT`
- L5923 `defaults()`
- L5925 `bmr()`
- L5931 constante `DEF_P` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L5932 `targetFor(d)`
- L5948 `cleanNutrients(o,required=false)`
- L5960 `cleanEntry(e)`
- L5965 `cleanPlan(p)`
- L5969 `planEntry(p)`
- L5978 `seedPlan(d,whichDate)`
- L5982 `ensureDay(d=date)`
- L5989 `effectiveEntries(d=day()`
- L5990 constante `SALTED_IDS`
- L5991 constante `SWEET_RE`
- L5992 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6010 `inferredNutrients(e)`
- L6049 `totals(entries=effectiveEntries()`
- L6058 `change(fn,message='Guardado')`
- L6062 `undo()`
- L6069 `toast(text,canUndo=false)`
- L6077 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6078 `onClick(fn)`
- L6080 `attempt(fn)`
- L6084 `modal(title,body)`
- L6093 `modalRestore()`
- L6103 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6104 `modalBack()`
- L6105 `goDate(d)`
- L6112 `renderHeader()`
- L6123 `renderRows(entries)`
- L6127 `entryValues(e)`
- L6128 `renderLog()`
- L6135 `fromFood(id,amount,meal)`
- L6141 `pantryId(name)`
- L6143 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6149 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6158 `recipe(kind)`
- L6164 `summary(entries)`
- L6168 `renderPresetInfo()`
- L6172 `stripCode(raw)`
- L6178 `parseBIO(raw,meal=$('meal-select')`
- L6184 `parseSmart(raw)`
- L6188 constante `COUNT`
- L6191 `nutrientFields(n,prefix='n_')`
- L6192 `readNutrients(form,prefix='n_')`
- L6197 `editEntry(id)`
- L6206 `editFood(id,pending=null)`
- L6211 `usageStats(days=90)`
- L6217 `renderFoods()`
- L6225 `nutrientSources(key)`
- L6232 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6233 `suppSlot(meal)`
- L6234 `renderSupps()`
- L6249 `editPlan(id)`
- L6256 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6275 `makePrompt(meal='Comida',note='')`
- L6280 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6284 `photoPrompt(meal,note)`
- L6287 `resetPhoto()`
- L6298 `openPhoto()`
- L6304 `shrinkPhoto(file)`
- L6307 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6333 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6340 `cleanFood(id,f)`
- L6344 `migrateBase(o)`
- L6363 `download(name,text,type)`
- L6372 `portable()`
- L6408 `syncAppIcons()`
- L6416 `downloadAppIcons()`
- L6453 constante `PROFILES_KEY`
- L6455 `ensureProfilesStore()`
- L6474 `saveProfilesStore(st)`
- L6478 `syncCurrentProfileToStore(rawStr)`
- L6484 `activeProfileName()`
- L6488 `renderProfilesList()`
- L6529 `switchProfile(id)`
- L6550 `createNewProfile(name,weight,height,age,mode)`
- L6587 `deleteProfileById(id)`
- L6611 `refreshDrawerSummary()`
- L6628 `toggleLeftDrawer(force)`
- L6642 `buildAIExportText(rangeOverride)`
- L6889 `copyAIExport()`
- L6903 `downloadAIExport()`
- L6912 `renderDrawerChat()`
- L6931 `buildDrawerChatPrompt(question)`
- L6943 `askDrawerAI(rawQuestion)`
- L7033 `storageStatus()`
- L7039 `idbReadWrite(mode,value)`
- L7040 `openDB()`
- L7041 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L7054 `setQuantity(id,value,msg='Cantidad actualizada')`
- L7058 `niceStep(v)`
- L7059 `stepQuantity(id,dir)`
- L7113 `renderAppInfo()`
- L7128 `init()`

### Corrección de la pauta declarada (revisión 11 de los datos)

- L7146 `planFamily(e)`
- L7158 `correctedPlan(plan)`
- L7164 `syncCorrectedDay(s,dt)`
- L7173 `upgradeTo11(s,o)`

### Navegación: una sola página; la barra inferior solo desplaza

- L7179 `setNav(v)`
- L7184 `go(v,focus)`
- L7196 `syncDatePill()`
- L7200 `animateValue(el,to,suffix='%',digits=0)`
- L7209 `tick(now)`
- L7212 `macroCard(key,name,color)`
- L7213 `renderToday()`
- L7236 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L7238 constante `HOME`
- L7240 `coachCandidates()`
- L7246 `coachIdeas(t,g,ref,meal)`
- L7259 `renderCoach()`
- L7276 `coachPrompt()`
- L7284 `nutrientDetailStandard(key)`
- L7298 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L7304 `upgradeTo12(s,o)`
- L7309 `benfotiamineTotals(entries=effectiveEntries()`
- L7318 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L7320 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L7332 `microStat(m,t=totals()`
- L7337 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L7345 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L7346 `ratioInfo(key,t=totals()`
- L7381 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L7398 constante `RATIO_ENDS`
- L7399 `ratioBar(i,big=false)`
- L7404 `ratioNeed(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L7421 `needHTML(i,t)`
- L7422 `renderRatios()`
- L7427 `ratioDetail(key)`
- L7437 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L7454 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L7469 `renderMicroMap()`
- L7473 `nutrientDetailForDay(key)`
- L7478 `editTargetsForm()`
- L7488 `mealData()`
- L7493 `renderMealSegments()`
- L7501 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L7511 constante `FAT_KEYS`
- L7513 `fatData(entries=effectiveEntries()`
- L7519 `energyData(entries=effectiveEntries()`
- L7523 `segmentedBar(items,total,attr)`
- L7527 `renderMealChart()`
- L7532 `renderFat()`
- L7540 `fatDetail(key)`
- L7545 `energyDetail(key)`
- L7552 `portionCandidates(q='')`
- L7557 `openPortion()`
- L7570 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L7585 `templates()`
- L7589 `renderExtra()`
- L7600 `updateExtra(reset=true)`
- L7612 `addExtra(id,amount)`
- L7628 `shakePreview()`
- L7629 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L7644 constante `LENS`
- L7650 `lensKey(key)`
- L7651 `lensHTML(key)`
- L7655 `appendLens(key)`
- L7664 `weekDates()`

### IA en la página: conexión directa o por servidor

- L7674 constante `MEAL_WORD`
- L7675 `mealOfWord(w)`
- L7676 `mealFromText(raw,fallback)`
- L7680 `canonMeal(v,fallback)`
- L7688 `localMeal(raw,meal)`
- L7694 constante `AI_FALLBACK`
- L7695 `applyAIConfig(raw)`
- L7721 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L7722 `callGemini(model,key,prompt,img,signal,think=true)`
- L7739 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L7771 constante `AI_PREF`
- L7772 `aiConnected()`
- L7773 `syncAI()`
- L7775 `saveAIPrefs()`
- L7776 `loadAIPrefs()`
- L7777 `openAISetup()`
- L7783 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L7790 constante `MACROS`
- L7792 `cleanGoals(o,fallback)`
- L7797 `cleanCompare(o={})`
- L7801 `snapshotDay(d,reference='saved')`
- L7806 `upgradeTo17(s,o)`
- L7811 `entriesFor(d,source=weekSource)`
- L7815 `dayRow(dt,source=weekSource)`
- L7819 `goalsFor(dt)`
- L7825 `metricValue(r,key)`
- L7831 `targetOf(dt,key)`
- L7835 `weekSummary()`
- L7839 `aggregate(key,summary=weekSummary()`
- L7843 `tone(pct,mode='macro')`
- L7850 `pctText(a)`
- L7851 `weekProgress(a,color)`
- L7852 `renderWeekMicros(s)`
- L7864 `ratioAggregate(s,num,den)`
- L7868 `renderWeekRatios(s)`
- L7874 `renderWeekTable(s)`
- L7875 `weeklyDetail(key,oneDate=null)`
- L7884 `weekRatioDetail(key)`
- L7892 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L7898 `openDay(dt)`
- L7936 `withDayGoals(fn)`
- L7941 `renderMicros()`
- L7942 `nutrientDetail(key)`
- L7943 `editTargets()`
- L7944 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L7954 `summaryFor(start)`
- L7958 `ringSVG(pct,color,marker)`
- L7960 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L7964 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L7979 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L7980 `macroTone(p)`
- L7981 `dayMacroPct(dt,k)`
- L7982 `renderWeekly()`
- L8005 `weekDetail(dt,picked)`
- L8013 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L8023 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L8029 `sparkline(pts)`
- L8035 `renderCalendar()`
- L8052 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L8053 `splitMeals(raw)`
- L8063 `localDay(raw,fallback)`
- L8070 `promptDay(raw,fallback)`
- L8071 `analyzeDay(usePhoto=false)`

### Gimnasio: importación de CSV de HEVY, sesiones y análisis IA

- L8093 `parseCsv(text)`
- L8108 `hevyDate(value,format='auto')`
- L8117 constante `MAP`
- L8118 `hevyMapping()`
- L8119 `renderMapping(parsed)`
- L8126 `optionalNum(v,min=0,max=1e7)`
- L8130 `buildHevy(parsed,map)`
- L8140 `cleanWorkout(s)`
- L8147 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L8162 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L8163 constante `GP_ALIAS`
- L8173 `gpNorm(s)`
- L8174 `gpKey(name)`
- L8178 `gpF(n,d=0)`
- L8179 `gpDate(d,opt)`
- L8180 `gpMonday(d)`
- L8181 constante `GP_GROUPS`
- L8196 constante `GP_COLORS`
- L8197 `gpGroup(name)`
- L8198 `gpWorkSets(s)`
- L8199 `gpModel()`
- L8223 `gpSessionMetrics(e,sets)`
- L8238 constante `GP_METRICS`
- L8243 `gpMetricsFor(e)`
- L8244 `gpRangeHist(e)`
- L8245 `gpPRs(model)`
- L8268 `gpStatus(e)`
- L8286 `gpNext(e)`
- L8294 `gpChart(e)`
- L8322 `gpPointDetail(e)`
- L8328 `gpRepTable(e)`
- L8335 `gpKpis(model)`
- L8343 `gpWeekly(model)`
- L8349 `gpMuscles(model)`
- L8356 `gpHeat(model)`
- L8363 `gpExList(model)`
- L8370 `gpExDetail(model)`
- L8383 `gpDayFood(dt)`
- L8384 `gpNutrition(model)`
- L8391 `gpRecentPRs(model)`
- L8395 `gpSessions(model)`
- L8401 `gpSessionModal(id)`
- L8412 `gpWeekModal(w)`
- L8413 `gpSelect(key)`
- L8414 `gpClick(e)`
- L8426 `renderGym()`
- L8446 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L8455 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L8461 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L8485 `openMoreMenu()` — Menú «Más»: secciones poco frecuentes, sin saturar la barra inferior.
- L8492 `showHelp()`
- L8496 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L8498 `markBackup()`
- L8502 `exportJSON()`
- L8507 `drawBackupReminder()`
- L8517 `applyDensity()`
- L8529 `syncDayComplete()`
- L8532 `drawMeals()` — Comidas del día de un vistazo.
- L8540 `filterLog()` — Buscador de Registro.
- L8553 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L8559 `recentFoods()`
- L8564 `quickChip(e,fav)`
- L8582 `drawQuickFoods()`
- L8611 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L8615 `toggleAddPanel(id)`
- L8627 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L8638 `pasteMessage(text,ok)`
- L8646 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L8657 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L8666 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L8684 `storableState()`

### Render único: actualiza toda la página

- L8692 `nearView(el)`
- L8694 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L8698 `render()`
- L8733 `mealByHour(h=new Date()`
- L8740 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L8750 `dataSummary(s)`
- L8754 `confirmImport(next,name)`
- L8761 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L8767 `checkUpdate()`
- L8772 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L8787 constante `GAP_PREFER`
- L8788 constante `GAP_SKIP`
- L8789 constante `GAP_UNIT`
- L8790 `gapQty(f,x)`
- L8791 `gapFoods(key,gap,ctx)`
- L8810 `weekSources(key,sum)`
- L8816 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L8829 `gapRow(x,open,meal,sum,ctx)`
- L8845 `renderGaps(sum,s)`

### Arranque

