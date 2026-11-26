# MAPA DEL CÓDIGO · BioPeat v83 (revisión de datos 27)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

Arquitectura modular: `index.html` (65 KB), `assets/styles.css`, `assets/data.js`, `assets/app.js` (512 KB) y `assets/i18n-en.js`.

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

- L72 constante `REF_MAP` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L73 constante `REF_CACHE`
- L75 `ensureRefIndex()`
- L82 `refNutrients(id)`
- L90 constante `STRIP_PREP_RE`
- L91 `findRef(text,strict=false)`
- L114 `refCatalogCompact()`
- L115 `fromRef(id,amount,meal,note='',srcText='')`
- L120 `optInfo(k,goal)`
- L127 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L135 `optLine(k,goal,unit)`
- L142 `optRefHTML(k,goal,unit)`
- L143 constante `FAF`
- L145 constante `LOC`
- L149 `number(v,min=0,max=1e6)`
- L155 `decimalInputs(root=document)`
- L156 `localDate(d=new Date()`
- L157 `validDate(s)`
- L162 `shift(s,n)`
- L170 `stripProto(o)`
- L177 `cleanBio(b)`
- L186 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L188 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L194 constante `DAY_TYPES`
- L195 constante `NEW_V54`
- L199 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L202 `bmr(w=state.profile.weight)` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L208 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L233 `cleanNutrients(o,required=false)`
- L245 `cleanEntry(e)`
- L250 `cleanPlan(p)`
- L254 `planEntry(p)`
- L263 `seedPlan(d,whichDate)`
- L267 `ensureDay(d=date)`
- L274 `effectiveEntries(d=day()`
- L275 constante `SALTED_IDS`
- L276 constante `SWEET_RE`
- L277 `inferFatShares(e,txt=normalize((e?.name||'')`
- L295 `inferredNutrients(e)`
- L337 `totals(entries)`
- L349 `change(fn,message='Guardado')`
- L353 `undo()`
- L361 `toast(text,canUndo=false)`
- L369 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L370 `onClick(fn)`
- L372 `attempt(fn)`
- L376 `modal(title,body)`
- L385 `modalRestore()`
- L395 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L396 `modalBack()`
- L397 `goDate(d)`
- L404 `renderHeader()`
- L417 `renderRows(entries)`
- L421 `entryValues(e)`
- L422 `renderLog()`
- L429 `fromFood(id,amount,meal)`
- L435 `pantryId(name)`
- L437 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L456 `addEntries(entries,message='Añadido',d=date,opts={})`
- L465 `recipe(kind)`
- L472 `summary(entries)`
- L476 `renderPresetInfo()`
- L489 `stripCode(raw)`
- L495 `sanitizeNutrients(o,grams=100,fallbackRefId='')`
- L522 `parseBIO(raw,meal=$('meal-select')`
- L534 `parseSmart(raw)`
- L538 constante `COUNT`
- L539 constante `UNIT_RE`
- L603 `offToNutrients(nut={},fallbackName='')` — Open Food Facts (gratis, sin clave, CORS nativo): consulta por código de barras o texto.
- L624 `lookupOFFBarcode(code,signal,ms=3200)`
- L640 `searchOFF(query,signal,ms=4500)`
- L659 `openProductSearch()`
- L698 `nutrientFields(n,prefix='n_')`
- L699 `readNutrients(form,prefix='n_')`
- L704 `editEntry(id)`
- L713 `editFood(id,pending=null)`
- L718 `usageStats(days=90)`
- L726 `renderFoods(forceList=false)`
- L738 `nutrientSources(key)`
- L745 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L746 `suppSlot(meal)`
- L747 `renderSupps()`
- L762 `editPlan(id)`
- L769 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L790 `makePrompt(meal='Comida',note='')`
- L795 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L799 `pantryCompact()`
- L803 constante `MEAL_AI_SCHEMA`
- L844 `mealSystemPrompt(usePhoto)`
- L860 `hydrateAIItems(rawItems,fallback,usePhoto,aiModel,signal)`
- L909 `photoPrompt(meal,note)`
- L912 `resetPhoto()`
- L923 `openPhoto()`
- L929 `shrinkPhoto(file)`
- L932 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L958 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L965 `cleanFood(id,f)`
- L972 `migrateBase(o)`
- L992 `download(name,text,type)`
- L1001 `portable()`
- L1055 `syncAppIcons()`
- L1063 `downloadAppIcons()`
- L1100 constante `PROFILES_KEY`
- L1102 `ensureProfilesStore()`
- L1122 `resetProfileSessionUI()`
- L1129 `saveProfilesStore(st)`
- L1138 `syncCurrentProfileToStore(snapObj=null,immediate=true)`
- L1149 `activeProfileName()`
- L1153 `renderProfilesList()`
- L1195 `switchProfile(id)`
- L1217 `deleteProfileById(id)`
- L1242 `refreshDrawerSummary()`
- L1259 `toggleLeftDrawer(force)`
- L1274 `buildAIExportText(rangeOverride)`
- L1529 `copyAIExport()`
- L1543 `downloadAIExport()`
- L1552 `renderDrawerChat()`
- L1571 `buildDrawerChatContext()`
- L1610 `buildDrawerChatPrompt(question)`
- L1622 `askDrawerAI(rawQuestion)`
- L1711 constante `CLOUD_OFF_KEY`
- L1722 `bytesToB64(u8)`
- L1723 `b64ToBytes(s)`
- L1724 `bytesToB64Url(u8)`
- L1725 `sha256Hex(str)`
- L1726 `sha256Bytes(str)`
- L1727 `generateSyncKey()`
- L1728 `ensureSyncKey()`
- L1729 `mirrorSyncKey(k)`
- L1730 `deriveSyncCreds(keyStr)`
- L1736 `hasMeaningfulData()`
- L1743 `buildCloudBundle()`
- L1750 `encryptVaultPayload(obj,keyStr)`
- L1758 `readDecompressedText(bytes,maxBytes=10*1024*1024)`
- L1774 `decryptVaultPayload(resp,keyStr)`
- L1786 `bundleHash(bundle)`
- L1790 `applyCloudBundle(o,rev=1)`
- L1800 `cloudPull(keyStr,opts={})`
- L1820 `cloudPush(opts={})`
- L1857 `scheduleCloudPush()`
- L1863 `scheduleAutoCloudPull(delayMs=120)`
- L1877 `saveSyncToPassMgr()`
- L1884 `trySilentPassMgrRecovery()`
- L1894 `extractSyncKeyInput(val)`
- L1900 `applySyncKey(rawKey,opts={})`
- L1921 `takeSyncCode()`
- L1932 `renderCloudStatus()`
- L1955 `buildMagicSyncUrl()`
- L1962 `openMagicSyncModal()`
- L1971 `shareMagicSyncLink()`
- L1978 `copyMagicSyncLink()`
- L1983 `openCloudLinkModal()`
- L1986 `deleteCloudBackup(confirmed=false)`
- L2023 `mirrorToIDB(raw,profRaw)`
- L2026 `storageStatus()`
- L2033 `idbReadWrite(mode,value,key='current')`
- L2034 `openDB()`
- L2036 `flushDeferredSave()`
- L2046 `save(skipCloud=false)`

