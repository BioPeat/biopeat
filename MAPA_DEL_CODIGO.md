# MAPA DEL CÓDIGO · BioPeat v82 (revisión de datos 27)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

Arquitectura modular: `index.html` (66 KB), `assets/styles.css`, `assets/data.js`, `assets/app.js` (507 KB) y `assets/i18n-en.js`.

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

- L71 constante `REF_MAP` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L72 constante `REF_CACHE`
- L74 `ensureRefIndex()`
- L81 `refNutrients(id)`
- L89 constante `STRIP_PREP_RE`
- L90 `findRef(text,strict=false)`
- L113 `refCatalogCompact()`
- L114 `fromRef(id,amount,meal,note='',srcText='')`
- L119 `optInfo(k,goal)`
- L126 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L134 `optLine(k,goal,unit)`
- L141 `optRefHTML(k,goal,unit)`
- L142 constante `FAF`
- L144 constante `LOC`
- L148 `number(v,min=0,max=1e6)`
- L154 `decimalInputs(root=document)`
- L155 `localDate(d=new Date()`
- L156 `validDate(s)`
- L161 `shift(s,n)`
- L169 `stripProto(o)`
- L176 `cleanBio(b)`
- L185 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L187 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L193 constante `DAY_TYPES`
- L194 constante `NEW_V54`
- L198 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L201 `bmr(w=state.profile.weight)` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L207 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L232 `cleanNutrients(o,required=false)`
- L244 `cleanEntry(e)`
- L249 `cleanPlan(p)`
- L253 `planEntry(p)`
- L262 `seedPlan(d,whichDate)`
- L266 `ensureDay(d=date)`
- L273 `effectiveEntries(d=day()`
- L274 constante `SALTED_IDS`
- L275 constante `SWEET_RE`
- L276 `inferFatShares(e,txt=normalize((e?.name||'')`
- L294 `inferredNutrients(e)`
- L336 `totals(entries)`
- L348 `change(fn,message='Guardado')`
- L352 `undo()`
- L360 `toast(text,canUndo=false)`
- L368 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L369 `onClick(fn)`
- L371 `attempt(fn)`
- L375 `modal(title,body)`
- L384 `modalRestore()`
- L394 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L395 `modalBack()`
- L396 `goDate(d)`
- L403 `renderHeader()`
- L416 `renderRows(entries)`
- L420 `entryValues(e)`
- L421 `renderLog()`
- L428 `fromFood(id,amount,meal)`
- L434 `pantryId(name)`
- L436 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L455 `addEntries(entries,message='Añadido',d=date,opts={})`
- L464 `recipe(kind)`
- L471 `summary(entries)`
- L475 `renderPresetInfo()`
- L488 `stripCode(raw)`
- L494 `sanitizeNutrients(o,grams=100,fallbackRefId='')`
- L521 `parseBIO(raw,meal=$('meal-select')`
- L533 `parseSmart(raw)`
- L537 constante `COUNT`
- L538 constante `UNIT_RE`
- L602 `offToNutrients(nut={},fallbackName='')` — Open Food Facts (gratis, sin clave, CORS nativo): consulta por código de barras o texto.
- L623 `lookupOFFBarcode(code,signal,ms=3200)`
- L639 `searchOFF(query,signal,ms=4500)`
- L658 `openProductSearch()`
- L697 `nutrientFields(n,prefix='n_')`
- L698 `readNutrients(form,prefix='n_')`
- L703 `editEntry(id)`
- L712 `editFood(id,pending=null)`
- L717 `usageStats(days=90)`
- L725 `renderFoods(forceList=false)`
- L737 `nutrientSources(key)`
- L744 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L745 `suppSlot(meal)`
- L746 `renderSupps()`
- L761 `editPlan(id)`
- L768 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L789 `makePrompt(meal='Comida',note='')`
- L794 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L798 `pantryCompact()`
- L802 constante `MEAL_AI_SCHEMA`
- L843 `mealSystemPrompt(usePhoto)`
- L859 `hydrateAIItems(rawItems,fallback,usePhoto,aiModel,signal)`
- L908 `photoPrompt(meal,note)`
- L911 `resetPhoto()`
- L922 `openPhoto()`
- L928 `shrinkPhoto(file)`
- L931 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L957 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L964 `cleanFood(id,f)`
- L971 `migrateBase(o)`
- L991 `download(name,text,type)`
- L1000 `portable()`
- L1054 `syncAppIcons()`
- L1062 `downloadAppIcons()`
- L1099 constante `PROFILES_KEY`
- L1101 `ensureProfilesStore()`
- L1121 `resetProfileSessionUI()`
- L1128 `saveProfilesStore(st)`
- L1137 `syncCurrentProfileToStore(snapObj=null,immediate=true)`
- L1148 `activeProfileName()`
- L1152 `renderProfilesList()`
- L1194 `switchProfile(id)`
- L1216 `deleteProfileById(id)`
- L1241 `refreshDrawerSummary()`
- L1258 `toggleLeftDrawer(force)`
- L1273 `buildAIExportText(rangeOverride)`
- L1528 `copyAIExport()`
- L1542 `downloadAIExport()`
- L1551 `renderDrawerChat()`
- L1570 `buildDrawerChatContext()`
- L1609 `buildDrawerChatPrompt(question)`
- L1621 `askDrawerAI(rawQuestion)`
- L1710 constante `CLOUD_OFF_KEY`
- L1721 `bytesToB64(u8)`
- L1722 `b64ToBytes(s)`
- L1723 `bytesToB64Url(u8)`
- L1724 `sha256Hex(str)`
- L1725 `sha256Bytes(str)`
- L1726 `generateSyncKey()`
- L1727 `ensureSyncKey()`
- L1728 `mirrorSyncKey(k)`
- L1729 `deriveSyncCreds(keyStr)`
- L1735 `hasMeaningfulData()`
- L1742 `buildCloudBundle()`
- L1749 `encryptVaultPayload(obj,keyStr)`
- L1757 `readDecompressedText(bytes,maxBytes=10*1024*1024)`
- L1773 `decryptVaultPayload(resp,keyStr)`
- L1785 `bundleHash(bundle)`
- L1789 `applyCloudBundle(o,rev=1)`
- L1799 `cloudPull(keyStr,opts={})`
- L1819 `cloudPush(opts={})`
- L1856 `scheduleCloudPush()`
- L1862 `scheduleAutoCloudPull(delayMs=120)`
- L1876 `saveSyncToPassMgr()`
- L1883 `trySilentPassMgrRecovery()`
- L1893 `extractSyncKeyInput(val)`
- L1899 `applySyncKey(rawKey,opts={})`
- L1920 `takeSyncCode()`
- L1931 `renderCloudStatus()`
- L1954 `buildMagicSyncUrl()`
- L1961 `openMagicSyncModal()`
- L1970 `shareMagicSyncLink()`
- L1977 `copyMagicSyncLink()`
- L1982 `openCloudLinkModal()`
- L1985 `deleteCloudBackup(confirmed=false)`
- L2022 `mirrorToIDB(raw,profRaw)`
- L2025 `storageStatus()`
- L2032 `idbReadWrite(mode,value,key='current')`
- L2033 `openDB()`
- L2035 `flushDeferredSave()`
- L2045 `save(skipCloud=false)`

