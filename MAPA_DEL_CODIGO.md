# MAPA DEL CÓDIGO · BioPeat v79 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (1006 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-6482; todo el JavaScript en `<script id="app">` (desde la línea 6483).

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
- L8913 `applyMenuBtnState()`
- L8936 `syncDatePill()`
- L8949 `clampBtnPos(el,x,y)`
- L8959 `bindDraggableBtn(el,storeKey)`
- L9044 `bindDrawerGestures()`
- L9082 `animateValue(el,to,suffix='%',digits=0)`
- L9091 `tick(now)`
- L9094 `macroCard(key,name,color)`
- L9095 `renderToday()`
- L9119 `renderBio()`
- L9144 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L9146 constante `HOME`
- L9148 `coachCandidates()`
- L9154 `coachIdeas(t,g,ref,meal)`
- L9173 `coachQuickAdd(key)`
- L9181 `renderCoach()`
- L9203 `coachPrompt()`
- L9212 `nutrientDetailStandard(key)`
- L9227 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L9233 `upgradeTo12(s,o)`
- L9238 `benfotiamineTotals(entries=effectiveEntries()`
- L9247 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L9249 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L9261 `microStat(m,t=totals()`
- L9266 `metric(m,t=totals()`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L9273 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L9274 `ratioInfo(key,t=totals()`
- L9313 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L9330 constante `RATIO_ENDS`
- L9332 `ratioZones(i)` — v68: cada equilibrio tiene una zona «aceptable» (ni verde ni mala) y su meta visible en la tarjeta.
- L9340 `ratioTone(i)`
- L9345 constante `NEAR_HEAD`
- L9346 `ratioBar(i,big=false)`
- L9355 `ratioNeedBase(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L9373 `needHTML(i,t)`
- L9374 `ratioNeed(i,t=totals()`
- L9378 `adBalance(t=totals()`
- L9405 `zncuSuppKey()`
- L9406 `zncuSuppCfg()`
- L9428 `zncuDoseLabel(zn,cu)`
- L9431 `hasZncuSupp(d=day()`
- L9436 `toggleZncuSupp()`
- L9456 `openZncuConfig()`
- L9462 `renderRatios()`
- L9473 `ratioDetail(key)`
- L9490 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L9507 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L9522 `renderMicroMap(t=totals()`
- L9535 `nutrientDetailForDay(key)`
- L9540 `editTargetsForm()`
- L9550 `mealData()`
- L9555 `renderMealSegments()`
- L9563 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L9598 constante `FAT_KEYS`
- L9600 `fatData(entries=effectiveEntries()`
- L9606 `energyData(entries=effectiveEntries()`
- L9610 `segmentedBar(items,total,attr)`
- L9614 `renderMealChart()`
- L9619 `renderFat()`
- L9627 `fatDetail(key)`
- L9632 `energyDetail(key)`
- L9639 `portionCandidates(q='')`
- L9644 `openPortion()`
- L9657 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L9672 `templates()`
- L9676 `renderExtra()`
- L9687 `updateExtra(reset=true)`
- L9699 `addExtra(id,amount)`
- L9715 `shakePreview()`
- L9716 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L9731 constante `LENS`
- L9737 `lensKey(key)`
- L9738 `lensHTML(key)`
- L9742 `appendLens(key)`
- L9751 `weekDates()`

### IA en la página: conexión directa o por servidor

- L9761 constante `MEAL_WORD`
- L9762 `mealOfWord(w)`
- L9763 `mealFromText(raw,fallback)`
- L9767 `canonMeal(v,fallback)`
- L9775 `localMeal(raw,meal)`
- L9781 constante `AI_FALLBACK`
- L9782 constante `GEMINI_DEFAULTS`
- L9783 constante `GROQ_DEFAULTS`
- L9784 `aiTaskProfile(task,hasImg=false)`
- L9791 `geminiThinkLevel(model,want)`
- L9797 `supportsGeminiTemp(model)`
- L9798 `readSSE(res,onEvent)`
- L9817 `applyAIConfig(raw)`
- L9843 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L9844 `callGemini(model,key,prompt,img,signal,opts={})`
- L9890 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), Groq (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L9898 `aiProv(m=$('ai-mode')`
- L9899 `aiBase(mode)`
- L9908 `chatHeaders(mode,key)`
- L9915 `callChat(mode,model,key,prompt,img,signal,opts={})` — ChatGPT, Claude, Groq, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L9969 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L9984 constante `OLD_GEMINI_RE`
- L9985 constante `MODEL_PREF`
- L9986 `pickModel(ids,mode=$('ai-mode')`
- L10000 `ensureModel(st)`
- L10016 `syncProvider()`
- L10035 `requestAI(prompt,img,signal,modelOverride='',onStep=null,opts={})`
- L10072 constante `AI_PREF`
- L10073 `aiConnected()`
- L10074 `syncAI()`
- L10076 `saveAIPrefs()`
- L10077 `loadAIPrefs()`
- L10078 `openAISetup()`
- L10085 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L10092 constante `MACROS`
- L10094 `cleanGoals(o,fallback)`
- L10099 `cleanCompare(o={})`
- L10103 `snapshotDay(d,reference='saved')`
- L10108 `upgradeTo17(s,o)`
- L10113 `entriesFor(d,source=weekSource)`
- L10117 `dayRow(dt,source=weekSource)`
- L10121 `goalsFor(dt)`
- L10127 `metricValue(r,key)`
- L10133 `targetOf(dt,key)`
- L10137 `weekSummary()`
- L10141 `aggregate(key,summary=weekSummary()`
- L10145 `tone(pct,mode='macro')`
- L10152 `pctText(a)`
- L10153 `weekProgress(a,color)`
- L10154 `renderWeekMicros(s)`
- L10166 `ratioAggregate(s,num,den)`
- L10170 `renderWeekRatios(s)`
- L10176 `renderWeekTable(s)`
- L10177 `weeklyDetail(key,oneDate=null)`
- L10186 `weekRatioDetail(key)`
- L10194 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L10200 `openDay(dt)`
- L10238 `withDayGoals(fn)`
- L10243 `renderMicros()`
- L10244 `nutrientDetail(key)`
- L10245 `editTargets()`
- L10246 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L10256 `summaryFor(start)`
- L10260 `ringSVG(pct,color,marker)`
- L10262 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L10266 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L10283 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L10284 `macroTone(p)`
- L10285 `dayMacroPct(dt,k)`
- L10286 `renderWeekly()`
- L10309 `weekDetail(dt,picked)`
- L10317 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L10327 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L10333 `sparkline(pts)`
- L10339 `renderCalendar()`
- L10356 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L10357 `splitMeals(raw)`
- L10367 `localDay(raw,fallback)`
- L10374 `promptDay(raw,fallback)`
- L10375 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L10414 `parseCsv(text)`
- L10429 `hevyDate(value,format='auto')`
- L10446 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L10461 constante `GYM_APPS`
- L10463 `gymSig(headers)`
- L10464 `gymApp(headers)`
- L10465 `hevyMapping()`
- L10466 `gymSaved()`
- L10467 `renderMapping(parsed)`
- L10484 `optionalNum(v,min=0,max=1e7)`
- L10489 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L10496 `buildHevy(parsed,map)`
- L10530 `cleanWorkout(s)`
- L10537 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L10552 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L10553 constante `GP_ALIAS`
- L10563 `gpNorm(s)`
- L10564 `gpKey(name)`
- L10568 `gpF(n,d=0)`
- L10569 `gpDate(d,opt)`
- L10570 `gpMonday(d)`
- L10571 constante `GP_GROUPS`
- L10586 constante `GP_COLORS`
- L10587 `gpGroup(name)`
- L10588 `gpWorkSets(s)`
- L10589 `gpModel()`
- L10613 `gpSessionMetrics(e,sets)`
- L10628 constante `GP_METRICS`
- L10633 `gpMetricsFor(e)`
- L10634 `gpRangeHist(e)`
- L10635 `gpPRs(model)`
- L10658 `gpStatus(e)`
- L10676 `gpNext(e)`
- L10684 `gpChart(e)`
- L10712 `gpPointDetail(e)`
- L10718 `gpRepTable(e)`
- L10725 `gpKpis(model)`
- L10734 `gpWeekData(model,w)` — Datos de una semana de gimnasio (series por músculo y sesiones).
- L10739 `gpWeekLabel(w,short)`
- L10740 `gpWeekly(model)`
- L10759 `gpMuscles(model)`
- L10767 `gpHeat(model)` — v69: «Constancia» — mapa de días entrenados (como antes), con días de la semana, meses, intensidad y detalle al tocar.
- L10787 `gpExList(model)`
- L10794 `gpExDetail(model)`
- L10807 `gpDayFood(dt)`
- L10808 `gpNutrition(model)`
- L10815 `gpRecentPRs(model)`
- L10819 `gpSessions(model)`
- L10825 `gpSessionModal(id)`
- L10836 `gpWeekModal(w)`
- L10843 `gpSelect(key)`
- L10844 `gpClick(e)`
- L10860 `renderGym()`
- L10880 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L10889 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L10895 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L10920 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L10924 `showHelp()`
- L10928 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L10930 `markBackup()`
- L10934 `exportJSON()`
- L10939 `drawBackupReminder()`
- L10949 `applyDensity()`
- L10961 `syncDayComplete()`
- L10964 `drawMeals()` — Comidas del día de un vistazo.
- L10972 `filterLog()` — Buscador de Registro.
- L10985 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L10991 `recentFoods()`
- L10996 `quickChip(e,fav)`
- L11014 `drawQuickFoods()`
- L11043 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L11047 `toggleAddPanel(id)`
- L11060 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L11071 `pasteMessage(text,ok)`
- L11079 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L11090 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L11101 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L11107 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L11128 `storableState()`

### Render único: actualiza toda la página

- L11137 `nearView(el)`
- L11139 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L11144 `scheduleLazyRender()`
- L11148 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L11185 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L11186 constante `REF_TABLE`
- L11193 `refTargets(mode)`
- L11194 `syncMicroMode()`
- L11207 `mealByHour(h=new Date()`
- L11214 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L11225 `dataSummary(s)`
- L11229 `confirmImport(next,name)`
- L11236 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L11242 `checkUpdate()`
- L11247 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L11262 constante `GAP_PREFER`
- L11263 constante `GAP_SKIP`
- L11264 constante `GAP_UNIT`
- L11265 `gapQty(f,x)`
- L11266 `gapFoods(key,gap,ctx)`
- L11285 `weekSources(key,sum)`
- L11291 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L11304 `gapRow(x,open,meal,sum,ctx)`
- L11320 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L11345 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L11346 `isFemale(s=state)`
- L11347 `sexLabel(s=state)`
- L11348 `sexBadge(sex)`
- L11350 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L11351 constante `OPT_FEMALE`
- L11362 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba; A (1.500 µg = 5.000 UI) y D (50 µg = 2.000 UI) mantienen A:D en zona verde (2,5:1).
- L11363 `applySexOpt(sex)`
- L11365 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L11370 `cleanPreset(p,fb)`
- L11374 `dayNamesFor(types)`
- L11376 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L11386 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L11394 `profV()`
- L11395 `isTrainDay(i)`
- L11396 `activityName(i)`
- L11397 `dayFaf(i)`
- L11398 `presetDesc(cfg,shake)`
- L11402 `profileDescription()`
- L11410 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L11412 `wizCatalog()`
- L11413 `wizOpen(opts={})`
- L11429 `wizTitle()`
- L11430 `wizPaint(sameStep=true)`
- L11439 `wizSync()`
- L11458 `wizFoodOptions()`
- L11461 `wizPresetSummary(cfg,whey)`
- L11466 `wizPresetHTML(kind)`
- L11474 `wizPreview()`
- L11485 `wizLiveHTML()`
- L11489 `wizHTML()`
- L11535 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L11633 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L11634 constante `SUPP_CATALOG`
- L11659 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L11660 constante `PEAT_BREAKFAST`
- L11661 constante `PEAT_SHAKE`
- L11663 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L11670 `benfoUser()`
- L11672 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L11688 `ico(n)`
- L11690 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L11699 `showTour(i=0)`
- L11711 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L11712 `hubAction(v)`
- L11720 constante `FB_CATS` — Envíos anónimos directos al buzón de BioPeat (sin cuentas ni datos personales).
- L11722 `openFeedback()`
- L11726 `feedbackData()`
- L11733 `feedbackText()`
- L11734 `sendFeedback()`
- L11754 `shareFeedback()`
- L11771 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L11778 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L11786 constante `I18N_EN`

### v59: idioma (español / inglés)

- L13715 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L13716 constante `WD_EN`
- L13717 `trOne(s)`
- L13725 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L13726 constante `ES_FOOD_GYM`
- L13763 `trFood(s)`
- L13775 constante `TR_TPL`
- L13816 `trLower(s)`
- L13817 `trTpl(s,attr)`
- L13818 constante `FOOD_SEL`
- L13819 `trText(s,attr=false)`
- L13829 `trNode(n)`
- L13848 `trEl(el)`
- L13861 `trTree(root)`
- L13870 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L13884 `flushTr()`
- L13885 `syncTrObserver()`
- L13889 `setLang(l,quiet)`
- L13903 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter + Worker agregados), solo en la web publicada

- L13912 constante `GC_CODE`
- L13913 `pingAnalytics(extra={})`
- L13929 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L13941 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L13942 `packMove()`
- L13950 `unpackMove(code)`
- L13961 `moveData()`
- L13971 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L13977 `checkMove(code)`
- L13996 `aiFrameworkLines()` — v69: marco de referencia del informe para IA. Así cualquier IA, aunque no conozca la app ni al usuario, sabe con qué comparar.

### Arranque

