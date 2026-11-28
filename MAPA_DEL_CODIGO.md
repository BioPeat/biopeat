# MAPA DEL CÓDIGO · BioPeat v84 (revisión de datos 27)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

Arquitectura modular: `index.html` (65 KB), `assets/styles.css`, `assets/data.js`, `assets/app.js` (513 KB) y `assets/i18n-en.js`.

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

- L73 constante `REF_MAP` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L74 constante `REF_CACHE`
- L76 `ensureRefIndex()`
- L83 `refNutrients(id)`
- L91 constante `STRIP_PREP_RE`
- L92 `findRef(text,strict=false)`
- L115 `refCatalogCompact()`
- L116 `fromRef(id,amount,meal,note='',srcText='')`
- L121 `optInfo(k,goal)`
- L128 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L136 `optLine(k,goal,unit)`
- L143 `optRefHTML(k,goal,unit)`
- L144 constante `FAF`
- L146 constante `LOC`
- L150 `number(v,min=0,max=1e6)`
- L156 `decimalInputs(root=document)`
- L157 `localDate(d=new Date()`
- L158 `validDate(s)`
- L163 `shift(s,n)`
- L171 `stripProto(o)`
- L178 `cleanBio(b)`
- L187 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L189 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L195 constante `DAY_TYPES`
- L196 constante `NEW_V54`
- L200 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L203 `bmr(w=state.profile.weight)` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L209 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L234 `cleanNutrients(o,required=false)`
- L246 `cleanEntry(e)`
- L251 `cleanPlan(p)`
- L255 `planEntry(p)`
- L264 `seedPlan(d,whichDate)`
- L268 `ensureDay(d=date)`
- L275 `effectiveEntries(d=day()`
- L276 constante `SALTED_IDS`
- L277 constante `SWEET_RE`
- L278 `inferFatShares(e,txt=normalize((e?.name||'')`
- L296 `inferredNutrients(e)`
- L338 `totals(entries)`
- L350 `change(fn,message='Guardado')`
- L356 `afterPaint(fn)`
- L357 `queueSave(idle=false)`
- L364 `flushQueuedSave(hard=false)`
- L369 `undo()`
- L377 `toast(text,canUndo=false)`
- L385 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L386 `onClick(fn)`
- L388 `attempt(fn)`
- L392 `modal(title,body)`
- L401 `modalRestore()`
- L411 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L412 `modalBack()`
- L413 `goDate(d)`
- L420 `renderHeader()`
- L433 `renderRows(entries)`
- L437 `entryValues(e)`
- L438 `renderLog()`
- L445 `fromFood(id,amount,meal)`
- L451 `pantryId(name)`
- L453 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L472 `addEntries(entries,message='Añadido',d=date,opts={})`
- L481 `recipe(kind)`
- L488 `summary(entries)`
- L492 `renderPresetInfo()`
- L505 `stripCode(raw)`
- L511 `sanitizeNutrients(o,grams=100,fallbackRefId='')`
- L538 `parseBIO(raw,meal=$('meal-select')`
- L550 `parseSmart(raw)`
- L554 constante `COUNT`
- L555 constante `UNIT_RE`
- L619 `offToNutrients(nut={},fallbackName='')` — Open Food Facts (gratis, sin clave, CORS nativo): consulta por código de barras o texto.
- L640 `lookupOFFBarcode(code,signal,ms=3200)`
- L656 `searchOFF(query,signal,ms=4500)`
- L675 `openProductSearch()`
- L714 `nutrientFields(n,prefix='n_')`
- L715 `readNutrients(form,prefix='n_')`
- L720 `editEntry(id)`
- L729 `editFood(id,pending=null)`
- L734 `usageStats(days=90)`
- L742 `renderFoods(forceList=false)`
- L754 `nutrientSources(key)`
- L761 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L762 `suppSlot(meal)`
- L763 `renderSupps()`
- L778 `editPlan(id)`
- L785 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L806 `makePrompt(meal='Comida',note='')`
- L811 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L815 `pantryCompact()`
- L819 constante `MEAL_AI_SCHEMA`
- L860 `mealSystemPrompt(usePhoto)`
- L876 `hydrateAIItems(rawItems,fallback,usePhoto,aiModel,signal)`
- L925 `photoPrompt(meal,note)`
- L928 `resetPhoto()`
- L939 `openPhoto()`
- L945 `shrinkPhoto(file)`
- L948 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L974 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L981 `cleanFood(id,f)`
- L988 `migrateBase(o)`
- L1008 `download(name,text,type)`
- L1017 `portable()`
- L1071 `syncAppIcons()`
- L1079 `downloadAppIcons()`
- L1116 constante `PROFILES_KEY`
- L1118 `ensureProfilesStore()`
- L1138 `resetProfileSessionUI()`
- L1145 `saveProfilesStore(st)`
- L1154 `syncCurrentProfileToStore(snapObj=null,immediate=true)`
- L1165 `activeProfileName()`
- L1169 `renderProfilesList()`
- L1211 `switchProfile(id)`
- L1233 `deleteProfileById(id)`
- L1258 `refreshDrawerSummary()`
- L1275 `toggleLeftDrawer(force)`
- L1290 `buildAIExportText(rangeOverride)`
- L1545 `copyAIExport()`
- L1559 `downloadAIExport()`
- L1568 `renderDrawerChat()`
- L1587 `buildDrawerChatContext()`
- L1626 `buildDrawerChatPrompt(question)`
- L1638 `askDrawerAI(rawQuestion)`
- L1727 constante `CLOUD_OFF_KEY`
- L1738 `bytesToB64(u8)`
- L1739 `b64ToBytes(s)`
- L1740 `bytesToB64Url(u8)`
- L1741 `sha256Hex(str)`
- L1742 `sha256Bytes(str)`
- L1743 `generateSyncKey()`
- L1744 `ensureSyncKey()`
- L1745 `mirrorSyncKey(k)`
- L1746 `deriveSyncCreds(keyStr)`
- L1752 `hasMeaningfulData()`
- L1759 `buildCloudBundle()`
- L1766 `encryptVaultPayload(obj,keyStr)`
- L1774 `readDecompressedText(bytes,maxBytes=10*1024*1024)`
- L1790 `decryptVaultPayload(resp,keyStr)`
- L1802 `bundleHash(bundle)`
- L1806 `applyCloudBundle(o,rev=1)`
- L1816 `cloudPull(keyStr,opts={})`
- L1836 `cloudPush(opts={})`
- L1873 `scheduleCloudPush()`
- L1879 `scheduleAutoCloudPull(delayMs=120)`
- L1893 `saveSyncToPassMgr()`
- L1900 `trySilentPassMgrRecovery()`
- L1910 `extractSyncKeyInput(val)`
- L1916 `applySyncKey(rawKey,opts={})`
- L1937 `takeSyncCode()`
- L1948 `renderCloudStatus()`
- L1971 `buildMagicSyncUrl()`
- L1978 `openMagicSyncModal()`
- L1987 `shareMagicSyncLink()`
- L1994 `copyMagicSyncLink()`
- L1999 `openCloudLinkModal()`
- L2002 `deleteCloudBackup(confirmed=false)`
- L2039 `mirrorToIDB(raw,profRaw)`
- L2042 `storageStatus()`
- L2049 `idbReadWrite(mode,value,key='current')`
- L2050 `openDB()`
- L2052 `flushDeferredSave()`
- L2063 `save(skipCloud=false)`

