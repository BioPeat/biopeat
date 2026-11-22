# MAPA DEL CÓDIGO · BioPeat v77 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (1001 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-6470; todo el JavaScript en `<script id="app">` (desde la línea 6471).

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

- L6537 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L6538 constante `AZUCAR_N`
- L6539 constante `USDA_N`
- L6545 constante `FOODS`
- L6547 constante `BASE_FAT_FIX`
- L6551 constante `REF_COLS` — Base de referencia verificada (USDA FoodData Central / BEDCA, por 100 g o 100 ml comestibles).
- L6552 constante `REF_RAW`
- L6717 constante `REF_MAP`
- L6718 constante `REF_CACHE`
- L6720 `ensureRefIndex()`
- L6727 `refNutrients(id)`
- L6735 constante `STRIP_PREP_RE`
- L6736 `findRef(text,strict=false)`
- L6759 `refCatalogCompact()`
- L6760 `fromRef(id,amount,meal,note='',srcText='')`
- L6765 constante `EXTRA`
- L6766 constante `KEYS`
- L6768 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L6770 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L6774 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6775 constante `OPT`
- L6801 constante `LIMIT`
- L6802 `optInfo(k,goal)`
- L6809 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6817 `optLine(k,goal,unit)`
- L6824 `optRefHTML(k,goal,unit)`
- L6826 constante `DAYS`
- L6827 constante `FAF`
- L6829 constante `LOC`
- L6833 `number(v,min=0,max=1e6)`
- L6839 `decimalInputs(root=document)`
- L6840 `localDate(d=new Date()`
- L6841 `validDate(s)`
- L6846 `shift(s,n)`
- L6854 `stripProto(o)`
- L6861 `cleanBio(b)`
- L6870 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6872 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6878 constante `DAY_TYPES`
- L6879 constante `NEW_V54`
- L6883 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6886 `bmr(w=state.profile.weight)` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6892 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6917 `cleanNutrients(o,required=false)`
- L6929 `cleanEntry(e)`
- L6934 `cleanPlan(p)`
- L6938 `planEntry(p)`
- L6947 `seedPlan(d,whichDate)`
- L6951 `ensureDay(d=date)`
- L6958 `effectiveEntries(d=day()`
- L6959 constante `SALTED_IDS`
- L6960 constante `SWEET_RE`
- L6961 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6979 `inferredNutrients(e)`
- L7021 `totals(entries)`
- L7033 `change(fn,message='Guardado')`
- L7037 `undo()`
- L7045 `toast(text,canUndo=false)`
- L7053 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L7054 `onClick(fn)`
- L7056 `attempt(fn)`
- L7060 `modal(title,body)`
- L7069 `modalRestore()`
- L7079 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L7080 `modalBack()`
- L7081 `goDate(d)`
- L7088 `renderHeader()`
- L7101 `renderRows(entries)`
- L7105 `entryValues(e)`
- L7106 `renderLog()`
- L7113 `fromFood(id,amount,meal)`
- L7119 `pantryId(name)`
- L7121 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L7137 `addEntries(entries,message='Añadido',d=date,opts={})`
- L7146 `recipe(kind)`
- L7153 `summary(entries)`
- L7157 `renderPresetInfo()`
- L7170 `stripCode(raw)`
- L7176 `sanitizeNutrients(o,grams=100,fallbackRefId='')`
- L7203 `parseBIO(raw,meal=$('meal-select')`
- L7215 `parseSmart(raw)`
- L7219 constante `COUNT`
- L7220 constante `UNIT_RE`
- L7272 `offToNutrients(nut={},fallbackName='')` — Open Food Facts (gratis, sin clave, CORS nativo): consulta por código de barras o texto.
- L7293 `lookupOFFBarcode(code,signal,ms=3200)`
- L7308 `searchOFF(query,signal,ms=4500)`
- L7326 `openProductSearch()`
- L7364 `nutrientFields(n,prefix='n_')`
- L7365 `readNutrients(form,prefix='n_')`
- L7370 `editEntry(id)`
- L7379 `editFood(id,pending=null)`
- L7384 `usageStats(days=90)`
- L7392 `renderFoods(forceList=false)`
- L7404 `nutrientSources(key)`
- L7411 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L7412 `suppSlot(meal)`
- L7413 `renderSupps()`
- L7428 `editPlan(id)`
- L7435 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L7456 `makePrompt(meal='Comida',note='')`
- L7461 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L7465 `pantryCompact()`
- L7469 constante `MEAL_AI_SCHEMA`
- L7509 `mealSystemPrompt(usePhoto)`
- L7525 `hydrateAIItems(rawItems,fallback,usePhoto,aiModel,signal)`
- L7568 `photoPrompt(meal,note)`
- L7571 `resetPhoto()`
- L7582 `openPhoto()`
- L7588 `shrinkPhoto(file)`
- L7591 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L7617 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L7624 `cleanFood(id,f)`
- L7628 `migrateBase(o)`
- L7648 `download(name,text,type)`
- L7657 `portable()`
- L7699 `syncAppIcons()`
- L7707 `downloadAppIcons()`
- L7744 constante `PROFILES_KEY`
- L7746 `ensureProfilesStore()`
- L7766 `resetProfileSessionUI()`
- L7773 `saveProfilesStore(st)`
- L7782 `syncCurrentProfileToStore(snapObj=null,immediate=true)`
- L7793 `activeProfileName()`
- L7797 `renderProfilesList()`
- L7839 `switchProfile(id)`
- L7861 `deleteProfileById(id)`
- L7886 `refreshDrawerSummary()`
- L7903 `toggleLeftDrawer(force)`
- L7918 `buildAIExportText(rangeOverride)`
- L8173 `copyAIExport()`
- L8187 `downloadAIExport()`
- L8196 `renderDrawerChat()`
- L8215 `buildDrawerChatContext()`
- L8254 `buildDrawerChatPrompt(question)`
- L8266 `askDrawerAI(rawQuestion)`
- L8355 constante `CLOUD_OFF_KEY`
- L8366 `bytesToB64(u8)`
- L8367 `b64ToBytes(s)`
- L8368 `bytesToB64Url(u8)`
- L8369 `sha256Hex(str)`
- L8370 `sha256Bytes(str)`
- L8371 `generateSyncKey()`
- L8372 `ensureSyncKey()`
- L8373 `mirrorSyncKey(k)`
- L8374 `deriveSyncCreds(keyStr)`
- L8380 `hasMeaningfulData()`
- L8387 `buildCloudBundle()`
- L8394 `encryptVaultPayload(obj,keyStr)`
- L8402 `readDecompressedText(bytes,maxBytes=10*1024*1024)`
- L8418 `decryptVaultPayload(resp,keyStr)`
- L8430 `bundleHash(bundle)`
- L8434 `applyCloudBundle(o,rev=1)`
- L8444 `cloudPull(keyStr,opts={})`
- L8464 `cloudPush(opts={})`
- L8501 `scheduleCloudPush()`
- L8507 `scheduleAutoCloudPull(delayMs=120)`
- L8521 `saveSyncToPassMgr()`
- L8528 `trySilentPassMgrRecovery()`
- L8538 `extractSyncKeyInput(val)`
- L8544 `applySyncKey(rawKey,opts={})`
- L8565 `takeSyncCode()`
- L8576 `renderCloudStatus()`
- L8593 `openCloudLinkModal()`
- L8596 `copyMagicSyncLink()`
- L8603 `deleteCloudBackup(confirmed=false)`
- L8638 `mirrorToIDB(raw,profRaw)`
- L8641 `storageStatus()`
- L8648 `idbReadWrite(mode,value,key='current')`
- L8649 `openDB()`
- L8651 `flushDeferredSave()`
- L8661 `save(skipCloud=false)`

