# MAPA DEL CÓDIGO · BioPeat v85 (revisión de datos 27)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

Arquitectura modular: `index.html` (66 KB), `assets/styles.css`, `assets/data.js`, `assets/app.js` (513 KB) y `assets/i18n-en.js`.

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

- L74 constante `REF_MAP` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L75 constante `REF_CACHE`
- L77 `ensureRefIndex()`
- L84 `refNutrients(id)`
- L92 constante `STRIP_PREP_RE`
- L93 `findRef(text,strict=false)`
- L116 `refCatalogCompact()`
- L117 `fromRef(id,amount,meal,note='',srcText='')`
- L122 `optInfo(k,goal)`
- L129 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L137 `optLine(k,goal,unit)`
- L144 `optRefHTML(k,goal,unit)`
- L145 constante `FAF`
- L147 constante `LOC`
- L151 `number(v,min=0,max=1e6)`
- L157 `decimalInputs(root=document)`
- L158 `localDate(d=new Date()`
- L159 `validDate(s)`
- L164 `shift(s,n)`
- L172 `stripProto(o)`
- L179 `cleanBio(b)`
- L188 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L190 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L196 constante `DAY_TYPES`
- L197 constante `NEW_V54`
- L201 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L204 `bmr(w=state.profile.weight)` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L210 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L235 `cleanNutrients(o,required=false)`
- L247 `cleanEntry(e)`
- L252 `cleanPlan(p)`
- L256 `planEntry(p)`
- L265 `seedPlan(d,whichDate)`
- L269 `ensureDay(d=date)`
- L276 `effectiveEntries(d=day()`
- L277 constante `SALTED_IDS`
- L278 constante `SWEET_RE`
- L279 `inferFatShares(e,txt=normalize((e?.name||'')`
- L297 `inferredNutrients(e)`
- L339 `totals(entries)`
- L351 `change(fn,message='Guardado')`
- L357 `afterPaint(fn)`
- L358 `queueSave(idle=false)`
- L365 `flushQueuedSave(hard=false)`
- L370 `undo()`
- L378 `toast(text,canUndo=false)`
- L386 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L387 `onClick(fn)`
- L389 `attempt(fn)`
- L393 `modal(title,body)`
- L402 `modalRestore()`
- L412 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L413 `modalBack()`
- L414 `goDate(d)`
- L421 `renderHeader()`
- L434 `renderRows(entries)`
- L438 `entryValues(e)`
- L439 `renderLog()`
- L446 `fromFood(id,amount,meal)`
- L452 `pantryId(name)`
- L454 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L473 `addEntries(entries,message='Añadido',d=date,opts={})`
- L482 `recipe(kind)`
- L489 `summary(entries)`
- L493 `renderPresetInfo()`
- L506 `stripCode(raw)`
- L512 `sanitizeNutrients(o,grams=100,fallbackRefId='')`
- L539 `parseBIO(raw,meal=$('meal-select')`
- L551 `parseSmart(raw)`
- L555 constante `COUNT`
- L556 constante `UNIT_RE`
- L620 `offToNutrients(nut={},fallbackName='')` — Open Food Facts (gratis, sin clave, CORS nativo): consulta por código de barras o texto.
- L641 `lookupOFFBarcode(code,signal,ms=3200)`
- L657 `searchOFF(query,signal,ms=4500)`
- L676 `openProductSearch()`
- L715 `nutrientFields(n,prefix='n_')`
- L716 `readNutrients(form,prefix='n_')`
- L721 `editEntry(id)`
- L730 `editFood(id,pending=null)`
- L735 `usageStats(days=90)`
- L743 `renderFoods(forceList=false)`
- L755 `nutrientSources(key)`
- L762 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L763 `suppSlot(meal)`
- L764 `renderSupps()`
- L779 `editPlan(id)`
- L786 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L807 `makePrompt(meal='Comida',note='')`
- L812 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L816 `pantryCompact()`
- L820 constante `MEAL_AI_SCHEMA`
- L861 `mealSystemPrompt(usePhoto)`
- L877 `hydrateAIItems(rawItems,fallback,usePhoto,aiModel,signal)`
- L926 `photoPrompt(meal,note)`
- L929 `resetPhoto()`
- L940 `openPhoto()`
- L946 `shrinkPhoto(file)`
- L949 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L975 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L982 `cleanFood(id,f)`
- L989 `migrateBase(o)`
- L1009 `download(name,text,type)`
- L1018 `portable()`
- L1072 `syncAppIcons()`
- L1080 `downloadAppIcons()`
- L1117 constante `PROFILES_KEY`
- L1119 `ensureProfilesStore()`
- L1139 `resetProfileSessionUI()`
- L1146 `saveProfilesStore(st)`
- L1155 `syncCurrentProfileToStore(snapObj=null,immediate=true)`
- L1166 `activeProfileName()`
- L1170 `renderProfilesList()`
- L1212 `switchProfile(id)`
- L1234 `deleteProfileById(id)`
- L1259 `refreshDrawerSummary()`
- L1276 `toggleLeftDrawer(force)`
- L1291 `buildAIExportText(rangeOverride)`
- L1546 `copyAIExport()`
- L1560 `downloadAIExport()`
- L1569 `renderDrawerChat()`
- L1588 `buildDrawerChatContext()`
- L1627 `buildDrawerChatPrompt(question)`
- L1639 `askDrawerAI(rawQuestion)`
- L1728 constante `CLOUD_OFF_KEY`
- L1739 `bytesToB64(u8)`
- L1740 `b64ToBytes(s)`
- L1741 `bytesToB64Url(u8)`
- L1742 `sha256Hex(str)`
- L1743 `sha256Bytes(str)`
- L1744 `generateSyncKey()`
- L1745 `ensureSyncKey()`
- L1746 `mirrorSyncKey(k)`
- L1747 `deriveSyncCreds(keyStr)`
- L1753 `hasMeaningfulData()`
- L1760 `buildCloudBundle()`
- L1767 `encryptVaultPayload(obj,keyStr)`
- L1775 `readDecompressedText(bytes,maxBytes=10*1024*1024)`
- L1791 `decryptVaultPayload(resp,keyStr)`
- L1803 `bundleHash(bundle)`
- L1807 `applyCloudBundle(o,rev=1)`
- L1817 `cloudPull(keyStr,opts={})`
- L1837 `cloudPush(opts={})`
- L1874 `scheduleCloudPush()`
- L1880 `scheduleAutoCloudPull(delayMs=120)`
- L1894 `saveSyncToPassMgr()`
- L1901 `trySilentPassMgrRecovery()`
- L1911 `extractSyncKeyInput(val)`
- L1917 `applySyncKey(rawKey,opts={})`
- L1938 `takeSyncCode()`
- L1949 `renderCloudStatus()`
- L1972 `buildMagicSyncUrl()`
- L1979 `openMagicSyncModal()`
- L1988 `shareMagicSyncLink()`
- L1995 `copyMagicSyncLink()`
- L2000 `openCloudLinkModal()`
- L2003 `deleteCloudBackup(confirmed=false)`
- L2040 `mirrorToIDB(raw,profRaw)`
- L2043 `storageStatus()`
- L2050 `idbReadWrite(mode,value,key='current')`
- L2051 `openDB()`
- L2053 `flushDeferredSave()`
- L2064 `save(skipCloud=false)`

