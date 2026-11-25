# MAPA DEL CÓDIGO · BioPeat v80 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (1008 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-6481; todo el JavaScript en `<script id="app">` (desde la línea 6482).

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

- L6551 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L6552 constante `AZUCAR_N`
- L6553 constante `USDA_N`
- L6559 constante `FOODS`
- L6561 constante `BASE_FAT_FIX`
- L6565 constante `REF_COLS` — Base de referencia verificada (USDA FoodData Central / BEDCA, por 100 g o 100 ml comestibles).
- L6566 constante `REF_RAW`
- L6731 constante `REF_MAP`
- L6732 constante `REF_CACHE`
- L6734 `ensureRefIndex()`
- L6741 `refNutrients(id)`
- L6749 constante `STRIP_PREP_RE`
- L6750 `findRef(text,strict=false)`
- L6773 `refCatalogCompact()`
- L6774 `fromRef(id,amount,meal,note='',srcText='')`
- L6779 constante `EXTRA`
- L6780 constante `KEYS`
- L6782 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L6784 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L6788 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6789 constante `OPT`
- L6815 constante `LIMIT`
- L6816 `optInfo(k,goal)`
- L6823 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6831 `optLine(k,goal,unit)`
- L6838 `optRefHTML(k,goal,unit)`
- L6840 constante `DAYS`
- L6841 constante `FAF`
- L6843 constante `LOC`
- L6847 `number(v,min=0,max=1e6)`
- L6853 `decimalInputs(root=document)`
- L6854 `localDate(d=new Date()`
- L6855 `validDate(s)`
- L6860 `shift(s,n)`
- L6868 `stripProto(o)`
- L6875 `cleanBio(b)`
- L6884 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6886 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6892 constante `DAY_TYPES`
- L6893 constante `NEW_V54`
- L6897 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6900 `bmr(w=state.profile.weight)` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6906 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6931 `cleanNutrients(o,required=false)`
- L6943 `cleanEntry(e)`
- L6948 `cleanPlan(p)`
- L6952 `planEntry(p)`
- L6961 `seedPlan(d,whichDate)`
- L6965 `ensureDay(d=date)`
- L6972 `effectiveEntries(d=day()`
- L6973 constante `SALTED_IDS`
- L6974 constante `SWEET_RE`
- L6975 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6993 `inferredNutrients(e)`
- L7035 `totals(entries)`
- L7047 `change(fn,message='Guardado')`
- L7051 `undo()`
- L7059 `toast(text,canUndo=false)`
- L7067 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L7068 `onClick(fn)`
- L7070 `attempt(fn)`
- L7074 `modal(title,body)`
- L7083 `modalRestore()`
- L7093 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L7094 `modalBack()`
- L7095 `goDate(d)`
- L7102 `renderHeader()`
- L7115 `renderRows(entries)`
- L7119 `entryValues(e)`
- L7120 `renderLog()`
- L7127 `fromFood(id,amount,meal)`
- L7133 `pantryId(name)`
- L7135 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L7151 `addEntries(entries,message='Añadido',d=date,opts={})`
- L7160 `recipe(kind)`
- L7167 `summary(entries)`
- L7171 `renderPresetInfo()`
- L7184 `stripCode(raw)`
- L7190 `sanitizeNutrients(o,grams=100,fallbackRefId='')`
- L7217 `parseBIO(raw,meal=$('meal-select')`
- L7229 `parseSmart(raw)`
- L7233 constante `COUNT`
- L7234 constante `UNIT_RE`
- L7286 `offToNutrients(nut={},fallbackName='')` — Open Food Facts (gratis, sin clave, CORS nativo): consulta por código de barras o texto.
- L7307 `lookupOFFBarcode(code,signal,ms=3200)`
- L7322 `searchOFF(query,signal,ms=4500)`
- L7340 `openProductSearch()`
- L7378 `nutrientFields(n,prefix='n_')`
- L7379 `readNutrients(form,prefix='n_')`
- L7384 `editEntry(id)`
- L7393 `editFood(id,pending=null)`
- L7398 `usageStats(days=90)`
- L7406 `renderFoods(forceList=false)`
- L7418 `nutrientSources(key)`
- L7425 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L7426 `suppSlot(meal)`
- L7427 `renderSupps()`
- L7442 `editPlan(id)`
- L7449 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L7470 `makePrompt(meal='Comida',note='')`
- L7475 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L7479 `pantryCompact()`
- L7483 constante `MEAL_AI_SCHEMA`
- L7523 `mealSystemPrompt(usePhoto)`
- L7539 `hydrateAIItems(rawItems,fallback,usePhoto,aiModel,signal)`
- L7582 `photoPrompt(meal,note)`
- L7585 `resetPhoto()`
- L7596 `openPhoto()`
- L7602 `shrinkPhoto(file)`
- L7605 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L7631 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L7638 `cleanFood(id,f)`
- L7642 `migrateBase(o)`
- L7662 `download(name,text,type)`
- L7671 `portable()`
- L7713 `syncAppIcons()`
- L7721 `downloadAppIcons()`
- L7758 constante `PROFILES_KEY`
- L7760 `ensureProfilesStore()`
- L7780 `resetProfileSessionUI()`
- L7787 `saveProfilesStore(st)`
- L7796 `syncCurrentProfileToStore(snapObj=null,immediate=true)`
- L7807 `activeProfileName()`
- L7811 `renderProfilesList()`
- L7853 `switchProfile(id)`
- L7875 `deleteProfileById(id)`
- L7900 `refreshDrawerSummary()`
- L7917 `toggleLeftDrawer(force)`
- L7932 `buildAIExportText(rangeOverride)`
- L8187 `copyAIExport()`
- L8201 `downloadAIExport()`
- L8210 `renderDrawerChat()`
- L8229 `buildDrawerChatContext()`
- L8268 `buildDrawerChatPrompt(question)`
- L8280 `askDrawerAI(rawQuestion)`
- L8369 constante `CLOUD_OFF_KEY`
- L8380 `bytesToB64(u8)`
- L8381 `b64ToBytes(s)`
- L8382 `bytesToB64Url(u8)`
- L8383 `sha256Hex(str)`
- L8384 `sha256Bytes(str)`
- L8385 `generateSyncKey()`
- L8386 `ensureSyncKey()`
- L8387 `mirrorSyncKey(k)`
- L8388 `deriveSyncCreds(keyStr)`
- L8394 `hasMeaningfulData()`
- L8401 `buildCloudBundle()`
- L8408 `encryptVaultPayload(obj,keyStr)`
- L8416 `readDecompressedText(bytes,maxBytes=10*1024*1024)`
- L8432 `decryptVaultPayload(resp,keyStr)`
- L8444 `bundleHash(bundle)`
- L8448 `applyCloudBundle(o,rev=1)`
- L8458 `cloudPull(keyStr,opts={})`
- L8478 `cloudPush(opts={})`
- L8515 `scheduleCloudPush()`
- L8521 `scheduleAutoCloudPull(delayMs=120)`
- L8535 `saveSyncToPassMgr()`
- L8542 `trySilentPassMgrRecovery()`
- L8552 `extractSyncKeyInput(val)`
- L8558 `applySyncKey(rawKey,opts={})`
- L8579 `takeSyncCode()`
- L8590 `renderCloudStatus()`
- L8613 `buildMagicSyncUrl()`
- L8620 `openMagicSyncModal()`
- L8629 `shareMagicSyncLink()`
- L8636 `copyMagicSyncLink()`
- L8641 `openCloudLinkModal()`
- L8644 `deleteCloudBackup(confirmed=false)`
- L8681 `mirrorToIDB(raw,profRaw)`
- L8684 `storageStatus()`
- L8691 `idbReadWrite(mode,value,key='current')`
- L8692 `openDB()`
- L8694 `flushDeferredSave()`
- L8704 `save(skipCloud=false)`

