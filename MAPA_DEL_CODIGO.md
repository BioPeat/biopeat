# MAPA DEL CÓDIGO · BioPeat v78 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (1008 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-6482; todo el JavaScript en `<script id="app">` (desde la línea 6483).

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

- L6550 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L6551 constante `AZUCAR_N`
- L6552 constante `USDA_N`
- L6558 constante `FOODS`
- L6560 constante `BASE_FAT_FIX`
- L6564 constante `REF_COLS` — Base de referencia verificada (USDA FoodData Central / BEDCA, por 100 g o 100 ml comestibles).
- L6565 constante `REF_RAW`
- L6730 constante `REF_MAP`
- L6731 constante `REF_CACHE`
- L6733 `ensureRefIndex()`
- L6740 `refNutrients(id)`
- L6748 constante `STRIP_PREP_RE`
- L6749 `findRef(text,strict=false)`
- L6772 `refCatalogCompact()`
- L6773 `fromRef(id,amount,meal,note='',srcText='')`
- L6778 constante `EXTRA`
- L6779 constante `KEYS`
- L6781 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L6783 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L6787 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6788 constante `OPT`
- L6814 constante `LIMIT`
- L6815 `optInfo(k,goal)`
- L6822 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6830 `optLine(k,goal,unit)`
- L6837 `optRefHTML(k,goal,unit)`
- L6839 constante `DAYS`
- L6840 constante `FAF`
- L6842 constante `LOC`
- L6846 `number(v,min=0,max=1e6)`
- L6852 `decimalInputs(root=document)`
- L6853 `localDate(d=new Date()`
- L6854 `validDate(s)`
- L6859 `shift(s,n)`
- L6867 `stripProto(o)`
- L6874 `cleanBio(b)`
- L6883 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6885 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6891 constante `DAY_TYPES`
- L6892 constante `NEW_V54`
- L6896 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6899 `bmr(w=state.profile.weight)` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6905 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6930 `cleanNutrients(o,required=false)`
- L6942 `cleanEntry(e)`
- L6947 `cleanPlan(p)`
- L6951 `planEntry(p)`
- L6960 `seedPlan(d,whichDate)`
- L6964 `ensureDay(d=date)`
- L6971 `effectiveEntries(d=day()`
- L6972 constante `SALTED_IDS`
- L6973 constante `SWEET_RE`
- L6974 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6992 `inferredNutrients(e)`
- L7034 `totals(entries)`
- L7046 `change(fn,message='Guardado')`
- L7050 `undo()`
- L7058 `toast(text,canUndo=false)`
- L7066 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L7067 `onClick(fn)`
- L7069 `attempt(fn)`
- L7073 `modal(title,body)`
- L7082 `modalRestore()`
- L7092 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L7093 `modalBack()`
- L7094 `goDate(d)`
- L7101 `renderHeader()`
- L7114 `renderRows(entries)`
- L7118 `entryValues(e)`
- L7119 `renderLog()`
- L7126 `fromFood(id,amount,meal)`
- L7132 `pantryId(name)`
- L7134 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L7150 `addEntries(entries,message='Añadido',d=date,opts={})`
- L7159 `recipe(kind)`
- L7166 `summary(entries)`
- L7170 `renderPresetInfo()`
- L7183 `stripCode(raw)`
- L7189 `sanitizeNutrients(o,grams=100,fallbackRefId='')`
- L7216 `parseBIO(raw,meal=$('meal-select')`
- L7228 `parseSmart(raw)`
- L7232 constante `COUNT`
- L7233 constante `UNIT_RE`
- L7285 `offToNutrients(nut={},fallbackName='')` — Open Food Facts (gratis, sin clave, CORS nativo): consulta por código de barras o texto.
- L7306 `lookupOFFBarcode(code,signal,ms=3200)`
- L7321 `searchOFF(query,signal,ms=4500)`
- L7339 `openProductSearch()`
- L7377 `nutrientFields(n,prefix='n_')`
- L7378 `readNutrients(form,prefix='n_')`
- L7383 `editEntry(id)`
- L7392 `editFood(id,pending=null)`
- L7397 `usageStats(days=90)`
- L7405 `renderFoods(forceList=false)`
- L7417 `nutrientSources(key)`
- L7424 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L7425 `suppSlot(meal)`
- L7426 `renderSupps()`
- L7441 `editPlan(id)`
- L7448 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L7469 `makePrompt(meal='Comida',note='')`
- L7474 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L7478 `pantryCompact()`
- L7482 constante `MEAL_AI_SCHEMA`
- L7522 `mealSystemPrompt(usePhoto)`
- L7538 `hydrateAIItems(rawItems,fallback,usePhoto,aiModel,signal)`
- L7581 `photoPrompt(meal,note)`
- L7584 `resetPhoto()`
- L7595 `openPhoto()`
- L7601 `shrinkPhoto(file)`
- L7604 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L7630 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L7637 `cleanFood(id,f)`
- L7641 `migrateBase(o)`
- L7661 `download(name,text,type)`
- L7670 `portable()`
- L7712 `syncAppIcons()`
- L7720 `downloadAppIcons()`
- L7757 constante `PROFILES_KEY`
- L7759 `ensureProfilesStore()`
- L7779 `resetProfileSessionUI()`
- L7786 `saveProfilesStore(st)`
- L7795 `syncCurrentProfileToStore(snapObj=null,immediate=true)`
- L7806 `activeProfileName()`
- L7810 `renderProfilesList()`
- L7852 `switchProfile(id)`
- L7874 `deleteProfileById(id)`
- L7899 `refreshDrawerSummary()`
- L7916 `toggleLeftDrawer(force)`
- L7931 `buildAIExportText(rangeOverride)`
- L8186 `copyAIExport()`
- L8200 `downloadAIExport()`
- L8209 `renderDrawerChat()`
- L8228 `buildDrawerChatContext()`
- L8267 `buildDrawerChatPrompt(question)`
- L8279 `askDrawerAI(rawQuestion)`
- L8368 constante `CLOUD_OFF_KEY`
- L8379 `bytesToB64(u8)`
- L8380 `b64ToBytes(s)`
- L8381 `bytesToB64Url(u8)`
- L8382 `sha256Hex(str)`
- L8383 `sha256Bytes(str)`
- L8384 `generateSyncKey()`
- L8385 `ensureSyncKey()`
- L8386 `mirrorSyncKey(k)`
- L8387 `deriveSyncCreds(keyStr)`
- L8393 `hasMeaningfulData()`
- L8400 `buildCloudBundle()`
- L8407 `encryptVaultPayload(obj,keyStr)`
- L8415 `readDecompressedText(bytes,maxBytes=10*1024*1024)`
- L8431 `decryptVaultPayload(resp,keyStr)`
- L8443 `bundleHash(bundle)`
- L8447 `applyCloudBundle(o,rev=1)`
- L8457 `cloudPull(keyStr,opts={})`
- L8477 `cloudPush(opts={})`
- L8514 `scheduleCloudPush()`
- L8520 `scheduleAutoCloudPull(delayMs=120)`
- L8534 `saveSyncToPassMgr()`
- L8541 `trySilentPassMgrRecovery()`
- L8551 `extractSyncKeyInput(val)`
- L8557 `applySyncKey(rawKey,opts={})`
- L8578 `takeSyncCode()`
- L8589 `renderCloudStatus()`
- L8612 `buildMagicSyncUrl()`
- L8619 `openMagicSyncModal()`
- L8628 `shareMagicSyncLink()`
- L8635 `copyMagicSyncLink()`
- L8640 `openCloudLinkModal()`
- L8643 `deleteCloudBackup(confirmed=false)`
- L8680 `mirrorToIDB(raw,profRaw)`
- L8683 `storageStatus()`
- L8690 `idbReadWrite(mode,value,key='current')`
- L8691 `openDB()`
- L8693 `flushDeferredSave()`
- L8703 `save(skipCloud=false)`