### Eventos generales: añadir con un toque, editar, eliminar

- L2073 `setQuantity(id,value,msg='Cantidad actualizada')`
- L2077 `niceStep(v)`
- L2078 `stepQuantity(id,dir)`
- L2132 `renderAppInfo(force=false)`
- L2164 `init()`
- L2200 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L2202 `setNav(v)`
- L2207 `go(v,focus)`
- L2218 constante `THEME_KEY`
- L2219 constante `SUN_SVG`
- L2220 constante `MOON_SVG`
- L2222 `syncThemeUI()`
- L2235 `toggleTheme()`
- L2245 `syncLogoTheme()`
- L2254 `applyMenuBtnState()`
- L2261 `syncDatePill()`
- L2273 `bindDrawerGestures()`
- L2299 `animateValue(el,to,suffix='%',digits=0)`
- L2308 `tick(now)`
- L2311 `macroCard(key,name,color)`
- L2312 `renderToday()`
- L2336 `renderBio()`
- L2361 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L2363 constante `HOME`
- L2365 `coachCandidates()`
- L2371 `coachIdeas(t,g,ref,meal)`
- L2390 `coachQuickAdd(key)`
- L2398 `renderCoach()`
- L2420 `coachPrompt()`
- L2429 `nutrientDetailStandard(key)`
- L2444 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L2450 `upgradeTo12(s,o)`
- L2455 `benfotiamineTotals(entries=effectiveEntries()`
- L2464 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L2466 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L2478 `microStat(m,t=totals()`
- L2483 `metric(m,t=totals()`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L2490 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L2491 `ratioInfo(key,t=totals()`
- L2530 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L2547 constante `RATIO_ENDS`
- L2549 `ratioZones(i)` — v68: cada equilibrio tiene una zona «aceptable» (ni verde ni mala) y su meta visible en la tarjeta.
- L2557 `ratioTone(i)`
- L2562 constante `NEAR_HEAD`
- L2563 `ratioBar(i,big=false)`
- L2572 `ratioNeedBase(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L2590 `needHTML(i,t)`
- L2591 `ratioNeed(i,t=totals()`
- L2595 `adBalance(t=totals()`
- L2622 `zncuSuppKey()`
- L2623 `zncuSuppCfg()`
- L2645 `zncuDoseLabel(zn,cu)`
- L2648 `hasZncuSupp(d=day()`
- L2653 `toggleZncuSupp()`
- L2673 `openZncuConfig()`
- L2679 `renderRatios()`
- L2690 `ratioDetail(key)`
- L2707 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L2724 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L2739 `renderMicroMap(t=totals()`
- L2752 `nutrientDetailForDay(key)`
- L2757 `editTargetsForm()`
- L2767 `mealData()`
- L2772 `renderMealSegments()`
- L2780 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L2815 constante `FAT_KEYS`
- L2817 `fatData(entries=effectiveEntries()`
- L2823 `energyData(entries=effectiveEntries()`
- L2827 `segmentedBar(items,total,attr)`
- L2831 `renderMealChart()`
- L2836 `renderFat()`
- L2844 `fatDetail(key)`
- L2849 `energyDetail(key)`
- L2856 `portionCandidates(q='')`
- L2861 `openPortion()`
- L2874 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L2889 `templates()`
- L2893 `renderExtra()`
- L2904 `updateExtra(reset=true)`
- L2916 `addExtra(id,amount)`
- L2932 `shakePreview()`
- L2933 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L2948 constante `LENS`
- L2954 `lensKey(key)`
- L2955 `lensHTML(key)`
- L2959 `appendLens(key)`
- L2968 `weekDates()`

### IA en la página: conexión directa o por servidor

- L2978 constante `MEAL_WORD`
- L2979 `mealOfWord(w)`
- L2980 `mealFromText(raw,fallback)`
- L2984 `canonMeal(v,fallback)`
- L2992 `localMeal(raw,meal)`
- L2998 constante `AI_FALLBACK`
- L2999 constante `GEMINI_DEFAULTS`
- L3000 constante `GROQ_DEFAULTS`
- L3001 `aiTaskProfile(task,hasImg=false)`
- L3009 `geminiThinkLevel(model,want)`
- L3015 `supportsGeminiTemp(model)`
- L3016 `readSSE(res,onEvent)`
- L3035 `applyAIConfig(raw)`
- L3061 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L3062 `callGemini(model,key,prompt,img,signal,opts={})`
- L3108 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), Groq (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L3116 `aiProv(m=$('ai-mode')`
- L3117 `aiBase(mode)`
- L3126 `chatHeaders(mode,key)`
- L3133 `callChat(mode,model,key,prompt,img,signal,opts={})` — ChatGPT, Claude, Groq, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L3187 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L3202 constante `OLD_GEMINI_RE`
- L3203 constante `MODEL_PREF`
- L3204 `pickModel(ids,mode=$('ai-mode')`
- L3218 `ensureModel(st)`
- L3234 `syncProvider()`
- L3253 `requestAI(prompt,img,signal,modelOverride='',onStep=null,opts={})`
- L3290 constante `AI_PREF`
- L3291 `aiConnected()`
- L3292 `syncAI()`
- L3294 `saveAIPrefs()`
- L3295 `loadAIPrefs()`
- L3296 `openAISetup()`
- L3303 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L3310 constante `MACROS`
- L3312 `cleanGoals(o,fallback)`
- L3317 `cleanCompare(o={})`
- L3321 `snapshotDay(d,reference='saved')`
- L3326 `upgradeTo17(s,o)`
- L3331 `entriesFor(d,source=weekSource)`
- L3335 `dayRow(dt,source=weekSource)`
- L3339 `goalsFor(dt)`
- L3345 `metricValue(r,key)`
- L3351 `targetOf(dt,key)`
- L3355 `weekSummary()`
- L3359 `aggregate(key,summary=weekSummary()`
- L3363 `tone(pct,mode='macro')`
- L3370 `pctText(a)`
- L3371 `weekProgress(a,color)`
- L3372 `renderWeekMicros(s)`
- L3384 `ratioAggregate(s,num,den)`
- L3388 `renderWeekRatios(s)`
- L3394 `renderWeekTable(s)`
- L3395 `weeklyDetail(key,oneDate=null)`
- L3404 `weekRatioDetail(key)`
- L3412 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L3418 `openDay(dt)`
- L3456 `withDayGoals(fn)`
- L3461 `renderMicros()`
- L3462 `nutrientDetail(key)`
- L3463 `editTargets()`
- L3464 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L3474 `summaryFor(start)`
- L3478 `ringSVG(pct,color,marker)`
- L3480 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L3484 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L3501 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L3502 `macroTone(p)`
- L3503 `dayMacroPct(dt,k)`
- L3504 `renderWeekly()`
- L3527 `weekDetail(dt,picked)`
- L3535 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L3545 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L3551 `sparkline(pts)`
- L3557 `renderCalendar()`
- L3574 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L3575 `splitMeals(raw)`
- L3585 `localDay(raw,fallback)`
- L3592 `askUnitWeightAI(foodName)`
- L3602 `promptUnitWeight(foodId,count,meal)`
- L3618 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L3678 `parseCsv(text)`
- L3693 `hevyDate(value,format='auto')`
- L3710 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L3725 constante `GYM_APPS`
- L3727 `gymSig(headers)`
- L3728 `gymApp(headers)`
- L3729 `hevyMapping()`
- L3730 `gymSaved()`
- L3731 `renderMapping(parsed)`
- L3748 `optionalNum(v,min=0,max=1e7)`
- L3753 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L3760 `buildHevy(parsed,map)`
- L3794 `cleanWorkout(s)`
- L3801 `formatGymAI(txt)`
- L3812 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L3837 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L3838 constante `GP_ALIAS`
- L3848 `gpNorm(s)`
- L3849 `gpKey(name)`
- L3853 `gpF(n,d=0)`
- L3854 `gpDate(d,opt)`
- L3855 `gpMonday(d)`
- L3856 constante `GP_GROUPS`
- L3871 constante `GP_COLORS`
- L3872 `gpGroup(name)`
- L3873 `gpWorkSets(s)`
- L3875 `gpModel()`
- L3903 `gpSessionMetrics(e,sets)`
- L3918 constante `GP_METRICS`
- L3923 `gpMetricsFor(e)`
- L3924 `gpRangeHist(e)`
- L3925 `gpPRs(model)`
- L3948 `gpStatus(e)`
- L3966 `gpNext(e)`
- L3974 `gpChart(e)`
- L4002 `gpPointDetail(e)`
- L4008 `gpRepTable(e)`
- L4015 `gpKpis(model)`
- L4024 `gpWeekData(model,w)` — Datos de una semana de gimnasio (series por músculo y sesiones).
- L4029 `gpWeekLabel(w,short)`
- L4030 `gpWeekly(model)`
- L4049 `gpMuscles(model)`
- L4057 `gpHeat(model)` — v69: «Constancia» — mapa de días entrenados (como antes), con días de la semana, meses, intensidad y detalle al tocar.
- L4077 `gpExList(model)`
- L4084 `gpExDetail(model)`
- L4097 `gpDayFood(dt)`
- L4098 `gpNutrition(model)`
- L4105 `gpRecentPRs(model)`
- L4109 `gpSessions(model)`
- L4115 `gpSessionModal(id)`
- L4126 `gpWeekModal(w)`
- L4133 `gpSelect(key)`
- L4134 `gpClick(e)`
- L4151 `renderGym()`
- L4175 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L4184 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L4190 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L4215 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L4219 `showHelp()`
- L4223 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L4225 `markBackup()`
- L4229 `exportJSON()`
- L4234 `drawBackupReminder()`
- L4246 `applyDensity()`
- L4258 `syncDayComplete()`
- L4261 `drawMeals()` — Comidas del día de un vistazo.
- L4269 `filterLog()` — Buscador de Registro.
- L4282 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L4288 `recentFoods()`
- L4293 `quickChip(e,fav)`
- L4311 `drawQuickFoods()`
- L4340 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L4344 `toggleAddPanel(id)`
- L4357 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L4368 `pasteMessage(text,ok)`
- L4376 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L4387 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L4398 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L4404 `upgradeTo27(s,o)`
- L4421 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L4443 `storableState()`

### Render único: actualiza toda la página

- L4452 `nearView(el)`
- L4454 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L4459 `scheduleLazyRender()`
- L4463 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L4500 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L4501 constante `REF_TABLE`
- L4508 `refTargets(mode)`
- L4509 `syncMicroMode()`
- L4522 `mealByHour(h=new Date()`
- L4529 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L4540 `dataSummary(s)`
- L4544 `confirmImport(next,name)`
- L4551 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L4557 `checkUpdate()`
- L4562 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L4577 constante `GAP_PREFER`
- L4578 constante `GAP_SKIP`
- L4579 constante `GAP_UNIT`
- L4580 `gapQty(f,x)`
- L4581 `gapFoods(key,gap,ctx)`
- L4600 `weekSources(key,sum)`
- L4606 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L4619 `gapRow(x,open,meal,sum,ctx)`
- L4635 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L4660 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L4661 `isFemale(s=state)`
- L4662 `sexLabel(s=state)`
- L4663 `sexBadge(sex)`
- L4665 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L4666 constante `OPT_FEMALE`
- L4677 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba; A (1.500 µg = 5.000 UI) y D (50 µg = 2.000 UI) mantienen A:D en zona verde (2,5:1).
- L4678 `applySexOpt(sex)`
- L4680 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L4685 `cleanPreset(p,fb)`
- L4689 `dayNamesFor(types)`
- L4691 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L4701 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L4709 `profV()`
- L4710 `isTrainDay(i)`
- L4711 `activityName(i)`
- L4712 `dayFaf(i)`
- L4713 `presetDesc(cfg,shake)`
- L4717 `profileDescription()`
- L4725 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L4727 `wizCatalog()`
- L4728 `wizOpen(opts={})`
- L4744 `wizTitle()`
- L4745 `wizPaint(sameStep=true)`
- L4754 `wizSync()`
- L4773 `wizFoodOptions()`
- L4776 `wizPresetSummary(cfg,whey)`
- L4781 `wizPresetHTML(kind)`
- L4789 `wizPreview()`
- L4800 `wizLiveHTML()`
- L4804 `wizHTML()`
- L4851 `isStandalonePWA()`
- L4852 `isInAppWebview()`
- L4853 `isBraveBrowser()`
- L4854 `syncInstallButtons()`
- L4860 `buildTransferUrl()`
- L4875 `triggerPWAInstall()`
- L4910 `wizCommit()`
- L4961 `showPostWizInstallBanner(name)`

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L5023 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L5024 constante `SUPP_CATALOG`
- L5049 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L5050 constante `PEAT_BREAKFAST`
- L5051 constante `PEAT_SHAKE`
- L5053 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L5060 `benfoUser()`
- L5062 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L5078 `ico(n)`
- L5080 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L5089 `showTour(i=0)`
- L5101 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L5102 `hubAction(v)`
- L5110 constante `FB_CATS` — Envíos anónimos directos al buzón de BioPeat (sin cuentas ni datos personales).
- L5112 `openFeedback()`
- L5116 `feedbackData()`
- L5123 `feedbackText()`
- L5124 `sendFeedback()`
- L5144 `shareFeedback()`
- L5161 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L5168 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L5176 constante `I18N_EN`

### v59: idioma (español / inglés)

- L5181 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L5182 constante `WD_EN`
- L5183 `trOne(s)`
- L5191 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L5192 constante `ES_FOOD_GYM`
- L5229 `trFood(s)`
- L5241 constante `TR_TPL`
- L5282 `trLower(s)`
- L5283 `trTpl(s,attr)`
- L5284 constante `FOOD_SEL`
- L5285 `trText(s,attr=false)`
- L5295 `trNode(n)`
- L5314 `trEl(el)`
- L5327 `trTree(root)`
- L5336 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L5350 `flushTr()`
- L5351 `syncTrObserver()`
- L5356 `loadEnDict()`
- L5368 `setLang(l,quiet)`
- L5383 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter + Worker agregados), solo en la web publicada

- L5392 constante `GC_CODE`
- L5393 `pingAnalytics(extra={})`
- L5409 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L5421 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L5422 `packMove()`
- L5430 `unpackMove(code)`
- L5441 `moveData()`
- L5451 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L5457 `checkMove(code)`
- L5476 `aiFrameworkLines()` — v69: marco de referencia del informe para IA. Así cualquier IA, aunque no conozca la app ni al usuario, sabe con qué comparar.

### Arranque

