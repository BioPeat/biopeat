# MAPA DEL CÓDIGO · BioPeat v66 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (803 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-6222; todo el JavaScript en `<script id="app">` (desde la línea 6223).

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

- L6278 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L6279 constante `AZUCAR_N`
- L6280 constante `USDA_N`
- L6286 constante `FOODS`
- L6288 constante `BASE_FAT_FIX`
- L6291 constante `EXTRA`
- L6292 constante `KEYS`
- L6294 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L6296 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L6300 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6301 constante `OPT`
- L6319 constante `LIMIT`
- L6320 `optInfo(k,goal)`
- L6327 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6335 `optLine(k,goal,unit)`
- L6342 `optRefHTML(k,goal,unit)`
- L6344 constante `DAYS`
- L6345 constante `FAF`
- L6347 constante `LOC`
- L6351 `number(v,min=0,max=1e6)`
- L6357 `decimalInputs(root=document)`
- L6358 `localDate(d=new Date()`
- L6359 `validDate(s)`
- L6364 `shift(s,n)`
- L6373 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6375 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6381 constante `DAY_TYPES`
- L6382 constante `NEW_V54`
- L6386 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6389 `bmr()` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6395 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6417 `cleanNutrients(o,required=false)`
- L6429 `cleanEntry(e)`
- L6434 `cleanPlan(p)`
- L6438 `planEntry(p)`
- L6447 `seedPlan(d,whichDate)`
- L6451 `ensureDay(d=date)`
- L6458 `effectiveEntries(d=day()`
- L6459 constante `SALTED_IDS`
- L6460 constante `SWEET_RE`
- L6461 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6479 `inferredNutrients(e)`
- L6518 `totals(entries=effectiveEntries()`
- L6527 `change(fn,message='Guardado')`
- L6531 `undo()`
- L6538 `toast(text,canUndo=false)`
- L6546 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6547 `onClick(fn)`
- L6549 `attempt(fn)`
- L6553 `modal(title,body)`
- L6562 `modalRestore()`
- L6572 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6573 `modalBack()`
- L6574 `goDate(d)`
- L6581 `renderHeader()`
- L6594 `renderRows(entries)`
- L6598 `entryValues(e)`
- L6599 `renderLog()`
- L6606 `fromFood(id,amount,meal)`
- L6612 `pantryId(name)`
- L6614 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6620 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6629 `recipe(kind)`
- L6636 `summary(entries)`
- L6640 `renderPresetInfo()`
- L6653 `stripCode(raw)`
- L6659 `parseBIO(raw,meal=$('meal-select')`
- L6665 `parseSmart(raw)`
- L6669 constante `COUNT`
- L6672 `nutrientFields(n,prefix='n_')`
- L6673 `readNutrients(form,prefix='n_')`
- L6678 `editEntry(id)`
- L6687 `editFood(id,pending=null)`
- L6692 `usageStats(days=90)`
- L6698 `renderFoods()`
- L6706 `nutrientSources(key)`
- L6713 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6714 `suppSlot(meal)`
- L6715 `renderSupps()`
- L6730 `editPlan(id)`
- L6737 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6757 `makePrompt(meal='Comida',note='')`
- L6762 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6766 `photoPrompt(meal,note)`
- L6769 `resetPhoto()`
- L6780 `openPhoto()`
- L6786 `shrinkPhoto(file)`
- L6789 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6815 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6822 `cleanFood(id,f)`
- L6826 `migrateBase(o)`
- L6845 `download(name,text,type)`
- L6854 `portable()`
- L6894 `syncAppIcons()`
- L6902 `downloadAppIcons()`
- L6939 constante `PROFILES_KEY`
- L6941 `ensureProfilesStore()`
- L6960 `saveProfilesStore(st)`
- L6964 `syncCurrentProfileToStore(rawStr)`
- L6970 `activeProfileName()`
- L6974 `renderProfilesList()`
- L7016 `switchProfile(id)`
- L7038 `deleteProfileById(id)`
- L7062 `refreshDrawerSummary()`
- L7079 `toggleLeftDrawer(force)`
- L7094 `buildAIExportText(rangeOverride)`
- L7342 `copyAIExport()`
- L7356 `downloadAIExport()`
- L7365 `renderDrawerChat()`
- L7384 `buildDrawerChatPrompt(question)`
- L7396 `askDrawerAI(rawQuestion)`
- L7483 `storageStatus()`
- L7489 `idbReadWrite(mode,value)`
- L7490 `openDB()`
- L7491 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L7504 `setQuantity(id,value,msg='Cantidad actualizada')`
- L7508 `niceStep(v)`
- L7509 `stepQuantity(id,dir)`
- L7563 `renderAppInfo()`
- L7578 `init()`
- L7602 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L7604 `setNav(v)`
- L7609 `go(v,focus)`
- L7620 constante `THEME_KEY`
- L7621 constante `SUN_SVG`
- L7622 constante `MOON_SVG`
- L7624 `syncThemeUI()`
- L7636 `toggleTheme()`
- L7645 `syncLogoTheme()`
- L7656 `applyMenuBtnState()`
- L7679 `syncDatePill()`
- L7690 `clampBtnPos(el,x,y)`
- L7700 `bindDraggableBtn(el,storeKey)`
- L7785 `bindDrawerGestures()`
- L7822 `animateValue(el,to,suffix='%',digits=0)`
- L7831 `tick(now)`
- L7834 `macroCard(key,name,color)`
- L7835 `renderToday()`
- L7858 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L7860 constante `HOME`
- L7862 `coachCandidates()`
- L7868 `coachIdeas(t,g,ref,meal)`
- L7881 `renderCoach()`
- L7899 `coachPrompt()`
- L7907 `nutrientDetailStandard(key)`
- L7921 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L7927 `upgradeTo12(s,o)`
- L7932 `benfotiamineTotals(entries=effectiveEntries()`
- L7941 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L7943 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L7955 `microStat(m,t=totals()`
- L7960 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L7968 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L7969 `ratioInfo(key,t=totals()`
- L8004 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L8021 constante `RATIO_ENDS`
- L8022 `ratioBar(i,big=false)`
- L8027 `ratioNeed(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L8044 `needHTML(i,t)`
- L8045 `renderRatios()`
- L8050 `ratioDetail(key)`
- L8060 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L8077 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L8092 `renderMicroMap()`
- L8096 `nutrientDetailForDay(key)`
- L8101 `editTargetsForm()`
- L8111 `mealData()`
- L8116 `renderMealSegments()`
- L8124 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L8134 constante `FAT_KEYS`
- L8136 `fatData(entries=effectiveEntries()`
- L8142 `energyData(entries=effectiveEntries()`
- L8146 `segmentedBar(items,total,attr)`
- L8150 `renderMealChart()`
- L8155 `renderFat()`
- L8163 `fatDetail(key)`
- L8168 `energyDetail(key)`
- L8175 `portionCandidates(q='')`
- L8180 `openPortion()`
- L8193 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L8208 `templates()`
- L8212 `renderExtra()`
- L8223 `updateExtra(reset=true)`
- L8235 `addExtra(id,amount)`
- L8251 `shakePreview()`
- L8252 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L8267 constante `LENS`
- L8273 `lensKey(key)`
- L8274 `lensHTML(key)`
- L8278 `appendLens(key)`
- L8287 `weekDates()`

### IA en la página: conexión directa o por servidor

- L8297 constante `MEAL_WORD`
- L8298 `mealOfWord(w)`
- L8299 `mealFromText(raw,fallback)`
- L8303 `canonMeal(v,fallback)`
- L8311 `localMeal(raw,meal)`
- L8317 constante `AI_FALLBACK`
- L8318 `applyAIConfig(raw)`
- L8344 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L8345 `callGemini(model,key,prompt,img,signal,think=true)`
- L8363 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L8370 `aiProv(m=$('ai-mode')`
- L8371 `aiBase(mode)`
- L8380 `chatHeaders(mode,key)`
- L8387 `callChat(mode,model,key,prompt,img,signal)` — ChatGPT, Claude, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L8417 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L8425 constante `MODEL_PREF`
- L8426 `pickModel(ids)`
- L8431 `ensureModel(st)`
- L8442 `syncProvider()`
- L8455 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L8489 constante `AI_PREF`
- L8490 `aiConnected()`
- L8491 `syncAI()`
- L8493 `saveAIPrefs()`
- L8494 `loadAIPrefs()`
- L8495 `openAISetup()`
- L8501 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L8508 constante `MACROS`
- L8510 `cleanGoals(o,fallback)`
- L8515 `cleanCompare(o={})`
- L8519 `snapshotDay(d,reference='saved')`
- L8524 `upgradeTo17(s,o)`
- L8529 `entriesFor(d,source=weekSource)`
- L8533 `dayRow(dt,source=weekSource)`
- L8537 `goalsFor(dt)`
- L8543 `metricValue(r,key)`
- L8549 `targetOf(dt,key)`
- L8553 `weekSummary()`
- L8557 `aggregate(key,summary=weekSummary()`
- L8561 `tone(pct,mode='macro')`
- L8568 `pctText(a)`
- L8569 `weekProgress(a,color)`
- L8570 `renderWeekMicros(s)`
- L8582 `ratioAggregate(s,num,den)`
- L8586 `renderWeekRatios(s)`
- L8592 `renderWeekTable(s)`
- L8593 `weeklyDetail(key,oneDate=null)`
- L8602 `weekRatioDetail(key)`
- L8610 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L8616 `openDay(dt)`
- L8654 `withDayGoals(fn)`
- L8659 `renderMicros()`
- L8660 `nutrientDetail(key)`
- L8661 `editTargets()`
- L8662 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L8672 `summaryFor(start)`
- L8676 `ringSVG(pct,color,marker)`
- L8678 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L8682 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L8697 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L8698 `macroTone(p)`
- L8699 `dayMacroPct(dt,k)`
- L8700 `renderWeekly()`
- L8723 `weekDetail(dt,picked)`
- L8731 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L8741 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L8747 `sparkline(pts)`
- L8753 `renderCalendar()`
- L8770 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L8771 `splitMeals(raw)`
- L8781 `localDay(raw,fallback)`
- L8788 `promptDay(raw,fallback)`
- L8789 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L8811 `parseCsv(text)`
- L8826 `hevyDate(value,format='auto')`
- L8843 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L8858 constante `GYM_APPS`
- L8860 `gymSig(headers)`
- L8861 `gymApp(headers)`
- L8862 `hevyMapping()`
- L8863 `gymSaved()`
- L8864 `renderMapping(parsed)`
- L8881 `optionalNum(v,min=0,max=1e7)`
- L8886 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L8893 `buildHevy(parsed,map)`
- L8927 `cleanWorkout(s)`
- L8934 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L8949 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L8950 constante `GP_ALIAS`
- L8960 `gpNorm(s)`
- L8961 `gpKey(name)`
- L8965 `gpF(n,d=0)`
- L8966 `gpDate(d,opt)`
- L8967 `gpMonday(d)`
- L8968 constante `GP_GROUPS`
- L8983 constante `GP_COLORS`
- L8984 `gpGroup(name)`
- L8985 `gpWorkSets(s)`
- L8986 `gpModel()`
- L9010 `gpSessionMetrics(e,sets)`
- L9025 constante `GP_METRICS`
- L9030 `gpMetricsFor(e)`
- L9031 `gpRangeHist(e)`
- L9032 `gpPRs(model)`
- L9055 `gpStatus(e)`
- L9073 `gpNext(e)`
- L9081 `gpChart(e)`
- L9109 `gpPointDetail(e)`
- L9115 `gpRepTable(e)`
- L9122 `gpKpis(model)`
- L9130 `gpWeekly(model)`
- L9136 `gpMuscles(model)`
- L9143 `gpHeat(model)`
- L9150 `gpExList(model)`
- L9157 `gpExDetail(model)`
- L9170 `gpDayFood(dt)`
- L9171 `gpNutrition(model)`
- L9178 `gpRecentPRs(model)`
- L9182 `gpSessions(model)`
- L9188 `gpSessionModal(id)`
- L9199 `gpWeekModal(w)`
- L9200 `gpSelect(key)`
- L9201 `gpClick(e)`
- L9213 `renderGym()`
- L9233 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L9242 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L9248 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L9273 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L9277 `showHelp()`
- L9281 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L9283 `markBackup()`
- L9287 `exportJSON()`
- L9292 `drawBackupReminder()`
- L9302 `applyDensity()`
- L9314 `syncDayComplete()`
- L9317 `drawMeals()` — Comidas del día de un vistazo.
- L9325 `filterLog()` — Buscador de Registro.
- L9338 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L9344 `recentFoods()`
- L9349 `quickChip(e,fav)`
- L9367 `drawQuickFoods()`
- L9396 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L9400 `toggleAddPanel(id)`
- L9412 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L9423 `pasteMessage(text,ok)`
- L9431 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L9442 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L9453 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L9459 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L9480 `storableState()`

### Render único: actualiza toda la página

- L9488 `nearView(el)`
- L9490 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L9494 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L9525 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L9526 constante `REF_TABLE`
- L9533 `refTargets(mode)`
- L9534 `syncMicroMode()`
- L9547 `mealByHour(h=new Date()`
- L9554 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L9565 `dataSummary(s)`
- L9569 `confirmImport(next,name)`
- L9576 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L9582 `checkUpdate()`
- L9587 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L9602 constante `GAP_PREFER`
- L9603 constante `GAP_SKIP`
- L9604 constante `GAP_UNIT`
- L9605 `gapQty(f,x)`
- L9606 `gapFoods(key,gap,ctx)`
- L9625 `weekSources(key,sum)`
- L9631 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L9644 `gapRow(x,open,meal,sum,ctx)`
- L9660 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L9685 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L9686 `isFemale(s=state)`
- L9687 `sexLabel(s=state)`
- L9688 `sexBadge(sex)`
- L9690 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L9691 constante `OPT_FEMALE`
- L9702 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba.
- L9703 `applySexOpt(sex)`
- L9705 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L9710 `cleanPreset(p,fb)`
- L9714 `dayNamesFor(types)`
- L9716 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L9726 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L9734 `profV()`
- L9735 `isTrainDay(i)`
- L9736 `activityName(i)`
- L9737 `dayFaf(i)`
- L9738 `presetDesc(cfg,shake)`
- L9742 `profileDescription()`
- L9750 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L9752 `wizCatalog()`
- L9753 `wizOpen(opts={})`
- L9768 `wizTitle()`
- L9769 `wizPaint(sameStep=true)`
- L9778 `wizSync()`
- L9791 `wizFoodOptions()`
- L9794 `wizPresetSummary(cfg,whey)`
- L9799 `wizPresetHTML(kind)`
- L9807 `wizPreview()`
- L9818 `wizHTML()`
- L9859 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L9943 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L9944 constante `SUPP_CATALOG`
- L9966 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L9967 constante `PEAT_BREAKFAST`
- L9968 constante `PEAT_SHAKE`
- L9970 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L9977 `benfoUser()`
- L9979 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L9995 `ico(n)`
- L9997 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L10006 `showTour(i=0)`
- L10018 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L10019 `hubAction(v)`
- L10027 constante `FORM_URL` — Llegan solas a una hoja de Google (formulario del creador de la app). Sin cuentas ni datos personales.
- L10028 constante `FORM_FIELDS`
- L10029 constante `FB_CATS`
- L10031 `openFeedback()`
- L10035 `feedbackData()`
- L10042 `feedbackText()`
- L10043 `sendFeedback()`
- L10056 `shareFeedback()`
- L10073 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L10080 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L10088 constante `I18N_EN`

### v59: idioma (español / inglés)

- L11664 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L11665 constante `WD_EN`
- L11666 `trOne(s)`
- L11674 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L11675 constante `ES_FOOD_GYM`
- L11712 `trFood(s)`
- L11724 constante `TR_TPL`
- L11758 `trLower(s)`
- L11759 `trTpl(s,attr)`
- L11760 constante `FOOD_SEL`
- L11761 `trText(s,attr=false)`
- L11771 `trNode(n)`
- L11786 `trEl(el)`
- L11794 `trTree(root)`
- L11803 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L11814 `setLang(l,quiet)`
- L11827 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter), solo en la web publicada

- L11836 constante `GC_CODE`
- L11837 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L11847 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L11848 `packMove()`
- L11856 `unpackMove(code)`
- L11865 `moveData()`
- L11875 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L11881 `checkMove(code)`

### Arranque

