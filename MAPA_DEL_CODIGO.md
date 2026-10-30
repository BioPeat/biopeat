# MAPA DEL CÓDIGO · BioPeat v63 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (785 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-6133; todo el JavaScript en `<script id="app">` (desde la línea 6134).

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

- L6186 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L6187 constante `AZUCAR_N`
- L6188 constante `USDA_N`
- L6194 constante `FOODS`
- L6196 constante `BASE_FAT_FIX`
- L6199 constante `EXTRA`
- L6200 constante `KEYS`
- L6202 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L6204 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L6208 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6209 constante `OPT`
- L6227 constante `LIMIT`
- L6228 `optInfo(k,goal)`
- L6235 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6243 `optLine(k,goal,unit)`
- L6250 `optRefHTML(k,goal,unit)`
- L6252 constante `DAYS`
- L6253 constante `FAF`
- L6255 constante `LOC`
- L6259 `number(v,min=0,max=1e6)`
- L6265 `decimalInputs(root=document)`
- L6266 `localDate(d=new Date()`
- L6267 `validDate(s)`
- L6272 `shift(s,n)`
- L6281 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6283 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6289 constante `DAY_TYPES`
- L6290 constante `NEW_V54`
- L6294 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6297 `bmr()` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6303 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6325 `cleanNutrients(o,required=false)`
- L6337 `cleanEntry(e)`
- L6342 `cleanPlan(p)`
- L6346 `planEntry(p)`
- L6355 `seedPlan(d,whichDate)`
- L6359 `ensureDay(d=date)`
- L6366 `effectiveEntries(d=day()`
- L6367 constante `SALTED_IDS`
- L6368 constante `SWEET_RE`
- L6369 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6387 `inferredNutrients(e)`
- L6426 `totals(entries=effectiveEntries()`
- L6435 `change(fn,message='Guardado')`
- L6439 `undo()`
- L6446 `toast(text,canUndo=false)`
- L6454 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6455 `onClick(fn)`
- L6457 `attempt(fn)`
- L6461 `modal(title,body)`
- L6470 `modalRestore()`
- L6480 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6481 `modalBack()`
- L6482 `goDate(d)`
- L6489 `renderHeader()`
- L6501 `renderRows(entries)`
- L6505 `entryValues(e)`
- L6506 `renderLog()`
- L6513 `fromFood(id,amount,meal)`
- L6519 `pantryId(name)`
- L6521 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6527 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6536 `recipe(kind)`
- L6543 `summary(entries)`
- L6547 `renderPresetInfo()`
- L6560 `stripCode(raw)`
- L6566 `parseBIO(raw,meal=$('meal-select')`
- L6572 `parseSmart(raw)`
- L6576 constante `COUNT`
- L6579 `nutrientFields(n,prefix='n_')`
- L6580 `readNutrients(form,prefix='n_')`
- L6585 `editEntry(id)`
- L6594 `editFood(id,pending=null)`
- L6599 `usageStats(days=90)`
- L6605 `renderFoods()`
- L6613 `nutrientSources(key)`
- L6620 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6621 `suppSlot(meal)`
- L6622 `renderSupps()`
- L6637 `editPlan(id)`
- L6644 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6664 `makePrompt(meal='Comida',note='')`
- L6669 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6673 `photoPrompt(meal,note)`
- L6676 `resetPhoto()`
- L6687 `openPhoto()`
- L6693 `shrinkPhoto(file)`
- L6696 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6722 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6729 `cleanFood(id,f)`
- L6733 `migrateBase(o)`
- L6752 `download(name,text,type)`
- L6761 `portable()`
- L6798 `syncAppIcons()`
- L6806 `downloadAppIcons()`
- L6843 constante `PROFILES_KEY`
- L6845 `ensureProfilesStore()`
- L6864 `saveProfilesStore(st)`
- L6868 `syncCurrentProfileToStore(rawStr)`
- L6874 `activeProfileName()`
- L6878 `renderProfilesList()`
- L6920 `switchProfile(id)`
- L6942 `deleteProfileById(id)`
- L6966 `refreshDrawerSummary()`
- L6983 `toggleLeftDrawer(force)`
- L6998 `buildAIExportText(rangeOverride)`
- L7246 `copyAIExport()`
- L7260 `downloadAIExport()`
- L7269 `renderDrawerChat()`
- L7288 `buildDrawerChatPrompt(question)`
- L7300 `askDrawerAI(rawQuestion)`
- L7387 `storageStatus()`
- L7393 `idbReadWrite(mode,value)`
- L7394 `openDB()`
- L7395 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L7408 `setQuantity(id,value,msg='Cantidad actualizada')`
- L7412 `niceStep(v)`
- L7413 `stepQuantity(id,dir)`
- L7467 `renderAppInfo()`
- L7482 `init()`
- L7506 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L7508 `setNav(v)`
- L7513 `go(v,focus)`
- L7524 constante `THEME_KEY`
- L7525 constante `SUN_SVG`
- L7526 constante `MOON_SVG`
- L7528 `syncThemeUI()`
- L7540 `toggleTheme()`
- L7548 `syncDatePill()`
- L7552 `animateValue(el,to,suffix='%',digits=0)`
- L7561 `tick(now)`
- L7564 `macroCard(key,name,color)`
- L7565 `renderToday()`
- L7588 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L7590 constante `HOME`
- L7592 `coachCandidates()`
- L7598 `coachIdeas(t,g,ref,meal)`
- L7611 `renderCoach()`
- L7629 `coachPrompt()`
- L7637 `nutrientDetailStandard(key)`
- L7651 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L7657 `upgradeTo12(s,o)`
- L7662 `benfotiamineTotals(entries=effectiveEntries()`
- L7671 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L7673 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L7685 `microStat(m,t=totals()`
- L7690 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L7698 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L7699 `ratioInfo(key,t=totals()`
- L7734 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L7751 constante `RATIO_ENDS`
- L7752 `ratioBar(i,big=false)`
- L7757 `ratioNeed(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L7774 `needHTML(i,t)`
- L7775 `renderRatios()`
- L7780 `ratioDetail(key)`
- L7790 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L7807 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L7822 `renderMicroMap()`
- L7826 `nutrientDetailForDay(key)`
- L7831 `editTargetsForm()`
- L7841 `mealData()`
- L7846 `renderMealSegments()`
- L7854 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L7864 constante `FAT_KEYS`
- L7866 `fatData(entries=effectiveEntries()`
- L7872 `energyData(entries=effectiveEntries()`
- L7876 `segmentedBar(items,total,attr)`
- L7880 `renderMealChart()`
- L7885 `renderFat()`
- L7893 `fatDetail(key)`
- L7898 `energyDetail(key)`
- L7905 `portionCandidates(q='')`
- L7910 `openPortion()`
- L7923 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L7938 `templates()`
- L7942 `renderExtra()`
- L7953 `updateExtra(reset=true)`
- L7965 `addExtra(id,amount)`
- L7981 `shakePreview()`
- L7982 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L7997 constante `LENS`
- L8003 `lensKey(key)`
- L8004 `lensHTML(key)`
- L8008 `appendLens(key)`
- L8017 `weekDates()`

### IA en la página: conexión directa o por servidor

- L8027 constante `MEAL_WORD`
- L8028 `mealOfWord(w)`
- L8029 `mealFromText(raw,fallback)`
- L8033 `canonMeal(v,fallback)`
- L8041 `localMeal(raw,meal)`
- L8047 constante `AI_FALLBACK`
- L8048 `applyAIConfig(raw)`
- L8074 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L8075 `callGemini(model,key,prompt,img,signal,think=true)`
- L8093 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L8100 `aiProv(m=$('ai-mode')`
- L8101 `aiBase(mode)`
- L8110 `chatHeaders(mode,key)`
- L8117 `callChat(mode,model,key,prompt,img,signal)` — ChatGPT, Claude, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L8147 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L8155 constante `MODEL_PREF`
- L8156 `pickModel(ids)`
- L8161 `ensureModel(st)`
- L8172 `syncProvider()`
- L8185 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L8219 constante `AI_PREF`
- L8220 `aiConnected()`
- L8221 `syncAI()`
- L8223 `saveAIPrefs()`
- L8224 `loadAIPrefs()`
- L8225 `openAISetup()`
- L8231 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L8238 constante `MACROS`
- L8240 `cleanGoals(o,fallback)`
- L8245 `cleanCompare(o={})`
- L8249 `snapshotDay(d,reference='saved')`
- L8254 `upgradeTo17(s,o)`
- L8259 `entriesFor(d,source=weekSource)`
- L8263 `dayRow(dt,source=weekSource)`
- L8267 `goalsFor(dt)`
- L8273 `metricValue(r,key)`
- L8279 `targetOf(dt,key)`
- L8283 `weekSummary()`
- L8287 `aggregate(key,summary=weekSummary()`
- L8291 `tone(pct,mode='macro')`
- L8298 `pctText(a)`
- L8299 `weekProgress(a,color)`
- L8300 `renderWeekMicros(s)`
- L8312 `ratioAggregate(s,num,den)`
- L8316 `renderWeekRatios(s)`
- L8322 `renderWeekTable(s)`
- L8323 `weeklyDetail(key,oneDate=null)`
- L8332 `weekRatioDetail(key)`
- L8340 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L8346 `openDay(dt)`
- L8384 `withDayGoals(fn)`
- L8389 `renderMicros()`
- L8390 `nutrientDetail(key)`
- L8391 `editTargets()`
- L8392 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L8402 `summaryFor(start)`
- L8406 `ringSVG(pct,color,marker)`
- L8408 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L8412 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L8427 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L8428 `macroTone(p)`
- L8429 `dayMacroPct(dt,k)`
- L8430 `renderWeekly()`
- L8453 `weekDetail(dt,picked)`
- L8461 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L8471 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L8477 `sparkline(pts)`
- L8483 `renderCalendar()`
- L8500 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L8501 `splitMeals(raw)`
- L8511 `localDay(raw,fallback)`
- L8518 `promptDay(raw,fallback)`
- L8519 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L8541 `parseCsv(text)`
- L8556 `hevyDate(value,format='auto')`
- L8573 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L8588 constante `GYM_APPS`
- L8590 `gymSig(headers)`
- L8591 `gymApp(headers)`
- L8592 `hevyMapping()`
- L8593 `gymSaved()`
- L8594 `renderMapping(parsed)`
- L8611 `optionalNum(v,min=0,max=1e7)`
- L8616 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L8623 `buildHevy(parsed,map)`
- L8657 `cleanWorkout(s)`
- L8664 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L8679 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L8680 constante `GP_ALIAS`
- L8690 `gpNorm(s)`
- L8691 `gpKey(name)`
- L8695 `gpF(n,d=0)`
- L8696 `gpDate(d,opt)`
- L8697 `gpMonday(d)`
- L8698 constante `GP_GROUPS`
- L8713 constante `GP_COLORS`
- L8714 `gpGroup(name)`
- L8715 `gpWorkSets(s)`
- L8716 `gpModel()`
- L8740 `gpSessionMetrics(e,sets)`
- L8755 constante `GP_METRICS`
- L8760 `gpMetricsFor(e)`
- L8761 `gpRangeHist(e)`
- L8762 `gpPRs(model)`
- L8785 `gpStatus(e)`
- L8803 `gpNext(e)`
- L8811 `gpChart(e)`
- L8839 `gpPointDetail(e)`
- L8845 `gpRepTable(e)`
- L8852 `gpKpis(model)`
- L8860 `gpWeekly(model)`
- L8866 `gpMuscles(model)`
- L8873 `gpHeat(model)`
- L8880 `gpExList(model)`
- L8887 `gpExDetail(model)`
- L8900 `gpDayFood(dt)`
- L8901 `gpNutrition(model)`
- L8908 `gpRecentPRs(model)`
- L8912 `gpSessions(model)`
- L8918 `gpSessionModal(id)`
- L8929 `gpWeekModal(w)`
- L8930 `gpSelect(key)`
- L8931 `gpClick(e)`
- L8943 `renderGym()`
- L8963 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L8972 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L8978 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L9003 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L9007 `showHelp()`
- L9011 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L9013 `markBackup()`
- L9017 `exportJSON()`
- L9022 `drawBackupReminder()`
- L9032 `applyDensity()`
- L9044 `syncDayComplete()`
- L9047 `drawMeals()` — Comidas del día de un vistazo.
- L9055 `filterLog()` — Buscador de Registro.
- L9068 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L9074 `recentFoods()`
- L9079 `quickChip(e,fav)`
- L9097 `drawQuickFoods()`
- L9126 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L9130 `toggleAddPanel(id)`
- L9142 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L9153 `pasteMessage(text,ok)`
- L9161 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L9172 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L9183 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L9189 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L9210 `storableState()`

### Render único: actualiza toda la página

- L9218 `nearView(el)`
- L9220 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L9224 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L9255 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L9256 constante `REF_TABLE`
- L9263 `refTargets(mode)`
- L9264 `syncMicroMode()`
- L9277 `mealByHour(h=new Date()`
- L9284 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L9295 `dataSummary(s)`
- L9299 `confirmImport(next,name)`
- L9306 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L9312 `checkUpdate()`
- L9317 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L9332 constante `GAP_PREFER`
- L9333 constante `GAP_SKIP`
- L9334 constante `GAP_UNIT`
- L9335 `gapQty(f,x)`
- L9336 `gapFoods(key,gap,ctx)`
- L9355 `weekSources(key,sum)`
- L9361 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L9374 `gapRow(x,open,meal,sum,ctx)`
- L9390 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L9415 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L9416 `isFemale(s=state)`
- L9417 `sexLabel(s=state)`
- L9418 `sexBadge(sex)`
- L9420 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L9421 constante `OPT_FEMALE`
- L9432 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba.
- L9433 `applySexOpt(sex)`
- L9435 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L9440 `cleanPreset(p,fb)`
- L9444 `dayNamesFor(types)`
- L9446 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L9456 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L9464 `profV()`
- L9465 `isTrainDay(i)`
- L9466 `activityName(i)`
- L9467 `dayFaf(i)`
- L9468 `presetDesc(cfg,shake)`
- L9472 `profileDescription()`
- L9480 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L9482 `wizCatalog()`
- L9483 `wizOpen(opts={})`
- L9498 `wizTitle()`
- L9499 `wizPaint(sameStep=true)`
- L9508 `wizSync()`
- L9521 `wizFoodOptions()`
- L9524 `wizPresetSummary(cfg,whey)`
- L9529 `wizPresetHTML(kind)`
- L9537 `wizPreview()`
- L9548 `wizHTML()`
- L9589 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L9673 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L9674 constante `SUPP_CATALOG`
- L9696 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L9697 constante `PEAT_BREAKFAST`
- L9698 constante `PEAT_SHAKE`
- L9700 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L9707 `benfoUser()`
- L9709 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L9725 `ico(n)`
- L9727 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L9736 `showTour(i=0)`
- L9748 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L9749 `hubAction(v)`
- L9757 constante `FORM_URL` — Llegan solas a una hoja de Google (formulario del creador de la app). Sin cuentas ni datos personales.
- L9758 constante `FORM_FIELDS`
- L9759 constante `FB_CATS`
- L9761 `openFeedback()`
- L9765 `feedbackData()`
- L9772 `feedbackText()`
- L9773 `sendFeedback()`
- L9786 `shareFeedback()`
- L9803 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L9810 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L9818 constante `I18N_EN`

### v59: idioma (español / inglés)

- L11394 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L11395 constante `WD_EN`
- L11396 `trOne(s)`
- L11404 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L11405 constante `ES_FOOD_GYM`
- L11442 `trFood(s)`
- L11454 constante `TR_TPL`
- L11488 `trLower(s)`
- L11489 `trTpl(s,attr)`
- L11490 constante `FOOD_SEL`
- L11491 `trText(s,attr=false)`
- L11501 `trNode(n)`
- L11516 `trEl(el)`
- L11524 `trTree(root)`
- L11533 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L11544 `setLang(l,quiet)`
- L11557 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter), solo en la web publicada

- L11566 constante `GC_CODE`
- L11567 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L11577 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L11578 `packMove()`
- L11586 `unpackMove(code)`
- L11595 `moveData()`
- L11605 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L11611 `checkMove(code)`

### Arranque

