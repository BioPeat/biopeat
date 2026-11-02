# MAPA DEL CÓDIGO · BioPeat v68 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (815 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-6273; todo el JavaScript en `<script id="app">` (desde la línea 6274).

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

- L6331 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L6332 constante `AZUCAR_N`
- L6333 constante `USDA_N`
- L6339 constante `FOODS`
- L6341 constante `BASE_FAT_FIX`
- L6344 constante `EXTRA`
- L6345 constante `KEYS`
- L6347 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L6349 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L6353 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6354 constante `OPT`
- L6372 constante `LIMIT`
- L6373 `optInfo(k,goal)`
- L6380 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6388 `optLine(k,goal,unit)`
- L6395 `optRefHTML(k,goal,unit)`
- L6397 constante `DAYS`
- L6398 constante `FAF`
- L6400 constante `LOC`
- L6404 `number(v,min=0,max=1e6)`
- L6410 `decimalInputs(root=document)`
- L6411 `localDate(d=new Date()`
- L6412 `validDate(s)`
- L6417 `shift(s,n)`
- L6426 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6428 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6434 constante `DAY_TYPES`
- L6435 constante `NEW_V54`
- L6439 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6442 `bmr()` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6448 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6470 `cleanNutrients(o,required=false)`
- L6482 `cleanEntry(e)`
- L6487 `cleanPlan(p)`
- L6491 `planEntry(p)`
- L6500 `seedPlan(d,whichDate)`
- L6504 `ensureDay(d=date)`
- L6511 `effectiveEntries(d=day()`
- L6512 constante `SALTED_IDS`
- L6513 constante `SWEET_RE`
- L6514 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6532 `inferredNutrients(e)`
- L6571 `totals(entries=effectiveEntries()`
- L6580 `change(fn,message='Guardado')`
- L6584 `undo()`
- L6591 `toast(text,canUndo=false)`
- L6599 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6600 `onClick(fn)`
- L6602 `attempt(fn)`
- L6606 `modal(title,body)`
- L6615 `modalRestore()`
- L6625 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6626 `modalBack()`
- L6627 `goDate(d)`
- L6634 `renderHeader()`
- L6647 `renderRows(entries)`
- L6651 `entryValues(e)`
- L6652 `renderLog()`
- L6659 `fromFood(id,amount,meal)`
- L6665 `pantryId(name)`
- L6667 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6673 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6682 `recipe(kind)`
- L6689 `summary(entries)`
- L6693 `renderPresetInfo()`
- L6706 `stripCode(raw)`
- L6712 `parseBIO(raw,meal=$('meal-select')`
- L6718 `parseSmart(raw)`
- L6722 constante `COUNT`
- L6725 `nutrientFields(n,prefix='n_')`
- L6726 `readNutrients(form,prefix='n_')`
- L6731 `editEntry(id)`
- L6740 `editFood(id,pending=null)`
- L6745 `usageStats(days=90)`
- L6751 `renderFoods()`
- L6759 `nutrientSources(key)`
- L6766 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6767 `suppSlot(meal)`
- L6768 `renderSupps()`
- L6783 `editPlan(id)`
- L6790 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6810 `makePrompt(meal='Comida',note='')`
- L6815 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6819 `photoPrompt(meal,note)`
- L6822 `resetPhoto()`
- L6833 `openPhoto()`
- L6839 `shrinkPhoto(file)`
- L6842 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6868 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6875 `cleanFood(id,f)`
- L6879 `migrateBase(o)`
- L6898 `download(name,text,type)`
- L6907 `portable()`
- L6947 `syncAppIcons()`
- L6955 `downloadAppIcons()`
- L6992 constante `PROFILES_KEY`
- L6994 `ensureProfilesStore()`
- L7013 `saveProfilesStore(st)`
- L7017 `syncCurrentProfileToStore(rawStr)`
- L7023 `activeProfileName()`
- L7027 `renderProfilesList()`
- L7069 `switchProfile(id)`
- L7091 `deleteProfileById(id)`
- L7115 `refreshDrawerSummary()`
- L7132 `toggleLeftDrawer(force)`
- L7147 `buildAIExportText(rangeOverride)`
- L7395 `copyAIExport()`
- L7409 `downloadAIExport()`
- L7418 `renderDrawerChat()`
- L7437 `buildDrawerChatPrompt(question)`
- L7449 `askDrawerAI(rawQuestion)`
- L7536 `storageStatus()`
- L7542 `idbReadWrite(mode,value)`
- L7543 `openDB()`
- L7544 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L7557 `setQuantity(id,value,msg='Cantidad actualizada')`
- L7561 `niceStep(v)`
- L7562 `stepQuantity(id,dir)`
- L7616 `renderAppInfo()`
- L7631 `init()`
- L7658 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L7660 `setNav(v)`
- L7665 `go(v,focus)`
- L7676 constante `THEME_KEY`
- L7677 constante `SUN_SVG`
- L7678 constante `MOON_SVG`
- L7680 `syncThemeUI()`
- L7692 `toggleTheme()`
- L7701 `syncLogoTheme()`
- L7712 `applyMenuBtnState()`
- L7735 `syncDatePill()`
- L7746 `clampBtnPos(el,x,y)`
- L7756 `bindDraggableBtn(el,storeKey)`
- L7841 `bindDrawerGestures()`
- L7878 `animateValue(el,to,suffix='%',digits=0)`
- L7887 `tick(now)`
- L7890 `macroCard(key,name,color)`
- L7891 `renderToday()`
- L7914 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L7916 constante `HOME`
- L7918 `coachCandidates()`
- L7924 `coachIdeas(t,g,ref,meal)`
- L7937 `renderCoach()`
- L7955 `coachPrompt()`
- L7963 `nutrientDetailStandard(key)`
- L7977 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L7983 `upgradeTo12(s,o)`
- L7988 `benfotiamineTotals(entries=effectiveEntries()`
- L7997 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L7999 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L8011 `microStat(m,t=totals()`
- L8016 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L8024 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L8025 `ratioInfo(key,t=totals()`
- L8060 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L8077 constante `RATIO_ENDS`
- L8079 `ratioZones(i)` — v68: cada equilibrio tiene una zona «aceptable» (ni verde ni mala) y su meta visible en la tarjeta.
- L8087 `ratioTone(i)`
- L8092 constante `NEAR_HEAD`
- L8093 `ratioBar(i,big=false)`
- L8102 `ratioNeedBase(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L8119 `needHTML(i,t)`
- L8120 `ratioNeed(i,t=totals()`
- L8124 `renderRatios()`
- L8131 `ratioDetail(key)`
- L8141 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L8158 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L8173 `renderMicroMap()`
- L8177 `nutrientDetailForDay(key)`
- L8182 `editTargetsForm()`
- L8192 `mealData()`
- L8197 `renderMealSegments()`
- L8205 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L8215 constante `FAT_KEYS`
- L8217 `fatData(entries=effectiveEntries()`
- L8223 `energyData(entries=effectiveEntries()`
- L8227 `segmentedBar(items,total,attr)`
- L8231 `renderMealChart()`
- L8236 `renderFat()`
- L8244 `fatDetail(key)`
- L8249 `energyDetail(key)`
- L8256 `portionCandidates(q='')`
- L8261 `openPortion()`
- L8274 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L8289 `templates()`
- L8293 `renderExtra()`
- L8304 `updateExtra(reset=true)`
- L8316 `addExtra(id,amount)`
- L8332 `shakePreview()`
- L8333 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L8348 constante `LENS`
- L8354 `lensKey(key)`
- L8355 `lensHTML(key)`
- L8359 `appendLens(key)`
- L8368 `weekDates()`

### IA en la página: conexión directa o por servidor

- L8378 constante `MEAL_WORD`
- L8379 `mealOfWord(w)`
- L8380 `mealFromText(raw,fallback)`
- L8384 `canonMeal(v,fallback)`
- L8392 `localMeal(raw,meal)`
- L8398 constante `AI_FALLBACK`
- L8399 `applyAIConfig(raw)`
- L8425 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L8426 `callGemini(model,key,prompt,img,signal,think=true)`
- L8444 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L8451 `aiProv(m=$('ai-mode')`
- L8452 `aiBase(mode)`
- L8461 `chatHeaders(mode,key)`
- L8468 `callChat(mode,model,key,prompt,img,signal)` — ChatGPT, Claude, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L8498 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L8506 constante `MODEL_PREF`
- L8507 `pickModel(ids)`
- L8512 `ensureModel(st)`
- L8523 `syncProvider()`
- L8536 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L8570 constante `AI_PREF`
- L8571 `aiConnected()`
- L8572 `syncAI()`
- L8574 `saveAIPrefs()`
- L8575 `loadAIPrefs()`
- L8576 `openAISetup()`
- L8582 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L8589 constante `MACROS`
- L8591 `cleanGoals(o,fallback)`
- L8596 `cleanCompare(o={})`
- L8600 `snapshotDay(d,reference='saved')`
- L8605 `upgradeTo17(s,o)`
- L8610 `entriesFor(d,source=weekSource)`
- L8614 `dayRow(dt,source=weekSource)`
- L8618 `goalsFor(dt)`
- L8624 `metricValue(r,key)`
- L8630 `targetOf(dt,key)`
- L8634 `weekSummary()`
- L8638 `aggregate(key,summary=weekSummary()`
- L8642 `tone(pct,mode='macro')`
- L8649 `pctText(a)`
- L8650 `weekProgress(a,color)`
- L8651 `renderWeekMicros(s)`
- L8663 `ratioAggregate(s,num,den)`
- L8667 `renderWeekRatios(s)`
- L8673 `renderWeekTable(s)`
- L8674 `weeklyDetail(key,oneDate=null)`
- L8683 `weekRatioDetail(key)`
- L8691 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L8697 `openDay(dt)`
- L8735 `withDayGoals(fn)`
- L8740 `renderMicros()`
- L8741 `nutrientDetail(key)`
- L8742 `editTargets()`
- L8743 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L8753 `summaryFor(start)`
- L8757 `ringSVG(pct,color,marker)`
- L8759 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L8763 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L8778 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L8779 `macroTone(p)`
- L8780 `dayMacroPct(dt,k)`
- L8781 `renderWeekly()`
- L8804 `weekDetail(dt,picked)`
- L8812 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L8822 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L8828 `sparkline(pts)`
- L8834 `renderCalendar()`
- L8851 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L8852 `splitMeals(raw)`
- L8862 `localDay(raw,fallback)`
- L8869 `promptDay(raw,fallback)`
- L8870 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L8892 `parseCsv(text)`
- L8907 `hevyDate(value,format='auto')`
- L8924 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L8939 constante `GYM_APPS`
- L8941 `gymSig(headers)`
- L8942 `gymApp(headers)`
- L8943 `hevyMapping()`
- L8944 `gymSaved()`
- L8945 `renderMapping(parsed)`
- L8962 `optionalNum(v,min=0,max=1e7)`
- L8967 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L8974 `buildHevy(parsed,map)`
- L9008 `cleanWorkout(s)`
- L9015 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L9030 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L9031 constante `GP_ALIAS`
- L9041 `gpNorm(s)`
- L9042 `gpKey(name)`
- L9046 `gpF(n,d=0)`
- L9047 `gpDate(d,opt)`
- L9048 `gpMonday(d)`
- L9049 constante `GP_GROUPS`
- L9064 constante `GP_COLORS`
- L9065 `gpGroup(name)`
- L9066 `gpWorkSets(s)`
- L9067 `gpModel()`
- L9091 `gpSessionMetrics(e,sets)`
- L9106 constante `GP_METRICS`
- L9111 `gpMetricsFor(e)`
- L9112 `gpRangeHist(e)`
- L9113 `gpPRs(model)`
- L9136 `gpStatus(e)`
- L9154 `gpNext(e)`
- L9162 `gpChart(e)`
- L9190 `gpPointDetail(e)`
- L9196 `gpRepTable(e)`
- L9203 `gpKpis(model)`
- L9212 `gpWeekData(model,w)` — v68: «¿Cuánto entrenas cada semana?» — series de trabajo por semana frente a tu media, en filas fáciles de leer.
- L9217 `gpWeekLabel(w,short)`
- L9218 `gpWeekly(model)`
- L9231 `gpMuscles(model)`
- L9239 `gpHeat(model)` — v68: «¿Qué días entrenas?» — las últimas 12 semanas, una fila por semana y un círculo por día.
- L9259 `gpExList(model)`
- L9266 `gpExDetail(model)`
- L9279 `gpDayFood(dt)`
- L9280 `gpNutrition(model)`
- L9287 `gpRecentPRs(model)`
- L9291 `gpSessions(model)`
- L9297 `gpSessionModal(id)`
- L9308 `gpWeekModal(w)`
- L9315 `gpSelect(key)`
- L9316 `gpClick(e)`
- L9328 `renderGym()`
- L9348 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L9357 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L9363 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L9388 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L9392 `showHelp()`
- L9396 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L9398 `markBackup()`
- L9402 `exportJSON()`
- L9407 `drawBackupReminder()`
- L9417 `applyDensity()`
- L9429 `syncDayComplete()`
- L9432 `drawMeals()` — Comidas del día de un vistazo.
- L9440 `filterLog()` — Buscador de Registro.
- L9453 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L9459 `recentFoods()`
- L9464 `quickChip(e,fav)`
- L9482 `drawQuickFoods()`
- L9511 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L9515 `toggleAddPanel(id)`
- L9527 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L9538 `pasteMessage(text,ok)`
- L9546 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L9557 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L9568 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L9574 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L9595 `storableState()`

### Render único: actualiza toda la página

- L9603 `nearView(el)`
- L9605 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L9609 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L9640 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L9641 constante `REF_TABLE`
- L9648 `refTargets(mode)`
- L9649 `syncMicroMode()`
- L9662 `mealByHour(h=new Date()`
- L9669 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L9680 `dataSummary(s)`
- L9684 `confirmImport(next,name)`
- L9691 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L9697 `checkUpdate()`
- L9702 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L9717 constante `GAP_PREFER`
- L9718 constante `GAP_SKIP`
- L9719 constante `GAP_UNIT`
- L9720 `gapQty(f,x)`
- L9721 `gapFoods(key,gap,ctx)`
- L9740 `weekSources(key,sum)`
- L9746 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L9759 `gapRow(x,open,meal,sum,ctx)`
- L9775 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L9800 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L9801 `isFemale(s=state)`
- L9802 `sexLabel(s=state)`
- L9803 `sexBadge(sex)`
- L9805 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L9806 constante `OPT_FEMALE`
- L9817 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba.
- L9818 `applySexOpt(sex)`
- L9820 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L9825 `cleanPreset(p,fb)`
- L9829 `dayNamesFor(types)`
- L9831 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L9841 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L9849 `profV()`
- L9850 `isTrainDay(i)`
- L9851 `activityName(i)`
- L9852 `dayFaf(i)`
- L9853 `presetDesc(cfg,shake)`
- L9857 `profileDescription()`
- L9865 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L9867 `wizCatalog()`
- L9868 `wizOpen(opts={})`
- L9883 `wizTitle()`
- L9884 `wizPaint(sameStep=true)`
- L9893 `wizSync()`
- L9906 `wizFoodOptions()`
- L9909 `wizPresetSummary(cfg,whey)`
- L9914 `wizPresetHTML(kind)`
- L9922 `wizPreview()`
- L9933 `wizHTML()`
- L9974 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L10058 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L10059 constante `SUPP_CATALOG`
- L10081 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L10082 constante `PEAT_BREAKFAST`
- L10083 constante `PEAT_SHAKE`
- L10085 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L10092 `benfoUser()`
- L10094 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L10110 `ico(n)`
- L10112 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L10121 `showTour(i=0)`
- L10133 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L10134 `hubAction(v)`
- L10142 constante `FORM_URL` — Llegan solas a una hoja de Google (formulario del creador de la app). Sin cuentas ni datos personales.
- L10143 constante `FORM_FIELDS`
- L10144 constante `FB_CATS`
- L10146 `openFeedback()`
- L10150 `feedbackData()`
- L10157 `feedbackText()`
- L10158 `sendFeedback()`
- L10171 `shareFeedback()`
- L10188 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L10195 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L10203 constante `I18N_EN`

### v59: idioma (español / inglés)

- L11813 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L11814 constante `WD_EN`
- L11815 `trOne(s)`
- L11823 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L11824 constante `ES_FOOD_GYM`
- L11861 `trFood(s)`
- L11873 constante `TR_TPL`
- L11907 `trLower(s)`
- L11908 `trTpl(s,attr)`
- L11909 constante `FOOD_SEL`
- L11910 `trText(s,attr=false)`
- L11920 `trNode(n)`
- L11935 `trEl(el)`
- L11943 `trTree(root)`
- L11952 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L11963 `setLang(l,quiet)`
- L11976 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter), solo en la web publicada

- L11985 constante `GC_CODE`
- L11986 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L11996 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L11997 `packMove()`
- L12005 `unpackMove(code)`
- L12014 `moveData()`
- L12024 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L12030 `checkMove(code)`

### Arranque

