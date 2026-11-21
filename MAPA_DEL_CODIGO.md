# MAPA DEL CÓDIGO · BioPeat v76 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (989 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-6398; todo el JavaScript en `<script id="app">` (desde la línea 6399).

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

- L6464 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L6465 constante `AZUCAR_N`
- L6466 constante `USDA_N`
- L6472 constante `FOODS`
- L6474 constante `BASE_FAT_FIX`
- L6478 constante `REF_COLS` — Base de referencia verificada (USDA FoodData Central / BEDCA, por 100 g o 100 ml comestibles).
- L6479 constante `REF_RAW`
- L6644 constante `REF_MAP`
- L6645 constante `REF_CACHE`
- L6647 `ensureRefIndex()`
- L6654 `refNutrients(id)`
- L6662 constante `STRIP_PREP_RE`
- L6663 `findRef(text,strict=false)`
- L6686 `refCatalogCompact()`
- L6687 `fromRef(id,amount,meal,note='',srcText='')`
- L6692 constante `EXTRA`
- L6693 constante `KEYS`
- L6695 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L6697 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L6701 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6702 constante `OPT`
- L6728 constante `LIMIT`
- L6729 `optInfo(k,goal)`
- L6736 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6744 `optLine(k,goal,unit)`
- L6751 `optRefHTML(k,goal,unit)`
- L6753 constante `DAYS`
- L6754 constante `FAF`
- L6756 constante `LOC`
- L6760 `number(v,min=0,max=1e6)`
- L6766 `decimalInputs(root=document)`
- L6767 `localDate(d=new Date()`
- L6768 `validDate(s)`
- L6773 `shift(s,n)`
- L6781 `stripProto(o)`
- L6788 `cleanBio(b)`
- L6797 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6799 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6805 constante `DAY_TYPES`
- L6806 constante `NEW_V54`
- L6810 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6813 `bmr(w=state.profile.weight)` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6819 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6844 `cleanNutrients(o,required=false)`
- L6856 `cleanEntry(e)`
- L6861 `cleanPlan(p)`
- L6865 `planEntry(p)`
- L6874 `seedPlan(d,whichDate)`
- L6878 `ensureDay(d=date)`
- L6885 `effectiveEntries(d=day()`
- L6886 constante `SALTED_IDS`
- L6887 constante `SWEET_RE`
- L6888 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6906 `inferredNutrients(e)`
- L6948 `totals(entries)`
- L6960 `change(fn,message='Guardado')`
- L6964 `undo()`
- L6972 `toast(text,canUndo=false)`
- L6980 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6981 `onClick(fn)`
- L6983 `attempt(fn)`
- L6987 `modal(title,body)`
- L6996 `modalRestore()`
- L7006 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L7007 `modalBack()`
- L7008 `goDate(d)`
- L7015 `renderHeader()`
- L7028 `renderRows(entries)`
- L7032 `entryValues(e)`
- L7033 `renderLog()`
- L7040 `fromFood(id,amount,meal)`
- L7046 `pantryId(name)`
- L7048 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L7064 `addEntries(entries,message='Añadido',d=date,opts={})`
- L7073 `recipe(kind)`
- L7080 `summary(entries)`
- L7084 `renderPresetInfo()`
- L7097 `stripCode(raw)`
- L7103 `sanitizeNutrients(o,grams=100,fallbackRefId='')`
- L7130 `parseBIO(raw,meal=$('meal-select')`
- L7142 `parseSmart(raw)`
- L7146 constante `COUNT`
- L7147 constante `UNIT_RE`
- L7199 `offToNutrients(nut={},fallbackName='')` — Open Food Facts (gratis, sin clave, CORS nativo): consulta por código de barras o texto.
- L7220 `lookupOFFBarcode(code,signal,ms=3200)`
- L7235 `searchOFF(query,signal,ms=4500)`
- L7253 `openProductSearch()`
- L7291 `nutrientFields(n,prefix='n_')`
- L7292 `readNutrients(form,prefix='n_')`
- L7297 `editEntry(id)`
- L7306 `editFood(id,pending=null)`
- L7311 `usageStats(days=90)`
- L7319 `renderFoods(forceList=false)`
- L7331 `nutrientSources(key)`
- L7338 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L7339 `suppSlot(meal)`
- L7340 `renderSupps()`
- L7355 `editPlan(id)`
- L7362 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L7383 `makePrompt(meal='Comida',note='')`
- L7388 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L7392 `pantryCompact()`
- L7396 constante `MEAL_AI_SCHEMA`
- L7436 `mealSystemPrompt(usePhoto)`
- L7452 `hydrateAIItems(rawItems,fallback,usePhoto,aiModel,signal)`
- L7495 `photoPrompt(meal,note)`
- L7498 `resetPhoto()`
- L7509 `openPhoto()`
- L7515 `shrinkPhoto(file)`
- L7518 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L7544 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L7551 `cleanFood(id,f)`
- L7555 `migrateBase(o)`
- L7575 `download(name,text,type)`
- L7584 `portable()`
- L7625 `syncAppIcons()`
- L7633 `downloadAppIcons()`
- L7670 constante `PROFILES_KEY`
- L7672 `ensureProfilesStore()`
- L7692 `resetProfileSessionUI()`
- L7699 `saveProfilesStore(st)`
- L7708 `syncCurrentProfileToStore(snapObj=null,immediate=true)`
- L7719 `activeProfileName()`
- L7723 `renderProfilesList()`
- L7765 `switchProfile(id)`
- L7787 `deleteProfileById(id)`
- L7812 `refreshDrawerSummary()`
- L7829 `toggleLeftDrawer(force)`
- L7844 `buildAIExportText(rangeOverride)`
- L8099 `copyAIExport()`
- L8113 `downloadAIExport()`
- L8122 `renderDrawerChat()`
- L8141 `buildDrawerChatContext()`
- L8180 `buildDrawerChatPrompt(question)`
- L8192 `askDrawerAI(rawQuestion)`
- L8281 constante `CLOUD_OFF_KEY`
- L8292 `bytesToB64(u8)`
- L8293 `b64ToBytes(s)`
- L8294 `bytesToB64Url(u8)`
- L8295 `sha256Hex(str)`
- L8296 `sha256Bytes(str)`
- L8297 `generateSyncKey()`
- L8298 `ensureSyncKey()`
- L8299 `mirrorSyncKey(k)`
- L8300 `deriveSyncCreds(keyStr)`
- L8306 `hasMeaningfulData()`
- L8313 `buildCloudBundle()`
- L8320 `encryptVaultPayload(obj,keyStr)`
- L8328 `readDecompressedText(bytes,maxBytes=10*1024*1024)`
- L8344 `decryptVaultPayload(resp,keyStr)`
- L8356 `bundleHash(bundle)`
- L8360 `applyCloudBundle(o,rev=1)`
- L8370 `cloudPull(keyStr,opts={})`
- L8390 `cloudPush(opts={})`
- L8427 `scheduleCloudPush()`
- L8433 `scheduleAutoCloudPull(delayMs=120)`
- L8447 `saveSyncToPassMgr()`
- L8454 `trySilentPassMgrRecovery()`
- L8464 `extractSyncKeyInput(val)`
- L8470 `applySyncKey(rawKey,opts={})`
- L8491 `takeSyncCode()`
- L8502 `renderCloudStatus()`
- L8519 `openCloudLinkModal()`
- L8522 `copyMagicSyncLink()`
- L8529 `deleteCloudBackup(confirmed=false)`
- L8564 `mirrorToIDB(raw,profRaw)`
- L8567 `storageStatus()`
- L8574 `idbReadWrite(mode,value,key='current')`
- L8575 `openDB()`
- L8577 `flushDeferredSave()`
- L8587 `save(skipCloud=false)`

