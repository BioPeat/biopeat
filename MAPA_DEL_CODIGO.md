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
- L7369 `photoPrompt(meal,note)`
- L7372 `resetPhoto()`
- L7383 `openPhoto()`
- L7389 `shrinkPhoto(file)`
- L7392 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L7418 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L7425 `cleanFood(id,f)`
- L7429 `migrateBase(o)`
- L7448 `download(name,text,type)`
- L7457 `portable()`
- L7498 `syncAppIcons()`
- L7506 `downloadAppIcons()`
- L7543 constante `PROFILES_KEY`
- L7545 `ensureProfilesStore()`
- L7565 `resetProfileSessionUI()`
- L7572 `saveProfilesStore(st)`
- L7581 `syncCurrentProfileToStore(rawStr)`
- L7587 `activeProfileName()`
- L7591 `renderProfilesList()`
- L7633 `switchProfile(id)`
- L7655 `deleteProfileById(id)`
- L7680 `refreshDrawerSummary()`
- L7697 `toggleLeftDrawer(force)`
- L7712 `buildAIExportText(rangeOverride)`
- L7963 `copyAIExport()`
- L7977 `downloadAIExport()`
- L7986 `renderDrawerChat()`
- L8005 `buildDrawerChatContext()`
- L8042 `buildDrawerChatPrompt(question)`
- L8054 `askDrawerAI(rawQuestion)`
- L8143 `storageStatus()`
- L8149 `idbReadWrite(mode,value,key='current')`
- L8150 `openDB()`
- L8151 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L8164 `setQuantity(id,value,msg='Cantidad actualizada')`
- L8168 `niceStep(v)`
- L8169 `stepQuantity(id,dir)`
- L8223 `renderAppInfo()`
- L8238 `init()`
- L8266 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L8268 `setNav(v)`
- L8273 `go(v,focus)`
- L8284 constante `THEME_KEY`
- L8285 constante `SUN_SVG`
- L8286 constante `MOON_SVG`
- L8288 `syncThemeUI()`
- L8300 `toggleTheme()`
- L8309 `syncLogoTheme()`
- L8320 `applyMenuBtnState()`
- L8343 `syncDatePill()`
- L8356 `clampBtnPos(el,x,y)`
- L8366 `bindDraggableBtn(el,storeKey)`
- L8451 `bindDrawerGestures()`
- L8488 `animateValue(el,to,suffix='%',digits=0)`
- L8497 `tick(now)`
- L8500 `macroCard(key,name,color)`
- L8501 `renderToday()`
- L8524 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L8526 constante `HOME`
- L8528 `coachCandidates()`
- L8534 `coachIdeas(t,g,ref,meal)`
- L8547 `renderCoach()`
- L8567 `coachPrompt()`
- L8576 `nutrientDetailStandard(key)`
- L8590 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L8596 `upgradeTo12(s,o)`
- L8601 `benfotiamineTotals(entries=effectiveEntries()`
- L8610 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L8612 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L8624 `microStat(m,t=totals()`
- L8629 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L8637 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L8638 `ratioInfo(key,t=totals()`
- L8677 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L8694 constante `RATIO_ENDS`
- L8696 `ratioZones(i)` — v68: cada equilibrio tiene una zona «aceptable» (ni verde ni mala) y su meta visible en la tarjeta.
- L8704 `ratioTone(i)`
- L8709 constante `NEAR_HEAD`
- L8710 `ratioBar(i,big=false)`
- L8719 `ratioNeedBase(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L8737 `needHTML(i,t)`
- L8738 `ratioNeed(i,t=totals()`
- L8742 `adBalance(t=totals()`
- L8769 `zncuSuppKey()`
- L8770 `zncuSuppCfg()`
- L8792 `zncuDoseLabel(zn,cu)`
- L8795 `hasZncuSupp(d=day()`
- L8800 `toggleZncuSupp()`
- L8820 `openZncuConfig()`
- L8826 `renderRatios()`
- L8837 `ratioDetail(key)`
- L8854 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L8871 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L8886 `renderMicroMap()`
- L8890 `nutrientDetailForDay(key)`
- L8895 `editTargetsForm()`
- L8905 `mealData()`
- L8910 `renderMealSegments()`
- L8918 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L8953 constante `FAT_KEYS`
- L8955 `fatData(entries=effectiveEntries()`
- L8961 `energyData(entries=effectiveEntries()`
- L8965 `segmentedBar(items,total,attr)`
- L8969 `renderMealChart()`
- L8974 `renderFat()`
- L8982 `fatDetail(key)`
- L8987 `energyDetail(key)`
- L8994 `portionCandidates(q='')`
- L8999 `openPortion()`
- L9012 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L9027 `templates()`
- L9031 `renderExtra()`
- L9042 `updateExtra(reset=true)`
- L9054 `addExtra(id,amount)`
- L9070 `shakePreview()`
- L9071 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L9086 constante `LENS`
- L9092 `lensKey(key)`
- L9093 `lensHTML(key)`
- L9097 `appendLens(key)`
- L9106 `weekDates()`

### IA en la página: conexión directa o por servidor

- L9116 constante `MEAL_WORD`
- L9117 `mealOfWord(w)`
- L9118 `mealFromText(raw,fallback)`
- L9122 `canonMeal(v,fallback)`
- L9130 `localMeal(raw,meal)`
- L9136 constante `AI_FALLBACK`
- L9137 constante `GEMINI_DEFAULTS`
- L9138 constante `GROQ_DEFAULTS`
- L9139 `aiTaskProfile(task,hasImg=false)`
- L9146 `geminiThinkLevel(model,want)`
- L9152 `supportsGeminiTemp(model)`
- L9153 `readSSE(res,onEvent)`
- L9172 `applyAIConfig(raw)`
- L9198 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L9199 `callGemini(model,key,prompt,img,signal,opts={})`
- L9245 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), Groq (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L9253 `aiProv(m=$('ai-mode')`
- L9254 `aiBase(mode)`
- L9263 `chatHeaders(mode,key)`
- L9270 `callChat(mode,model,key,prompt,img,signal,opts={})` — ChatGPT, Claude, Groq, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L9324 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L9339 constante `MODEL_PREF`
- L9340 `pickModel(ids,mode=$('ai-mode')`
- L9354 `ensureModel(st)`
- L9370 `syncProvider()`
- L9389 `requestAI(prompt,img,signal,modelOverride='',onStep=null,opts={})`
- L9425 constante `AI_PREF`
- L9426 `aiConnected()`
- L9427 `syncAI()`
- L9429 `saveAIPrefs()`
- L9430 `loadAIPrefs()`
- L9431 `openAISetup()`
- L9438 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L9445 constante `MACROS`
- L9447 `cleanGoals(o,fallback)`
- L9452 `cleanCompare(o={})`
- L9456 `snapshotDay(d,reference='saved')`
- L9461 `upgradeTo17(s,o)`
- L9466 `entriesFor(d,source=weekSource)`
- L9470 `dayRow(dt,source=weekSource)`
- L9474 `goalsFor(dt)`
- L9480 `metricValue(r,key)`
- L9486 `targetOf(dt,key)`
- L9490 `weekSummary()`
- L9494 `aggregate(key,summary=weekSummary()`
- L9498 `tone(pct,mode='macro')`
- L9505 `pctText(a)`
- L9506 `weekProgress(a,color)`
- L9507 `renderWeekMicros(s)`
- L9519 `ratioAggregate(s,num,den)`
- L9523 `renderWeekRatios(s)`
- L9529 `renderWeekTable(s)`
- L9530 `weeklyDetail(key,oneDate=null)`
- L9539 `weekRatioDetail(key)`
- L9547 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L9553 `openDay(dt)`
- L9591 `withDayGoals(fn)`
- L9596 `renderMicros()`
- L9597 `nutrientDetail(key)`
- L9598 `editTargets()`
- L9599 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L9609 `summaryFor(start)`
- L9613 `ringSVG(pct,color,marker)`
- L9615 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L9619 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L9636 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L9637 `macroTone(p)`
- L9638 `dayMacroPct(dt,k)`
- L9639 `renderWeekly()`
- L9662 `weekDetail(dt,picked)`
- L9670 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L9680 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L9686 `sparkline(pts)`
- L9692 `renderCalendar()`
- L9709 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L9710 `splitMeals(raw)`
- L9720 `localDay(raw,fallback)`
- L9727 `promptDay(raw,fallback)`
- L9728 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L9766 `parseCsv(text)`
- L9781 `hevyDate(value,format='auto')`
- L9798 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L9813 constante `GYM_APPS`
- L9815 `gymSig(headers)`
- L9816 `gymApp(headers)`
- L9817 `hevyMapping()`
- L9818 `gymSaved()`
- L9819 `renderMapping(parsed)`
- L9836 `optionalNum(v,min=0,max=1e7)`
- L9841 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L9848 `buildHevy(parsed,map)`
- L9882 `cleanWorkout(s)`
- L9889 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L9904 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L9905 constante `GP_ALIAS`
- L9915 `gpNorm(s)`
- L9916 `gpKey(name)`
- L9920 `gpF(n,d=0)`
- L9921 `gpDate(d,opt)`
- L9922 `gpMonday(d)`
- L9923 constante `GP_GROUPS`
- L9938 constante `GP_COLORS`
- L9939 `gpGroup(name)`
- L9940 `gpWorkSets(s)`
- L9941 `gpModel()`
- L9965 `gpSessionMetrics(e,sets)`
- L9980 constante `GP_METRICS`
- L9985 `gpMetricsFor(e)`
- L9986 `gpRangeHist(e)`
- L9987 `gpPRs(model)`
- L10010 `gpStatus(e)`
- L10028 `gpNext(e)`
- L10036 `gpChart(e)`
- L10064 `gpPointDetail(e)`
- L10070 `gpRepTable(e)`
- L10077 `gpKpis(model)`
- L10086 `gpWeekData(model,w)` — Datos de una semana de gimnasio (series por músculo y sesiones).
- L10091 `gpWeekLabel(w,short)`
- L10092 `gpWeekly(model)`
- L10111 `gpMuscles(model)`
- L10119 `gpHeat(model)` — v69: «Constancia» — mapa de días entrenados (como antes), con días de la semana, meses, intensidad y detalle al tocar.
- L10139 `gpExList(model)`
- L10146 `gpExDetail(model)`
- L10159 `gpDayFood(dt)`
- L10160 `gpNutrition(model)`
- L10167 `gpRecentPRs(model)`
- L10171 `gpSessions(model)`
- L10177 `gpSessionModal(id)`
- L10188 `gpWeekModal(w)`
- L10195 `gpSelect(key)`
- L10196 `gpClick(e)`
- L10212 `renderGym()`
- L10232 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L10241 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L10247 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L10272 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L10276 `showHelp()`
- L10280 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L10282 `markBackup()`
- L10286 `exportJSON()`
- L10291 `drawBackupReminder()`
- L10301 `applyDensity()`
- L10313 `syncDayComplete()`
- L10316 `drawMeals()` — Comidas del día de un vistazo.
- L10324 `filterLog()` — Buscador de Registro.
- L10337 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L10343 `recentFoods()`
- L10348 `quickChip(e,fav)`
- L10366 `drawQuickFoods()`
- L10395 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L10399 `toggleAddPanel(id)`
- L10412 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L10423 `pasteMessage(text,ok)`
- L10431 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L10442 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L10453 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L10459 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L10480 `storableState()`

### Render único: actualiza toda la página

- L10488 `nearView(el)`
- L10490 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L10494 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L10525 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L10526 constante `REF_TABLE`
- L10533 `refTargets(mode)`
- L10534 `syncMicroMode()`
- L10547 `mealByHour(h=new Date()`
- L10554 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L10565 `dataSummary(s)`
- L10569 `confirmImport(next,name)`
- L10576 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L10582 `checkUpdate()`
- L10587 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L10602 constante `GAP_PREFER`
- L10603 constante `GAP_SKIP`
- L10604 constante `GAP_UNIT`
- L10605 `gapQty(f,x)`
- L10606 `gapFoods(key,gap,ctx)`
- L10625 `weekSources(key,sum)`
- L10631 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L10644 `gapRow(x,open,meal,sum,ctx)`
- L10660 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L10685 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L10686 `isFemale(s=state)`
- L10687 `sexLabel(s=state)`
- L10688 `sexBadge(sex)`
- L10690 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L10691 constante `OPT_FEMALE`
- L10702 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba.
- L10703 `applySexOpt(sex)`
- L10705 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L10710 `cleanPreset(p,fb)`
- L10714 `dayNamesFor(types)`
- L10716 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L10726 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L10734 `profV()`
- L10735 `isTrainDay(i)`
- L10736 `activityName(i)`
- L10737 `dayFaf(i)`
- L10738 `presetDesc(cfg,shake)`
- L10742 `profileDescription()`
- L10750 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L10752 `wizCatalog()`
- L10753 `wizOpen(opts={})`
- L10768 `wizTitle()`
- L10769 `wizPaint(sameStep=true)`
- L10778 `wizSync()`
- L10791 `wizFoodOptions()`
- L10794 `wizPresetSummary(cfg,whey)`
- L10799 `wizPresetHTML(kind)`
- L10807 `wizPreview()`
- L10818 `wizHTML()`
- L10859 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L10943 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L10944 constante `SUPP_CATALOG`
- L10966 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L10967 constante `PEAT_BREAKFAST`
- L10968 constante `PEAT_SHAKE`
- L10970 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L10977 `benfoUser()`
- L10979 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L10995 `ico(n)`
- L10997 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L11006 `showTour(i=0)`
- L11018 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L11019 `hubAction(v)`
- L11027 constante `FORM_URL` — Llegan solas a una hoja de Google (formulario del creador de la app). Sin cuentas ni datos personales.
- L11028 constante `FORM_FIELDS`
- L11029 constante `FB_CATS`
- L11031 `openFeedback()`
- L11035 `feedbackData()`
- L11042 `feedbackText()`
- L11043 `sendFeedback()`
- L11056 `shareFeedback()`
- L11073 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L11080 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L11088 constante `I18N_EN`

### v59: idioma (español / inglés)

- L12806 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L12807 constante `WD_EN`
- L12808 `trOne(s)`
- L12816 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L12817 constante `ES_FOOD_GYM`
- L12854 `trFood(s)`
- L12866 constante `TR_TPL`
- L12905 `trLower(s)`
- L12906 `trTpl(s,attr)`
- L12907 constante `FOOD_SEL`
- L12908 `trText(s,attr=false)`
- L12918 `trNode(n)`
- L12937 `trEl(el)`
- L12950 `trTree(root)`
- L12959 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L12973 `setLang(l,quiet)`
- L12986 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter), solo en la web publicada

- L12995 constante `GC_CODE`
- L12996 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L13006 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L13007 `packMove()`
- L13015 `unpackMove(code)`
- L13024 `moveData()`
- L13034 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L13040 `checkMove(code)`
- L13059 `aiFrameworkLines()` — v69: marco de referencia del informe para IA. Así cualquier IA, aunque no conozca la app ni al usuario, sabe con qué comparar.

### Arranque