### Eventos generales: añadir con un toque, editar, eliminar

- L8689 `setQuantity(id,value,msg='Cantidad actualizada')`
- L8693 `niceStep(v)`
- L8694 `stepQuantity(id,dir)`
- L8748 `renderAppInfo(force=false)`
- L8780 `init()`
- L8816 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L8818 `setNav(v)`
- L8823 `go(v,focus)`
- L8834 constante `THEME_KEY`
- L8835 constante `SUN_SVG`
- L8836 constante `MOON_SVG`
- L8838 `syncThemeUI()`
- L8850 `toggleTheme()`
- L8859 `syncLogoTheme()`
- L8870 `applyMenuBtnState()`
- L8893 `syncDatePill()`
- L8906 `clampBtnPos(el,x,y)`
- L8916 `bindDraggableBtn(el,storeKey)`
- L9001 `bindDrawerGestures()`
- L9039 `animateValue(el,to,suffix='%',digits=0)`
- L9048 `tick(now)`
- L9051 `macroCard(key,name,color)`
- L9052 `renderToday()`
- L9076 `renderBio()`
- L9101 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L9103 constante `HOME`
- L9105 `coachCandidates()`
- L9111 `coachIdeas(t,g,ref,meal)`
- L9130 `coachQuickAdd(key)`
- L9138 `renderCoach()`
- L9160 `coachPrompt()`
- L9169 `nutrientDetailStandard(key)`
- L9184 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L9190 `upgradeTo12(s,o)`
- L9195 `benfotiamineTotals(entries=effectiveEntries()`
- L9204 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L9206 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L9218 `microStat(m,t=totals()`
- L9223 `metric(m,t=totals()`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L9230 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L9231 `ratioInfo(key,t=totals()`
- L9270 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L9287 constante `RATIO_ENDS`
- L9289 `ratioZones(i)` — v68: cada equilibrio tiene una zona «aceptable» (ni verde ni mala) y su meta visible en la tarjeta.
- L9297 `ratioTone(i)`
- L9302 constante `NEAR_HEAD`
- L9303 `ratioBar(i,big=false)`
- L9312 `ratioNeedBase(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L9330 `needHTML(i,t)`
- L9331 `ratioNeed(i,t=totals()`
- L9335 `adBalance(t=totals()`
- L9362 `zncuSuppKey()`
- L9363 `zncuSuppCfg()`
- L9385 `zncuDoseLabel(zn,cu)`
- L9388 `hasZncuSupp(d=day()`
- L9393 `toggleZncuSupp()`
- L9413 `openZncuConfig()`
- L9419 `renderRatios()`
- L9430 `ratioDetail(key)`
- L9447 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L9464 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L9479 `renderMicroMap(t=totals()`
- L9492 `nutrientDetailForDay(key)`
- L9497 `editTargetsForm()`
- L9507 `mealData()`
- L9512 `renderMealSegments()`
- L9520 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L9555 constante `FAT_KEYS`
- L9557 `fatData(entries=effectiveEntries()`
- L9563 `energyData(entries=effectiveEntries()`
- L9567 `segmentedBar(items,total,attr)`
- L9571 `renderMealChart()`
- L9576 `renderFat()`
- L9584 `fatDetail(key)`
- L9589 `energyDetail(key)`
- L9596 `portionCandidates(q='')`
- L9601 `openPortion()`
- L9614 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L9629 `templates()`
- L9633 `renderExtra()`
- L9644 `updateExtra(reset=true)`
- L9656 `addExtra(id,amount)`
- L9672 `shakePreview()`
- L9673 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L9688 constante `LENS`
- L9694 `lensKey(key)`
- L9695 `lensHTML(key)`
- L9699 `appendLens(key)`
- L9708 `weekDates()`

### IA en la página: conexión directa o por servidor

- L9718 constante `MEAL_WORD`
- L9719 `mealOfWord(w)`
- L9720 `mealFromText(raw,fallback)`
- L9724 `canonMeal(v,fallback)`
- L9732 `localMeal(raw,meal)`
- L9738 constante `AI_FALLBACK`
- L9739 constante `GEMINI_DEFAULTS`
- L9740 constante `GROQ_DEFAULTS`
- L9741 `aiTaskProfile(task,hasImg=false)`
- L9748 `geminiThinkLevel(model,want)`
- L9754 `supportsGeminiTemp(model)`
- L9755 `readSSE(res,onEvent)`
- L9774 `applyAIConfig(raw)`
- L9800 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L9801 `callGemini(model,key,prompt,img,signal,opts={})`
- L9847 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), Groq (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L9855 `aiProv(m=$('ai-mode')`
- L9856 `aiBase(mode)`
- L9865 `chatHeaders(mode,key)`
- L9872 `callChat(mode,model,key,prompt,img,signal,opts={})` — ChatGPT, Claude, Groq, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L9926 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L9941 constante `OLD_GEMINI_RE`
- L9942 constante `MODEL_PREF`
- L9943 `pickModel(ids,mode=$('ai-mode')`
- L9957 `ensureModel(st)`
- L9973 `syncProvider()`
- L9992 `requestAI(prompt,img,signal,modelOverride='',onStep=null,opts={})`
- L10029 constante `AI_PREF`
- L10030 `aiConnected()`
- L10031 `syncAI()`
- L10033 `saveAIPrefs()`
- L10034 `loadAIPrefs()`
- L10035 `openAISetup()`
- L10042 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L10049 constante `MACROS`
- L10051 `cleanGoals(o,fallback)`
- L10056 `cleanCompare(o={})`
- L10060 `snapshotDay(d,reference='saved')`
- L10065 `upgradeTo17(s,o)`
- L10070 `entriesFor(d,source=weekSource)`
- L10074 `dayRow(dt,source=weekSource)`
- L10078 `goalsFor(dt)`
- L10084 `metricValue(r,key)`
- L10090 `targetOf(dt,key)`
- L10094 `weekSummary()`
- L10098 `aggregate(key,summary=weekSummary()`
- L10102 `tone(pct,mode='macro')`
- L10109 `pctText(a)`
- L10110 `weekProgress(a,color)`
- L10111 `renderWeekMicros(s)`
- L10123 `ratioAggregate(s,num,den)`
- L10127 `renderWeekRatios(s)`
- L10133 `renderWeekTable(s)`
- L10134 `weeklyDetail(key,oneDate=null)`
- L10143 `weekRatioDetail(key)`
- L10151 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L10157 `openDay(dt)`
- L10195 `withDayGoals(fn)`
- L10200 `renderMicros()`
- L10201 `nutrientDetail(key)`
- L10202 `editTargets()`
- L10203 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L10213 `summaryFor(start)`
- L10217 `ringSVG(pct,color,marker)`
- L10219 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L10223 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L10240 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L10241 `macroTone(p)`
- L10242 `dayMacroPct(dt,k)`
- L10243 `renderWeekly()`
- L10266 `weekDetail(dt,picked)`
- L10274 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L10284 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L10290 `sparkline(pts)`
- L10296 `renderCalendar()`
- L10313 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L10314 `splitMeals(raw)`
- L10324 `localDay(raw,fallback)`
- L10331 `promptDay(raw,fallback)`
- L10332 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L10371 `parseCsv(text)`
- L10386 `hevyDate(value,format='auto')`
- L10403 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L10418 constante `GYM_APPS`
- L10420 `gymSig(headers)`
- L10421 `gymApp(headers)`
- L10422 `hevyMapping()`
- L10423 `gymSaved()`
- L10424 `renderMapping(parsed)`
- L10441 `optionalNum(v,min=0,max=1e7)`
- L10446 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L10453 `buildHevy(parsed,map)`
- L10487 `cleanWorkout(s)`
- L10494 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L10509 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L10510 constante `GP_ALIAS`
- L10520 `gpNorm(s)`
- L10521 `gpKey(name)`
- L10525 `gpF(n,d=0)`
- L10526 `gpDate(d,opt)`
- L10527 `gpMonday(d)`
- L10528 constante `GP_GROUPS`
- L10543 constante `GP_COLORS`
- L10544 `gpGroup(name)`
- L10545 `gpWorkSets(s)`
- L10546 `gpModel()`
- L10570 `gpSessionMetrics(e,sets)`
- L10585 constante `GP_METRICS`
- L10590 `gpMetricsFor(e)`
- L10591 `gpRangeHist(e)`
- L10592 `gpPRs(model)`
- L10615 `gpStatus(e)`
- L10633 `gpNext(e)`
- L10641 `gpChart(e)`
- L10669 `gpPointDetail(e)`
- L10675 `gpRepTable(e)`
- L10682 `gpKpis(model)`
- L10691 `gpWeekData(model,w)` — Datos de una semana de gimnasio (series por músculo y sesiones).
- L10696 `gpWeekLabel(w,short)`
- L10697 `gpWeekly(model)`
- L10716 `gpMuscles(model)`
- L10724 `gpHeat(model)` — v69: «Constancia» — mapa de días entrenados (como antes), con días de la semana, meses, intensidad y detalle al tocar.
- L10744 `gpExList(model)`
- L10751 `gpExDetail(model)`
- L10764 `gpDayFood(dt)`
- L10765 `gpNutrition(model)`
- L10772 `gpRecentPRs(model)`
- L10776 `gpSessions(model)`
- L10782 `gpSessionModal(id)`
- L10793 `gpWeekModal(w)`
- L10800 `gpSelect(key)`
- L10801 `gpClick(e)`
- L10817 `renderGym()`
- L10837 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L10846 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L10852 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L10877 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L10881 `showHelp()`
- L10885 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L10887 `markBackup()`
- L10891 `exportJSON()`
- L10896 `drawBackupReminder()`
- L10906 `applyDensity()`
- L10918 `syncDayComplete()`
- L10921 `drawMeals()` — Comidas del día de un vistazo.
- L10929 `filterLog()` — Buscador de Registro.
- L10942 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L10948 `recentFoods()`
- L10953 `quickChip(e,fav)`
- L10971 `drawQuickFoods()`
- L11000 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L11004 `toggleAddPanel(id)`
- L11017 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L11028 `pasteMessage(text,ok)`
- L11036 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L11047 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L11058 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L11064 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L11085 `storableState()`

### Render único: actualiza toda la página

- L11094 `nearView(el)`
- L11096 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L11101 `scheduleLazyRender()`
- L11105 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L11142 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L11143 constante `REF_TABLE`
- L11150 `refTargets(mode)`
- L11151 `syncMicroMode()`
- L11164 `mealByHour(h=new Date()`
- L11171 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L11182 `dataSummary(s)`
- L11186 `confirmImport(next,name)`
- L11193 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L11199 `checkUpdate()`
- L11204 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L11219 constante `GAP_PREFER`
- L11220 constante `GAP_SKIP`
- L11221 constante `GAP_UNIT`
- L11222 `gapQty(f,x)`
- L11223 `gapFoods(key,gap,ctx)`
- L11242 `weekSources(key,sum)`
- L11248 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L11261 `gapRow(x,open,meal,sum,ctx)`
- L11277 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L11302 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L11303 `isFemale(s=state)`
- L11304 `sexLabel(s=state)`
- L11305 `sexBadge(sex)`
- L11307 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L11308 constante `OPT_FEMALE`
- L11319 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba; A (1.500 µg = 5.000 UI) y D (50 µg = 2.000 UI) mantienen A:D en zona verde (2,5:1).
- L11320 `applySexOpt(sex)`
- L11322 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L11327 `cleanPreset(p,fb)`
- L11331 `dayNamesFor(types)`
- L11333 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L11343 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L11351 `profV()`
- L11352 `isTrainDay(i)`
- L11353 `activityName(i)`
- L11354 `dayFaf(i)`
- L11355 `presetDesc(cfg,shake)`
- L11359 `profileDescription()`
- L11367 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L11369 `wizCatalog()`
- L11370 `wizOpen(opts={})`
- L11386 `wizTitle()`
- L11387 `wizPaint(sameStep=true)`
- L11396 `wizSync()`
- L11415 `wizFoodOptions()`
- L11418 `wizPresetSummary(cfg,whey)`
- L11423 `wizPresetHTML(kind)`
- L11431 `wizPreview()`
- L11442 `wizLiveHTML()`
- L11446 `wizHTML()`
- L11492 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L11590 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L11591 constante `SUPP_CATALOG`
- L11616 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L11617 constante `PEAT_BREAKFAST`
- L11618 constante `PEAT_SHAKE`
- L11620 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L11627 `benfoUser()`
- L11629 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L11645 `ico(n)`
- L11647 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L11656 `showTour(i=0)`
- L11668 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L11669 `hubAction(v)`
- L11677 constante `FB_CATS` — Envíos anónimos directos al buzón de BioPeat (sin cuentas ni datos personales).
- L11679 `openFeedback()`
- L11683 `feedbackData()`
- L11690 `feedbackText()`
- L11691 `sendFeedback()`
- L11711 `shareFeedback()`
- L11728 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L11735 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L11743 constante `I18N_EN`

### v59: idioma (español / inglés)

- L13656 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L13657 constante `WD_EN`
- L13658 `trOne(s)`
- L13666 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L13667 constante `ES_FOOD_GYM`
- L13704 `trFood(s)`
- L13716 constante `TR_TPL`
- L13757 `trLower(s)`
- L13758 `trTpl(s,attr)`
- L13759 constante `FOOD_SEL`
- L13760 `trText(s,attr=false)`
- L13770 `trNode(n)`
- L13789 `trEl(el)`
- L13802 `trTree(root)`
- L13811 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L13825 `flushTr()`
- L13826 `syncTrObserver()`
- L13830 `setLang(l,quiet)`
- L13844 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter + Worker agregados), solo en la web publicada

- L13853 constante `GC_CODE`
- L13854 `pingAnalytics(extra={})`
- L13870 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L13882 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L13883 `packMove()`
- L13891 `unpackMove(code)`
- L13902 `moveData()`
- L13912 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L13918 `checkMove(code)`
- L13937 `aiFrameworkLines()` — v69: marco de referencia del informe para IA. Así cualquier IA, aunque no conozca la app ni al usuario, sabe con qué comparar.

### Arranque

