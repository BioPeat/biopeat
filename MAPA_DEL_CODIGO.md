# MAPA DEL CÓDIGO · BioPeat v87 (revisión de datos 27)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

Arquitectura modular: `index.html` (65 KB), `assets/styles.css`, `assets/data.js`, `assets/app.js` (514 KB) y `assets/i18n-en.js`.

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

- L76 constante `REF_MAP` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L77 constante `REF_CACHE`
- L79 `ensureRefIndex()`
- L86 `refNutrients(id)`
- L94 constante `STRIP_PREP_RE`
- L95 `findRef(text,strict=false)`
- L118 `refCatalogCompact()`
- L119 `fromRef(id,amount,meal,note='',srcText='')`
- L124 `optInfo(k,goal)`
- L131 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L139 `optLine(k,goal,unit)`
- L146 `optRefHTML(k,goal,unit)`
- L147 constante `FAF`
- L149 constante `LOC`
- L153 `number(v,min=0,max=1e6)`
- L159 `decimalInputs(root=document)`
- L160 `localDate(d=new Date()`
- L161 `validDate(s)`
- L166 `shift(s,n)`
- L174 `stripProto(o)`
- L181 `cleanBio(b)`
- L190 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L192 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L198 constante `DAY_TYPES`
- L199 constante `NEW_V54`
- L203 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L206 `bmr(w=state.profile.weight)` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L212 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L237 `cleanNutrients(o,required=false)`
- L249 `cleanEntry(e)`
- L254 `cleanPlan(p)`
- L258 `planEntry(p)`
- L267 `seedPlan(d,whichDate)`
- L271 `ensureDay(d=date)`
- L278 `effectiveEntries(d=day()`
- L279 constante `SALTED_IDS`
- L280 constante `SWEET_RE`
- L281 `inferFatShares(e,txt=normalize((e?.name||'')`
- L299 `inferredNutrients(e)`
- L341 `totals(entries)`
- L353 `change(fn,message='Guardado')`
- L359 `afterPaint(fn)`
- L360 `queueSave(idle=false)`
- L367 `flushQueuedSave(hard=false)`
- L372 `undo()`
- L380 `toast(text,canUndo=false)`
- L388 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L389 `onClick(fn)`
- L391 `attempt(fn)`
- L395 `modal(title,body)`
- L404 `modalRestore()`
- L414 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L415 `modalBack()`
- L416 `goDate(d)`
- L423 `renderHeader()`
- L436 `renderRows(entries)`
- L440 `entryValues(e)`
- L441 `renderLog()`
- L448 `fromFood(id,amount,meal)`
- L454 `pantryId(name)`
- L456 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L475 `addEntries(entries,message='Añadido',d=date,opts={})`
- L484 `recipe(kind)`
- L491 `summary(entries)`
- L495 `renderPresetInfo()`
- L508 `stripCode(raw)`
- L514 `sanitizeNutrients(o,grams=100,fallbackRefId='')`
- L541 `parseBIO(raw,meal=$('meal-select')`
- L553 `parseSmart(raw)`
- L557 constante `COUNT`
- L558 constante `UNIT_RE`
- L622 `offToNutrients(nut={},fallbackName='')` — Open Food Facts (gratis, sin clave, CORS nativo): consulta por código de barras o texto.
- L643 `lookupOFFBarcode(code,signal,ms=3200)`
- L659 `searchOFF(query,signal,ms=4500)`
- L678 `openProductSearch()`
- L717 `nutrientFields(n,prefix='n_')`
- L718 `readNutrients(form,prefix='n_')`
- L723 `editEntry(id)`
- L732 `editFood(id,pending=null)`
- L737 `usageStats(days=90)`
- L745 `renderFoods(forceList=false)`
- L757 `nutrientSources(key)`
- L764 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L765 `suppSlot(meal)`
- L766 `renderSupps()`
- L781 `editPlan(id)`
- L788 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L809 `makePrompt(meal='Comida',note='')`
- L814 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L818 `pantryCompact()`
- L822 constante `MEAL_AI_SCHEMA`
- L863 `mealSystemPrompt(usePhoto)`
- L879 `hydrateAIItems(rawItems,fallback,usePhoto,aiModel,signal)`
- L928 `photoPrompt(meal,note)`
- L931 `resetPhoto()`
- L942 `openPhoto()`
- L948 `shrinkPhoto(file)`
- L951 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L977 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L984 `cleanFood(id,f)`
- L991 `migrateBase(o)`
- L1011 `download(name,text,type)`
- L1020 `portable()`
- L1074 `syncAppIcons()`
- L1082 `downloadAppIcons()`
- L1119 constante `PROFILES_KEY`
- L1121 `ensureProfilesStore()`
- L1141 `resetProfileSessionUI()`
- L1148 `saveProfilesStore(st)`
- L1157 `syncCurrentProfileToStore(snapObj=null,immediate=true)`
- L1168 `activeProfileName()`
- L1172 `renderProfilesList()`
- L1214 `switchProfile(id)`
- L1236 `deleteProfileById(id)`
- L1261 `refreshDrawerSummary()`
- L1278 `toggleLeftDrawer(force)`
- L1293 `buildAIExportText(rangeOverride)`
- L1548 `copyAIExport()`
- L1562 `downloadAIExport()`
- L1571 `renderDrawerChat()`
- L1590 `buildDrawerChatContext()`
- L1629 `buildDrawerChatPrompt(question)`
- L1641 `askDrawerAI(rawQuestion)`
- L1730 constante `CLOUD_OFF_KEY`
- L1741 `bytesToB64(u8)`
- L1742 `b64ToBytes(s)`
- L1743 `bytesToB64Url(u8)`
- L1744 `sha256Hex(str)`
- L1745 `sha256Bytes(str)`
- L1746 `generateSyncKey()`
- L1747 `ensureSyncKey()`
- L1748 `mirrorSyncKey(k)`
- L1749 `deriveSyncCreds(keyStr)`
- L1755 `hasMeaningfulData()`
- L1762 `buildCloudBundle()`
- L1769 `encryptVaultPayload(obj,keyStr)`
- L1777 `readDecompressedText(bytes,maxBytes=10*1024*1024)`
- L1793 `decryptVaultPayload(resp,keyStr)`
- L1805 `bundleHash(bundle)`
- L1809 `applyCloudBundle(o,rev=1)`
- L1819 `cloudPull(keyStr,opts={})`
- L1839 `cloudPush(opts={})`
- L1876 `scheduleCloudPush()`
- L1882 `scheduleAutoCloudPull(delayMs=120)`
- L1896 `saveSyncToPassMgr()`
- L1903 `trySilentPassMgrRecovery()`
- L1913 `extractSyncKeyInput(val)`
- L1919 `applySyncKey(rawKey,opts={})`
- L1940 `takeSyncCode()`
- L1951 `renderCloudStatus()`
- L1974 `buildMagicSyncUrl()`
- L1981 `openMagicSyncModal()`
- L1990 `shareMagicSyncLink()`
- L1997 `copyMagicSyncLink()`
- L2002 `openCloudLinkModal()`
- L2005 `deleteCloudBackup(confirmed=false)`
- L2042 `mirrorToIDB(raw,profRaw)`
- L2045 `storageStatus()`
- L2052 `idbReadWrite(mode,value,key='current')`
- L2053 `openDB()`
- L2055 `flushDeferredSave()`
- L2066 `save(skipCloud=false)`