### Eventos generales: añadir con un toque, editar, eliminar

- L2074 `setQuantity(id,value,msg='Cantidad actualizada')`
- L2078 `niceStep(v)`
- L2079 `stepQuantity(id,dir)`
- L2133 `renderAppInfo(force=false)`
- L2165 `init()`
- L2201 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L2203 `setNav(v)`
- L2208 `go(v,focus)`
- L2219 constante `THEME_KEY`
- L2220 constante `SUN_SVG`
- L2221 constante `MOON_SVG`
- L2223 `syncThemeUI()`
- L2236 `toggleTheme()`
- L2246 `syncLogoTheme()`
- L2255 `applyMenuBtnState()`
- L2279 `syncDatePill()`
- L2291 `clampBtnPos(el,x,y)`
- L2301 `bindDraggableBtn(el,storeKey)`
- L2362 `bindDrawerGestures()`
- L2400 `animateValue(el,to,suffix='%',digits=0)`
- L2409 `tick(now)`
- L2412 `macroCard(key,name,color)`
- L2413 `renderToday()`
- L2437 `renderBio()`
- L2462 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L2464 constante `HOME`
- L2466 `coachCandidates()`
- L2472 `coachIdeas(t,g,ref,meal)`
- L2491 `coachQuickAdd(key)`
- L2499 `renderCoach()`
- L2521 `coachPrompt()`
- L2530 `nutrientDetailStandard(key)`
- L2545 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L2551 `upgradeTo12(s,o)`
- L2556 `benfotiamineTotals(entries=effectiveEntries()`
- L2565 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L2567 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L2579 `microStat(m,t=totals()`
- L2584 `metric(m,t=totals()`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L2591 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L2592 `ratioInfo(key,t=totals()`
- L2631 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L2648 constante `RATIO_ENDS`
- L2650 `ratioZones(i)` — v68: cada equilibrio tiene una zona «aceptable» (ni verde ni mala) y su meta visible en la tarjeta.
- L2658 `ratioTone(i)`
- L2663 constante `NEAR_HEAD`
- L2664 `ratioBar(i,big=false)`
- L2673 `ratioNeedBase(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L2691 `needHTML(i,t)`
- L2692 `ratioNeed(i,t=totals()`
- L2696 `adBalance(t=totals()`
- L2723 `zncuSuppKey()`
- L2724 `zncuSuppCfg()`
- L2746 `zncuDoseLabel(zn,cu)`
- L2749 `hasZncuSupp(d=day()`
- L2754 `toggleZncuSupp()`
- L2774 `openZncuConfig()`
- L2780 `renderRatios()`
- L2791 `ratioDetail(key)`
- L2808 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L2825 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L2840 `renderMicroMap(t=totals()`
- L2853 `nutrientDetailForDay(key)`
- L2858 `editTargetsForm()`
- L2868 `mealData()`
- L2873 `renderMealSegments()`
- L2881 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L2916 constante `FAT_KEYS`
- L2918 `fatData(entries=effectiveEntries()`
- L2924 `energyData(entries=effectiveEntries()`
- L2928 `segmentedBar(items,total,attr)`
- L2932 `renderMealChart()`
- L2937 `renderFat()`
- L2945 `fatDetail(key)`
- L2950 `energyDetail(key)`
- L2957 `portionCandidates(q='')`
- L2962 `openPortion()`
- L2975 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L2990 `templates()`
- L2994 `renderExtra()`
- L3005 `updateExtra(reset=true)`
- L3017 `addExtra(id,amount)`
- L3033 `shakePreview()`
- L3034 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L3049 constante `LENS`
- L3055 `lensKey(key)`
- L3056 `lensHTML(key)`
- L3060 `appendLens(key)`
- L3069 `weekDates()`

### IA en la página: conexión directa o por servidor

- L3079 constante `MEAL_WORD`
- L3080 `mealOfWord(w)`
- L3081 `mealFromText(raw,fallback)`
- L3085 `canonMeal(v,fallback)`
- L3093 `localMeal(raw,meal)`
- L3099 constante `AI_FALLBACK`
- L3100 constante `GEMINI_DEFAULTS`
- L3101 constante `GROQ_DEFAULTS`
- L3102 `aiTaskProfile(task,hasImg=false)`
- L3110 `geminiThinkLevel(model,want)`
- L3116 `supportsGeminiTemp(model)`
- L3117 `readSSE(res,onEvent)`
- L3136 `applyAIConfig(raw)`
- L3162 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L3163 `callGemini(model,key,prompt,img,signal,opts={})`
- L3209 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), Groq (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L3217 `aiProv(m=$('ai-mode')`
- L3218 `aiBase(mode)`
- L3227 `chatHeaders(mode,key)`
- L3234 `callChat(mode,model,key,prompt,img,signal,opts={})` — ChatGPT, Claude, Groq, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L3288 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L3303 constante `OLD_GEMINI_RE`
- L3304 constante `MODEL_PREF`
- L3305 `pickModel(ids,mode=$('ai-mode')`
- L3319 `ensureModel(st)`
- L3335 `syncProvider()`
- L3354 `requestAI(prompt,img,signal,modelOverride='',onStep=null,opts={})`
- L3391 constante `AI_PREF`
- L3392 `aiConnected()`
- L3393 `syncAI()`
- L3395 `saveAIPrefs()`
- L3396 `loadAIPrefs()`
- L3397 `openAISetup()`
- L3404 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L3411 constante `MACROS`
- L3413 `cleanGoals(o,fallback)`
- L3418 `cleanCompare(o={})`
- L3422 `snapshotDay(d,reference='saved')`
- L3427 `upgradeTo17(s,o)`
- L3432 `entriesFor(d,source=weekSource)`
- L3436 `dayRow(dt,source=weekSource)`
- L3440 `goalsFor(dt)`
- L3446 `metricValue(r,key)`
- L3452 `targetOf(dt,key)`
- L3456 `weekSummary()`
- L3460 `aggregate(key,summary=weekSummary()`
- L3464 `tone(pct,mode='macro')`
- L3471 `pctText(a)`
- L3472 `weekProgress(a,color)`
- L3473 `renderWeekMicros(s)`
- L3485 `ratioAggregate(s,num,den)`
- L3489 `renderWeekRatios(s)`
- L3495 `renderWeekTable(s)`
- L3496 `weeklyDetail(key,oneDate=null)`
- L3505 `weekRatioDetail(key)`
- L3513 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L3519 `openDay(dt)`
- L3557 `withDayGoals(fn)`
- L3562 `renderMicros()`
- L3563 `nutrientDetail(key)`
- L3564 `editTargets()`
- L3565 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L3575 `summaryFor(start)`
- L3579 `ringSVG(pct,color,marker)`
- L3581 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L3585 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L3602 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L3603 `macroTone(p)`
- L3604 `dayMacroPct(dt,k)`
- L3605 `renderWeekly()`
- L3628 `weekDetail(dt,picked)`
- L3636 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L3646 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L3652 `sparkline(pts)`
- L3658 `renderCalendar()`
- L3675 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L3676 `splitMeals(raw)`
- L3686 `localDay(raw,fallback)`
- L3693 `askUnitWeightAI(foodName)`
- L3703 `promptUnitWeight(foodId,count,meal)`
- L3719 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L3779 `parseCsv(text)`
- L3794 `hevyDate(value,format='auto')`
- L3811 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L3826 constante `GYM_APPS`
- L3828 `gymSig(headers)`
- L3829 `gymApp(headers)`
- L3830 `hevyMapping()`
- L3831 `gymSaved()`
- L3832 `renderMapping(parsed)`
- L3849 `optionalNum(v,min=0,max=1e7)`
- L3854 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L3861 `buildHevy(parsed,map)`
- L3895 `cleanWorkout(s)`
- L3902 `formatGymAI(txt)`
- L3913 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L3938 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L3939 constante `GP_ALIAS`
- L3949 `gpNorm(s)`
- L3950 `gpKey(name)`
- L3954 `gpF(n,d=0)`
- L3955 `gpDate(d,opt)`
- L3956 `gpMonday(d)`
- L3957 constante `GP_GROUPS`
- L3972 constante `GP_COLORS`
- L3973 `gpGroup(name)`
- L3974 `gpWorkSets(s)`
- L3976 `gpModel()`
- L4004 `gpSessionMetrics(e,sets)`
- L4019 constante `GP_METRICS`
- L4024 `gpMetricsFor(e)`
- L4025 `gpRangeHist(e)`
- L4026 `gpPRs(model)`
- L4049 `gpStatus(e)`
- L4067 `gpNext(e)`
- L4075 `gpChart(e)`
- L4103 `gpPointDetail(e)`
- L4109 `gpRepTable(e)`
- L4116 `gpKpis(model)`
- L4125 `gpWeekData(model,w)` — Datos de una semana de gimnasio (series por músculo y sesiones).
- L4130 `gpWeekLabel(w,short)`
- L4131 `gpWeekly(model)`
- L4150 `gpMuscles(model)`
- L4158 `gpHeat(model)` — v69: «Constancia» — mapa de días entrenados (como antes), con días de la semana, meses, intensidad y detalle al tocar.
- L4178 `gpExList(model)`
- L4185 `gpExDetail(model)`
- L4198 `gpDayFood(dt)`
- L4199 `gpNutrition(model)`
- L4206 `gpRecentPRs(model)`
- L4210 `gpSessions(model)`
- L4216 `gpSessionModal(id)`
- L4227 `gpWeekModal(w)`
- L4234 `gpSelect(key)`
- L4235 `gpClick(e)`
- L4252 `renderGym()`
- L4276 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L4285 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L4291 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L4316 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L4320 `showHelp()`
- L4324 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L4326 `markBackup()`
- L4330 `exportJSON()`
- L4335 `drawBackupReminder()`
- L4347 `applyDensity()`
- L4359 `syncDayComplete()`
- L4362 `drawMeals()` — Comidas del día de un vistazo.
- L4370 `filterLog()` — Buscador de Registro.
- L4383 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L4389 `recentFoods()`
- L4394 `quickChip(e,fav)`
- L4412 `drawQuickFoods()`
- L4441 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L4445 `toggleAddPanel(id)`
- L4458 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L4469 `pasteMessage(text,ok)`
- L4477 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L4488 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L4499 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L4505 `upgradeTo27(s,o)`
- L4522 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L4544 `storableState()`

### Render único: actualiza toda la página

- L4553 `nearView(el)`
- L4555 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L4560 `scheduleLazyRender()`
- L4564 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L4601 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L4602 constante `REF_TABLE`
- L4609 `refTargets(mode)`
- L4610 `syncMicroMode()`
- L4623 `mealByHour(h=new Date()`
- L4630 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L4641 `dataSummary(s)`
- L4645 `confirmImport(next,name)`
- L4652 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L4658 `checkUpdate()`
- L4663 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L4678 constante `GAP_PREFER`
- L4679 constante `GAP_SKIP`
- L4680 constante `GAP_UNIT`
- L4681 `gapQty(f,x)`
- L4682 `gapFoods(key,gap,ctx)`
- L4701 `weekSources(key,sum)`
- L4707 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L4720 `gapRow(x,open,meal,sum,ctx)`
- L4736 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L4761 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L4762 `isFemale(s=state)`
- L4763 `sexLabel(s=state)`
- L4764 `sexBadge(sex)`
- L4766 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L4767 constante `OPT_FEMALE`
- L4778 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba; A (1.500 µg = 5.000 UI) y D (50 µg = 2.000 UI) mantienen A:D en zona verde (2,5:1).
- L4779 `applySexOpt(sex)`
- L4781 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L4786 `cleanPreset(p,fb)`
- L4790 `dayNamesFor(types)`
- L4792 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L4802 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L4810 `profV()`
- L4811 `isTrainDay(i)`
- L4812 `activityName(i)`
- L4813 `dayFaf(i)`
- L4814 `presetDesc(cfg,shake)`
- L4818 `profileDescription()`
- L4826 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L4828 `wizCatalog()`
- L4829 `wizOpen(opts={})`
- L4845 `wizTitle()`
- L4846 `wizPaint(sameStep=true)`
- L4855 `wizSync()`
- L4874 `wizFoodOptions()`
- L4877 `wizPresetSummary(cfg,whey)`
- L4882 `wizPresetHTML(kind)`
- L4890 `wizPreview()`
- L4901 `wizLiveHTML()`
- L4905 `wizHTML()`
- L4952 `isStandalonePWA()`
- L4953 `isInAppWebview()`
- L4954 `isBraveBrowser()`
- L4955 `syncInstallButtons()`
- L4961 `buildTransferUrl()`
- L4976 `triggerPWAInstall()`
- L5011 `wizCommit()`
- L5062 `showPostWizInstallBanner(name)`

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L5124 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L5125 constante `SUPP_CATALOG`
- L5150 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L5151 constante `PEAT_BREAKFAST`
- L5152 constante `PEAT_SHAKE`
- L5154 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L5161 `benfoUser()`
- L5163 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L5179 `ico(n)`
- L5181 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L5190 `showTour(i=0)`
- L5202 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L5203 `hubAction(v)`
- L5211 constante `FB_CATS` — Envíos anónimos directos al buzón de BioPeat (sin cuentas ni datos personales).
- L5213 `openFeedback()`
- L5217 `feedbackData()`
- L5224 `feedbackText()`
- L5225 `sendFeedback()`
- L5245 `shareFeedback()`
- L5262 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L5269 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L5277 constante `I18N_EN`

### v59: idioma (español / inglés)

- L5282 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L5283 constante `WD_EN`
- L5284 `trOne(s)`
- L5292 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L5293 constante `ES_FOOD_GYM`
- L5330 `trFood(s)`
- L5342 constante `TR_TPL`
- L5383 `trLower(s)`
- L5384 `trTpl(s,attr)`
- L5385 constante `FOOD_SEL`
- L5386 `trText(s,attr=false)`
- L5396 `trNode(n)`
- L5415 `trEl(el)`
- L5428 `trTree(root)`
- L5437 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L5451 `flushTr()`
- L5452 `syncTrObserver()`
- L5457 `loadEnDict()`
- L5469 `setLang(l,quiet)`
- L5484 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter + Worker agregados), solo en la web publicada

- L5493 constante `GC_CODE`
- L5494 `pingAnalytics(extra={})`
- L5510 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L5522 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L5523 `packMove()`
- L5531 `unpackMove(code)`
- L5542 `moveData()`
- L5552 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L5558 `checkMove(code)`
- L5577 `aiFrameworkLines()` — v69: marco de referencia del informe para IA. Así cualquier IA, aunque no conozca la app ni al usuario, sabe con qué comparar.

### Arranque

