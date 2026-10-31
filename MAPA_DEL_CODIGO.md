# MAPA DEL CÓDIGO · BioPeat v65 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (798 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-6212; todo el JavaScript en `<script id="app">` (desde la línea 6213).

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

- L6267 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L6268 constante `AZUCAR_N`
- L6269 constante `USDA_N`
- L6275 constante `FOODS`
- L6277 constante `BASE_FAT_FIX`
- L6280 constante `EXTRA`
- L6281 constante `KEYS`
- L6283 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L6285 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L6289 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6290 constante `OPT`
- L6308 constante `LIMIT`
- L6309 `optInfo(k,goal)`
- L6316 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6324 `optLine(k,goal,unit)`
- L6331 `optRefHTML(k,goal,unit)`
- L6333 constante `DAYS`
- L6334 constante `FAF`
- L6336 constante `LOC`
- L6340 `number(v,min=0,max=1e6)`
- L6346 `decimalInputs(root=document)`
- L6347 `localDate(d=new Date()`
- L6348 `validDate(s)`
- L6353 `shift(s,n)`
- L6362 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6364 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6370 constante `DAY_TYPES`
- L6371 constante `NEW_V54`
- L6375 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6378 `bmr()` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6384 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6406 `cleanNutrients(o,required=false)`
- L6418 `cleanEntry(e)`
- L6423 `cleanPlan(p)`
- L6427 `planEntry(p)`
- L6436 `seedPlan(d,whichDate)`
- L6440 `ensureDay(d=date)`
- L6447 `effectiveEntries(d=day()`
- L6448 constante `SALTED_IDS`
- L6449 constante `SWEET_RE`
- L6450 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6468 `inferredNutrients(e)`
- L6507 `totals(entries=effectiveEntries()`
- L6516 `change(fn,message='Guardado')`
- L6520 `undo()`
- L6527 `toast(text,canUndo=false)`
- L6535 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6536 `onClick(fn)`
- L6538 `attempt(fn)`
- L6542 `modal(title,body)`
- L6551 `modalRestore()`
- L6561 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6562 `modalBack()`
- L6563 `goDate(d)`
- L6570 `renderHeader()`
- L6582 `renderRows(entries)`
- L6586 `entryValues(e)`
- L6587 `renderLog()`
- L6594 `fromFood(id,amount,meal)`
- L6600 `pantryId(name)`
- L6602 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6608 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6617 `recipe(kind)`
- L6624 `summary(entries)`
- L6628 `renderPresetInfo()`
- L6641 `stripCode(raw)`
- L6647 `parseBIO(raw,meal=$('meal-select')`
- L6653 `parseSmart(raw)`
- L6657 constante `COUNT`
- L6660 `nutrientFields(n,prefix='n_')`
- L6661 `readNutrients(form,prefix='n_')`
- L6666 `editEntry(id)`
- L6675 `editFood(id,pending=null)`
- L6680 `usageStats(days=90)`
- L6686 `renderFoods()`
- L6694 `nutrientSources(key)`
- L6701 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6702 `suppSlot(meal)`
- L6703 `renderSupps()`
- L6718 `editPlan(id)`
- L6725 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6745 `makePrompt(meal='Comida',note='')`
- L6750 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6754 `photoPrompt(meal,note)`
- L6757 `resetPhoto()`
- L6768 `openPhoto()`
- L6774 `shrinkPhoto(file)`
- L6777 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6803 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6810 `cleanFood(id,f)`
- L6814 `migrateBase(o)`
- L6833 `download(name,text,type)`
- L6842 `portable()`
- L6882 `syncAppIcons()`
- L6890 `downloadAppIcons()`
- L6927 constante `PROFILES_KEY`
- L6929 `ensureProfilesStore()`
- L6948 `saveProfilesStore(st)`
- L6952 `syncCurrentProfileToStore(rawStr)`
- L6958 `activeProfileName()`
- L6962 `renderProfilesList()`
- L7004 `switchProfile(id)`
- L7026 `deleteProfileById(id)`
- L7050 `refreshDrawerSummary()`
- L7067 `toggleLeftDrawer(force)`
- L7082 `buildAIExportText(rangeOverride)`
- L7330 `copyAIExport()`
- L7344 `downloadAIExport()`
- L7353 `renderDrawerChat()`
- L7372 `buildDrawerChatPrompt(question)`
- L7384 `askDrawerAI(rawQuestion)`
- L7471 `storageStatus()`
- L7477 `idbReadWrite(mode,value)`
- L7478 `openDB()`
- L7479 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L7492 `setQuantity(id,value,msg='Cantidad actualizada')`
- L7496 `niceStep(v)`
- L7497 `stepQuantity(id,dir)`
- L7551 `renderAppInfo()`
- L7566 `init()`
- L7590 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L7592 `setNav(v)`
- L7597 `go(v,focus)`
- L7608 constante `THEME_KEY`
- L7609 constante `SUN_SVG`
- L7610 constante `MOON_SVG`
- L7612 `syncThemeUI()`
- L7624 `toggleTheme()`
- L7632 `syncDatePill()`
- L7633 `clampBtnPos(el,x,y)`
- L7643 `bindDraggableBtn(el,storeKey)`
- L7681 `bindDrawerGestures()`
- L7714 `animateValue(el,to,suffix='%',digits=0)`
- L7723 `tick(now)`
- L7726 `macroCard(key,name,color)`
- L7727 `renderToday()`
- L7750 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L7752 constante `HOME`
- L7754 `coachCandidates()`
- L7760 `coachIdeas(t,g,ref,meal)`
- L7773 `renderCoach()`
- L7791 `coachPrompt()`
- L7799 `nutrientDetailStandard(key)`
- L7813 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L7819 `upgradeTo12(s,o)`
- L7824 `benfotiamineTotals(entries=effectiveEntries()`
- L7833 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L7835 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L7847 `microStat(m,t=totals()`
- L7852 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L7860 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L7861 `ratioInfo(key,t=totals()`
- L7896 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L7913 constante `RATIO_ENDS`
- L7914 `ratioBar(i,big=false)`
- L7919 `ratioNeed(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L7936 `needHTML(i,t)`
- L7937 `renderRatios()`
- L7942 `ratioDetail(key)`
- L7952 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L7969 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L7984 `renderMicroMap()`
- L7988 `nutrientDetailForDay(key)`
- L7993 `editTargetsForm()`
- L8003 `mealData()`
- L8008 `renderMealSegments()`
- L8016 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L8026 constante `FAT_KEYS`
- L8028 `fatData(entries=effectiveEntries()`
- L8034 `energyData(entries=effectiveEntries()`
- L8038 `segmentedBar(items,total,attr)`
- L8042 `renderMealChart()`
- L8047 `renderFat()`
- L8055 `fatDetail(key)`
- L8060 `energyDetail(key)`
- L8067 `portionCandidates(q='')`
- L8072 `openPortion()`
- L8085 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L8100 `templates()`
- L8104 `renderExtra()`
- L8115 `updateExtra(reset=true)`
- L8127 `addExtra(id,amount)`
- L8143 `shakePreview()`
- L8144 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L8159 constante `LENS`
- L8165 `lensKey(key)`
- L8166 `lensHTML(key)`
- L8170 `appendLens(key)`
- L8179 `weekDates()`

### IA en la página: conexión directa o por servidor

- L8189 constante `MEAL_WORD`
- L8190 `mealOfWord(w)`
- L8191 `mealFromText(raw,fallback)`
- L8195 `canonMeal(v,fallback)`
- L8203 `localMeal(raw,meal)`
- L8209 constante `AI_FALLBACK`
- L8210 `applyAIConfig(raw)`
- L8236 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L8237 `callGemini(model,key,prompt,img,signal,think=true)`
- L8255 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L8262 `aiProv(m=$('ai-mode')`
- L8263 `aiBase(mode)`
- L8272 `chatHeaders(mode,key)`
- L8279 `callChat(mode,model,key,prompt,img,signal)` — ChatGPT, Claude, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L8309 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L8317 constante `MODEL_PREF`
- L8318 `pickModel(ids)`
- L8323 `ensureModel(st)`
- L8334 `syncProvider()`
- L8347 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L8381 constante `AI_PREF`
- L8382 `aiConnected()`
- L8383 `syncAI()`
- L8385 `saveAIPrefs()`
- L8386 `loadAIPrefs()`
- L8387 `openAISetup()`
- L8393 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L8400 constante `MACROS`
- L8402 `cleanGoals(o,fallback)`
- L8407 `cleanCompare(o={})`
- L8411 `snapshotDay(d,reference='saved')`
- L8416 `upgradeTo17(s,o)`
- L8421 `entriesFor(d,source=weekSource)`
- L8425 `dayRow(dt,source=weekSource)`
- L8429 `goalsFor(dt)`
- L8435 `metricValue(r,key)`
- L8441 `targetOf(dt,key)`
- L8445 `weekSummary()`
- L8449 `aggregate(key,summary=weekSummary()`
- L8453 `tone(pct,mode='macro')`
- L8460 `pctText(a)`
- L8461 `weekProgress(a,color)`
- L8462 `renderWeekMicros(s)`
- L8474 `ratioAggregate(s,num,den)`
- L8478 `renderWeekRatios(s)`
- L8484 `renderWeekTable(s)`
- L8485 `weeklyDetail(key,oneDate=null)`
- L8494 `weekRatioDetail(key)`
- L8502 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L8508 `openDay(dt)`
- L8546 `withDayGoals(fn)`
- L8551 `renderMicros()`
- L8552 `nutrientDetail(key)`
- L8553 `editTargets()`
- L8554 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L8564 `summaryFor(start)`
- L8568 `ringSVG(pct,color,marker)`
- L8570 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L8574 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L8589 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L8590 `macroTone(p)`
- L8591 `dayMacroPct(dt,k)`
- L8592 `renderWeekly()`
- L8615 `weekDetail(dt,picked)`
- L8623 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L8633 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L8639 `sparkline(pts)`
- L8645 `renderCalendar()`
- L8662 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L8663 `splitMeals(raw)`
- L8673 `localDay(raw,fallback)`
- L8680 `promptDay(raw,fallback)`
- L8681 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L8703 `parseCsv(text)`
- L8718 `hevyDate(value,format='auto')`
- L8735 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L8750 constante `GYM_APPS`
- L8752 `gymSig(headers)`
- L8753 `gymApp(headers)`
- L8754 `hevyMapping()`
- L8755 `gymSaved()`
- L8756 `renderMapping(parsed)`
- L8773 `optionalNum(v,min=0,max=1e7)`
- L8778 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L8785 `buildHevy(parsed,map)`
- L8819 `cleanWorkout(s)`
- L8826 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L8841 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L8842 constante `GP_ALIAS`
- L8852 `gpNorm(s)`
- L8853 `gpKey(name)`
- L8857 `gpF(n,d=0)`
- L8858 `gpDate(d,opt)`
- L8859 `gpMonday(d)`
- L8860 constante `GP_GROUPS`
- L8875 constante `GP_COLORS`
- L8876 `gpGroup(name)`
- L8877 `gpWorkSets(s)`
- L8878 `gpModel()`
- L8902 `gpSessionMetrics(e,sets)`
- L8917 constante `GP_METRICS`
- L8922 `gpMetricsFor(e)`
- L8923 `gpRangeHist(e)`
- L8924 `gpPRs(model)`
- L8947 `gpStatus(e)`
- L8965 `gpNext(e)`
- L8973 `gpChart(e)`
- L9001 `gpPointDetail(e)`
- L9007 `gpRepTable(e)`
- L9014 `gpKpis(model)`
- L9022 `gpWeekly(model)`
- L9028 `gpMuscles(model)`
- L9035 `gpHeat(model)`
- L9042 `gpExList(model)`
- L9049 `gpExDetail(model)`
- L9062 `gpDayFood(dt)`
- L9063 `gpNutrition(model)`
- L9070 `gpRecentPRs(model)`
- L9074 `gpSessions(model)`
- L9080 `gpSessionModal(id)`
- L9091 `gpWeekModal(w)`
- L9092 `gpSelect(key)`
- L9093 `gpClick(e)`
- L9105 `renderGym()`
- L9125 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L9134 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L9140 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L9165 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L9169 `showHelp()`
- L9173 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L9175 `markBackup()`
- L9179 `exportJSON()`
- L9184 `drawBackupReminder()`
- L9194 `applyDensity()`
- L9206 `syncDayComplete()`
- L9209 `drawMeals()` — Comidas del día de un vistazo.
- L9217 `filterLog()` — Buscador de Registro.
- L9230 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L9236 `recentFoods()`
- L9241 `quickChip(e,fav)`
- L9259 `drawQuickFoods()`
- L9288 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L9292 `toggleAddPanel(id)`
- L9304 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L9315 `pasteMessage(text,ok)`
- L9323 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L9334 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L9345 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L9351 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L9372 `storableState()`

### Render único: actualiza toda la página

- L9380 `nearView(el)`
- L9382 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L9386 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L9417 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L9418 constante `REF_TABLE`
- L9425 `refTargets(mode)`
- L9426 `syncMicroMode()`
- L9439 `mealByHour(h=new Date()`
- L9446 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L9457 `dataSummary(s)`
- L9461 `confirmImport(next,name)`
- L9468 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L9474 `checkUpdate()`
- L9479 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L9494 constante `GAP_PREFER`
- L9495 constante `GAP_SKIP`
- L9496 constante `GAP_UNIT`
- L9497 `gapQty(f,x)`
- L9498 `gapFoods(key,gap,ctx)`
- L9517 `weekSources(key,sum)`
- L9523 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L9536 `gapRow(x,open,meal,sum,ctx)`
- L9552 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L9577 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L9578 `isFemale(s=state)`
- L9579 `sexLabel(s=state)`
- L9580 `sexBadge(sex)`
- L9582 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L9583 constante `OPT_FEMALE`
- L9594 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba.
- L9595 `applySexOpt(sex)`
- L9597 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L9602 `cleanPreset(p,fb)`
- L9606 `dayNamesFor(types)`
- L9608 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L9618 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L9626 `profV()`
- L9627 `isTrainDay(i)`
- L9628 `activityName(i)`
- L9629 `dayFaf(i)`
- L9630 `presetDesc(cfg,shake)`
- L9634 `profileDescription()`
- L9642 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L9644 `wizCatalog()`
- L9645 `wizOpen(opts={})`
- L9660 `wizTitle()`
- L9661 `wizPaint(sameStep=true)`
- L9670 `wizSync()`
- L9683 `wizFoodOptions()`
- L9686 `wizPresetSummary(cfg,whey)`
- L9691 `wizPresetHTML(kind)`
- L9699 `wizPreview()`
- L9710 `wizHTML()`
- L9751 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L9835 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L9836 constante `SUPP_CATALOG`
- L9858 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L9859 constante `PEAT_BREAKFAST`
- L9860 constante `PEAT_SHAKE`
- L9862 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L9869 `benfoUser()`
- L9871 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L9887 `ico(n)`
- L9889 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L9898 `showTour(i=0)`
- L9910 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L9911 `hubAction(v)`
- L9919 constante `FORM_URL` — Llegan solas a una hoja de Google (formulario del creador de la app). Sin cuentas ni datos personales.
- L9920 constante `FORM_FIELDS`
- L9921 constante `FB_CATS`
- L9923 `openFeedback()`
- L9927 `feedbackData()`
- L9934 `feedbackText()`
- L9935 `sendFeedback()`
- L9948 `shareFeedback()`
- L9965 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L9972 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L9980 constante `I18N_EN`

### v59: idioma (español / inglés)

- L11556 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L11557 constante `WD_EN`
- L11558 `trOne(s)`
- L11566 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L11567 constante `ES_FOOD_GYM`
- L11604 `trFood(s)`
- L11616 constante `TR_TPL`
- L11650 `trLower(s)`
- L11651 `trTpl(s,attr)`
- L11652 constante `FOOD_SEL`
- L11653 `trText(s,attr=false)`
- L11663 `trNode(n)`
- L11678 `trEl(el)`
- L11686 `trTree(root)`
- L11695 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L11706 `setLang(l,quiet)`
- L11719 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter), solo en la web publicada

- L11728 constante `GC_CODE`
- L11729 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L11739 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L11740 `packMove()`
- L11748 `unpackMove(code)`
- L11757 `moveData()`
- L11767 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L11773 `checkMove(code)`

### Arranque