### Eventos generales: añadir con un toque, editar, eliminar

- L2095 `setQuantity(id,value,msg='Cantidad actualizada')`
- L2099 `niceStep(v)`
- L2100 `stepQuantity(id,dir)`
- L2154 `renderAppInfo(force=false)`
- L2186 `init()`
- L2222 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L2224 `setNav(v)`
- L2229 `go(v,focus)`
- L2240 constante `THEME_KEY`
- L2241 constante `SUN_SVG`
- L2242 constante `MOON_SVG`
- L2244 `syncThemeUI()`
- L2258 `toggleTheme()`
- L2268 `syncLogoTheme()`
- L2277 `applyMenuBtnState()`
- L2301 `syncDatePill()`
- L2313 `clampBtnPos(el,x,y)`
- L2323 `bindDraggableBtn(el,storeKey)`
- L2384 `bindDrawerGestures()`
- L2422 `animateValue(el,to,suffix='%',digits=0)`
- L2431 `tick(now)`
- L2434 `macroCard(key,name,color)`
- L2435 `renderToday()`
- L2459 `renderBio()`
- L2484 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L2486 constante `HOME`
- L2488 `coachCandidates()`
- L2494 `coachIdeas(t,g,ref,meal)`
- L2513 `coachQuickAdd(key)`
- L2521 `renderCoach()`
- L2543 `coachPrompt()`
- L2552 `nutrientDetailStandard(key)`
- L2567 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L2573 `upgradeTo12(s,o)`
- L2578 `benfotiamineTotals(entries=effectiveEntries()`
- L2587 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L2589 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L2601 `microStat(m,t=totals()`
- L2606 `metric(m,t=totals()`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L2613 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L2614 `ratioInfo(key,t=totals()`
- L2653 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L2670 constante `RATIO_ENDS`
- L2672 `ratioZones(i)` — v68: cada equilibrio tiene una zona «aceptable» (ni verde ni mala) y su meta visible en la tarjeta.
- L2680 `ratioTone(i)`
- L2685 constante `NEAR_HEAD`
- L2686 `ratioBar(i,big=false)`
- L2695 `ratioNeedBase(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L2713 `needHTML(i,t)`
- L2714 `ratioNeed(i,t=totals()`
- L2718 `adBalance(t=totals()`
- L2745 `zncuSuppKey()`
- L2746 `zncuSuppCfg()`
- L2768 `zncuDoseLabel(zn,cu)`
- L2771 `hasZncuSupp(d=day()`
- L2776 `toggleZncuSupp()`
- L2796 `openZncuConfig()`
- L2802 `renderRatios()`
- L2813 `ratioDetail(key)`
- L2830 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L2847 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L2862 `renderMicroMap(t=totals()`
- L2875 `nutrientDetailForDay(key)`
- L2880 `editTargetsForm()`
- L2890 `mealData()`
- L2895 `renderMealSegments()`
- L2903 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L2938 constante `FAT_KEYS`
- L2940 `fatData(entries=effectiveEntries()`
- L2946 `energyData(entries=effectiveEntries()`
- L2950 `segmentedBar(items,total,attr)`
- L2954 `renderMealChart()`
- L2959 `renderFat()`
- L2967 `fatDetail(key)`
- L2972 `energyDetail(key)`
- L2979 `portionCandidates(q='')`
- L2984 `openPortion()`
- L2997 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L3012 `templates()`
- L3016 `renderExtra()`
- L3027 `updateExtra(reset=true)`
- L3039 `addExtra(id,amount)`
- L3055 `shakePreview()`
- L3056 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L3071 constante `LENS`
- L3077 `lensKey(key)`
- L3078 `lensHTML(key)`
- L3082 `appendLens(key)`
- L3091 `weekDates()`

### IA en la página: conexión directa o por servidor

- L3101 constante `MEAL_WORD`
- L3102 `mealOfWord(w)`
- L3103 `mealFromText(raw,fallback)`
- L3107 `canonMeal(v,fallback)`
- L3115 `localMeal(raw,meal)`
- L3121 constante `AI_FALLBACK`
- L3122 constante `GEMINI_DEFAULTS`
- L3123 constante `GROQ_DEFAULTS`
- L3124 `aiTaskProfile(task,hasImg=false)`
- L3132 `geminiThinkLevel(model,want)`
- L3138 `supportsGeminiTemp(model)`
- L3139 `readSSE(res,onEvent)`
- L3158 `applyAIConfig(raw)`
- L3184 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L3185 `callGemini(model,key,prompt,img,signal,opts={})`
- L3231 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), Groq (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L3239 `aiProv(m=$('ai-mode')`
- L3240 `aiBase(mode)`
- L3249 `chatHeaders(mode,key)`
- L3256 `callChat(mode,model,key,prompt,img,signal,opts={})` — ChatGPT, Claude, Groq, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L3310 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L3325 constante `OLD_GEMINI_RE`
- L3326 constante `MODEL_PREF`
- L3327 `pickModel(ids,mode=$('ai-mode')`
- L3341 `ensureModel(st)`
- L3357 `syncProvider()`
- L3376 `requestAI(prompt,img,signal,modelOverride='',onStep=null,opts={})`
- L3413 constante `AI_PREF`
- L3414 `aiConnected()`
- L3415 `syncAI()`
- L3417 `saveAIPrefs()`
- L3418 `loadAIPrefs()`
- L3419 `openAISetup()`
- L3426 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L3433 constante `MACROS`
- L3435 `cleanGoals(o,fallback)`
- L3440 `cleanCompare(o={})`
- L3444 `snapshotDay(d,reference='saved')`
- L3449 `upgradeTo17(s,o)`
- L3454 `entriesFor(d,source=weekSource)`
- L3458 `dayRow(dt,source=weekSource)`
- L3462 `goalsFor(dt)`
- L3468 `metricValue(r,key)`
- L3474 `targetOf(dt,key)`
- L3478 `weekSummary()`
- L3482 `aggregate(key,summary=weekSummary()`
- L3486 `tone(pct,mode='macro')`
- L3493 `pctText(a)`
- L3494 `weekProgress(a,color)`
- L3495 `renderWeekMicros(s)`
- L3507 `ratioAggregate(s,num,den)`
- L3511 `renderWeekRatios(s)`
- L3517 `renderWeekTable(s)`
- L3518 `weeklyDetail(key,oneDate=null)`
- L3527 `weekRatioDetail(key)`
- L3535 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L3541 `openDay(dt)`
- L3579 `withDayGoals(fn)`
- L3584 `renderMicros()`
- L3585 `nutrientDetail(key)`
- L3586 `editTargets()`
- L3587 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L3597 `summaryFor(start)`
- L3601 `ringSVG(pct,color,marker)`
- L3603 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L3607 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L3624 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L3625 `macroTone(p)`
- L3626 `dayMacroPct(dt,k)`
- L3627 `renderWeekly()`
- L3650 `weekDetail(dt,picked)`
- L3658 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L3668 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L3674 `sparkline(pts)`
- L3680 `renderCalendar()`
- L3697 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L3698 `splitMeals(raw)`
- L3708 `localDay(raw,fallback)`
- L3715 `askUnitWeightAI(foodName)`
- L3725 `promptUnitWeight(foodId,count,meal)`
- L3741 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L3801 `parseCsv(text)`
- L3816 `hevyDate(value,format='auto')`
- L3833 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L3848 constante `GYM_APPS`
- L3850 `gymSig(headers)`
- L3851 `gymApp(headers)`
- L3852 `hevyMapping()`
- L3853 `gymSaved()`
- L3854 `renderMapping(parsed)`
- L3871 `optionalNum(v,min=0,max=1e7)`
- L3876 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L3883 `buildHevy(parsed,map)`
- L3917 `cleanWorkout(s)`
- L3924 `formatGymAI(txt)`
- L3935 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L3960 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L3961 constante `GP_ALIAS`
- L3971 `gpNorm(s)`
- L3972 `gpKey(name)`
- L3976 `gpF(n,d=0)`
- L3977 `gpDate(d,opt)`
- L3978 `gpMonday(d)`
- L3979 constante `GP_GROUPS`
- L3994 constante `GP_COLORS`
- L3995 `gpGroup(name)`
- L3996 `gpWorkSets(s)`
- L3998 `gpModel()`
- L4026 `gpSessionMetrics(e,sets)`
- L4041 constante `GP_METRICS`
- L4046 `gpMetricsFor(e)`
- L4047 `gpRangeHist(e)`
- L4048 `gpPRs(model)`
- L4071 `gpStatus(e)`
- L4089 `gpNext(e)`
- L4097 `gpChart(e)`
- L4125 `gpPointDetail(e)`
- L4131 `gpRepTable(e)`
- L4138 `gpKpis(model)`
- L4147 `gpWeekData(model,w)` — Datos de una semana de gimnasio (series por músculo y sesiones).
- L4152 `gpWeekLabel(w,short)`
- L4153 `gpWeekly(model)`
- L4172 `gpMuscles(model)`
- L4180 `gpHeat(model)` — v69: «Constancia» — mapa de días entrenados (como antes), con días de la semana, meses, intensidad y detalle al tocar.
- L4200 `gpExList(model)`
- L4207 `gpExDetail(model)`
- L4220 `gpDayFood(dt)`
- L4221 `gpNutrition(model)`
- L4228 `gpRecentPRs(model)`
- L4232 `gpSessions(model)`
- L4238 `gpSessionModal(id)`
- L4249 `gpWeekModal(w)`
- L4256 `gpSelect(key)`
- L4257 `gpClick(e)`
- L4274 `renderGym()`
- L4298 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L4307 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L4313 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L4338 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L4342 `showHelp()`
- L4346 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L4348 `markBackup()`
- L4352 `exportJSON()`
- L4357 `drawBackupReminder()`
- L4369 `applyDensity()`
- L4381 `syncDayComplete()`
- L4384 `drawMeals()` — Comidas del día de un vistazo.
- L4392 `filterLog()` — Buscador de Registro.
- L4405 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L4411 `recentFoods()`
- L4416 `quickChip(e,fav)`
- L4434 `drawQuickFoods()`
- L4463 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L4467 `toggleAddPanel(id)`
- L4480 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L4491 `pasteMessage(text,ok)`
- L4499 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L4510 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L4521 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L4527 `upgradeTo27(s,o)`
- L4544 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L4566 `storableState()`

### Render único: actualiza toda la página

- L4575 `nearView(el)`
- L4577 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L4582 `scheduleLazyRender()`
- L4586 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L4623 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L4624 constante `REF_TABLE`
- L4631 `refTargets(mode)`
- L4632 `syncMicroMode()`
- L4645 `mealByHour(h=new Date()`
- L4652 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L4663 `dataSummary(s)`
- L4667 `confirmImport(next,name)`
- L4674 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L4680 `checkUpdate()`
- L4685 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L4701 constante `GAP_PREFER`
- L4702 constante `GAP_SKIP`
- L4703 constante `GAP_UNIT`
- L4704 `gapQty(f,x)`
- L4705 `gapFoods(key,gap,ctx)`
- L4724 `weekSources(key,sum)`
- L4730 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L4743 `gapRow(x,open,meal,sum,ctx)`
- L4759 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L4784 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L4785 `isFemale(s=state)`
- L4786 `sexLabel(s=state)`
- L4787 `sexBadge(sex)`
- L4789 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L4790 constante `OPT_FEMALE`
- L4801 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba; A (1.500 µg = 5.000 UI) y D (50 µg = 2.000 UI) mantienen A:D en zona verde (2,5:1).
- L4802 `applySexOpt(sex)`
- L4804 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L4809 `cleanPreset(p,fb)`
- L4813 `dayNamesFor(types)`
- L4815 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L4825 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L4833 `profV()`
- L4834 `isTrainDay(i)`
- L4835 `activityName(i)`
- L4836 `dayFaf(i)`
- L4837 `presetDesc(cfg,shake)`
- L4841 `profileDescription()`
- L4849 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L4851 `wizCatalog()`
- L4852 `wizOpen(opts={})`
- L4868 `wizTitle()`
- L4869 `wizPaint(sameStep=true)`
- L4878 `wizSync()`
- L4897 `wizFoodOptions()`
- L4900 `wizPresetSummary(cfg,whey)`
- L4905 `wizPresetHTML(kind)`
- L4913 `wizPreview()`
- L4924 `wizLiveHTML()`
- L4928 `wizHTML()`
- L4975 `isStandalonePWA()`
- L4976 `isInAppWebview()`
- L4977 `isBraveBrowser()`
- L4978 `syncInstallButtons()`
- L4984 `buildTransferUrl()`
- L4999 `triggerPWAInstall()`
- L5034 `wizCommit()`
- L5085 `showPostWizInstallBanner(name)`

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L5147 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L5148 constante `SUPP_CATALOG`
- L5173 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L5174 constante `PEAT_BREAKFAST`
- L5175 constante `PEAT_SHAKE`
- L5177 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L5184 `benfoUser()`
- L5186 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L5202 `ico(n)`
- L5204 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L5213 `showTour(i=0)`
- L5225 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L5226 `hubAction(v)`
- L5234 constante `FB_CATS` — Envíos anónimos directos al buzón de BioPeat (sin cuentas ni datos personales).
- L5236 `openFeedback()`
- L5240 `feedbackData()`
- L5247 `feedbackText()`
- L5248 `sendFeedback()`
- L5268 `shareFeedback()`
- L5285 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L5292 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L5300 constante `I18N_EN`

### v59: idioma (español / inglés)

- L5305 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L5306 constante `WD_EN`
- L5307 `trOne(s)`
- L5315 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L5316 constante `ES_FOOD_GYM`
- L5353 `trFood(s)`
- L5365 constante `TR_TPL`
- L5406 `trLower(s)`
- L5407 `trTpl(s,attr)`
- L5408 constante `FOOD_SEL`
- L5409 `trText(s,attr=false)`
- L5419 `trNode(n)`
- L5438 `trEl(el)`
- L5451 `trTree(root)`
- L5460 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L5474 `flushTr()`
- L5475 `syncTrObserver()`
- L5480 `loadEnDict()`
- L5492 `setLang(l,quiet)`
- L5507 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter + Worker agregados), solo en la web publicada

- L5516 constante `GC_CODE`
- L5517 `pingAnalytics(extra={})`
- L5533 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L5545 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L5546 `packMove()`
- L5554 `unpackMove(code)`
- L5565 `moveData()`
- L5575 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L5581 `checkMove(code)`
- L5600 `aiFrameworkLines()` — v69: marco de referencia del informe para IA. Así cualquier IA, aunque no conozca la app ni al usuario, sabe con qué comparar.

### Arranque