### Eventos generales: añadir con un toque, editar, eliminar

- L2093 `setQuantity(id,value,msg='Cantidad actualizada')`
- L2097 `niceStep(v)`
- L2098 `stepQuantity(id,dir)`
- L2152 `renderAppInfo(force=false)`
- L2184 `init()`
- L2221 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L2223 `setNav(v)`
- L2228 `go(v,focus)`
- L2239 constante `THEME_KEY`
- L2240 constante `SUN_SVG`
- L2241 constante `MOON_SVG`
- L2243 `syncThemeUI()`
- L2257 `toggleTheme()`
- L2267 `syncLogoTheme()`
- L2276 `applyMenuBtnState()`
- L2300 `syncDatePill()`
- L2312 `clampBtnPos(el,x,y)`
- L2322 `bindDraggableBtn(el,storeKey)`
- L2383 `bindDrawerGestures()`
- L2421 `animateValue(el,to,suffix='%',digits=0)`
- L2430 `tick(now)`
- L2433 `macroCard(key,name,color)`
- L2434 `renderToday()`
- L2458 `renderBio()`
- L2483 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L2485 constante `HOME`
- L2487 `coachCandidates()`
- L2493 `coachIdeas(t,g,ref,meal)`
- L2512 `coachQuickAdd(key)`
- L2520 `renderCoach()`
- L2542 `coachPrompt()`
- L2551 `nutrientDetailStandard(key)`
- L2566 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L2572 `upgradeTo12(s,o)`
- L2577 `benfotiamineTotals(entries=effectiveEntries()`
- L2586 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L2588 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L2600 `microStat(m,t=totals()`
- L2605 `metric(m,t=totals()`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L2612 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L2613 `ratioInfo(key,t=totals()`
- L2652 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L2669 constante `RATIO_ENDS`
- L2671 `ratioZones(i)` — v68: cada equilibrio tiene una zona «aceptable» (ni verde ni mala) y su meta visible en la tarjeta.
- L2679 `ratioTone(i)`
- L2684 constante `NEAR_HEAD`
- L2685 `ratioBar(i,big=false)`
- L2694 `ratioNeedBase(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L2712 `needHTML(i,t)`
- L2713 `ratioNeed(i,t=totals()`
- L2717 `adBalance(t=totals()`
- L2744 `zncuSuppKey()`
- L2745 `zncuSuppCfg()`
- L2767 `zncuDoseLabel(zn,cu)`
- L2770 `hasZncuSupp(d=day()`
- L2775 `toggleZncuSupp()`
- L2795 `openZncuConfig()`
- L2801 `renderRatios()`
- L2812 `ratioDetail(key)`
- L2829 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L2846 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L2861 `renderMicroMap(t=totals()`
- L2874 `nutrientDetailForDay(key)`
- L2879 `editTargetsForm()`
- L2889 `mealData()`
- L2894 `renderMealSegments()`
- L2902 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L2937 constante `FAT_KEYS`
- L2939 `fatData(entries=effectiveEntries()`
- L2945 `energyData(entries=effectiveEntries()`
- L2949 `segmentedBar(items,total,attr)`
- L2953 `renderMealChart()`
- L2958 `renderFat()`
- L2966 `fatDetail(key)`
- L2971 `energyDetail(key)`
- L2978 `portionCandidates(q='')`
- L2983 `openPortion()`
- L2996 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L3011 `templates()`
- L3015 `renderExtra()`
- L3026 `updateExtra(reset=true)`
- L3038 `addExtra(id,amount)`
- L3054 `shakePreview()`
- L3055 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L3070 constante `LENS`
- L3076 `lensKey(key)`
- L3077 `lensHTML(key)`
- L3081 `appendLens(key)`
- L3090 `weekDates()`

### IA en la página: conexión directa o por servidor

- L3100 constante `MEAL_WORD`
- L3101 `mealOfWord(w)`
- L3102 `mealFromText(raw,fallback)`
- L3106 `canonMeal(v,fallback)`
- L3114 `localMeal(raw,meal)`
- L3120 constante `AI_FALLBACK`
- L3121 constante `GEMINI_DEFAULTS`
- L3122 constante `GROQ_DEFAULTS`
- L3123 `aiTaskProfile(task,hasImg=false)`
- L3131 `geminiThinkLevel(model,want)`
- L3137 `supportsGeminiTemp(model)`
- L3138 `readSSE(res,onEvent)`
- L3157 `applyAIConfig(raw)`
- L3183 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L3184 `callGemini(model,key,prompt,img,signal,opts={})`
- L3230 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), Groq (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L3238 `aiProv(m=$('ai-mode')`
- L3239 `aiBase(mode)`
- L3248 `chatHeaders(mode,key)`
- L3255 `callChat(mode,model,key,prompt,img,signal,opts={})` — ChatGPT, Claude, Groq, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L3309 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L3324 constante `OLD_GEMINI_RE`
- L3325 constante `MODEL_PREF`
- L3326 `pickModel(ids,mode=$('ai-mode')`
- L3340 `ensureModel(st)`
- L3356 `syncProvider()`
- L3375 `requestAI(prompt,img,signal,modelOverride='',onStep=null,opts={})`
- L3412 constante `AI_PREF`
- L3413 `aiConnected()`
- L3414 `syncAI()`
- L3416 `saveAIPrefs()`
- L3417 `loadAIPrefs()`
- L3418 `openAISetup()`
- L3425 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L3432 constante `MACROS`
- L3434 `cleanGoals(o,fallback)`
- L3439 `cleanCompare(o={})`
- L3443 `snapshotDay(d,reference='saved')`
- L3448 `upgradeTo17(s,o)`
- L3453 `entriesFor(d,source=weekSource)`
- L3457 `dayRow(dt,source=weekSource)`
- L3461 `goalsFor(dt)`
- L3467 `metricValue(r,key)`
- L3473 `targetOf(dt,key)`
- L3477 `weekSummary()`
- L3481 `aggregate(key,summary=weekSummary()`
- L3485 `tone(pct,mode='macro')`
- L3492 `pctText(a)`
- L3493 `weekProgress(a,color)`
- L3494 `renderWeekMicros(s)`
- L3506 `ratioAggregate(s,num,den)`
- L3510 `renderWeekRatios(s)`
- L3516 `renderWeekTable(s)`
- L3517 `weeklyDetail(key,oneDate=null)`
- L3526 `weekRatioDetail(key)`
- L3534 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L3540 `openDay(dt)`
- L3578 `withDayGoals(fn)`
- L3583 `renderMicros()`
- L3584 `nutrientDetail(key)`
- L3585 `editTargets()`
- L3586 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L3596 `summaryFor(start)`
- L3600 `ringSVG(pct,color,marker)`
- L3602 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L3606 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L3623 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L3624 `macroTone(p)`
- L3625 `dayMacroPct(dt,k)`
- L3626 `renderWeekly()`
- L3649 `weekDetail(dt,picked)`
- L3657 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L3667 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L3673 `sparkline(pts)`
- L3679 `renderCalendar()`
- L3696 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L3697 `splitMeals(raw)`
- L3707 `localDay(raw,fallback)`
- L3714 `askUnitWeightAI(foodName)`
- L3724 `promptUnitWeight(foodId,count,meal)`
- L3740 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L3800 `parseCsv(text)`
- L3815 `hevyDate(value,format='auto')`
- L3832 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L3847 constante `GYM_APPS`
- L3849 `gymSig(headers)`
- L3850 `gymApp(headers)`
- L3851 `hevyMapping()`
- L3852 `gymSaved()`
- L3853 `renderMapping(parsed)`
- L3870 `optionalNum(v,min=0,max=1e7)`
- L3875 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L3882 `buildHevy(parsed,map)`
- L3916 `cleanWorkout(s)`
- L3923 `formatGymAI(txt)`
- L3934 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L3959 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L3960 constante `GP_ALIAS`
- L3970 `gpNorm(s)`
- L3971 `gpKey(name)`
- L3975 `gpF(n,d=0)`
- L3976 `gpDate(d,opt)`
- L3977 `gpMonday(d)`
- L3978 constante `GP_GROUPS`
- L3993 constante `GP_COLORS`
- L3994 `gpGroup(name)`
- L3995 `gpWorkSets(s)`
- L3997 `gpModel()`
- L4025 `gpSessionMetrics(e,sets)`
- L4040 constante `GP_METRICS`
- L4045 `gpMetricsFor(e)`
- L4046 `gpRangeHist(e)`
- L4047 `gpPRs(model)`
- L4070 `gpStatus(e)`
- L4088 `gpNext(e)`
- L4096 `gpChart(e)`
- L4124 `gpPointDetail(e)`
- L4130 `gpRepTable(e)`
- L4137 `gpKpis(model)`
- L4146 `gpWeekData(model,w)` — Datos de una semana de gimnasio (series por músculo y sesiones).
- L4151 `gpWeekLabel(w,short)`
- L4152 `gpWeekly(model)`
- L4171 `gpMuscles(model)`
- L4179 `gpHeat(model)` — v69: «Constancia» — mapa de días entrenados (como antes), con días de la semana, meses, intensidad y detalle al tocar.
- L4199 `gpExList(model)`
- L4206 `gpExDetail(model)`
- L4219 `gpDayFood(dt)`
- L4220 `gpNutrition(model)`
- L4227 `gpRecentPRs(model)`
- L4231 `gpSessions(model)`
- L4237 `gpSessionModal(id)`
- L4248 `gpWeekModal(w)`
- L4255 `gpSelect(key)`
- L4256 `gpClick(e)`
- L4273 `renderGym()`
- L4297 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L4306 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L4312 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L4337 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L4341 `showHelp()`
- L4345 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L4347 `markBackup()`
- L4351 `exportJSON()`
- L4356 `drawBackupReminder()`
- L4368 `applyDensity()`
- L4380 `syncDayComplete()`
- L4383 `drawMeals()` — Comidas del día de un vistazo.
- L4391 `filterLog()` — Buscador de Registro.
- L4404 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L4410 `recentFoods()`
- L4415 `quickChip(e,fav)`
- L4433 `drawQuickFoods()`
- L4462 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L4466 `toggleAddPanel(id)`
- L4479 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L4490 `pasteMessage(text,ok)`
- L4498 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L4509 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L4520 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L4526 `upgradeTo27(s,o)`
- L4543 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L4565 `storableState()`

### Render único: actualiza toda la página

- L4574 `nearView(el)`
- L4576 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L4581 `scheduleLazyRender()`
- L4585 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L4622 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L4623 constante `REF_TABLE`
- L4630 `refTargets(mode)`
- L4631 `syncMicroMode()`
- L4644 `mealByHour(h=new Date()`
- L4651 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L4662 `dataSummary(s)`
- L4666 `confirmImport(next,name)`
- L4673 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L4679 `checkUpdate()`
- L4684 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L4700 constante `GAP_PREFER`
- L4701 constante `GAP_SKIP`
- L4702 constante `GAP_UNIT`
- L4703 `gapQty(f,x)`
- L4704 `gapFoods(key,gap,ctx)`
- L4723 `weekSources(key,sum)`
- L4729 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L4742 `gapRow(x,open,meal,sum,ctx)`
- L4758 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L4783 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L4784 `isFemale(s=state)`
- L4785 `sexLabel(s=state)`
- L4786 `sexBadge(sex)`
- L4788 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L4789 constante `OPT_FEMALE`
- L4800 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba; A (1.500 µg = 5.000 UI) y D (50 µg = 2.000 UI) mantienen A:D en zona verde (2,5:1).
- L4801 `applySexOpt(sex)`
- L4803 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L4808 `cleanPreset(p,fb)`
- L4812 `dayNamesFor(types)`
- L4814 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L4824 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L4832 `profV()`
- L4833 `isTrainDay(i)`
- L4834 `activityName(i)`
- L4835 `dayFaf(i)`
- L4836 `presetDesc(cfg,shake)`
- L4840 `profileDescription()`
- L4848 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L4850 `wizCatalog()`
- L4851 `wizOpen(opts={})`
- L4867 `wizTitle()`
- L4868 `wizPaint(sameStep=true)`
- L4877 `wizSync()`
- L4896 `wizFoodOptions()`
- L4899 `wizPresetSummary(cfg,whey)`
- L4904 `wizPresetHTML(kind)`
- L4912 `wizPreview()`
- L4923 `wizLiveHTML()`
- L4927 `wizHTML()`
- L4974 `isStandalonePWA()`
- L4975 `isInAppWebview()`
- L4976 `isBraveBrowser()`
- L4977 `syncInstallButtons()`
- L4983 `buildTransferUrl()`
- L4998 `triggerPWAInstall()`
- L5033 `wizCommit()`
- L5084 `showPostWizInstallBanner(name)`

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L5146 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L5147 constante `SUPP_CATALOG`
- L5172 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L5173 constante `PEAT_BREAKFAST`
- L5174 constante `PEAT_SHAKE`
- L5176 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L5183 `benfoUser()`
- L5185 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L5201 `ico(n)`
- L5203 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L5212 `showTour(i=0)`
- L5224 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L5225 `hubAction(v)`
- L5233 constante `FB_CATS` — Envíos anónimos directos al buzón de BioPeat (sin cuentas ni datos personales).
- L5235 `openFeedback()`
- L5239 `feedbackData()`
- L5246 `feedbackText()`
- L5247 `sendFeedback()`
- L5267 `shareFeedback()`
- L5284 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L5291 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L5299 constante `I18N_EN`

### v59: idioma (español / inglés)

- L5304 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L5305 constante `WD_EN`
- L5306 `trOne(s)`
- L5314 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L5315 constante `ES_FOOD_GYM`
- L5352 `trFood(s)`
- L5364 constante `TR_TPL`
- L5405 `trLower(s)`
- L5406 `trTpl(s,attr)`
- L5407 constante `FOOD_SEL`
- L5408 `trText(s,attr=false)`
- L5418 `trNode(n)`
- L5437 `trEl(el)`
- L5450 `trTree(root)`
- L5459 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L5473 `flushTr()`
- L5474 `syncTrObserver()`
- L5479 `loadEnDict()`
- L5491 `setLang(l,quiet)`
- L5506 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter + Worker agregados), solo en la web publicada

- L5515 constante `GC_CODE`
- L5516 `pingAnalytics(extra={})`
- L5532 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L5544 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L5545 `packMove()`
- L5553 `unpackMove(code)`
- L5564 `moveData()`
- L5574 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L5580 `checkMove(code)`
- L5599 `aiFrameworkLines()` — v69: marco de referencia del informe para IA. Así cualquier IA, aunque no conozca la app ni al usuario, sabe con qué comparar.

### Arranque

