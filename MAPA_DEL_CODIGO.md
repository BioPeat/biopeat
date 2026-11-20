# MAPA DEL CÓDIGO · BioPeat v74 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (923 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-6359; todo el JavaScript en `<script id="app">` (desde la línea 6360).

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

- L6423 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L6424 constante `AZUCAR_N`
- L6425 constante `USDA_N`
- L6431 constante `FOODS`
- L6433 constante `BASE_FAT_FIX`
- L6437 constante `REF_COLS` — Base de referencia verificada (USDA FoodData Central / BEDCA, por 100 g o 100 ml comestibles).
- L6438 constante `REF_RAW`
- L6600 constante `REF_MAP`
- L6601 constante `REF_CACHE`
- L6602 `refNutrients(id)`
- L6610 `findRef(text,strict=false)`
- L6632 `refCatalogCompact()`
- L6633 `fromRef(id,amount,meal,note='',srcText='')`
- L6638 constante `EXTRA`
- L6639 constante `KEYS`
- L6641 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L6643 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L6647 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6648 constante `OPT`
- L6669 constante `LIMIT`
- L6670 `optInfo(k,goal)`
- L6677 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6685 `optLine(k,goal,unit)`
- L6692 `optRefHTML(k,goal,unit)`
- L6694 constante `DAYS`
- L6695 constante `FAF`
- L6697 constante `LOC`
- L6701 `number(v,min=0,max=1e6)`
- L6707 `decimalInputs(root=document)`
- L6708 `localDate(d=new Date()`
- L6709 `validDate(s)`
- L6714 `shift(s,n)`
- L6723 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6725 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6731 constante `DAY_TYPES`
- L6732 constante `NEW_V54`
- L6736 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6739 `bmr()` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6745 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6767 `cleanNutrients(o,required=false)`
- L6779 `cleanEntry(e)`
- L6784 `cleanPlan(p)`
- L6788 `planEntry(p)`
- L6797 `seedPlan(d,whichDate)`
- L6801 `ensureDay(d=date)`
- L6808 `effectiveEntries(d=day()`
- L6809 constante `SALTED_IDS`
- L6810 constante `SWEET_RE`
- L6811 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6829 `inferredNutrients(e)`
- L6870 `totals(entries=effectiveEntries()`
- L6879 `change(fn,message='Guardado')`
- L6883 `undo()`
- L6890 `toast(text,canUndo=false)`
- L6898 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6899 `onClick(fn)`
- L6901 `attempt(fn)`
- L6905 `modal(title,body)`
- L6914 `modalRestore()`
- L6924 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6925 `modalBack()`
- L6926 `goDate(d)`
- L6933 `renderHeader()`
- L6946 `renderRows(entries)`
- L6950 `entryValues(e)`
- L6951 `renderLog()`
- L6958 `fromFood(id,amount,meal)`
- L6964 `pantryId(name)`
- L6966 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6972 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6981 `recipe(kind)`
- L6988 `summary(entries)`
- L6992 `renderPresetInfo()`
- L7005 `stripCode(raw)`
- L7011 `sanitizeNutrients(o,grams=100,fallbackRefId='')`
- L7038 `parseBIO(raw,meal=$('meal-select')`
- L7050 `parseSmart(raw)`
- L7054 constante `COUNT`
- L7055 constante `UNIT_RE`
- L7097 `offToNutrients(nut={},fallbackName='')` — Open Food Facts (gratis, sin clave, CORS nativo): consulta por código de barras o texto.
- L7118 `lookupOFFBarcode(code,signal,ms=3200)`
- L7133 `searchOFF(query,signal,ms=4500)`
- L7150 `openProductSearch()`
- L7175 `nutrientFields(n,prefix='n_')`
- L7176 `readNutrients(form,prefix='n_')`
- L7181 `editEntry(id)`
- L7190 `editFood(id,pending=null)`
- L7195 `usageStats(days=90)`
- L7201 `renderFoods()`
- L7209 `nutrientSources(key)`
- L7216 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L7217 `suppSlot(meal)`
- L7218 `renderSupps()`
- L7233 `editPlan(id)`
- L7240 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L7260 `makePrompt(meal='Comida',note='')`
- L7265 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L7269 `pantryCompact()`
- L7273 constante `MEAL_AI_SCHEMA`
- L7313 `mealSystemPrompt(usePhoto)`
- L7329 `hydrateAIItems(rawItems,fallback,usePhoto,aiModel,signal)`
- L7372 `photoPrompt(meal,note)`
- L7375 `resetPhoto()`
- L7386 `openPhoto()`
- L7392 `shrinkPhoto(file)`
- L7395 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L7421 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L7428 `cleanFood(id,f)`
- L7432 `migrateBase(o)`
- L7451 `download(name,text,type)`
- L7460 `portable()`
- L7501 `syncAppIcons()`
- L7509 `downloadAppIcons()`
- L7546 constante `PROFILES_KEY`
- L7548 `ensureProfilesStore()`
- L7568 `resetProfileSessionUI()`
- L7575 `saveProfilesStore(st)`
- L7584 `syncCurrentProfileToStore(rawStr)`
- L7590 `activeProfileName()`
- L7594 `renderProfilesList()`
- L7636 `switchProfile(id)`
- L7658 `deleteProfileById(id)`
- L7683 `refreshDrawerSummary()`
- L7700 `toggleLeftDrawer(force)`
- L7715 `buildAIExportText(rangeOverride)`
- L7966 `copyAIExport()`
- L7980 `downloadAIExport()`
- L7989 `renderDrawerChat()`
- L8008 `buildDrawerChatContext()`
- L8045 `buildDrawerChatPrompt(question)`
- L8057 `askDrawerAI(rawQuestion)`
- L8146 `storageStatus()`
- L8152 `idbReadWrite(mode,value,key='current')`
- L8153 `openDB()`
- L8154 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L8167 `setQuantity(id,value,msg='Cantidad actualizada')`
- L8171 `niceStep(v)`
- L8172 `stepQuantity(id,dir)`
- L8226 `renderAppInfo()`
- L8241 `init()`
- L8269 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L8271 `setNav(v)`
- L8276 `go(v,focus)`
- L8287 constante `THEME_KEY`
- L8288 constante `SUN_SVG`
- L8289 constante `MOON_SVG`
- L8291 `syncThemeUI()`
- L8303 `toggleTheme()`
- L8312 `syncLogoTheme()`
- L8323 `applyMenuBtnState()`
- L8346 `syncDatePill()`
- L8359 `clampBtnPos(el,x,y)`
- L8369 `bindDraggableBtn(el,storeKey)`
- L8454 `bindDrawerGestures()`
- L8491 `animateValue(el,to,suffix='%',digits=0)`
- L8500 `tick(now)`
- L8503 `macroCard(key,name,color)`
- L8504 `renderToday()`
- L8527 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L8529 constante `HOME`
- L8531 `coachCandidates()`
- L8537 `coachIdeas(t,g,ref,meal)`
- L8550 `renderCoach()`
- L8570 `coachPrompt()`
- L8579 `nutrientDetailStandard(key)`
- L8593 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L8599 `upgradeTo12(s,o)`
- L8604 `benfotiamineTotals(entries=effectiveEntries()`
- L8613 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L8615 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L8627 `microStat(m,t=totals()`
- L8632 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L8640 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L8641 `ratioInfo(key,t=totals()`
- L8680 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L8697 constante `RATIO_ENDS`
- L8699 `ratioZones(i)` — v68: cada equilibrio tiene una zona «aceptable» (ni verde ni mala) y su meta visible en la tarjeta.
- L8707 `ratioTone(i)`
- L8712 constante `NEAR_HEAD`
- L8713 `ratioBar(i,big=false)`
- L8722 `ratioNeedBase(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L8740 `needHTML(i,t)`
- L8741 `ratioNeed(i,t=totals()`
- L8745 `adBalance(t=totals()`
- L8772 `zncuSuppKey()`
- L8773 `zncuSuppCfg()`
- L8795 `zncuDoseLabel(zn,cu)`
- L8798 `hasZncuSupp(d=day()`
- L8803 `toggleZncuSupp()`
- L8823 `openZncuConfig()`
- L8829 `renderRatios()`
- L8840 `ratioDetail(key)`
- L8857 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L8874 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L8889 `renderMicroMap()`
- L8893 `nutrientDetailForDay(key)`
- L8898 `editTargetsForm()`
- L8908 `mealData()`
- L8913 `renderMealSegments()`
- L8921 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L8956 constante `FAT_KEYS`
- L8958 `fatData(entries=effectiveEntries()`
- L8964 `energyData(entries=effectiveEntries()`
- L8968 `segmentedBar(items,total,attr)`
- L8972 `renderMealChart()`
- L8977 `renderFat()`
- L8985 `fatDetail(key)`
- L8990 `energyDetail(key)`
- L8997 `portionCandidates(q='')`
- L9002 `openPortion()`
- L9015 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L9030 `templates()`
- L9034 `renderExtra()`
- L9045 `updateExtra(reset=true)`
- L9057 `addExtra(id,amount)`
- L9073 `shakePreview()`
- L9074 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L9089 constante `LENS`
- L9095 `lensKey(key)`
- L9096 `lensHTML(key)`
- L9100 `appendLens(key)`
- L9109 `weekDates()`

### IA en la página: conexión directa o por servidor

- L9119 constante `MEAL_WORD`
- L9120 `mealOfWord(w)`
- L9121 `mealFromText(raw,fallback)`
- L9125 `canonMeal(v,fallback)`
- L9133 `localMeal(raw,meal)`
- L9139 constante `AI_FALLBACK`
- L9140 constante `GEMINI_DEFAULTS`
- L9141 constante `GROQ_DEFAULTS`
- L9142 `aiTaskProfile(task,hasImg=false)`
- L9149 `geminiThinkLevel(model,want)`
- L9155 `supportsGeminiTemp(model)`
- L9156 `readSSE(res,onEvent)`
- L9175 `applyAIConfig(raw)`
- L9201 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L9202 `callGemini(model,key,prompt,img,signal,opts={})`
- L9248 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), Groq (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L9256 `aiProv(m=$('ai-mode')`
- L9257 `aiBase(mode)`
- L9266 `chatHeaders(mode,key)`
- L9273 `callChat(mode,model,key,prompt,img,signal,opts={})` — ChatGPT, Claude, Groq, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L9327 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L9342 constante `MODEL_PREF`
- L9343 `pickModel(ids,mode=$('ai-mode')`
- L9357 `ensureModel(st)`
- L9373 `syncProvider()`
- L9392 `requestAI(prompt,img,signal,modelOverride='',onStep=null,opts={})`
- L9428 constante `AI_PREF`
- L9429 `aiConnected()`
- L9430 `syncAI()`
- L9432 `saveAIPrefs()`
- L9433 `loadAIPrefs()`
- L9434 `openAISetup()`
- L9441 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L9448 constante `MACROS`
- L9450 `cleanGoals(o,fallback)`
- L9455 `cleanCompare(o={})`
- L9459 `snapshotDay(d,reference='saved')`
- L9464 `upgradeTo17(s,o)`
- L9469 `entriesFor(d,source=weekSource)`
- L9473 `dayRow(dt,source=weekSource)`
- L9477 `goalsFor(dt)`
- L9483 `metricValue(r,key)`
- L9489 `targetOf(dt,key)`
- L9493 `weekSummary()`
- L9497 `aggregate(key,summary=weekSummary()`
- L9501 `tone(pct,mode='macro')`
- L9508 `pctText(a)`
- L9509 `weekProgress(a,color)`
- L9510 `renderWeekMicros(s)`
- L9522 `ratioAggregate(s,num,den)`
- L9526 `renderWeekRatios(s)`
- L9532 `renderWeekTable(s)`
- L9533 `weeklyDetail(key,oneDate=null)`
- L9542 `weekRatioDetail(key)`
- L9550 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L9556 `openDay(dt)`
- L9594 `withDayGoals(fn)`
- L9599 `renderMicros()`
- L9600 `nutrientDetail(key)`
- L9601 `editTargets()`
- L9602 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L9612 `summaryFor(start)`
- L9616 `ringSVG(pct,color,marker)`
- L9618 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L9622 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L9639 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L9640 `macroTone(p)`
- L9641 `dayMacroPct(dt,k)`
- L9642 `renderWeekly()`
- L9665 `weekDetail(dt,picked)`
- L9673 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L9683 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L9689 `sparkline(pts)`
- L9695 `renderCalendar()`
- L9712 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L9713 `splitMeals(raw)`
- L9723 `localDay(raw,fallback)`
- L9730 `promptDay(raw,fallback)`
- L9731 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L9770 `parseCsv(text)`
- L9785 `hevyDate(value,format='auto')`
- L9802 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L9817 constante `GYM_APPS`
- L9819 `gymSig(headers)`
- L9820 `gymApp(headers)`
- L9821 `hevyMapping()`
- L9822 `gymSaved()`
- L9823 `renderMapping(parsed)`
- L9840 `optionalNum(v,min=0,max=1e7)`
- L9845 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L9852 `buildHevy(parsed,map)`
- L9886 `cleanWorkout(s)`
- L9893 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L9908 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L9909 constante `GP_ALIAS`
- L9919 `gpNorm(s)`
- L9920 `gpKey(name)`
- L9924 `gpF(n,d=0)`
- L9925 `gpDate(d,opt)`
- L9926 `gpMonday(d)`
- L9927 constante `GP_GROUPS`
- L9942 constante `GP_COLORS`
- L9943 `gpGroup(name)`
- L9944 `gpWorkSets(s)`
- L9945 `gpModel()`
- L9969 `gpSessionMetrics(e,sets)`
- L9984 constante `GP_METRICS`
- L9989 `gpMetricsFor(e)`
- L9990 `gpRangeHist(e)`
- L9991 `gpPRs(model)`
- L10014 `gpStatus(e)`
- L10032 `gpNext(e)`
- L10040 `gpChart(e)`
- L10068 `gpPointDetail(e)`
- L10074 `gpRepTable(e)`
- L10081 `gpKpis(model)`
- L10090 `gpWeekData(model,w)` — Datos de una semana de gimnasio (series por músculo y sesiones).
- L10095 `gpWeekLabel(w,short)`
- L10096 `gpWeekly(model)`
- L10115 `gpMuscles(model)`
- L10123 `gpHeat(model)` — v69: «Constancia» — mapa de días entrenados (como antes), con días de la semana, meses, intensidad y detalle al tocar.
- L10143 `gpExList(model)`
- L10150 `gpExDetail(model)`
- L10163 `gpDayFood(dt)`
- L10164 `gpNutrition(model)`
- L10171 `gpRecentPRs(model)`
- L10175 `gpSessions(model)`
- L10181 `gpSessionModal(id)`
- L10192 `gpWeekModal(w)`
- L10199 `gpSelect(key)`
- L10200 `gpClick(e)`
- L10216 `renderGym()`
- L10236 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L10245 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L10251 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L10276 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L10280 `showHelp()`
- L10284 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L10286 `markBackup()`
- L10290 `exportJSON()`
- L10295 `drawBackupReminder()`
- L10305 `applyDensity()`
- L10317 `syncDayComplete()`
- L10320 `drawMeals()` — Comidas del día de un vistazo.
- L10328 `filterLog()` — Buscador de Registro.
- L10341 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L10347 `recentFoods()`
- L10352 `quickChip(e,fav)`
- L10370 `drawQuickFoods()`
- L10399 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L10403 `toggleAddPanel(id)`
- L10416 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L10427 `pasteMessage(text,ok)`
- L10435 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L10446 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L10457 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L10463 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L10484 `storableState()`

### Render único: actualiza toda la página

- L10492 `nearView(el)`
- L10494 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L10498 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L10529 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L10530 constante `REF_TABLE`
- L10537 `refTargets(mode)`
- L10538 `syncMicroMode()`
- L10551 `mealByHour(h=new Date()`
- L10558 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L10569 `dataSummary(s)`
- L10573 `confirmImport(next,name)`
- L10580 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L10586 `checkUpdate()`
- L10591 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L10606 constante `GAP_PREFER`
- L10607 constante `GAP_SKIP`
- L10608 constante `GAP_UNIT`
- L10609 `gapQty(f,x)`
- L10610 `gapFoods(key,gap,ctx)`
- L10629 `weekSources(key,sum)`
- L10635 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L10648 `gapRow(x,open,meal,sum,ctx)`
- L10664 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L10689 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L10690 `isFemale(s=state)`
- L10691 `sexLabel(s=state)`
- L10692 `sexBadge(sex)`
- L10694 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L10695 constante `OPT_FEMALE`
- L10706 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba.
- L10707 `applySexOpt(sex)`
- L10709 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L10714 `cleanPreset(p,fb)`
- L10718 `dayNamesFor(types)`
- L10720 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L10730 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L10738 `profV()`
- L10739 `isTrainDay(i)`
- L10740 `activityName(i)`
- L10741 `dayFaf(i)`
- L10742 `presetDesc(cfg,shake)`
- L10746 `profileDescription()`
- L10754 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L10756 `wizCatalog()`
- L10757 `wizOpen(opts={})`
- L10772 `wizTitle()`
- L10773 `wizPaint(sameStep=true)`
- L10782 `wizSync()`
- L10795 `wizFoodOptions()`
- L10798 `wizPresetSummary(cfg,whey)`
- L10803 `wizPresetHTML(kind)`
- L10811 `wizPreview()`
- L10822 `wizHTML()`
- L10863 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L10947 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L10948 constante `SUPP_CATALOG`
- L10970 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L10971 constante `PEAT_BREAKFAST`
- L10972 constante `PEAT_SHAKE`
- L10974 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L10981 `benfoUser()`
- L10983 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L10999 `ico(n)`
- L11001 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L11010 `showTour(i=0)`
- L11022 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L11023 `hubAction(v)`
- L11031 constante `FORM_URL` — Llegan solas a una hoja de Google (formulario del creador de la app). Sin cuentas ni datos personales.
- L11032 constante `FORM_FIELDS`
- L11033 constante `FB_CATS`
- L11035 `openFeedback()`
- L11039 `feedbackData()`
- L11046 `feedbackText()`
- L11047 `sendFeedback()`
- L11060 `shareFeedback()`
- L11077 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L11084 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L11092 constante `I18N_EN`

### v59: idioma (español / inglés)

- L12810 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L12811 constante `WD_EN`
- L12812 `trOne(s)`
- L12820 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L12821 constante `ES_FOOD_GYM`
- L12858 `trFood(s)`
- L12870 constante `TR_TPL`
- L12909 `trLower(s)`
- L12910 `trTpl(s,attr)`
- L12911 constante `FOOD_SEL`
- L12912 `trText(s,attr=false)`
- L12922 `trNode(n)`
- L12941 `trEl(el)`
- L12954 `trTree(root)`
- L12963 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L12977 `setLang(l,quiet)`
- L12990 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter), solo en la web publicada

- L12999 constante `GC_CODE`
- L13000 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L13010 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L13011 `packMove()`
- L13019 `unpackMove(code)`
- L13028 `moveData()`
- L13038 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L13044 `checkMove(code)`
- L13063 `aiFrameworkLines()` — v69: marco de referencia del informe para IA. Así cualquier IA, aunque no conozca la app ni al usuario, sabe con qué comparar.

### Arranque

