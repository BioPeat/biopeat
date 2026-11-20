# MAPA DEL CÓDIGO · BioPeat v73 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (923 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-6359; todo el JavaScript en `<script id="app">` (desde la línea 6360).

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

- L6422 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L6423 constante `AZUCAR_N`
- L6424 constante `USDA_N`
- L6430 constante `FOODS`
- L6432 constante `BASE_FAT_FIX`
- L6436 constante `REF_COLS` — Base de referencia verificada (USDA FoodData Central / BEDCA, por 100 g o 100 ml comestibles).
- L6437 constante `REF_RAW`
- L6599 constante `REF_MAP`
- L6600 constante `REF_CACHE`
- L6601 `refNutrients(id)`
- L6609 `findRef(text,strict=false)`
- L6631 `refCatalogCompact()`
- L6632 `fromRef(id,amount,meal,note='',srcText='')`
- L6637 constante `EXTRA`
- L6638 constante `KEYS`
- L6640 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L6642 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L6646 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6647 constante `OPT`
- L6668 constante `LIMIT`
- L6669 `optInfo(k,goal)`
- L6676 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6684 `optLine(k,goal,unit)`
- L6691 `optRefHTML(k,goal,unit)`
- L6693 constante `DAYS`
- L6694 constante `FAF`
- L6696 constante `LOC`
- L6700 `number(v,min=0,max=1e6)`
- L6706 `decimalInputs(root=document)`
- L6707 `localDate(d=new Date()`
- L6708 `validDate(s)`
- L6713 `shift(s,n)`
- L6722 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6724 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6730 constante `DAY_TYPES`
- L6731 constante `NEW_V54`
- L6735 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6738 `bmr()` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6744 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6766 `cleanNutrients(o,required=false)`
- L6778 `cleanEntry(e)`
- L6783 `cleanPlan(p)`
- L6787 `planEntry(p)`
- L6796 `seedPlan(d,whichDate)`
- L6800 `ensureDay(d=date)`
- L6807 `effectiveEntries(d=day()`
- L6808 constante `SALTED_IDS`
- L6809 constante `SWEET_RE`
- L6810 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6828 `inferredNutrients(e)`
- L6869 `totals(entries=effectiveEntries()`
- L6878 `change(fn,message='Guardado')`
- L6882 `undo()`
- L6889 `toast(text,canUndo=false)`
- L6897 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6898 `onClick(fn)`
- L6900 `attempt(fn)`
- L6904 `modal(title,body)`
- L6913 `modalRestore()`
- L6923 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6924 `modalBack()`
- L6925 `goDate(d)`
- L6932 `renderHeader()`
- L6945 `renderRows(entries)`
- L6949 `entryValues(e)`
- L6950 `renderLog()`
- L6957 `fromFood(id,amount,meal)`
- L6963 `pantryId(name)`
- L6965 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6971 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6980 `recipe(kind)`
- L6987 `summary(entries)`
- L6991 `renderPresetInfo()`
- L7004 `stripCode(raw)`
- L7010 `sanitizeNutrients(o,grams=100,fallbackRefId='')`
- L7037 `parseBIO(raw,meal=$('meal-select')`
- L7049 `parseSmart(raw)`
- L7053 constante `COUNT`
- L7054 constante `UNIT_RE`
- L7096 `offToNutrients(nut={},fallbackName='')` — Open Food Facts (gratis, sin clave, CORS nativo): consulta por código de barras o texto.
- L7117 `lookupOFFBarcode(code,signal,ms=3200)`
- L7132 `searchOFF(query,signal,ms=4500)`
- L7149 `openProductSearch()`
- L7174 `nutrientFields(n,prefix='n_')`
- L7175 `readNutrients(form,prefix='n_')`
- L7180 `editEntry(id)`
- L7189 `editFood(id,pending=null)`
- L7194 `usageStats(days=90)`
- L7200 `renderFoods()`
- L7208 `nutrientSources(key)`
- L7215 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L7216 `suppSlot(meal)`
- L7217 `renderSupps()`
- L7232 `editPlan(id)`
- L7239 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L7259 `makePrompt(meal='Comida',note='')`
- L7264 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L7268 `pantryCompact()`
- L7272 constante `MEAL_AI_SCHEMA`
- L7312 `mealSystemPrompt(usePhoto)`
- L7328 `hydrateAIItems(rawItems,fallback,usePhoto,aiModel,signal)`
- L7371 `photoPrompt(meal,note)`
- L7374 `resetPhoto()`
- L7385 `openPhoto()`
- L7391 `shrinkPhoto(file)`
- L7394 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L7420 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L7427 `cleanFood(id,f)`
- L7431 `migrateBase(o)`
- L7450 `download(name,text,type)`
- L7459 `portable()`
- L7500 `syncAppIcons()`
- L7508 `downloadAppIcons()`
- L7545 constante `PROFILES_KEY`
- L7547 `ensureProfilesStore()`
- L7567 `resetProfileSessionUI()`
- L7574 `saveProfilesStore(st)`
- L7583 `syncCurrentProfileToStore(rawStr)`
- L7589 `activeProfileName()`
- L7593 `renderProfilesList()`
- L7635 `switchProfile(id)`
- L7657 `deleteProfileById(id)`
- L7682 `refreshDrawerSummary()`
- L7699 `toggleLeftDrawer(force)`
- L7714 `buildAIExportText(rangeOverride)`
- L7965 `copyAIExport()`
- L7979 `downloadAIExport()`
- L7988 `renderDrawerChat()`
- L8007 `buildDrawerChatContext()`
- L8044 `buildDrawerChatPrompt(question)`
- L8056 `askDrawerAI(rawQuestion)`
- L8145 `storageStatus()`
- L8151 `idbReadWrite(mode,value,key='current')`
- L8152 `openDB()`
- L8153 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L8166 `setQuantity(id,value,msg='Cantidad actualizada')`
- L8170 `niceStep(v)`
- L8171 `stepQuantity(id,dir)`
- L8225 `renderAppInfo()`
- L8240 `init()`
- L8268 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L8270 `setNav(v)`
- L8275 `go(v,focus)`
- L8286 constante `THEME_KEY`
- L8287 constante `SUN_SVG`
- L8288 constante `MOON_SVG`
- L8290 `syncThemeUI()`
- L8302 `toggleTheme()`
- L8311 `syncLogoTheme()`
- L8322 `applyMenuBtnState()`
- L8345 `syncDatePill()`
- L8358 `clampBtnPos(el,x,y)`
- L8368 `bindDraggableBtn(el,storeKey)`
- L8453 `bindDrawerGestures()`
- L8490 `animateValue(el,to,suffix='%',digits=0)`
- L8499 `tick(now)`
- L8502 `macroCard(key,name,color)`
- L8503 `renderToday()`
- L8526 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L8528 constante `HOME`
- L8530 `coachCandidates()`
- L8536 `coachIdeas(t,g,ref,meal)`
- L8549 `renderCoach()`
- L8569 `coachPrompt()`
- L8578 `nutrientDetailStandard(key)`
- L8592 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L8598 `upgradeTo12(s,o)`
- L8603 `benfotiamineTotals(entries=effectiveEntries()`
- L8612 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L8614 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L8626 `microStat(m,t=totals()`
- L8631 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L8639 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L8640 `ratioInfo(key,t=totals()`
- L8679 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L8696 constante `RATIO_ENDS`
- L8698 `ratioZones(i)` — v68: cada equilibrio tiene una zona «aceptable» (ni verde ni mala) y su meta visible en la tarjeta.
- L8706 `ratioTone(i)`
- L8711 constante `NEAR_HEAD`
- L8712 `ratioBar(i,big=false)`
- L8721 `ratioNeedBase(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L8739 `needHTML(i,t)`
- L8740 `ratioNeed(i,t=totals()`
- L8744 `adBalance(t=totals()`
- L8771 `zncuSuppKey()`
- L8772 `zncuSuppCfg()`
- L8794 `zncuDoseLabel(zn,cu)`
- L8797 `hasZncuSupp(d=day()`
- L8802 `toggleZncuSupp()`
- L8822 `openZncuConfig()`
- L8828 `renderRatios()`
- L8839 `ratioDetail(key)`
- L8856 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L8873 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L8888 `renderMicroMap()`
- L8892 `nutrientDetailForDay(key)`
- L8897 `editTargetsForm()`
- L8907 `mealData()`
- L8912 `renderMealSegments()`
- L8920 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L8955 constante `FAT_KEYS`
- L8957 `fatData(entries=effectiveEntries()`
- L8963 `energyData(entries=effectiveEntries()`
- L8967 `segmentedBar(items,total,attr)`
- L8971 `renderMealChart()`
- L8976 `renderFat()`
- L8984 `fatDetail(key)`
- L8989 `energyDetail(key)`
- L8996 `portionCandidates(q='')`
- L9001 `openPortion()`
- L9014 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L9029 `templates()`
- L9033 `renderExtra()`
- L9044 `updateExtra(reset=true)`
- L9056 `addExtra(id,amount)`
- L9072 `shakePreview()`
- L9073 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L9088 constante `LENS`
- L9094 `lensKey(key)`
- L9095 `lensHTML(key)`
- L9099 `appendLens(key)`
- L9108 `weekDates()`

### IA en la página: conexión directa o por servidor

- L9118 constante `MEAL_WORD`
- L9119 `mealOfWord(w)`
- L9120 `mealFromText(raw,fallback)`
- L9124 `canonMeal(v,fallback)`
- L9132 `localMeal(raw,meal)`
- L9138 constante `AI_FALLBACK`
- L9139 constante `GEMINI_DEFAULTS`
- L9140 constante `GROQ_DEFAULTS`
- L9141 `aiTaskProfile(task,hasImg=false)`
- L9148 `geminiThinkLevel(model,want)`
- L9154 `supportsGeminiTemp(model)`
- L9155 `readSSE(res,onEvent)`
- L9174 `applyAIConfig(raw)`
- L9200 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L9201 `callGemini(model,key,prompt,img,signal,opts={})`
- L9247 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), Groq (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L9255 `aiProv(m=$('ai-mode')`
- L9256 `aiBase(mode)`
- L9265 `chatHeaders(mode,key)`
- L9272 `callChat(mode,model,key,prompt,img,signal,opts={})` — ChatGPT, Claude, Groq, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L9326 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L9341 constante `MODEL_PREF`
- L9342 `pickModel(ids,mode=$('ai-mode')`
- L9356 `ensureModel(st)`
- L9372 `syncProvider()`
- L9391 `requestAI(prompt,img,signal,modelOverride='',onStep=null,opts={})`
- L9427 constante `AI_PREF`
- L9428 `aiConnected()`
- L9429 `syncAI()`
- L9431 `saveAIPrefs()`
- L9432 `loadAIPrefs()`
- L9433 `openAISetup()`
- L9440 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L9447 constante `MACROS`
- L9449 `cleanGoals(o,fallback)`
- L9454 `cleanCompare(o={})`
- L9458 `snapshotDay(d,reference='saved')`
- L9463 `upgradeTo17(s,o)`
- L9468 `entriesFor(d,source=weekSource)`
- L9472 `dayRow(dt,source=weekSource)`
- L9476 `goalsFor(dt)`
- L9482 `metricValue(r,key)`
- L9488 `targetOf(dt,key)`
- L9492 `weekSummary()`
- L9496 `aggregate(key,summary=weekSummary()`
- L9500 `tone(pct,mode='macro')`
- L9507 `pctText(a)`
- L9508 `weekProgress(a,color)`
- L9509 `renderWeekMicros(s)`
- L9521 `ratioAggregate(s,num,den)`
- L9525 `renderWeekRatios(s)`
- L9531 `renderWeekTable(s)`
- L9532 `weeklyDetail(key,oneDate=null)`
- L9541 `weekRatioDetail(key)`
- L9549 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L9555 `openDay(dt)`
- L9593 `withDayGoals(fn)`
- L9598 `renderMicros()`
- L9599 `nutrientDetail(key)`
- L9600 `editTargets()`
- L9601 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L9611 `summaryFor(start)`
- L9615 `ringSVG(pct,color,marker)`
- L9617 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L9621 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L9638 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L9639 `macroTone(p)`
- L9640 `dayMacroPct(dt,k)`
- L9641 `renderWeekly()`
- L9664 `weekDetail(dt,picked)`
- L9672 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L9682 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L9688 `sparkline(pts)`
- L9694 `renderCalendar()`
- L9711 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L9712 `splitMeals(raw)`
- L9722 `localDay(raw,fallback)`
- L9729 `promptDay(raw,fallback)`
- L9730 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L9769 `parseCsv(text)`
- L9784 `hevyDate(value,format='auto')`
- L9801 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L9816 constante `GYM_APPS`
- L9818 `gymSig(headers)`
- L9819 `gymApp(headers)`
- L9820 `hevyMapping()`
- L9821 `gymSaved()`
- L9822 `renderMapping(parsed)`
- L9839 `optionalNum(v,min=0,max=1e7)`
- L9844 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L9851 `buildHevy(parsed,map)`
- L9885 `cleanWorkout(s)`
- L9892 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L9907 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L9908 constante `GP_ALIAS`
- L9918 `gpNorm(s)`
- L9919 `gpKey(name)`
- L9923 `gpF(n,d=0)`
- L9924 `gpDate(d,opt)`
- L9925 `gpMonday(d)`
- L9926 constante `GP_GROUPS`
- L9941 constante `GP_COLORS`
- L9942 `gpGroup(name)`
- L9943 `gpWorkSets(s)`
- L9944 `gpModel()`
- L9968 `gpSessionMetrics(e,sets)`
- L9983 constante `GP_METRICS`
- L9988 `gpMetricsFor(e)`
- L9989 `gpRangeHist(e)`
- L9990 `gpPRs(model)`
- L10013 `gpStatus(e)`
- L10031 `gpNext(e)`
- L10039 `gpChart(e)`
- L10067 `gpPointDetail(e)`
- L10073 `gpRepTable(e)`
- L10080 `gpKpis(model)`
- L10089 `gpWeekData(model,w)` — Datos de una semana de gimnasio (series por músculo y sesiones).
- L10094 `gpWeekLabel(w,short)`
- L10095 `gpWeekly(model)`
- L10114 `gpMuscles(model)`
- L10122 `gpHeat(model)` — v69: «Constancia» — mapa de días entrenados (como antes), con días de la semana, meses, intensidad y detalle al tocar.
- L10142 `gpExList(model)`
- L10149 `gpExDetail(model)`
- L10162 `gpDayFood(dt)`
- L10163 `gpNutrition(model)`
- L10170 `gpRecentPRs(model)`
- L10174 `gpSessions(model)`
- L10180 `gpSessionModal(id)`
- L10191 `gpWeekModal(w)`
- L10198 `gpSelect(key)`
- L10199 `gpClick(e)`
- L10215 `renderGym()`
- L10235 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L10244 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L10250 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L10275 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L10279 `showHelp()`
- L10283 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L10285 `markBackup()`
- L10289 `exportJSON()`
- L10294 `drawBackupReminder()`
- L10304 `applyDensity()`
- L10316 `syncDayComplete()`
- L10319 `drawMeals()` — Comidas del día de un vistazo.
- L10327 `filterLog()` — Buscador de Registro.
- L10340 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L10346 `recentFoods()`
- L10351 `quickChip(e,fav)`
- L10369 `drawQuickFoods()`
- L10398 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L10402 `toggleAddPanel(id)`
- L10415 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L10426 `pasteMessage(text,ok)`
- L10434 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L10445 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L10456 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L10462 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L10483 `storableState()`

### Render único: actualiza toda la página

- L10491 `nearView(el)`
- L10493 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L10497 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L10528 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L10529 constante `REF_TABLE`
- L10536 `refTargets(mode)`
- L10537 `syncMicroMode()`
- L10550 `mealByHour(h=new Date()`
- L10557 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L10568 `dataSummary(s)`
- L10572 `confirmImport(next,name)`
- L10579 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L10585 `checkUpdate()`
- L10590 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L10605 constante `GAP_PREFER`
- L10606 constante `GAP_SKIP`
- L10607 constante `GAP_UNIT`
- L10608 `gapQty(f,x)`
- L10609 `gapFoods(key,gap,ctx)`
- L10628 `weekSources(key,sum)`
- L10634 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L10647 `gapRow(x,open,meal,sum,ctx)`
- L10663 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L10688 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L10689 `isFemale(s=state)`
- L10690 `sexLabel(s=state)`
- L10691 `sexBadge(sex)`
- L10693 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L10694 constante `OPT_FEMALE`
- L10705 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba.
- L10706 `applySexOpt(sex)`
- L10708 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L10713 `cleanPreset(p,fb)`
- L10717 `dayNamesFor(types)`
- L10719 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L10729 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L10737 `profV()`
- L10738 `isTrainDay(i)`
- L10739 `activityName(i)`
- L10740 `dayFaf(i)`
- L10741 `presetDesc(cfg,shake)`
- L10745 `profileDescription()`
- L10753 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L10755 `wizCatalog()`
- L10756 `wizOpen(opts={})`
- L10771 `wizTitle()`
- L10772 `wizPaint(sameStep=true)`
- L10781 `wizSync()`
- L10794 `wizFoodOptions()`
- L10797 `wizPresetSummary(cfg,whey)`
- L10802 `wizPresetHTML(kind)`
- L10810 `wizPreview()`
- L10821 `wizHTML()`
- L10862 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L10946 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L10947 constante `SUPP_CATALOG`
- L10969 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L10970 constante `PEAT_BREAKFAST`
- L10971 constante `PEAT_SHAKE`
- L10973 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L10980 `benfoUser()`
- L10982 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L10998 `ico(n)`
- L11000 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L11009 `showTour(i=0)`
- L11021 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L11022 `hubAction(v)`
- L11030 constante `FORM_URL` — Llegan solas a una hoja de Google (formulario del creador de la app). Sin cuentas ni datos personales.
- L11031 constante `FORM_FIELDS`
- L11032 constante `FB_CATS`
- L11034 `openFeedback()`
- L11038 `feedbackData()`
- L11045 `feedbackText()`
- L11046 `sendFeedback()`
- L11059 `shareFeedback()`
- L11076 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L11083 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L11091 constante `I18N_EN`

### v59: idioma (español / inglés)

- L12809 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L12810 constante `WD_EN`
- L12811 `trOne(s)`
- L12819 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L12820 constante `ES_FOOD_GYM`
- L12857 `trFood(s)`
- L12869 constante `TR_TPL`
- L12908 `trLower(s)`
- L12909 `trTpl(s,attr)`
- L12910 constante `FOOD_SEL`
- L12911 `trText(s,attr=false)`
- L12921 `trNode(n)`
- L12940 `trEl(el)`
- L12953 `trTree(root)`
- L12962 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L12976 `setLang(l,quiet)`
- L12989 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter), solo en la web publicada

- L12998 constante `GC_CODE`
- L12999 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L13009 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L13010 `packMove()`
- L13018 `unpackMove(code)`
- L13027 `moveData()`
- L13037 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L13043 `checkMove(code)`
- L13062 `aiFrameworkLines()` — v69: marco de referencia del informe para IA. Así cualquier IA, aunque no conozca la app ni al usuario, sabe con qué comparar.

### Arranque