### Eventos generales: añadir con un toque, editar, eliminar

- L8615 `setQuantity(id,value,msg='Cantidad actualizada')`
- L8619 `niceStep(v)`
- L8620 `stepQuantity(id,dir)`
- L8674 `renderAppInfo(force=false)`
- L8691 `init()`
- L8727 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L8729 `setNav(v)`
- L8734 `go(v,focus)`
- L8745 constante `THEME_KEY`
- L8746 constante `SUN_SVG`
- L8747 constante `MOON_SVG`
- L8749 `syncThemeUI()`
- L8761 `toggleTheme()`
- L8770 `syncLogoTheme()`
- L8781 `applyMenuBtnState()`
- L8804 `syncDatePill()`
- L8817 `clampBtnPos(el,x,y)`
- L8827 `bindDraggableBtn(el,storeKey)`
- L8912 `bindDrawerGestures()`
- L8950 `animateValue(el,to,suffix='%',digits=0)`
- L8959 `tick(now)`
- L8962 `macroCard(key,name,color)`
- L8963 `renderToday()`
- L8987 `renderBio()`
- L9012 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L9014 constante `HOME`
- L9016 `coachCandidates()`
- L9022 `coachIdeas(t,g,ref,meal)`
- L9035 `coachQuickAdd(key)`
- L9043 `renderCoach()`
- L9063 `coachPrompt()`
- L9072 `nutrientDetailStandard(key)`
- L9087 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L9093 `upgradeTo12(s,o)`
- L9098 `benfotiamineTotals(entries=effectiveEntries()`
- L9107 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L9109 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L9121 `microStat(m,t=totals()`
- L9126 `metric(m,t=totals()`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L9133 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L9134 `ratioInfo(key,t=totals()`
- L9173 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L9190 constante `RATIO_ENDS`
- L9192 `ratioZones(i)` — v68: cada equilibrio tiene una zona «aceptable» (ni verde ni mala) y su meta visible en la tarjeta.
- L9200 `ratioTone(i)`
- L9205 constante `NEAR_HEAD`
- L9206 `ratioBar(i,big=false)`
- L9215 `ratioNeedBase(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L9233 `needHTML(i,t)`
- L9234 `ratioNeed(i,t=totals()`
- L9238 `adBalance(t=totals()`
- L9265 `zncuSuppKey()`
- L9266 `zncuSuppCfg()`
- L9288 `zncuDoseLabel(zn,cu)`
- L9291 `hasZncuSupp(d=day()`
- L9296 `toggleZncuSupp()`
- L9316 `openZncuConfig()`
- L9322 `renderRatios()`
- L9333 `ratioDetail(key)`
- L9350 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L9367 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L9382 `renderMicroMap(t=totals()`
- L9386 `nutrientDetailForDay(key)`
- L9391 `editTargetsForm()`
- L9401 `mealData()`
- L9406 `renderMealSegments()`
- L9414 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L9449 constante `FAT_KEYS`
- L9451 `fatData(entries=effectiveEntries()`
- L9457 `energyData(entries=effectiveEntries()`
- L9461 `segmentedBar(items,total,attr)`
- L9465 `renderMealChart()`
- L9470 `renderFat()`
- L9478 `fatDetail(key)`
- L9483 `energyDetail(key)`
- L9490 `portionCandidates(q='')`
- L9495 `openPortion()`
- L9508 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L9523 `templates()`
- L9527 `renderExtra()`
- L9538 `updateExtra(reset=true)`
- L9550 `addExtra(id,amount)`
- L9566 `shakePreview()`
- L9567 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L9582 constante `LENS`
- L9588 `lensKey(key)`
- L9589 `lensHTML(key)`
- L9593 `appendLens(key)`
- L9602 `weekDates()`

### IA en la página: conexión directa o por servidor

- L9612 constante `MEAL_WORD`
- L9613 `mealOfWord(w)`
- L9614 `mealFromText(raw,fallback)`
- L9618 `canonMeal(v,fallback)`
- L9626 `localMeal(raw,meal)`
- L9632 constante `AI_FALLBACK`
- L9633 constante `GEMINI_DEFAULTS`
- L9634 constante `GROQ_DEFAULTS`
- L9635 `aiTaskProfile(task,hasImg=false)`
- L9642 `geminiThinkLevel(model,want)`
- L9648 `supportsGeminiTemp(model)`
- L9649 `readSSE(res,onEvent)`
- L9668 `applyAIConfig(raw)`
- L9694 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L9695 `callGemini(model,key,prompt,img,signal,opts={})`
- L9741 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), Groq (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L9749 `aiProv(m=$('ai-mode')`
- L9750 `aiBase(mode)`
- L9759 `chatHeaders(mode,key)`
- L9766 `callChat(mode,model,key,prompt,img,signal,opts={})` — ChatGPT, Claude, Groq, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L9820 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L9835 constante `OLD_GEMINI_RE`
- L9836 constante `MODEL_PREF`
- L9837 `pickModel(ids,mode=$('ai-mode')`
- L9851 `ensureModel(st)`
- L9867 `syncProvider()`
- L9886 `requestAI(prompt,img,signal,modelOverride='',onStep=null,opts={})`
- L9923 constante `AI_PREF`
- L9924 `aiConnected()`
- L9925 `syncAI()`
- L9927 `saveAIPrefs()`
- L9928 `loadAIPrefs()`
- L9929 `openAISetup()`
- L9936 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L9943 constante `MACROS`
- L9945 `cleanGoals(o,fallback)`
- L9950 `cleanCompare(o={})`
- L9954 `snapshotDay(d,reference='saved')`
- L9959 `upgradeTo17(s,o)`
- L9964 `entriesFor(d,source=weekSource)`
- L9968 `dayRow(dt,source=weekSource)`
- L9972 `goalsFor(dt)`
- L9978 `metricValue(r,key)`
- L9984 `targetOf(dt,key)`
- L9988 `weekSummary()`
- L9992 `aggregate(key,summary=weekSummary()`
- L9996 `tone(pct,mode='macro')`
- L10003 `pctText(a)`
- L10004 `weekProgress(a,color)`
- L10005 `renderWeekMicros(s)`
- L10017 `ratioAggregate(s,num,den)`
- L10021 `renderWeekRatios(s)`
- L10027 `renderWeekTable(s)`
- L10028 `weeklyDetail(key,oneDate=null)`
- L10037 `weekRatioDetail(key)`
- L10045 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L10051 `openDay(dt)`
- L10089 `withDayGoals(fn)`
- L10094 `renderMicros()`
- L10095 `nutrientDetail(key)`
- L10096 `editTargets()`
- L10097 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L10107 `summaryFor(start)`
- L10111 `ringSVG(pct,color,marker)`
- L10113 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L10117 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L10134 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L10135 `macroTone(p)`
- L10136 `dayMacroPct(dt,k)`
- L10137 `renderWeekly()`
- L10160 `weekDetail(dt,picked)`
- L10168 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L10178 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L10184 `sparkline(pts)`
- L10190 `renderCalendar()`
- L10207 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L10208 `splitMeals(raw)`
- L10218 `localDay(raw,fallback)`
- L10225 `promptDay(raw,fallback)`
- L10226 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L10265 `parseCsv(text)`
- L10280 `hevyDate(value,format='auto')`
- L10297 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L10312 constante `GYM_APPS`
- L10314 `gymSig(headers)`
- L10315 `gymApp(headers)`
- L10316 `hevyMapping()`
- L10317 `gymSaved()`
- L10318 `renderMapping(parsed)`
- L10335 `optionalNum(v,min=0,max=1e7)`
- L10340 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L10347 `buildHevy(parsed,map)`
- L10381 `cleanWorkout(s)`
- L10388 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L10403 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L10404 constante `GP_ALIAS`
- L10414 `gpNorm(s)`
- L10415 `gpKey(name)`
- L10419 `gpF(n,d=0)`
- L10420 `gpDate(d,opt)`
- L10421 `gpMonday(d)`
- L10422 constante `GP_GROUPS`
- L10437 constante `GP_COLORS`
- L10438 `gpGroup(name)`
- L10439 `gpWorkSets(s)`
- L10440 `gpModel()`
- L10464 `gpSessionMetrics(e,sets)`
- L10479 constante `GP_METRICS`
- L10484 `gpMetricsFor(e)`
- L10485 `gpRangeHist(e)`
- L10486 `gpPRs(model)`
- L10509 `gpStatus(e)`
- L10527 `gpNext(e)`
- L10535 `gpChart(e)`
- L10563 `gpPointDetail(e)`
- L10569 `gpRepTable(e)`
- L10576 `gpKpis(model)`
- L10585 `gpWeekData(model,w)` — Datos de una semana de gimnasio (series por músculo y sesiones).
- L10590 `gpWeekLabel(w,short)`
- L10591 `gpWeekly(model)`
- L10610 `gpMuscles(model)`
- L10618 `gpHeat(model)` — v69: «Constancia» — mapa de días entrenados (como antes), con días de la semana, meses, intensidad y detalle al tocar.
- L10638 `gpExList(model)`
- L10645 `gpExDetail(model)`
- L10658 `gpDayFood(dt)`
- L10659 `gpNutrition(model)`
- L10666 `gpRecentPRs(model)`
- L10670 `gpSessions(model)`
- L10676 `gpSessionModal(id)`
- L10687 `gpWeekModal(w)`
- L10694 `gpSelect(key)`
- L10695 `gpClick(e)`
- L10711 `renderGym()`
- L10731 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L10740 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L10746 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L10771 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L10775 `showHelp()`
- L10779 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L10781 `markBackup()`
- L10785 `exportJSON()`
- L10790 `drawBackupReminder()`
- L10800 `applyDensity()`
- L10812 `syncDayComplete()`
- L10815 `drawMeals()` — Comidas del día de un vistazo.
- L10823 `filterLog()` — Buscador de Registro.
- L10836 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L10842 `recentFoods()`
- L10847 `quickChip(e,fav)`
- L10865 `drawQuickFoods()`
- L10894 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L10898 `toggleAddPanel(id)`
- L10911 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L10922 `pasteMessage(text,ok)`
- L10930 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L10941 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L10952 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L10958 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L10979 `storableState()`

### Render único: actualiza toda la página

- L10988 `nearView(el)`
- L10990 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L10995 `scheduleLazyRender()`
- L10999 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L11036 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L11037 constante `REF_TABLE`
- L11044 `refTargets(mode)`
- L11045 `syncMicroMode()`
- L11058 `mealByHour(h=new Date()`
- L11065 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L11076 `dataSummary(s)`
- L11080 `confirmImport(next,name)`
- L11087 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L11093 `checkUpdate()`
- L11098 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L11113 constante `GAP_PREFER`
- L11114 constante `GAP_SKIP`
- L11115 constante `GAP_UNIT`
- L11116 `gapQty(f,x)`
- L11117 `gapFoods(key,gap,ctx)`
- L11136 `weekSources(key,sum)`
- L11142 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L11155 `gapRow(x,open,meal,sum,ctx)`
- L11171 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L11196 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L11197 `isFemale(s=state)`
- L11198 `sexLabel(s=state)`
- L11199 `sexBadge(sex)`
- L11201 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L11202 constante `OPT_FEMALE`
- L11213 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba; A (1.500 µg = 5.000 UI) y D (50 µg = 2.000 UI) mantienen A:D en zona verde (2,5:1).
- L11214 `applySexOpt(sex)`
- L11216 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L11221 `cleanPreset(p,fb)`
- L11225 `dayNamesFor(types)`
- L11227 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L11237 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L11245 `profV()`
- L11246 `isTrainDay(i)`
- L11247 `activityName(i)`
- L11248 `dayFaf(i)`
- L11249 `presetDesc(cfg,shake)`
- L11253 `profileDescription()`
- L11261 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L11263 `wizCatalog()`
- L11264 `wizOpen(opts={})`
- L11280 `wizTitle()`
- L11281 `wizPaint(sameStep=true)`
- L11290 `wizSync()`
- L11309 `wizFoodOptions()`
- L11312 `wizPresetSummary(cfg,whey)`
- L11317 `wizPresetHTML(kind)`
- L11325 `wizPreview()`
- L11336 `wizLiveHTML()`
- L11340 `wizHTML()`
- L11386 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L11484 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L11485 constante `SUPP_CATALOG`
- L11510 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L11511 constante `PEAT_BREAKFAST`
- L11512 constante `PEAT_SHAKE`
- L11514 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L11521 `benfoUser()`
- L11523 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L11539 `ico(n)`
- L11541 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L11550 `showTour(i=0)`
- L11562 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L11563 `hubAction(v)`
- L11571 constante `FB_CATS` — Envíos anónimos directos al buzón de BioPeat (sin cuentas ni datos personales).
- L11573 `openFeedback()`
- L11577 `feedbackData()`
- L11584 `feedbackText()`
- L11585 `sendFeedback()`
- L11605 `shareFeedback()`
- L11622 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L11629 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L11637 constante `I18N_EN`

### v59: idioma (español / inglés)

- L13512 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L13513 constante `WD_EN`
- L13514 `trOne(s)`
- L13522 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L13523 constante `ES_FOOD_GYM`
- L13560 `trFood(s)`
- L13572 constante `TR_TPL`
- L13613 `trLower(s)`
- L13614 `trTpl(s,attr)`
- L13615 constante `FOOD_SEL`
- L13616 `trText(s,attr=false)`
- L13626 `trNode(n)`
- L13645 `trEl(el)`
- L13658 `trTree(root)`
- L13667 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L13681 `flushTr()`
- L13682 `syncTrObserver()`
- L13686 `setLang(l,quiet)`
- L13700 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter + Worker agregados), solo en la web publicada

- L13709 constante `GC_CODE`
- L13710 `pingAnalytics(extra={})`
- L13726 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L13738 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L13739 `packMove()`
- L13747 `unpackMove(code)`
- L13758 `moveData()`
- L13768 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L13774 `checkMove(code)`
- L13793 `aiFrameworkLines()` — v69: marco de referencia del informe para IA. Así cualquier IA, aunque no conozca la app ni al usuario, sabe con qué comparar.

### Arranque

