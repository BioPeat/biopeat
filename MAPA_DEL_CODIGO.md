# MAPA DEL CÓDIGO · BioPeat v75 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (924 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-6359; todo el JavaScript en `<script id="app">` (desde la línea 6360).

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

- L6424 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L6425 constante `AZUCAR_N`
- L6426 constante `USDA_N`
- L6432 constante `FOODS`
- L6434 constante `BASE_FAT_FIX`
- L6438 constante `REF_COLS` — Base de referencia verificada (USDA FoodData Central / BEDCA, por 100 g o 100 ml comestibles).
- L6439 constante `REF_RAW`
- L6601 constante `REF_MAP`
- L6602 constante `REF_CACHE`
- L6603 `refNutrients(id)`
- L6611 `findRef(text,strict=false)`
- L6633 `refCatalogCompact()`
- L6634 `fromRef(id,amount,meal,note='',srcText='')`
- L6639 constante `EXTRA`
- L6640 constante `KEYS`
- L6642 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L6644 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L6648 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6649 constante `OPT`
- L6670 constante `LIMIT`
- L6671 `optInfo(k,goal)`
- L6678 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6686 `optLine(k,goal,unit)`
- L6693 `optRefHTML(k,goal,unit)`
- L6695 constante `DAYS`
- L6696 constante `FAF`
- L6698 constante `LOC`
- L6702 `number(v,min=0,max=1e6)`
- L6708 `decimalInputs(root=document)`
- L6709 `localDate(d=new Date()`
- L6710 `validDate(s)`
- L6715 `shift(s,n)`
- L6724 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6726 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6732 constante `DAY_TYPES`
- L6733 constante `NEW_V54`
- L6737 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6740 `bmr()` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6746 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6768 `cleanNutrients(o,required=false)`
- L6780 `cleanEntry(e)`
- L6785 `cleanPlan(p)`
- L6789 `planEntry(p)`
- L6798 `seedPlan(d,whichDate)`
- L6802 `ensureDay(d=date)`
- L6809 `effectiveEntries(d=day()`
- L6810 constante `SALTED_IDS`
- L6811 constante `SWEET_RE`
- L6812 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6830 `inferredNutrients(e)`
- L6871 `totals(entries=effectiveEntries()`
- L6880 `change(fn,message='Guardado')`
- L6884 `undo()`
- L6891 `toast(text,canUndo=false)`
- L6899 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6900 `onClick(fn)`
- L6902 `attempt(fn)`
- L6906 `modal(title,body)`
- L6915 `modalRestore()`
- L6925 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6926 `modalBack()`
- L6927 `goDate(d)`
- L6934 `renderHeader()`
- L6947 `renderRows(entries)`
- L6951 `entryValues(e)`
- L6952 `renderLog()`
- L6959 `fromFood(id,amount,meal)`
- L6965 `pantryId(name)`
- L6967 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6973 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6982 `recipe(kind)`
- L6989 `summary(entries)`
- L6993 `renderPresetInfo()`
- L7006 `stripCode(raw)`
- L7012 `sanitizeNutrients(o,grams=100,fallbackRefId='')`
- L7039 `parseBIO(raw,meal=$('meal-select')`
- L7051 `parseSmart(raw)`
- L7055 constante `COUNT`
- L7056 constante `UNIT_RE`
- L7098 `offToNutrients(nut={},fallbackName='')` — Open Food Facts (gratis, sin clave, CORS nativo): consulta por código de barras o texto.
- L7119 `lookupOFFBarcode(code,signal,ms=3200)`
- L7134 `searchOFF(query,signal,ms=4500)`
- L7151 `openProductSearch()`
- L7176 `nutrientFields(n,prefix='n_')`
- L7177 `readNutrients(form,prefix='n_')`
- L7182 `editEntry(id)`
- L7191 `editFood(id,pending=null)`
- L7196 `usageStats(days=90)`
- L7202 `renderFoods()`
- L7210 `nutrientSources(key)`
- L7217 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L7218 `suppSlot(meal)`
- L7219 `renderSupps()`
- L7234 `editPlan(id)`
- L7241 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L7261 `makePrompt(meal='Comida',note='')`
- L7266 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L7270 `pantryCompact()`
- L7274 constante `MEAL_AI_SCHEMA`
- L7314 `mealSystemPrompt(usePhoto)`
- L7330 `hydrateAIItems(rawItems,fallback,usePhoto,aiModel,signal)`
- L7373 `photoPrompt(meal,note)`
- L7376 `resetPhoto()`
- L7387 `openPhoto()`
- L7393 `shrinkPhoto(file)`
- L7396 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L7422 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L7429 `cleanFood(id,f)`
- L7433 `migrateBase(o)`
- L7452 `download(name,text,type)`
- L7461 `portable()`
- L7502 `syncAppIcons()`
- L7510 `downloadAppIcons()`
- L7547 constante `PROFILES_KEY`
- L7549 `ensureProfilesStore()`
- L7569 `resetProfileSessionUI()`
- L7576 `saveProfilesStore(st)`
- L7585 `syncCurrentProfileToStore(rawStr)`
- L7591 `activeProfileName()`
- L7595 `renderProfilesList()`
- L7637 `switchProfile(id)`
- L7659 `deleteProfileById(id)`
- L7684 `refreshDrawerSummary()`
- L7701 `toggleLeftDrawer(force)`
- L7716 `buildAIExportText(rangeOverride)`
- L7967 `copyAIExport()`
- L7981 `downloadAIExport()`
- L7990 `renderDrawerChat()`
- L8009 `buildDrawerChatContext()`
- L8046 `buildDrawerChatPrompt(question)`
- L8058 `askDrawerAI(rawQuestion)`
- L8147 `storageStatus()`
- L8153 `idbReadWrite(mode,value,key='current')`
- L8154 `openDB()`
- L8155 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L8168 `setQuantity(id,value,msg='Cantidad actualizada')`
- L8172 `niceStep(v)`
- L8173 `stepQuantity(id,dir)`
- L8227 `renderAppInfo()`
- L8242 `init()`
- L8270 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L8272 `setNav(v)`
- L8277 `go(v,focus)`
- L8288 constante `THEME_KEY`
- L8289 constante `SUN_SVG`
- L8290 constante `MOON_SVG`
- L8292 `syncThemeUI()`
- L8304 `toggleTheme()`
- L8313 `syncLogoTheme()`
- L8324 `applyMenuBtnState()`
- L8347 `syncDatePill()`
- L8360 `clampBtnPos(el,x,y)`
- L8370 `bindDraggableBtn(el,storeKey)`
- L8455 `bindDrawerGestures()`
- L8492 `animateValue(el,to,suffix='%',digits=0)`
- L8501 `tick(now)`
- L8504 `macroCard(key,name,color)`
- L8505 `renderToday()`
- L8528 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L8530 constante `HOME`
- L8532 `coachCandidates()`
- L8538 `coachIdeas(t,g,ref,meal)`
- L8551 `renderCoach()`
- L8571 `coachPrompt()`
- L8580 `nutrientDetailStandard(key)`
- L8594 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L8600 `upgradeTo12(s,o)`
- L8605 `benfotiamineTotals(entries=effectiveEntries()`
- L8614 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L8616 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L8628 `microStat(m,t=totals()`
- L8633 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L8641 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L8642 `ratioInfo(key,t=totals()`
- L8681 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L8698 constante `RATIO_ENDS`
- L8700 `ratioZones(i)` — v68: cada equilibrio tiene una zona «aceptable» (ni verde ni mala) y su meta visible en la tarjeta.
- L8708 `ratioTone(i)`
- L8713 constante `NEAR_HEAD`
- L8714 `ratioBar(i,big=false)`
- L8723 `ratioNeedBase(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L8741 `needHTML(i,t)`
- L8742 `ratioNeed(i,t=totals()`
- L8746 `adBalance(t=totals()`
- L8773 `zncuSuppKey()`
- L8774 `zncuSuppCfg()`
- L8796 `zncuDoseLabel(zn,cu)`
- L8799 `hasZncuSupp(d=day()`
- L8804 `toggleZncuSupp()`
- L8824 `openZncuConfig()`
- L8830 `renderRatios()`
- L8841 `ratioDetail(key)`
- L8858 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L8875 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L8890 `renderMicroMap()`
- L8894 `nutrientDetailForDay(key)`
- L8899 `editTargetsForm()`
- L8909 `mealData()`
- L8914 `renderMealSegments()`
- L8922 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L8957 constante `FAT_KEYS`
- L8959 `fatData(entries=effectiveEntries()`
- L8965 `energyData(entries=effectiveEntries()`
- L8969 `segmentedBar(items,total,attr)`
- L8973 `renderMealChart()`
- L8978 `renderFat()`
- L8986 `fatDetail(key)`
- L8991 `energyDetail(key)`
- L8998 `portionCandidates(q='')`
- L9003 `openPortion()`
- L9016 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L9031 `templates()`
- L9035 `renderExtra()`
- L9046 `updateExtra(reset=true)`
- L9058 `addExtra(id,amount)`
- L9074 `shakePreview()`
- L9075 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L9090 constante `LENS`
- L9096 `lensKey(key)`
- L9097 `lensHTML(key)`
- L9101 `appendLens(key)`
- L9110 `weekDates()`

### IA en la página: conexión directa o por servidor

- L9120 constante `MEAL_WORD`
- L9121 `mealOfWord(w)`
- L9122 `mealFromText(raw,fallback)`
- L9126 `canonMeal(v,fallback)`
- L9134 `localMeal(raw,meal)`
- L9140 constante `AI_FALLBACK`
- L9141 constante `GEMINI_DEFAULTS`
- L9142 constante `GROQ_DEFAULTS`
- L9143 `aiTaskProfile(task,hasImg=false)`
- L9150 `geminiThinkLevel(model,want)`
- L9156 `supportsGeminiTemp(model)`
- L9157 `readSSE(res,onEvent)`
- L9176 `applyAIConfig(raw)`
- L9202 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L9203 `callGemini(model,key,prompt,img,signal,opts={})`
- L9249 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), Groq (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L9257 `aiProv(m=$('ai-mode')`
- L9258 `aiBase(mode)`
- L9267 `chatHeaders(mode,key)`
- L9274 `callChat(mode,model,key,prompt,img,signal,opts={})` — ChatGPT, Claude, Groq, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L9328 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L9343 constante `OLD_GEMINI_RE`
- L9344 constante `MODEL_PREF`
- L9345 `pickModel(ids,mode=$('ai-mode')`
- L9359 `ensureModel(st)`
- L9375 `syncProvider()`
- L9394 `requestAI(prompt,img,signal,modelOverride='',onStep=null,opts={})`
- L9430 constante `AI_PREF`
- L9431 `aiConnected()`
- L9432 `syncAI()`
- L9434 `saveAIPrefs()`
- L9435 `loadAIPrefs()`
- L9436 `openAISetup()`
- L9443 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L9450 constante `MACROS`
- L9452 `cleanGoals(o,fallback)`
- L9457 `cleanCompare(o={})`
- L9461 `snapshotDay(d,reference='saved')`
- L9466 `upgradeTo17(s,o)`
- L9471 `entriesFor(d,source=weekSource)`
- L9475 `dayRow(dt,source=weekSource)`
- L9479 `goalsFor(dt)`
- L9485 `metricValue(r,key)`
- L9491 `targetOf(dt,key)`
- L9495 `weekSummary()`
- L9499 `aggregate(key,summary=weekSummary()`
- L9503 `tone(pct,mode='macro')`
- L9510 `pctText(a)`
- L9511 `weekProgress(a,color)`
- L9512 `renderWeekMicros(s)`
- L9524 `ratioAggregate(s,num,den)`
- L9528 `renderWeekRatios(s)`
- L9534 `renderWeekTable(s)`
- L9535 `weeklyDetail(key,oneDate=null)`
- L9544 `weekRatioDetail(key)`
- L9552 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L9558 `openDay(dt)`
- L9596 `withDayGoals(fn)`
- L9601 `renderMicros()`
- L9602 `nutrientDetail(key)`
- L9603 `editTargets()`
- L9604 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L9614 `summaryFor(start)`
- L9618 `ringSVG(pct,color,marker)`
- L9620 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L9624 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L9641 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L9642 `macroTone(p)`
- L9643 `dayMacroPct(dt,k)`
- L9644 `renderWeekly()`
- L9667 `weekDetail(dt,picked)`
- L9675 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L9685 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L9691 `sparkline(pts)`
- L9697 `renderCalendar()`
- L9714 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L9715 `splitMeals(raw)`
- L9725 `localDay(raw,fallback)`
- L9732 `promptDay(raw,fallback)`
- L9733 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L9772 `parseCsv(text)`
- L9787 `hevyDate(value,format='auto')`
- L9804 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L9819 constante `GYM_APPS`
- L9821 `gymSig(headers)`
- L9822 `gymApp(headers)`
- L9823 `hevyMapping()`
- L9824 `gymSaved()`
- L9825 `renderMapping(parsed)`
- L9842 `optionalNum(v,min=0,max=1e7)`
- L9847 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L9854 `buildHevy(parsed,map)`
- L9888 `cleanWorkout(s)`
- L9895 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L9910 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L9911 constante `GP_ALIAS`
- L9921 `gpNorm(s)`
- L9922 `gpKey(name)`
- L9926 `gpF(n,d=0)`
- L9927 `gpDate(d,opt)`
- L9928 `gpMonday(d)`
- L9929 constante `GP_GROUPS`
- L9944 constante `GP_COLORS`
- L9945 `gpGroup(name)`
- L9946 `gpWorkSets(s)`
- L9947 `gpModel()`
- L9971 `gpSessionMetrics(e,sets)`
- L9986 constante `GP_METRICS`
- L9991 `gpMetricsFor(e)`
- L9992 `gpRangeHist(e)`
- L9993 `gpPRs(model)`
- L10016 `gpStatus(e)`
- L10034 `gpNext(e)`
- L10042 `gpChart(e)`
- L10070 `gpPointDetail(e)`
- L10076 `gpRepTable(e)`
- L10083 `gpKpis(model)`
- L10092 `gpWeekData(model,w)` — Datos de una semana de gimnasio (series por músculo y sesiones).
- L10097 `gpWeekLabel(w,short)`
- L10098 `gpWeekly(model)`
- L10117 `gpMuscles(model)`
- L10125 `gpHeat(model)` — v69: «Constancia» — mapa de días entrenados (como antes), con días de la semana, meses, intensidad y detalle al tocar.
- L10145 `gpExList(model)`
- L10152 `gpExDetail(model)`
- L10165 `gpDayFood(dt)`
- L10166 `gpNutrition(model)`
- L10173 `gpRecentPRs(model)`
- L10177 `gpSessions(model)`
- L10183 `gpSessionModal(id)`
- L10194 `gpWeekModal(w)`
- L10201 `gpSelect(key)`
- L10202 `gpClick(e)`
- L10218 `renderGym()`
- L10238 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L10247 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L10253 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L10278 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L10282 `showHelp()`
- L10286 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L10288 `markBackup()`
- L10292 `exportJSON()`
- L10297 `drawBackupReminder()`
- L10307 `applyDensity()`
- L10319 `syncDayComplete()`
- L10322 `drawMeals()` — Comidas del día de un vistazo.
- L10330 `filterLog()` — Buscador de Registro.
- L10343 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L10349 `recentFoods()`
- L10354 `quickChip(e,fav)`
- L10372 `drawQuickFoods()`
- L10401 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L10405 `toggleAddPanel(id)`
- L10418 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L10429 `pasteMessage(text,ok)`
- L10437 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L10448 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L10459 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L10465 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L10486 `storableState()`

### Render único: actualiza toda la página

- L10494 `nearView(el)`
- L10496 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L10500 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L10531 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L10532 constante `REF_TABLE`
- L10539 `refTargets(mode)`
- L10540 `syncMicroMode()`
- L10553 `mealByHour(h=new Date()`
- L10560 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L10571 `dataSummary(s)`
- L10575 `confirmImport(next,name)`
- L10582 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L10588 `checkUpdate()`
- L10593 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L10608 constante `GAP_PREFER`
- L10609 constante `GAP_SKIP`
- L10610 constante `GAP_UNIT`
- L10611 `gapQty(f,x)`
- L10612 `gapFoods(key,gap,ctx)`
- L10631 `weekSources(key,sum)`
- L10637 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L10650 `gapRow(x,open,meal,sum,ctx)`
- L10666 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L10691 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L10692 `isFemale(s=state)`
- L10693 `sexLabel(s=state)`
- L10694 `sexBadge(sex)`
- L10696 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L10697 constante `OPT_FEMALE`
- L10708 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba.
- L10709 `applySexOpt(sex)`
- L10711 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L10716 `cleanPreset(p,fb)`
- L10720 `dayNamesFor(types)`
- L10722 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L10732 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L10740 `profV()`
- L10741 `isTrainDay(i)`
- L10742 `activityName(i)`
- L10743 `dayFaf(i)`
- L10744 `presetDesc(cfg,shake)`
- L10748 `profileDescription()`
- L10756 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L10758 `wizCatalog()`
- L10759 `wizOpen(opts={})`
- L10774 `wizTitle()`
- L10775 `wizPaint(sameStep=true)`
- L10784 `wizSync()`
- L10797 `wizFoodOptions()`
- L10800 `wizPresetSummary(cfg,whey)`
- L10805 `wizPresetHTML(kind)`
- L10813 `wizPreview()`
- L10824 `wizHTML()`
- L10865 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L10949 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L10950 constante `SUPP_CATALOG`
- L10972 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L10973 constante `PEAT_BREAKFAST`
- L10974 constante `PEAT_SHAKE`
- L10976 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L10983 `benfoUser()`
- L10985 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L11001 `ico(n)`
- L11003 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L11012 `showTour(i=0)`
- L11024 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L11025 `hubAction(v)`
- L11033 constante `FORM_URL` — Llegan solas a una hoja de Google (formulario del creador de la app). Sin cuentas ni datos personales.
- L11034 constante `FORM_FIELDS`
- L11035 constante `FB_CATS`
- L11037 `openFeedback()`
- L11041 `feedbackData()`
- L11048 `feedbackText()`
- L11049 `sendFeedback()`
- L11062 `shareFeedback()`
- L11079 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L11086 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L11094 constante `I18N_EN`

### v59: idioma (español / inglés)

- L12812 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L12813 constante `WD_EN`
- L12814 `trOne(s)`
- L12822 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L12823 constante `ES_FOOD_GYM`
- L12860 `trFood(s)`
- L12872 constante `TR_TPL`
- L12911 `trLower(s)`
- L12912 `trTpl(s,attr)`
- L12913 constante `FOOD_SEL`
- L12914 `trText(s,attr=false)`
- L12924 `trNode(n)`
- L12943 `trEl(el)`
- L12956 `trTree(root)`
- L12965 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L12979 `setLang(l,quiet)`
- L12992 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter), solo en la web publicada

- L13001 constante `GC_CODE`
- L13002 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L13012 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L13013 `packMove()`
- L13021 `unpackMove(code)`
- L13030 `moveData()`
- L13040 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L13046 `checkMove(code)`
- L13065 `aiFrameworkLines()` — v69: marco de referencia del informe para IA. Así cualquier IA, aunque no conozca la app ni al usuario, sabe con qué comparar.

### Arranque

