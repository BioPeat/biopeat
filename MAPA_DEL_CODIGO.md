# MAPA DEL CÓDIGO · BioPeat v81 (revisión de datos 27)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

Arquitectura modular: `index.html` (65 KB), `assets/styles.css`, `assets/data.js`, `assets/app.js` (511 KB) y `assets/i18n-en.js`.

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

- L70 constante `REF_MAP` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L71 constante `REF_CACHE`
- L73 `ensureRefIndex()`
- L80 `refNutrients(id)`
- L88 constante `STRIP_PREP_RE`
- L89 `findRef(text,strict=false)`
- L112 `refCatalogCompact()`
- L113 `fromRef(id,amount,meal,note='',srcText='')`
- L118 `optInfo(k,goal)`
- L125 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L133 `optLine(k,goal,unit)`
- L140 `optRefHTML(k,goal,unit)`
- L141 constante `FAF`
- L143 constante `LOC`
- L147 `number(v,min=0,max=1e6)`
- L153 `decimalInputs(root=document)`
- L154 `localDate(d=new Date()`
- L155 `validDate(s)`
- L160 `shift(s,n)`
- L168 `stripProto(o)`
- L175 `cleanBio(b)`
- L184 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L186 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L192 constante `DAY_TYPES`
- L193 constante `NEW_V54`
- L197 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L200 `bmr(w=state.profile.weight)` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L206 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L231 `cleanNutrients(o,required=false)`
- L243 `cleanEntry(e)`
- L248 `cleanPlan(p)`
- L252 `planEntry(p)`
- L261 `seedPlan(d,whichDate)`
- L265 `ensureDay(d=date)`
- L272 `effectiveEntries(d=day()`
- L273 constante `SALTED_IDS`
- L274 constante `SWEET_RE`
- L275 `inferFatShares(e,txt=normalize((e?.name||'')`
- L293 `inferredNutrients(e)`
- L335 `totals(entries)`
- L347 `change(fn,message='Guardado')`
- L351 `undo()`
- L359 `toast(text,canUndo=false)`
- L367 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L368 `onClick(fn)`
- L370 `attempt(fn)`
- L374 `modal(title,body)`
- L383 `modalRestore()`
- L393 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L394 `modalBack()`
- L395 `goDate(d)`
- L402 `renderHeader()`
- L415 `renderRows(entries)`
- L419 `entryValues(e)`
- L420 `renderLog()`
- L427 `fromFood(id,amount,meal)`
- L433 `pantryId(name)`
- L435 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L454 `addEntries(entries,message='Añadido',d=date,opts={})`
- L463 `recipe(kind)`
- L470 `summary(entries)`
- L474 `renderPresetInfo()`
- L487 `stripCode(raw)`
- L493 `sanitizeNutrients(o,grams=100,fallbackRefId='')`
- L520 `parseBIO(raw,meal=$('meal-select')`
- L532 `parseSmart(raw)`
- L536 constante `COUNT`
- L537 constante `UNIT_RE`
- L601 `offToNutrients(nut={},fallbackName='')` — Open Food Facts (gratis, sin clave, CORS nativo): consulta por código de barras o texto.
- L622 `lookupOFFBarcode(code,signal,ms=3200)`
- L638 `searchOFF(query,signal,ms=4500)`
- L657 `openProductSearch()`
- L696 `nutrientFields(n,prefix='n_')`
- L697 `readNutrients(form,prefix='n_')`
- L702 `editEntry(id)`
- L711 `editFood(id,pending=null)`
- L716 `usageStats(days=90)`
- L724 `renderFoods(forceList=false)`
- L736 `nutrientSources(key)`
- L743 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L744 `suppSlot(meal)`
- L745 `renderSupps()`
- L760 `editPlan(id)`
- L767 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L788 `makePrompt(meal='Comida',note='')`
- L793 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L797 `pantryCompact()`
- L801 constante `MEAL_AI_SCHEMA`
- L842 `mealSystemPrompt(usePhoto)`
- L858 `hydrateAIItems(rawItems,fallback,usePhoto,aiModel,signal)`
- L907 `photoPrompt(meal,note)`
- L910 `resetPhoto()`
- L921 `openPhoto()`
- L927 `shrinkPhoto(file)`
- L930 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L956 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L963 `cleanFood(id,f)`
- L970 `migrateBase(o)`
- L990 `download(name,text,type)`
- L999 `portable()`
- L1053 `syncAppIcons()`
- L1061 `downloadAppIcons()`
- L1098 constante `PROFILES_KEY`
- L1100 `ensureProfilesStore()`
- L1120 `resetProfileSessionUI()`
- L1127 `saveProfilesStore(st)`
- L1136 `syncCurrentProfileToStore(snapObj=null,immediate=true)`
- L1147 `activeProfileName()`
- L1151 `renderProfilesList()`
- L1193 `switchProfile(id)`
- L1215 `deleteProfileById(id)`
- L1240 `refreshDrawerSummary()`
- L1257 `toggleLeftDrawer(force)`
- L1272 `buildAIExportText(rangeOverride)`
- L1527 `copyAIExport()`
- L1541 `downloadAIExport()`
- L1550 `renderDrawerChat()`
- L1569 `buildDrawerChatContext()`
- L1608 `buildDrawerChatPrompt(question)`
- L1620 `askDrawerAI(rawQuestion)`
- L1709 constante `CLOUD_OFF_KEY`
- L1720 `bytesToB64(u8)`
- L1721 `b64ToBytes(s)`
- L1722 `bytesToB64Url(u8)`
- L1723 `sha256Hex(str)`
- L1724 `sha256Bytes(str)`
- L1725 `generateSyncKey()`
- L1726 `ensureSyncKey()`
- L1727 `mirrorSyncKey(k)`
- L1728 `deriveSyncCreds(keyStr)`
- L1734 `hasMeaningfulData()`
- L1741 `buildCloudBundle()`
- L1748 `encryptVaultPayload(obj,keyStr)`
- L1756 `readDecompressedText(bytes,maxBytes=10*1024*1024)`
- L1772 `decryptVaultPayload(resp,keyStr)`
- L1784 `bundleHash(bundle)`
- L1788 `applyCloudBundle(o,rev=1)`
- L1798 `cloudPull(keyStr,opts={})`
- L1818 `cloudPush(opts={})`
- L1855 `scheduleCloudPush()`
- L1861 `scheduleAutoCloudPull(delayMs=120)`
- L1875 `saveSyncToPassMgr()`
- L1882 `trySilentPassMgrRecovery()`
- L1892 `extractSyncKeyInput(val)`
- L1898 `applySyncKey(rawKey,opts={})`
- L1919 `takeSyncCode()`
- L1930 `renderCloudStatus()`
- L1953 `buildMagicSyncUrl()`
- L1960 `openMagicSyncModal()`
- L1969 `shareMagicSyncLink()`
- L1976 `copyMagicSyncLink()`
- L1981 `openCloudLinkModal()`
- L1984 `deleteCloudBackup(confirmed=false)`
- L2021 `mirrorToIDB(raw,profRaw)`
- L2024 `storageStatus()`
- L2031 `idbReadWrite(mode,value,key='current')`
- L2032 `openDB()`
- L2034 `flushDeferredSave()`
- L2044 `save(skipCloud=false)`