### Eventos generales: añadir con un toque, editar, eliminar

- L2092 `setQuantity(id,value,msg='Cantidad actualizada')`
- L2096 `niceStep(v)`
- L2097 `stepQuantity(id,dir)`
- L2151 `renderAppInfo(force=false)`
- L2183 `init()`
- L2219 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L2221 `setNav(v)`
- L2226 `go(v,focus)`
- L2237 constante `THEME_KEY`
- L2238 constante `SUN_SVG`
- L2239 constante `MOON_SVG`
- L2241 `syncThemeUI()`
- L2255 `toggleTheme()`
- L2265 `syncLogoTheme()`
- L2274 `applyMenuBtnState()`
- L2298 `syncDatePill()`
- L2310 `clampBtnPos(el,x,y)`
- L2320 `bindDraggableBtn(el,storeKey)`
- L2381 `bindDrawerGestures()`
- L2419 `animateValue(el,to,suffix='%',digits=0)`
- L2428 `tick(now)`
- L2431 `macroCard(key,name,color)`
- L2432 `renderToday()`
- L2456 `renderBio()`
- L2481 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L2483 constante `HOME`
- L2485 `coachCandidates()`
- L2491 `coachIdeas(t,g,ref,meal)`
- L2510 `coachQuickAdd(key)`
- L2518 `renderCoach()`
- L2540 `coachPrompt()`
- L2549 `nutrientDetailStandard(key)`
- L2564 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L2570 `upgradeTo12(s,o)`
- L2575 `benfotiamineTotals(entries=effectiveEntries()`
- L2584 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L2586 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L2598 `microStat(m,t=totals()`
- L2603 `metric(m,t=totals()`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L2610 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L2611 `ratioInfo(key,t=totals()`
- L2650 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L2667 constante `RATIO_ENDS`
- L2669 `ratioZones(i)` — v68: cada equilibrio tiene una zona «aceptable» (ni verde ni mala) y su meta visible en la tarjeta.
- L2677 `ratioTone(i)`
- L2682 constante `NEAR_HEAD`
- L2683 `ratioBar(i,big=false)`
- L2692 `ratioNeedBase(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L2710 `needHTML(i,t)`
- L2711 `ratioNeed(i,t=totals()`
- L2715 `adBalance(t=totals()`
- L2742 `zncuSuppKey()`
- L2743 `zncuSuppCfg()`
- L2765 `zncuDoseLabel(zn,cu)`
- L2768 `hasZncuSupp(d=day()`
- L2773 `toggleZncuSupp()`
- L2793 `openZncuConfig()`
- L2799 `renderRatios()`
- L2810 `ratioDetail(key)`
- L2827 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L2844 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L2859 `renderMicroMap(t=totals()`
- L2872 `nutrientDetailForDay(key)`
- L2877 `editTargetsForm()`
- L2887 `mealData()`
- L2892 `renderMealSegments()`
- L2900 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L2935 constante `FAT_KEYS`
- L2937 `fatData(entries=effectiveEntries()`
- L2943 `energyData(entries=effectiveEntries()`
- L2947 `segmentedBar(items,total,attr)`
- L2951 `renderMealChart()`
- L2956 `renderFat()`
- L2964 `fatDetail(key)`
- L2969 `energyDetail(key)`
- L2976 `portionCandidates(q='')`
- L2981 `openPortion()`
- L2994 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L3009 `templates()`
- L3013 `renderExtra()`
- L3024 `updateExtra(reset=true)`
- L3036 `addExtra(id,amount)`
- L3052 `shakePreview()`
- L3053 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L3068 constante `LENS`
- L3074 `lensKey(key)`
- L3075 `lensHTML(key)`
- L3079 `appendLens(key)`
- L3088 `weekDates()`

### IA en la página: conexión directa o por servidor

- L3098 constante `MEAL_WORD`
- L3099 `mealOfWord(w)`
- L3100 `mealFromText(raw,fallback)`
- L3104 `canonMeal(v,fallback)`
- L3112 `localMeal(raw,meal)`
- L3118 constante `AI_FALLBACK`
- L3119 constante `GEMINI_DEFAULTS`
- L3120 constante `GROQ_DEFAULTS`
- L3121 `aiTaskProfile(task,hasImg=false)`
- L3129 `geminiThinkLevel(model,want)`
- L3135 `supportsGeminiTemp(model)`
- L3136 `readSSE(res,onEvent)`
- L3155 `applyAIConfig(raw)`
- L3181 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L3182 `callGemini(model,key,prompt,img,signal,opts={})`
- L3228 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), Groq (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L3236 `aiProv(m=$('ai-mode')`
- L3237 `aiBase(mode)`
- L3246 `chatHeaders(mode,key)`
- L3253 `callChat(mode,model,key,prompt,img,signal,opts={})` — ChatGPT, Claude, Groq, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L3307 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L3322 constante `OLD_GEMINI_RE`
- L3323 constante `MODEL_PREF`
- L3324 `pickModel(ids,mode=$('ai-mode')`
- L3338 `ensureModel(st)`
- L3354 `syncProvider()`
- L3373 `requestAI(prompt,img,signal,modelOverride='',onStep=null,opts={})`
- L3410 constante `AI_PREF`
- L3411 `aiConnected()`
- L3412 `syncAI()`
- L3414 `saveAIPrefs()`
- L3415 `loadAIPrefs()`
- L3416 `openAISetup()`
- L3423 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L3430 constante `MACROS`
- L3432 `cleanGoals(o,fallback)`
- L3437 `cleanCompare(o={})`
- L3441 `snapshotDay(d,reference='saved')`
- L3446 `upgradeTo17(s,o)`
- L3451 `entriesFor(d,source=weekSource)`
- L3455 `dayRow(dt,source=weekSource)`
- L3459 `goalsFor(dt)`
- L3465 `metricValue(r,key)`
- L3471 `targetOf(dt,key)`
- L3475 `weekSummary()`
- L3479 `aggregate(key,summary=weekSummary()`
- L3483 `tone(pct,mode='macro')`
- L3490 `pctText(a)`
- L3491 `weekProgress(a,color)`
- L3492 `renderWeekMicros(s)`
- L3504 `ratioAggregate(s,num,den)`
- L3508 `renderWeekRatios(s)`
- L3514 `renderWeekTable(s)`
- L3515 `weeklyDetail(key,oneDate=null)`
- L3524 `weekRatioDetail(key)`
- L3532 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L3538 `openDay(dt)`
- L3576 `withDayGoals(fn)`
- L3581 `renderMicros()`
- L3582 `nutrientDetail(key)`
- L3583 `editTargets()`
- L3584 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L3594 `summaryFor(start)`
- L3598 `ringSVG(pct,color,marker)`
- L3600 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L3604 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L3621 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L3622 `macroTone(p)`
- L3623 `dayMacroPct(dt,k)`
- L3624 `renderWeekly()`
- L3647 `weekDetail(dt,picked)`
- L3655 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L3665 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L3671 `sparkline(pts)`
- L3677 `renderCalendar()`
- L3694 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L3695 `splitMeals(raw)`
- L3705 `localDay(raw,fallback)`
- L3712 `askUnitWeightAI(foodName)`
- L3722 `promptUnitWeight(foodId,count,meal)`
- L3738 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L3798 `parseCsv(text)`
- L3813 `hevyDate(value,format='auto')`
- L3830 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L3845 constante `GYM_APPS`
- L3847 `gymSig(headers)`
- L3848 `gymApp(headers)`
- L3849 `hevyMapping()`
- L3850 `gymSaved()`
- L3851 `renderMapping(parsed)`
- L3868 `optionalNum(v,min=0,max=1e7)`
- L3873 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L3880 `buildHevy(parsed,map)`
- L3914 `cleanWorkout(s)`
- L3921 `formatGymAI(txt)`
- L3932 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L3957 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L3958 constante `GP_ALIAS`
- L3968 `gpNorm(s)`
- L3969 `gpKey(name)`
- L3973 `gpF(n,d=0)`
- L3974 `gpDate(d,opt)`
- L3975 `gpMonday(d)`
- L3976 constante `GP_GROUPS`
- L3991 constante `GP_COLORS`
- L3992 `gpGroup(name)`
- L3993 `gpWorkSets(s)`
- L3995 `gpModel()`
- L4023 `gpSessionMetrics(e,sets)`
- L4038 constante `GP_METRICS`
- L4043 `gpMetricsFor(e)`
- L4044 `gpRangeHist(e)`
- L4045 `gpPRs(model)`
- L4068 `gpStatus(e)`
- L4086 `gpNext(e)`
- L4094 `gpChart(e)`
- L4122 `gpPointDetail(e)`
- L4128 `gpRepTable(e)`
- L4135 `gpKpis(model)`
- L4144 `gpWeekData(model,w)` — Datos de una semana de gimnasio (series por músculo y sesiones).
- L4149 `gpWeekLabel(w,short)`
- L4150 `gpWeekly(model)`
- L4169 `gpMuscles(model)`
- L4177 `gpHeat(model)` — v69: «Constancia» — mapa de días entrenados (como antes), con días de la semana, meses, intensidad y detalle al tocar.
- L4197 `gpExList(model)`
- L4204 `gpExDetail(model)`
- L4217 `gpDayFood(dt)`
- L4218 `gpNutrition(model)`
- L4225 `gpRecentPRs(model)`
- L4229 `gpSessions(model)`
- L4235 `gpSessionModal(id)`
- L4246 `gpWeekModal(w)`
- L4253 `gpSelect(key)`
- L4254 `gpClick(e)`
- L4271 `renderGym()`
- L4295 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L4304 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L4310 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L4335 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L4339 `showHelp()`
- L4343 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L4345 `markBackup()`
- L4349 `exportJSON()`
- L4354 `drawBackupReminder()`
- L4366 `applyDensity()`
- L4378 `syncDayComplete()`
- L4381 `drawMeals()` — Comidas del día de un vistazo.
- L4389 `filterLog()` — Buscador de Registro.
- L4402 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L4408 `recentFoods()`
- L4413 `quickChip(e,fav)`
- L4431 `drawQuickFoods()`
- L4460 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L4464 `toggleAddPanel(id)`
- L4477 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L4488 `pasteMessage(text,ok)`
- L4496 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L4507 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L4518 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L4524 `upgradeTo27(s,o)`
- L4541 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L4563 `storableState()`

### Render único: actualiza toda la página

- L4572 `nearView(el)`
- L4574 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L4579 `scheduleLazyRender()`
- L4583 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L4620 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L4621 constante `REF_TABLE`
- L4628 `refTargets(mode)`
- L4629 `syncMicroMode()`
- L4642 `mealByHour(h=new Date()`
- L4649 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L4660 `dataSummary(s)`
- L4664 `confirmImport(next,name)`
- L4671 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L4677 `checkUpdate()`
- L4682 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L4698 constante `GAP_PREFER`
- L4699 constante `GAP_SKIP`
- L4700 constante `GAP_UNIT`
- L4701 `gapQty(f,x)`
- L4702 `gapFoods(key,gap,ctx)`
- L4721 `weekSources(key,sum)`
- L4727 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L4740 `gapRow(x,open,meal,sum,ctx)`
- L4756 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L4781 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L4782 `isFemale(s=state)`
- L4783 `sexLabel(s=state)`
- L4784 `sexBadge(sex)`
- L4786 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L4787 constante `OPT_FEMALE`
- L4798 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba; A (1.500 µg = 5.000 UI) y D (50 µg = 2.000 UI) mantienen A:D en zona verde (2,5:1).
- L4799 `applySexOpt(sex)`
- L4801 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L4806 `cleanPreset(p,fb)`
- L4810 `dayNamesFor(types)`
- L4812 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L4822 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L4830 `profV()`
- L4831 `isTrainDay(i)`
- L4832 `activityName(i)`
- L4833 `dayFaf(i)`
- L4834 `presetDesc(cfg,shake)`
- L4838 `profileDescription()`
- L4846 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L4848 `wizCatalog()`
- L4849 `wizOpen(opts={})`
- L4865 `wizTitle()`
- L4866 `wizPaint(sameStep=true)`
- L4875 `wizSync()`
- L4894 `wizFoodOptions()`
- L4897 `wizPresetSummary(cfg,whey)`
- L4902 `wizPresetHTML(kind)`
- L4910 `wizPreview()`
- L4921 `wizLiveHTML()`
- L4925 `wizHTML()`
- L4972 `isStandalonePWA()`
- L4973 `isInAppWebview()`
- L4974 `isBraveBrowser()`
- L4975 `syncInstallButtons()`
- L4981 `buildTransferUrl()`
- L4996 `triggerPWAInstall()`
- L5031 `wizCommit()`
- L5082 `showPostWizInstallBanner(name)`

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L5144 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L5145 constante `SUPP_CATALOG`
- L5170 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L5171 constante `PEAT_BREAKFAST`
- L5172 constante `PEAT_SHAKE`
- L5174 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L5181 `benfoUser()`
- L5183 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L5199 `ico(n)`
- L5201 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L5210 `showTour(i=0)`
- L5222 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L5223 `hubAction(v)`
- L5231 constante `FB_CATS` — Envíos anónimos directos al buzón de BioPeat (sin cuentas ni datos personales).
- L5233 `openFeedback()`
- L5237 `feedbackData()`
- L5244 `feedbackText()`
- L5245 `sendFeedback()`
- L5265 `shareFeedback()`
- L5282 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L5289 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L5297 constante `I18N_EN`

### v59: idioma (español / inglés)

- L5302 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L5303 constante `WD_EN`
- L5304 `trOne(s)`
- L5312 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L5313 constante `ES_FOOD_GYM`
- L5350 `trFood(s)`
- L5362 constante `TR_TPL`
- L5403 `trLower(s)`
- L5404 `trTpl(s,attr)`
- L5405 constante `FOOD_SEL`
- L5406 `trText(s,attr=false)`
- L5416 `trNode(n)`
- L5435 `trEl(el)`
- L5448 `trTree(root)`
- L5457 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L5471 `flushTr()`
- L5472 `syncTrObserver()`
- L5477 `loadEnDict()`
- L5489 `setLang(l,quiet)`
- L5504 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter + Worker agregados), solo en la web publicada

- L5513 constante `GC_CODE`
- L5514 `pingAnalytics(extra={})`
- L5530 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L5542 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L5543 `packMove()`
- L5551 `unpackMove(code)`
- L5562 `moveData()`
- L5572 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L5578 `checkMove(code)`
- L5597 `aiFrameworkLines()` — v69: marco de referencia del informe para IA. Así cualquier IA, aunque no conozca la app ni al usuario, sabe con qué comparar.

### Arranque

