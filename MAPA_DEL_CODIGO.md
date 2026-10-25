# MAPA DEL CÓDIGO · BioPeat v51 (revisión de datos 23)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (516 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-5745; todo el JavaScript en `<script id="app">` (desde la línea 5746).

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

- L5787 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L5788 constante `AZUCAR_N`
- L5789 constante `USDA_N`
- L5795 constante `FOODS`
- L5797 constante `BASE_FAT_FIX`
- L5800 constante `EXTRA`
- L5801 constante `KEYS`
- L5803 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L5805 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L5809 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L5810 constante `OPT`
- L5828 constante `LIMIT`
- L5829 `optInfo(k,goal)`
- L5834 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L5842 `optLine(k,goal,unit)`
- L5849 `optRefHTML(k,goal,unit)`
- L5851 constante `DAYS`
- L5852 constante `FAF`
- L5856 `number(v,min=0,max=1e6)`
- L5862 `decimalInputs(root=document)`
- L5863 `localDate(d=new Date()`
- L5864 `validDate(s)`
- L5869 `shift(s,n)`
- L5877 constante `CONTEXT`
- L5878 `defaults()`
- L5880 `bmr()`
- L5886 constante `DEF_P` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L5887 `targetFor(d)`
- L5903 `cleanNutrients(o,required=false)`
- L5915 `cleanEntry(e)`
- L5920 `cleanPlan(p)`
- L5924 `planEntry(p)`
- L5933 `seedPlan(d,whichDate)`
- L5937 `ensureDay(d=date)`
- L5944 `effectiveEntries(d=day()`
- L5945 constante `SALTED_IDS`
- L5946 constante `SWEET_RE`
- L5947 `inferFatShares(e,txt=normalize((e?.name||'')`
- L5965 `inferredNutrients(e)`
- L6004 `totals(entries=effectiveEntries()`
- L6013 `change(fn,message='Guardado')`
- L6017 `undo()`
- L6024 `toast(text,canUndo=false)`
- L6032 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6033 `onClick(fn)`
- L6035 `attempt(fn)`
- L6039 `modal(title,body)`
- L6048 `modalRestore()`
- L6058 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6059 `modalBack()`
- L6060 `goDate(d)`
- L6067 `renderHeader()`
- L6076 `renderRows(entries)`
- L6080 `entryValues(e)`
- L6081 `renderLog()`
- L6088 `fromFood(id,amount,meal)`
- L6094 `pantryId(name)`
- L6096 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6102 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6111 `recipe(kind)`
- L6117 `summary(entries)`
- L6121 `renderPresetInfo()`
- L6125 `stripCode(raw)`
- L6131 `parseBIO(raw,meal=$('meal-select')`
- L6137 `parseSmart(raw)`
- L6141 constante `COUNT`
- L6144 `nutrientFields(n,prefix='n_')`
- L6145 `readNutrients(form,prefix='n_')`
- L6150 `editEntry(id)`
- L6159 `editFood(id,pending=null)`
- L6164 `usageStats(days=90)`
- L6170 `renderFoods()`
- L6178 `nutrientSources(key)`
- L6185 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6186 `suppSlot(meal)`
- L6187 `renderSupps()`
- L6202 `editPlan(id)`
- L6209 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6228 `makePrompt(meal='Comida',note='')`
- L6233 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6237 `photoPrompt(meal,note)`
- L6240 `resetPhoto()`
- L6251 `openPhoto()`
- L6257 `shrinkPhoto(file)`
- L6260 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6286 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6293 `cleanFood(id,f)`
- L6297 `migrateBase(o)`
- L6316 `download(name,text,type)`
- L6325 `portable()`
- L6354 `syncAppIcons()`
- L6362 `downloadAppIcons()`
- L6399 `refreshDrawerSummary()`
- L6414 `toggleLeftDrawer(force)`
- L6423 `buildAIExportText(rangeOverride)`
- L6670 `copyAIExport()`
- L6684 `downloadAIExport()`
- L6702 `storageStatus()`
- L6708 `idbReadWrite(mode,value)`
- L6709 `openDB()`
- L6710 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L6722 `setQuantity(id,value,msg='Cantidad actualizada')`
- L6726 `niceStep(v)`
- L6727 `stepQuantity(id,dir)`
- L6781 `renderAppInfo()`
- L6796 `init()`