### Eventos generales: añadir con un toque, editar, eliminar

- L2072 `setQuantity(id,value,msg='Cantidad actualizada')`
- L2076 `niceStep(v)`
- L2077 `stepQuantity(id,dir)`
- L2131 `renderAppInfo(force=false)`
- L2163 `init()`
- L2199 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L2201 `setNav(v)`
- L2206 `go(v,focus)`
- L2217 constante `THEME_KEY`
- L2218 constante `SUN_SVG`
- L2219 constante `MOON_SVG`
- L2221 `syncThemeUI()`
- L2233 `toggleTheme()`
- L2243 `syncLogoTheme()`
- L2252 `applyMenuBtnState()`
- L2259 `syncDatePill()`
- L2271 `clampBtnPos(el,x,y)`
- L2281 `bindDraggableBtn(el,storeKey)`
- L2366 `bindDrawerGestures()`
- L2404 `animateValue(el,to,suffix='%',digits=0)`
- L2413 `tick(now)`
- L2416 `macroCard(key,name,color)`
- L2417 `renderToday()`
- L2441 `renderBio()`
- L2466 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L2468 constante `HOME`
- L2470 `coachCandidates()`
- L2476 `coachIdeas(t,g,ref,meal)`
- L2495 `coachQuickAdd(key)`
- L2503 `renderCoach()`
- L2525 `coachPrompt()`
- L2534 `nutrientDetailStandard(key)`
- L2549 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L2555 `upgradeTo12(s,o)`
- L2560 `benfotiamineTotals(entries=effectiveEntries()`
- L2569 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L2571 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L2583 `microStat(m,t=totals()`
- L2588 `metric(m,t=totals()`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L2595 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L2596 `ratioInfo(key,t=totals()`
- L2635 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L2652 constante `RATIO_ENDS`
- L2654 `ratioZones(i)` — v68: cada equilibrio tiene una zona «aceptable» (ni verde ni mala) y su meta visible en la tarjeta.
- L2662 `ratioTone(i)`
- L2667 constante `NEAR_HEAD`
- L2668 `ratioBar(i,big=false)`
- L2677 `ratioNeedBase(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L2695 `needHTML(i,t)`
- L2696 `ratioNeed(i,t=totals()`
- L2700 `adBalance(t=totals()`
- L2727 `zncuSuppKey()`
- L2728 `zncuSuppCfg()`
- L2750 `zncuDoseLabel(zn,cu)`
- L2753 `hasZncuSupp(d=day()`
- L2758 `toggleZncuSupp()`
- L2778 `openZncuConfig()`
- L2784 `renderRatios()`
- L2795 `ratioDetail(key)`
- L2812 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L2829 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L2844 `renderMicroMap(t=totals()`
- L2857 `nutrientDetailForDay(key)`
- L2862 `editTargetsForm()`
- L2872 `mealData()`
- L2877 `renderMealSegments()`
- L2885 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L2920 constante `FAT_KEYS`
- L2922 `fatData(entries=effectiveEntries()`
- L2928 `energyData(entries=effectiveEntries()`
- L2932 `segmentedBar(items,total,attr)`
- L2936 `renderMealChart()`
- L2941 `renderFat()`
- L2949 `fatDetail(key)`
- L2954 `energyDetail(key)`
- L2961 `portionCandidates(q='')`
- L2966 `openPortion()`
- L2979 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L2994 `templates()`
- L2998 `renderExtra()`
- L3009 `updateExtra(reset=true)`
- L3021 `addExtra(id,amount)`
- L3037 `shakePreview()`
- L3038 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L3053 constante `LENS`
- L3059 `lensKey(key)`
- L3060 `lensHTML(key)`
- L3064 `appendLens(key)`
- L3073 `weekDates()`

### IA en la página: conexión directa o por servidor

- L3083 constante `MEAL_WORD`
- L3084 `mealOfWord(w)`
- L3085 `mealFromText(raw,fallback)`
- L3089 `canonMeal(v,fallback)`
- L3097 `localMeal(raw,meal)`
- L3103 constante `AI_FALLBACK`
- L3104 constante `GEMINI_DEFAULTS`
- L3105 constante `GROQ_DEFAULTS`
- L3106 `aiTaskProfile(task,hasImg=false)`
- L3114 `geminiThinkLevel(model,want)`
- L3120 `supportsGeminiTemp(model)`
- L3121 `readSSE(res,onEvent)`
- L3140 `applyAIConfig(raw)`
- L3166 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L3167 `callGemini(model,key,prompt,img,signal,opts={})`
- L3213 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), Groq (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L3221 `aiProv(m=$('ai-mode')`
- L3222 `aiBase(mode)`
- L3231 `chatHeaders(mode,key)`
- L3238 `callChat(mode,model,key,prompt,img,signal,opts={})` — ChatGPT, Claude, Groq, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L3292 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L3307 constante `OLD_GEMINI_RE`
- L3308 constante `MODEL_PREF`
- L3309 `pickModel(ids,mode=$('ai-mode')`
- L3323 `ensureModel(st)`
- L3339 `syncProvider()`
- L3358 `requestAI(prompt,img,signal,modelOverride='',onStep=null,opts={})`
- L3395 constante `AI_PREF`
- L3396 `aiConnected()`
- L3397 `syncAI()`
- L3399 `saveAIPrefs()`
- L3400 `loadAIPrefs()`
- L3401 `openAISetup()`
- L3408 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L3415 constante `MACROS`
- L3417 `cleanGoals(o,fallback)`
- L3422 `cleanCompare(o={})`
- L3426 `snapshotDay(d,reference='saved')`
- L3431 `upgradeTo17(s,o)`
- L3436 `entriesFor(d,source=weekSource)`
- L3440 `dayRow(dt,source=weekSource)`
- L3444 `goalsFor(dt)`
- L3450 `metricValue(r,key)`
- L3456 `targetOf(dt,key)`
- L3460 `weekSummary()`
- L3464 `aggregate(key,summary=weekSummary()`
- L3468 `tone(pct,mode='macro')`
- L3475 `pctText(a)`
- L3476 `weekProgress(a,color)`
- L3477 `renderWeekMicros(s)`
- L3489 `ratioAggregate(s,num,den)`
- L3493 `renderWeekRatios(s)`
- L3499 `renderWeekTable(s)`
- L3500 `weeklyDetail(key,oneDate=null)`
- L3509 `weekRatioDetail(key)`
- L3517 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L3523 `openDay(dt)`
- L3561 `withDayGoals(fn)`
- L3566 `renderMicros()`
- L3567 `nutrientDetail(key)`
- L3568 `editTargets()`
- L3569 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L3579 `summaryFor(start)`
- L3583 `ringSVG(pct,color,marker)`
- L3585 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L3589 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L3606 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L3607 `macroTone(p)`
- L3608 `dayMacroPct(dt,k)`
- L3609 `renderWeekly()`
- L3632 `weekDetail(dt,picked)`
- L3640 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L3650 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L3656 `sparkline(pts)`
- L3662 `renderCalendar()`
- L3679 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L3680 `splitMeals(raw)`
- L3690 `localDay(raw,fallback)`
- L3697 `promptDay(raw,fallback)`
- L3698 `askUnitWeightAI(foodName)`
- L3708 `promptUnitWeight(foodId,count,meal)`
- L3724 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L3784 `parseCsv(text)`
- L3799 `hevyDate(value,format='auto')`
- L3816 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L3831 constante `GYM_APPS`
- L3833 `gymSig(headers)`
- L3834 `gymApp(headers)`
- L3835 `hevyMapping()`
- L3836 `gymSaved()`
- L3837 `renderMapping(parsed)`
- L3854 `optionalNum(v,min=0,max=1e7)`
- L3859 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L3866 `buildHevy(parsed,map)`
- L3900 `cleanWorkout(s)`
- L3907 `formatGymAI(txt)`
- L3918 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L3943 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L3944 constante `GP_ALIAS`
- L3954 `gpNorm(s)`
- L3955 `gpKey(name)`
- L3959 `gpF(n,d=0)`
- L3960 `gpDate(d,opt)`
- L3961 `gpMonday(d)`
- L3962 constante `GP_GROUPS`
- L3977 constante `GP_COLORS`
- L3978 `gpGroup(name)`
- L3979 `gpWorkSets(s)`
- L3980 `gpModel()`
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
- L4251 `renderGym()`
- L4271 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L4280 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L4286 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L4311 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L4315 `showHelp()`
- L4319 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L4321 `markBackup()`
- L4325 `exportJSON()`
- L4330 `drawBackupReminder()`
- L4340 `applyDensity()`
- L4352 `syncDayComplete()`
- L4355 `drawMeals()` — Comidas del día de un vistazo.
- L4363 `filterLog()` — Buscador de Registro.
- L4376 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L4382 `recentFoods()`
- L4387 `quickChip(e,fav)`
- L4405 `drawQuickFoods()`
- L4434 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L4438 `toggleAddPanel(id)`
- L4451 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L4462 `pasteMessage(text,ok)`
- L4470 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L4481 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L4492 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L4498 `upgradeTo27(s,o)`
- L4515 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L4537 `storableState()`

### Render único: actualiza toda la página

- L4546 `nearView(el)`
- L4548 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L4553 `scheduleLazyRender()`
- L4557 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L4594 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L4595 constante `REF_TABLE`
- L4602 `refTargets(mode)`
- L4603 `syncMicroMode()`
- L4616 `mealByHour(h=new Date()`
- L4623 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L4634 `dataSummary(s)`
- L4638 `confirmImport(next,name)`
- L4645 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L4651 `checkUpdate()`
- L4656 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L4671 constante `GAP_PREFER`
- L4672 constante `GAP_SKIP`
- L4673 constante `GAP_UNIT`
- L4674 `gapQty(f,x)`
- L4675 `gapFoods(key,gap,ctx)`
- L4694 `weekSources(key,sum)`
- L4700 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L4713 `gapRow(x,open,meal,sum,ctx)`
- L4729 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L4754 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L4755 `isFemale(s=state)`
- L4756 `sexLabel(s=state)`
- L4757 `sexBadge(sex)`
- L4759 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L4760 constante `OPT_FEMALE`
- L4771 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba; A (1.500 µg = 5.000 UI) y D (50 µg = 2.000 UI) mantienen A:D en zona verde (2,5:1).
- L4772 `applySexOpt(sex)`
- L4774 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L4779 `cleanPreset(p,fb)`
- L4783 `dayNamesFor(types)`
- L4785 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L4795 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L4803 `profV()`
- L4804 `isTrainDay(i)`
- L4805 `activityName(i)`
- L4806 `dayFaf(i)`
- L4807 `presetDesc(cfg,shake)`
- L4811 `profileDescription()`
- L4819 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L4821 `wizCatalog()`
- L4822 `wizOpen(opts={})`
- L4838 `wizTitle()`
- L4839 `wizPaint(sameStep=true)`
- L4848 `wizSync()`
- L4867 `wizFoodOptions()`
- L4870 `wizPresetSummary(cfg,whey)`
- L4875 `wizPresetHTML(kind)`
- L4883 `wizPreview()`
- L4894 `wizLiveHTML()`
- L4898 `wizHTML()`
- L4945 `isStandalonePWA()`
- L4946 `isInAppWebview()`
- L4947 `isBraveBrowser()`
- L4948 `syncInstallButtons()`
- L4954 `buildTransferUrl()`
- L4969 `triggerPWAInstall()`
- L5004 `wizCommit()`
- L5055 `showPostWizInstallBanner(name)`

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L5117 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L5118 constante `SUPP_CATALOG`
- L5143 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L5144 constante `PEAT_BREAKFAST`
- L5145 constante `PEAT_SHAKE`
- L5147 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L5154 `benfoUser()`
- L5156 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L5172 `ico(n)`
- L5174 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L5183 `showTour(i=0)`
- L5195 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L5196 `hubAction(v)`
- L5204 constante `FB_CATS` — Envíos anónimos directos al buzón de BioPeat (sin cuentas ni datos personales).
- L5206 `openFeedback()`
- L5210 `feedbackData()`
- L5217 `feedbackText()`
- L5218 `sendFeedback()`
- L5238 `shareFeedback()`
- L5255 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L5262 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L5270 constante `I18N_EN`

### v59: idioma (español / inglés)

- L5275 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L5276 constante `WD_EN`
- L5277 `trOne(s)`
- L5285 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L5286 constante `ES_FOOD_GYM`
- L5323 `trFood(s)`
- L5335 constante `TR_TPL`
- L5376 `trLower(s)`
- L5377 `trTpl(s,attr)`
- L5378 constante `FOOD_SEL`
- L5379 `trText(s,attr=false)`
- L5389 `trNode(n)`
- L5408 `trEl(el)`
- L5421 `trTree(root)`
- L5430 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L5444 `flushTr()`
- L5445 `syncTrObserver()`
- L5450 `loadEnDict()`
- L5462 `setLang(l,quiet)`
- L5477 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter + Worker agregados), solo en la web publicada

- L5486 constante `GC_CODE`
- L5487 `pingAnalytics(extra={})`
- L5503 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L5515 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L5516 `packMove()`
- L5524 `unpackMove(code)`
- L5535 `moveData()`
- L5545 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L5551 `checkMove(code)`
- L5570 `aiFrameworkLines()` — v69: marco de referencia del informe para IA. Así cualquier IA, aunque no conozca la app ni al usuario, sabe con qué comparar.

### Arranque