### Eventos generales: añadir con un toque, editar, eliminar

- L8732 `setQuantity(id,value,msg='Cantidad actualizada')`
- L8736 `niceStep(v)`
- L8737 `stepQuantity(id,dir)`
- L8791 `renderAppInfo(force=false)`
- L8823 `init()`
- L8859 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L8861 `setNav(v)`
- L8866 `go(v,focus)`
- L8877 constante `THEME_KEY`
- L8878 constante `SUN_SVG`
- L8879 constante `MOON_SVG`
- L8881 `syncThemeUI()`
- L8893 `toggleTheme()`
- L8902 `syncLogoTheme()`
- L8911 `applyMenuBtnState()`
- L8934 `syncDatePill()`
- L8947 `clampBtnPos(el,x,y)`
- L8957 `bindDraggableBtn(el,storeKey)`
- L9042 `bindDrawerGestures()`
- L9080 `animateValue(el,to,suffix='%',digits=0)`
- L9089 `tick(now)`
- L9092 `macroCard(key,name,color)`
- L9093 `renderToday()`
- L9117 `renderBio()`
- L9142 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L9144 constante `HOME`
- L9146 `coachCandidates()`
- L9152 `coachIdeas(t,g,ref,meal)`
- L9171 `coachQuickAdd(key)`
- L9179 `renderCoach()`
- L9201 `coachPrompt()`
- L9210 `nutrientDetailStandard(key)`
- L9225 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L9231 `upgradeTo12(s,o)`
- L9236 `benfotiamineTotals(entries=effectiveEntries()`
- L9245 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L9247 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L9259 `microStat(m,t=totals()`
- L9264 `metric(m,t=totals()`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L9271 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L9272 `ratioInfo(key,t=totals()`
- L9311 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L9328 constante `RATIO_ENDS`
- L9330 `ratioZones(i)` — v68: cada equilibrio tiene una zona «aceptable» (ni verde ni mala) y su meta visible en la tarjeta.
- L9338 `ratioTone(i)`
- L9343 constante `NEAR_HEAD`
- L9344 `ratioBar(i,big=false)`
- L9353 `ratioNeedBase(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L9371 `needHTML(i,t)`
- L9372 `ratioNeed(i,t=totals()`
- L9376 `adBalance(t=totals()`
- L9403 `zncuSuppKey()`
- L9404 `zncuSuppCfg()`
- L9426 `zncuDoseLabel(zn,cu)`
- L9429 `hasZncuSupp(d=day()`
- L9434 `toggleZncuSupp()`
- L9454 `openZncuConfig()`
- L9460 `renderRatios()`
- L9471 `ratioDetail(key)`
- L9488 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L9505 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L9520 `renderMicroMap(t=totals()`
- L9533 `nutrientDetailForDay(key)`
- L9538 `editTargetsForm()`
- L9548 `mealData()`
- L9553 `renderMealSegments()`
- L9561 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L9596 constante `FAT_KEYS`
- L9598 `fatData(entries=effectiveEntries()`
- L9604 `energyData(entries=effectiveEntries()`
- L9608 `segmentedBar(items,total,attr)`
- L9612 `renderMealChart()`
- L9617 `renderFat()`
- L9625 `fatDetail(key)`
- L9630 `energyDetail(key)`
- L9637 `portionCandidates(q='')`
- L9642 `openPortion()`
- L9655 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L9670 `templates()`
- L9674 `renderExtra()`
- L9685 `updateExtra(reset=true)`
- L9697 `addExtra(id,amount)`
- L9713 `shakePreview()`
- L9714 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L9729 constante `LENS`
- L9735 `lensKey(key)`
- L9736 `lensHTML(key)`
- L9740 `appendLens(key)`
- L9749 `weekDates()`

### IA en la página: conexión directa o por servidor

- L9759 constante `MEAL_WORD`
- L9760 `mealOfWord(w)`
- L9761 `mealFromText(raw,fallback)`
- L9765 `canonMeal(v,fallback)`
- L9773 `localMeal(raw,meal)`
- L9779 constante `AI_FALLBACK`
- L9780 constante `GEMINI_DEFAULTS`
- L9781 constante `GROQ_DEFAULTS`
- L9782 `aiTaskProfile(task,hasImg=false)`
- L9789 `geminiThinkLevel(model,want)`
- L9795 `supportsGeminiTemp(model)`
- L9796 `readSSE(res,onEvent)`
- L9815 `applyAIConfig(raw)`
- L9841 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L9842 `callGemini(model,key,prompt,img,signal,opts={})`
- L9888 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), Groq (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L9896 `aiProv(m=$('ai-mode')`
- L9897 `aiBase(mode)`
- L9906 `chatHeaders(mode,key)`
- L9913 `callChat(mode,model,key,prompt,img,signal,opts={})` — ChatGPT, Claude, Groq, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L9967 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L9982 constante `OLD_GEMINI_RE`
- L9983 constante `MODEL_PREF`
- L9984 `pickModel(ids,mode=$('ai-mode')`
- L9998 `ensureModel(st)`
- L10014 `syncProvider()`
- L10033 `requestAI(prompt,img,signal,modelOverride='',onStep=null,opts={})`
- L10070 constante `AI_PREF`
- L10071 `aiConnected()`
- L10072 `syncAI()`
- L10074 `saveAIPrefs()`
- L10075 `loadAIPrefs()`
- L10076 `openAISetup()`
- L10083 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L10090 constante `MACROS`
- L10092 `cleanGoals(o,fallback)`
- L10097 `cleanCompare(o={})`
- L10101 `snapshotDay(d,reference='saved')`
- L10106 `upgradeTo17(s,o)`
- L10111 `entriesFor(d,source=weekSource)`
- L10115 `dayRow(dt,source=weekSource)`
- L10119 `goalsFor(dt)`
- L10125 `metricValue(r,key)`
- L10131 `targetOf(dt,key)`
- L10135 `weekSummary()`
- L10139 `aggregate(key,summary=weekSummary()`
- L10143 `tone(pct,mode='macro')`
- L10150 `pctText(a)`
- L10151 `weekProgress(a,color)`
- L10152 `renderWeekMicros(s)`
- L10164 `ratioAggregate(s,num,den)`
- L10168 `renderWeekRatios(s)`
- L10174 `renderWeekTable(s)`
- L10175 `weeklyDetail(key,oneDate=null)`
- L10184 `weekRatioDetail(key)`
- L10192 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L10198 `openDay(dt)`
- L10236 `withDayGoals(fn)`
- L10241 `renderMicros()`
- L10242 `nutrientDetail(key)`
- L10243 `editTargets()`
- L10244 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L10254 `summaryFor(start)`
- L10258 `ringSVG(pct,color,marker)`
- L10260 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L10264 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L10281 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L10282 `macroTone(p)`
- L10283 `dayMacroPct(dt,k)`
- L10284 `renderWeekly()`
- L10307 `weekDetail(dt,picked)`
- L10315 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L10325 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L10331 `sparkline(pts)`
- L10337 `renderCalendar()`
- L10354 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L10355 `splitMeals(raw)`
- L10365 `localDay(raw,fallback)`
- L10372 `promptDay(raw,fallback)`
- L10373 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L10412 `parseCsv(text)`
- L10427 `hevyDate(value,format='auto')`
- L10444 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L10459 constante `GYM_APPS`
- L10461 `gymSig(headers)`
- L10462 `gymApp(headers)`
- L10463 `hevyMapping()`
- L10464 `gymSaved()`
- L10465 `renderMapping(parsed)`
- L10482 `optionalNum(v,min=0,max=1e7)`
- L10487 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L10494 `buildHevy(parsed,map)`
- L10528 `cleanWorkout(s)`
- L10535 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L10550 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L10551 constante `GP_ALIAS`
- L10561 `gpNorm(s)`
- L10562 `gpKey(name)`
- L10566 `gpF(n,d=0)`
- L10567 `gpDate(d,opt)`
- L10568 `gpMonday(d)`
- L10569 constante `GP_GROUPS`
- L10584 constante `GP_COLORS`
- L10585 `gpGroup(name)`
- L10586 `gpWorkSets(s)`
- L10587 `gpModel()`
- L10611 `gpSessionMetrics(e,sets)`
- L10626 constante `GP_METRICS`
- L10631 `gpMetricsFor(e)`
- L10632 `gpRangeHist(e)`
- L10633 `gpPRs(model)`
- L10656 `gpStatus(e)`
- L10674 `gpNext(e)`
- L10682 `gpChart(e)`
- L10710 `gpPointDetail(e)`
- L10716 `gpRepTable(e)`
- L10723 `gpKpis(model)`
- L10732 `gpWeekData(model,w)` — Datos de una semana de gimnasio (series por músculo y sesiones).
- L10737 `gpWeekLabel(w,short)`
- L10738 `gpWeekly(model)`
- L10757 `gpMuscles(model)`
- L10765 `gpHeat(model)` — v69: «Constancia» — mapa de días entrenados (como antes), con días de la semana, meses, intensidad y detalle al tocar.
- L10785 `gpExList(model)`
- L10792 `gpExDetail(model)`
- L10805 `gpDayFood(dt)`
- L10806 `gpNutrition(model)`
- L10813 `gpRecentPRs(model)`
- L10817 `gpSessions(model)`
- L10823 `gpSessionModal(id)`
- L10834 `gpWeekModal(w)`
- L10841 `gpSelect(key)`
- L10842 `gpClick(e)`
- L10858 `renderGym()`
- L10878 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L10887 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L10893 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L10918 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L10922 `showHelp()`
- L10926 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L10928 `markBackup()`
- L10932 `exportJSON()`
- L10937 `drawBackupReminder()`
- L10947 `applyDensity()`
- L10959 `syncDayComplete()`
- L10962 `drawMeals()` — Comidas del día de un vistazo.
- L10970 `filterLog()` — Buscador de Registro.
- L10983 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L10989 `recentFoods()`
- L10994 `quickChip(e,fav)`
- L11012 `drawQuickFoods()`
- L11041 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L11045 `toggleAddPanel(id)`
- L11058 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L11069 `pasteMessage(text,ok)`
- L11077 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L11088 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L11099 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L11105 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L11126 `storableState()`

### Render único: actualiza toda la página

- L11135 `nearView(el)`
- L11137 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L11142 `scheduleLazyRender()`
- L11146 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L11183 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L11184 constante `REF_TABLE`
- L11191 `refTargets(mode)`
- L11192 `syncMicroMode()`
- L11205 `mealByHour(h=new Date()`
- L11212 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L11223 `dataSummary(s)`
- L11227 `confirmImport(next,name)`
- L11234 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L11240 `checkUpdate()`
- L11245 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L11260 constante `GAP_PREFER`
- L11261 constante `GAP_SKIP`
- L11262 constante `GAP_UNIT`
- L11263 `gapQty(f,x)`
- L11264 `gapFoods(key,gap,ctx)`
- L11283 `weekSources(key,sum)`
- L11289 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L11302 `gapRow(x,open,meal,sum,ctx)`
- L11318 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L11343 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L11344 `isFemale(s=state)`
- L11345 `sexLabel(s=state)`
- L11346 `sexBadge(sex)`
- L11348 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L11349 constante `OPT_FEMALE`
- L11360 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba; A (1.500 µg = 5.000 UI) y D (50 µg = 2.000 UI) mantienen A:D en zona verde (2,5:1).
- L11361 `applySexOpt(sex)`
- L11363 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L11368 `cleanPreset(p,fb)`
- L11372 `dayNamesFor(types)`
- L11374 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L11384 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L11392 `profV()`
- L11393 `isTrainDay(i)`
- L11394 `activityName(i)`
- L11395 `dayFaf(i)`
- L11396 `presetDesc(cfg,shake)`
- L11400 `profileDescription()`
- L11408 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L11410 `wizCatalog()`
- L11411 `wizOpen(opts={})`
- L11427 `wizTitle()`
- L11428 `wizPaint(sameStep=true)`
- L11437 `wizSync()`
- L11456 `wizFoodOptions()`
- L11459 `wizPresetSummary(cfg,whey)`
- L11464 `wizPresetHTML(kind)`
- L11472 `wizPreview()`
- L11483 `wizLiveHTML()`
- L11487 `wizHTML()`
- L11533 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L11631 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L11632 constante `SUPP_CATALOG`
- L11657 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L11658 constante `PEAT_BREAKFAST`
- L11659 constante `PEAT_SHAKE`
- L11661 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L11668 `benfoUser()`
- L11670 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L11686 `ico(n)`
- L11688 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L11697 `showTour(i=0)`
- L11709 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L11710 `hubAction(v)`
- L11718 constante `FB_CATS` — Envíos anónimos directos al buzón de BioPeat (sin cuentas ni datos personales).
- L11720 `openFeedback()`
- L11724 `feedbackData()`
- L11731 `feedbackText()`
- L11732 `sendFeedback()`
- L11752 `shareFeedback()`
- L11769 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L11776 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L11784 constante `I18N_EN`

### v59: idioma (español / inglés)

- L13713 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L13714 constante `WD_EN`
- L13715 `trOne(s)`
- L13723 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L13724 constante `ES_FOOD_GYM`
- L13761 `trFood(s)`
- L13773 constante `TR_TPL`
- L13814 `trLower(s)`
- L13815 `trTpl(s,attr)`
- L13816 constante `FOOD_SEL`
- L13817 `trText(s,attr=false)`
- L13827 `trNode(n)`
- L13846 `trEl(el)`
- L13859 `trTree(root)`
- L13868 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L13882 `flushTr()`
- L13883 `syncTrObserver()`
- L13887 `setLang(l,quiet)`
- L13901 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter + Worker agregados), solo en la web publicada

- L13910 constante `GC_CODE`
- L13911 `pingAnalytics(extra={})`
- L13927 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L13939 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L13940 `packMove()`
- L13948 `unpackMove(code)`
- L13959 `moveData()`
- L13969 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L13975 `checkMove(code)`
- L13994 `aiFrameworkLines()` — v69: marco de referencia del informe para IA. Así cualquier IA, aunque no conozca la app ni al usuario, sabe con qué comparar.

### Arranque