### Corrección de la pauta declarada (revisión 11 de los datos)

- L6814 `planFamily(e)`
- L6826 `correctedPlan(plan)`
- L6832 `syncCorrectedDay(s,dt)`
- L6841 `upgradeTo11(s,o)`

### Navegación: una sola página; la barra inferior solo desplaza

- L6847 `setNav(v)`
- L6852 `go(v,focus)`
- L6864 `syncDatePill()`
- L6868 `animateValue(el,to,suffix='%',digits=0)`
- L6877 `tick(now)`
- L6880 `macroCard(key,name,color)`
- L6881 `renderToday()`
- L6904 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L6906 constante `HOME`
- L6908 `coachCandidates()`
- L6914 `coachIdeas(t,g,ref,meal)`
- L6927 `renderCoach()`
- L6944 `coachPrompt()`
- L6952 `nutrientDetailStandard(key)`
- L6966 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L6972 `upgradeTo12(s,o)`
- L6977 `benfotiamineTotals(entries=effectiveEntries()`
- L6986 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L6988 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L7000 `microStat(m,t=totals()`
- L7005 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L7013 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L7014 `ratioInfo(key,t=totals()`
- L7049 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L7066 constante `RATIO_ENDS`
- L7067 `ratioBar(i,big=false)`
- L7072 `ratioNeed(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L7089 `needHTML(i,t)`
- L7090 `renderRatios()`
- L7095 `ratioDetail(key)`
- L7105 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L7122 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L7137 `renderMicroMap()`
- L7141 `nutrientDetailForDay(key)`
- L7146 `editTargetsForm()`
- L7156 `mealData()`
- L7161 `renderMealSegments()`
- L7169 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L7179 constante `FAT_KEYS`
- L7181 `fatData(entries=effectiveEntries()`
- L7187 `energyData(entries=effectiveEntries()`
- L7191 `segmentedBar(items,total,attr)`
- L7195 `renderMealChart()`
- L7200 `renderFat()`
- L7208 `fatDetail(key)`
- L7213 `energyDetail(key)`
- L7220 `portionCandidates(q='')`
- L7225 `openPortion()`
- L7238 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L7253 `templates()`
- L7257 `renderExtra()`
- L7268 `updateExtra(reset=true)`
- L7280 `addExtra(id,amount)`
- L7296 `shakePreview()`
- L7297 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L7312 constante `LENS`
- L7318 `lensKey(key)`
- L7319 `lensHTML(key)`
- L7323 `appendLens(key)`
- L7332 `weekDates()`

### IA en la página: conexión directa o por servidor

- L7342 constante `MEAL_WORD`
- L7343 `mealOfWord(w)`
- L7344 `mealFromText(raw,fallback)`
- L7348 `canonMeal(v,fallback)`
- L7356 `localMeal(raw,meal)`
- L7362 constante `AI_FALLBACK`
- L7363 `applyAIConfig(raw)`
- L7389 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L7390 `callGemini(model,key,prompt,img,signal,think=true)`
- L7407 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L7439 constante `AI_PREF`
- L7440 `aiConnected()`
- L7441 `syncAI()`
- L7443 `saveAIPrefs()`
- L7444 `loadAIPrefs()`
- L7445 `openAISetup()`
- L7451 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L7458 constante `MACROS`
- L7460 `cleanGoals(o,fallback)`
- L7465 `cleanCompare(o={})`
- L7469 `snapshotDay(d,reference='saved')`
- L7474 `upgradeTo17(s,o)`
- L7479 `entriesFor(d,source=weekSource)`
- L7483 `dayRow(dt,source=weekSource)`
- L7487 `goalsFor(dt)`
- L7493 `metricValue(r,key)`
- L7499 `targetOf(dt,key)`
- L7503 `weekSummary()`
- L7507 `aggregate(key,summary=weekSummary()`
- L7511 `tone(pct,mode='macro')`
- L7518 `pctText(a)`
- L7519 `weekProgress(a,color)`
- L7520 `renderWeekMicros(s)`
- L7532 `ratioAggregate(s,num,den)`
- L7536 `renderWeekRatios(s)`
- L7542 `renderWeekTable(s)`
- L7543 `weeklyDetail(key,oneDate=null)`
- L7552 `weekRatioDetail(key)`
- L7560 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L7566 `openDay(dt)`
- L7604 `withDayGoals(fn)`
- L7609 `renderMicros()`
- L7610 `nutrientDetail(key)`
- L7611 `editTargets()`
- L7612 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L7622 `summaryFor(start)`
- L7626 `ringSVG(pct,color,marker)`
- L7628 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L7632 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L7647 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L7648 `macroTone(p)`
- L7649 `dayMacroPct(dt,k)`
- L7650 `renderWeekly()`
- L7673 `weekDetail(dt,picked)`
- L7681 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L7691 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L7697 `sparkline(pts)`
- L7703 `renderCalendar()`
- L7720 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L7721 `splitMeals(raw)`
- L7731 `localDay(raw,fallback)`
- L7738 `promptDay(raw,fallback)`
- L7739 `analyzeDay(usePhoto=false)`

### Gimnasio: importación de CSV de HEVY, sesiones y análisis IA

- L7761 `parseCsv(text)`
- L7776 `hevyDate(value,format='auto')`
- L7785 constante `MAP`
- L7786 `hevyMapping()`
- L7787 `renderMapping(parsed)`
- L7794 `optionalNum(v,min=0,max=1e7)`
- L7798 `buildHevy(parsed,map)`
- L7808 `cleanWorkout(s)`
- L7815 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L7830 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L7831 constante `GP_ALIAS`
- L7841 `gpNorm(s)`
- L7842 `gpKey(name)`
- L7846 `gpF(n,d=0)`
- L7847 `gpDate(d,opt)`
- L7848 `gpMonday(d)`
- L7849 constante `GP_GROUPS`
- L7864 constante `GP_COLORS`
- L7865 `gpGroup(name)`
- L7866 `gpWorkSets(s)`
- L7867 `gpModel()`
- L7891 `gpSessionMetrics(e,sets)`
- L7906 constante `GP_METRICS`
- L7911 `gpMetricsFor(e)`
- L7912 `gpRangeHist(e)`
- L7913 `gpPRs(model)`
- L7936 `gpStatus(e)`
- L7954 `gpNext(e)`
- L7962 `gpChart(e)`
- L7990 `gpPointDetail(e)`
- L7996 `gpRepTable(e)`
- L8003 `gpKpis(model)`
- L8011 `gpWeekly(model)`
- L8017 `gpMuscles(model)`
- L8024 `gpHeat(model)`
- L8031 `gpExList(model)`
- L8038 `gpExDetail(model)`
- L8051 `gpDayFood(dt)`
- L8052 `gpNutrition(model)`
- L8059 `gpRecentPRs(model)`
- L8063 `gpSessions(model)`
- L8069 `gpSessionModal(id)`
- L8080 `gpWeekModal(w)`
- L8081 `gpSelect(key)`
- L8082 `gpClick(e)`
- L8094 `renderGym()`
- L8114 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L8123 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L8129 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L8153 `openMoreMenu()` — Menú «Más»: secciones poco frecuentes, sin saturar la barra inferior.
- L8160 `showHelp()`
- L8164 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L8166 `markBackup()`
- L8170 `exportJSON()`
- L8175 `drawBackupReminder()`
- L8185 `applyDensity()`
- L8197 `syncDayComplete()`
- L8200 `drawMeals()` — Comidas del día de un vistazo.
- L8208 `filterLog()` — Buscador de Registro.
- L8221 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L8227 `recentFoods()`
- L8232 `quickChip(e,fav)`
- L8250 `drawQuickFoods()`
- L8279 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L8283 `toggleAddPanel(id)`
- L8295 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L8306 `pasteMessage(text,ok)`
- L8314 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L8325 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L8334 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L8352 `storableState()`

### Render único: actualiza toda la página

- L8360 `nearView(el)`
- L8362 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L8366 `render()`
- L8401 `mealByHour(h=new Date()`
- L8408 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L8418 `dataSummary(s)`
- L8422 `confirmImport(next,name)`
- L8429 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L8435 `checkUpdate()`
- L8440 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L8455 constante `GAP_PREFER`
- L8456 constante `GAP_SKIP`
- L8457 constante `GAP_UNIT`
- L8458 `gapQty(f,x)`
- L8459 `gapFoods(key,gap,ctx)`
- L8478 `weekSources(key,sum)`
- L8484 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L8497 `gapRow(x,open,meal,sum,ctx)`
- L8513 `renderGaps(sum,s)`

### Arranque