### Eventos generales: añadir con un toque, editar, eliminar

- L8731 `setQuantity(id,value,msg='Cantidad actualizada')`
- L8735 `niceStep(v)`
- L8736 `stepQuantity(id,dir)`
- L8790 `renderAppInfo(force=false)`
- L8822 `init()`
- L8858 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L8860 `setNav(v)`
- L8865 `go(v,focus)`
- L8876 constante `THEME_KEY`
- L8877 constante `SUN_SVG`
- L8878 constante `MOON_SVG`
- L8880 `syncThemeUI()`
- L8892 `toggleTheme()`
- L8901 `syncLogoTheme()`
- L8912 `applyMenuBtnState()`
- L8935 `syncDatePill()`
- L8948 `clampBtnPos(el,x,y)`
- L8958 `bindDraggableBtn(el,storeKey)`
- L9043 `bindDrawerGestures()`
- L9081 `animateValue(el,to,suffix='%',digits=0)`
- L9090 `tick(now)`
- L9093 `macroCard(key,name,color)`
- L9094 `renderToday()`
- L9118 `renderBio()`
- L9143 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L9145 constante `HOME`
- L9147 `coachCandidates()`
- L9153 `coachIdeas(t,g,ref,meal)`
- L9172 `coachQuickAdd(key)`
- L9180 `renderCoach()`
- L9202 `coachPrompt()`
- L9211 `nutrientDetailStandard(key)`
- L9226 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L9232 `upgradeTo12(s,o)`
- L9237 `benfotiamineTotals(entries=effectiveEntries()`
- L9246 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L9248 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L9260 `microStat(m,t=totals()`
- L9265 `metric(m,t=totals()`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L9272 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L9273 `ratioInfo(key,t=totals()`
- L9312 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L9329 constante `RATIO_ENDS`
- L9331 `ratioZones(i)` — v68: cada equilibrio tiene una zona «aceptable» (ni verde ni mala) y su meta visible en la tarjeta.
- L9339 `ratioTone(i)`
- L9344 constante `NEAR_HEAD`
- L9345 `ratioBar(i,big=false)`
- L9354 `ratioNeedBase(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L9372 `needHTML(i,t)`
- L9373 `ratioNeed(i,t=totals()`
- L9377 `adBalance(t=totals()`
- L9404 `zncuSuppKey()`
- L9405 `zncuSuppCfg()`
- L9427 `zncuDoseLabel(zn,cu)`
- L9430 `hasZncuSupp(d=day()`
- L9435 `toggleZncuSupp()`
- L9455 `openZncuConfig()`
- L9461 `renderRatios()`
- L9472 `ratioDetail(key)`
- L9489 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L9506 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L9521 `renderMicroMap(t=totals()`
- L9534 `nutrientDetailForDay(key)`
- L9539 `editTargetsForm()`
- L9549 `mealData()`
- L9554 `renderMealSegments()`
- L9562 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L9597 constante `FAT_KEYS`
- L9599 `fatData(entries=effectiveEntries()`
- L9605 `energyData(entries=effectiveEntries()`
- L9609 `segmentedBar(items,total,attr)`
- L9613 `renderMealChart()`
- L9618 `renderFat()`
- L9626 `fatDetail(key)`
- L9631 `energyDetail(key)`
- L9638 `portionCandidates(q='')`
- L9643 `openPortion()`
- L9656 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L9671 `templates()`
- L9675 `renderExtra()`
- L9686 `updateExtra(reset=true)`
- L9698 `addExtra(id,amount)`
- L9714 `shakePreview()`
- L9715 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L9730 constante `LENS`
- L9736 `lensKey(key)`
- L9737 `lensHTML(key)`
- L9741 `appendLens(key)`
- L9750 `weekDates()`

### IA en la página: conexión directa o por servidor

- L9760 constante `MEAL_WORD`
- L9761 `mealOfWord(w)`
- L9762 `mealFromText(raw,fallback)`
- L9766 `canonMeal(v,fallback)`
- L9774 `localMeal(raw,meal)`
- L9780 constante `AI_FALLBACK`
- L9781 constante `GEMINI_DEFAULTS`
- L9782 constante `GROQ_DEFAULTS`
- L9783 `aiTaskProfile(task,hasImg=false)`
- L9790 `geminiThinkLevel(model,want)`
- L9796 `supportsGeminiTemp(model)`
- L9797 `readSSE(res,onEvent)`
- L9816 `applyAIConfig(raw)`
- L9842 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L9843 `callGemini(model,key,prompt,img,signal,opts={})`
- L9889 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), Groq (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L9897 `aiProv(m=$('ai-mode')`
- L9898 `aiBase(mode)`
- L9907 `chatHeaders(mode,key)`
- L9914 `callChat(mode,model,key,prompt,img,signal,opts={})` — ChatGPT, Claude, Groq, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L9968 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L9983 constante `OLD_GEMINI_RE`
- L9984 constante `MODEL_PREF`
- L9985 `pickModel(ids,mode=$('ai-mode')`
- L9999 `ensureModel(st)`
- L10015 `syncProvider()`
- L10034 `requestAI(prompt,img,signal,modelOverride='',onStep=null,opts={})`
- L10071 constante `AI_PREF`
- L10072 `aiConnected()`
- L10073 `syncAI()`
- L10075 `saveAIPrefs()`
- L10076 `loadAIPrefs()`
- L10077 `openAISetup()`
- L10084 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L10091 constante `MACROS`
- L10093 `cleanGoals(o,fallback)`
- L10098 `cleanCompare(o={})`
- L10102 `snapshotDay(d,reference='saved')`
- L10107 `upgradeTo17(s,o)`
- L10112 `entriesFor(d,source=weekSource)`
- L10116 `dayRow(dt,source=weekSource)`
- L10120 `goalsFor(dt)`
- L10126 `metricValue(r,key)`
- L10132 `targetOf(dt,key)`
- L10136 `weekSummary()`
- L10140 `aggregate(key,summary=weekSummary()`
- L10144 `tone(pct,mode='macro')`
- L10151 `pctText(a)`
- L10152 `weekProgress(a,color)`
- L10153 `renderWeekMicros(s)`
- L10165 `ratioAggregate(s,num,den)`
- L10169 `renderWeekRatios(s)`
- L10175 `renderWeekTable(s)`
- L10176 `weeklyDetail(key,oneDate=null)`
- L10185 `weekRatioDetail(key)`
- L10193 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L10199 `openDay(dt)`
- L10237 `withDayGoals(fn)`
- L10242 `renderMicros()`
- L10243 `nutrientDetail(key)`
- L10244 `editTargets()`
- L10245 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L10255 `summaryFor(start)`
- L10259 `ringSVG(pct,color,marker)`
- L10261 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L10265 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L10282 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L10283 `macroTone(p)`
- L10284 `dayMacroPct(dt,k)`
- L10285 `renderWeekly()`
- L10308 `weekDetail(dt,picked)`
- L10316 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L10326 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L10332 `sparkline(pts)`
- L10338 `renderCalendar()`
- L10355 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L10356 `splitMeals(raw)`
- L10366 `localDay(raw,fallback)`
- L10373 `promptDay(raw,fallback)`
- L10374 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L10413 `parseCsv(text)`
- L10428 `hevyDate(value,format='auto')`
- L10445 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L10460 constante `GYM_APPS`
- L10462 `gymSig(headers)`
- L10463 `gymApp(headers)`
- L10464 `hevyMapping()`
- L10465 `gymSaved()`
- L10466 `renderMapping(parsed)`
- L10483 `optionalNum(v,min=0,max=1e7)`
- L10488 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L10495 `buildHevy(parsed,map)`
- L10529 `cleanWorkout(s)`
- L10536 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L10551 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L10552 constante `GP_ALIAS`
- L10562 `gpNorm(s)`
- L10563 `gpKey(name)`
- L10567 `gpF(n,d=0)`
- L10568 `gpDate(d,opt)`
- L10569 `gpMonday(d)`
- L10570 constante `GP_GROUPS`
- L10585 constante `GP_COLORS`
- L10586 `gpGroup(name)`
- L10587 `gpWorkSets(s)`
- L10588 `gpModel()`
- L10612 `gpSessionMetrics(e,sets)`
- L10627 constante `GP_METRICS`
- L10632 `gpMetricsFor(e)`
- L10633 `gpRangeHist(e)`
- L10634 `gpPRs(model)`
- L10657 `gpStatus(e)`
- L10675 `gpNext(e)`
- L10683 `gpChart(e)`
- L10711 `gpPointDetail(e)`
- L10717 `gpRepTable(e)`
- L10724 `gpKpis(model)`
- L10733 `gpWeekData(model,w)` — Datos de una semana de gimnasio (series por músculo y sesiones).
- L10738 `gpWeekLabel(w,short)`
- L10739 `gpWeekly(model)`
- L10758 `gpMuscles(model)`
- L10766 `gpHeat(model)` — v69: «Constancia» — mapa de días entrenados (como antes), con días de la semana, meses, intensidad y detalle al tocar.
- L10786 `gpExList(model)`
- L10793 `gpExDetail(model)`
- L10806 `gpDayFood(dt)`
- L10807 `gpNutrition(model)`
- L10814 `gpRecentPRs(model)`
- L10818 `gpSessions(model)`
- L10824 `gpSessionModal(id)`
- L10835 `gpWeekModal(w)`
- L10842 `gpSelect(key)`
- L10843 `gpClick(e)`
- L10859 `renderGym()`
- L10879 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L10888 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L10894 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L10919 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L10923 `showHelp()`
- L10927 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L10929 `markBackup()`
- L10933 `exportJSON()`
- L10938 `drawBackupReminder()`
- L10948 `applyDensity()`
- L10960 `syncDayComplete()`
- L10963 `drawMeals()` — Comidas del día de un vistazo.
- L10971 `filterLog()` — Buscador de Registro.
- L10984 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L10990 `recentFoods()`
- L10995 `quickChip(e,fav)`
- L11013 `drawQuickFoods()`
- L11042 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L11046 `toggleAddPanel(id)`
- L11059 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L11070 `pasteMessage(text,ok)`
- L11078 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L11089 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L11100 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L11106 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L11127 `storableState()`

### Render único: actualiza toda la página

- L11136 `nearView(el)`
- L11138 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L11143 `scheduleLazyRender()`
- L11147 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L11184 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L11185 constante `REF_TABLE`
- L11192 `refTargets(mode)`
- L11193 `syncMicroMode()`
- L11206 `mealByHour(h=new Date()`
- L11213 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L11224 `dataSummary(s)`
- L11228 `confirmImport(next,name)`
- L11235 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L11241 `checkUpdate()`
- L11246 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L11261 constante `GAP_PREFER`
- L11262 constante `GAP_SKIP`
- L11263 constante `GAP_UNIT`
- L11264 `gapQty(f,x)`
- L11265 `gapFoods(key,gap,ctx)`
- L11284 `weekSources(key,sum)`
- L11290 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L11303 `gapRow(x,open,meal,sum,ctx)`
- L11319 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L11344 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L11345 `isFemale(s=state)`
- L11346 `sexLabel(s=state)`
- L11347 `sexBadge(sex)`
- L11349 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L11350 constante `OPT_FEMALE`
- L11361 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba; A (1.500 µg = 5.000 UI) y D (50 µg = 2.000 UI) mantienen A:D en zona verde (2,5:1).
- L11362 `applySexOpt(sex)`
- L11364 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L11369 `cleanPreset(p,fb)`
- L11373 `dayNamesFor(types)`
- L11375 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L11385 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L11393 `profV()`
- L11394 `isTrainDay(i)`
- L11395 `activityName(i)`
- L11396 `dayFaf(i)`
- L11397 `presetDesc(cfg,shake)`
- L11401 `profileDescription()`
- L11409 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L11411 `wizCatalog()`
- L11412 `wizOpen(opts={})`
- L11428 `wizTitle()`
- L11429 `wizPaint(sameStep=true)`
- L11438 `wizSync()`
- L11457 `wizFoodOptions()`
- L11460 `wizPresetSummary(cfg,whey)`
- L11465 `wizPresetHTML(kind)`
- L11473 `wizPreview()`
- L11484 `wizLiveHTML()`
- L11488 `wizHTML()`
- L11534 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L11632 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L11633 constante `SUPP_CATALOG`
- L11658 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L11659 constante `PEAT_BREAKFAST`
- L11660 constante `PEAT_SHAKE`
- L11662 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L11669 `benfoUser()`
- L11671 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L11687 `ico(n)`
- L11689 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L11698 `showTour(i=0)`
- L11710 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L11711 `hubAction(v)`
- L11719 constante `FB_CATS` — Envíos anónimos directos al buzón de BioPeat (sin cuentas ni datos personales).
- L11721 `openFeedback()`
- L11725 `feedbackData()`
- L11732 `feedbackText()`
- L11733 `sendFeedback()`
- L11753 `shareFeedback()`
- L11770 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L11777 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L11785 constante `I18N_EN`

### v59: idioma (español / inglés)

- L13714 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L13715 constante `WD_EN`
- L13716 `trOne(s)`
- L13724 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L13725 constante `ES_FOOD_GYM`
- L13762 `trFood(s)`
- L13774 constante `TR_TPL`
- L13815 `trLower(s)`
- L13816 `trTpl(s,attr)`
- L13817 constante `FOOD_SEL`
- L13818 `trText(s,attr=false)`
- L13828 `trNode(n)`
- L13847 `trEl(el)`
- L13860 `trTree(root)`
- L13869 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L13883 `flushTr()`
- L13884 `syncTrObserver()`
- L13888 `setLang(l,quiet)`
- L13902 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter + Worker agregados), solo en la web publicada

- L13911 constante `GC_CODE`
- L13912 `pingAnalytics(extra={})`
- L13928 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L13940 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L13941 `packMove()`
- L13949 `unpackMove(code)`
- L13960 `moveData()`
- L13970 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L13976 `checkMove(code)`
- L13995 `aiFrameworkLines()` — v69: marco de referencia del informe para IA. Así cualquier IA, aunque no conozca la app ni al usuario, sabe con qué comparar.

### Arranque

