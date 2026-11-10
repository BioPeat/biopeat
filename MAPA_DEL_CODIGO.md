# MAPA DEL CÓDIGO · BioPeat v71 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (839 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-6346; todo el JavaScript en `<script id="app">` (desde la línea 6347).

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

- L6407 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L6408 constante `AZUCAR_N`
- L6409 constante `USDA_N`
- L6415 constante `FOODS`
- L6417 constante `BASE_FAT_FIX`
- L6420 constante `EXTRA`
- L6421 constante `KEYS`
- L6423 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L6425 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L6429 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6430 constante `OPT`
- L6448 constante `LIMIT`
- L6449 `optInfo(k,goal)`
- L6456 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6464 `optLine(k,goal,unit)`
- L6471 `optRefHTML(k,goal,unit)`
- L6473 constante `DAYS`
- L6474 constante `FAF`
- L6476 constante `LOC`
- L6480 `number(v,min=0,max=1e6)`
- L6486 `decimalInputs(root=document)`
- L6487 `localDate(d=new Date()`
- L6488 `validDate(s)`
- L6493 `shift(s,n)`
- L6502 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6504 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6510 constante `DAY_TYPES`
- L6511 constante `NEW_V54`
- L6515 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6518 `bmr()` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6524 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6546 `cleanNutrients(o,required=false)`
- L6558 `cleanEntry(e)`
- L6563 `cleanPlan(p)`
- L6567 `planEntry(p)`
- L6576 `seedPlan(d,whichDate)`
- L6580 `ensureDay(d=date)`
- L6587 `effectiveEntries(d=day()`
- L6588 constante `SALTED_IDS`
- L6589 constante `SWEET_RE`
- L6590 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6608 `inferredNutrients(e)`
- L6647 `totals(entries=effectiveEntries()`
- L6656 `change(fn,message='Guardado')`
- L6660 `undo()`
- L6667 `toast(text,canUndo=false)`
- L6675 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6676 `onClick(fn)`
- L6678 `attempt(fn)`
- L6682 `modal(title,body)`
- L6691 `modalRestore()`
- L6701 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6702 `modalBack()`
- L6703 `goDate(d)`
- L6710 `renderHeader()`
- L6723 `renderRows(entries)`
- L6727 `entryValues(e)`
- L6728 `renderLog()`
- L6735 `fromFood(id,amount,meal)`
- L6741 `pantryId(name)`
- L6743 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6749 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6758 `recipe(kind)`
- L6765 `summary(entries)`
- L6769 `renderPresetInfo()`
- L6782 `stripCode(raw)`
- L6788 `parseBIO(raw,meal=$('meal-select')`
- L6794 `parseSmart(raw)`
- L6798 constante `COUNT`
- L6801 `nutrientFields(n,prefix='n_')`
- L6802 `readNutrients(form,prefix='n_')`
- L6807 `editEntry(id)`
- L6816 `editFood(id,pending=null)`
- L6821 `usageStats(days=90)`
- L6827 `renderFoods()`
- L6835 `nutrientSources(key)`
- L6842 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6843 `suppSlot(meal)`
- L6844 `renderSupps()`
- L6859 `editPlan(id)`
- L6866 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6886 `makePrompt(meal='Comida',note='')`
- L6891 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6895 `photoPrompt(meal,note)`
- L6898 `resetPhoto()`
- L6909 `openPhoto()`
- L6915 `shrinkPhoto(file)`
- L6918 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6944 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6951 `cleanFood(id,f)`
- L6955 `migrateBase(o)`
- L6974 `download(name,text,type)`
- L6983 `portable()`
- L7023 `syncAppIcons()`
- L7031 `downloadAppIcons()`
- L7068 constante `PROFILES_KEY`
- L7070 `ensureProfilesStore()`
- L7089 `saveProfilesStore(st)`
- L7093 `syncCurrentProfileToStore(rawStr)`
- L7099 `activeProfileName()`
- L7103 `renderProfilesList()`
- L7145 `switchProfile(id)`
- L7167 `deleteProfileById(id)`
- L7191 `refreshDrawerSummary()`
- L7208 `toggleLeftDrawer(force)`
- L7223 `buildAIExportText(rangeOverride)`
- L7473 `copyAIExport()`
- L7487 `downloadAIExport()`
- L7496 `renderDrawerChat()`
- L7515 `buildDrawerChatPrompt(question)`
- L7527 `askDrawerAI(rawQuestion)`
- L7614 `storageStatus()`
- L7620 `idbReadWrite(mode,value)`
- L7621 `openDB()`
- L7622 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L7635 `setQuantity(id,value,msg='Cantidad actualizada')`
- L7639 `niceStep(v)`
- L7640 `stepQuantity(id,dir)`
- L7694 `renderAppInfo()`
- L7709 `init()`
- L7736 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L7738 `setNav(v)`
- L7743 `go(v,focus)`
- L7754 constante `THEME_KEY`
- L7755 constante `SUN_SVG`
- L7756 constante `MOON_SVG`
- L7758 `syncThemeUI()`
- L7770 `toggleTheme()`
- L7779 `syncLogoTheme()`
- L7790 `applyMenuBtnState()`
- L7813 `syncDatePill()`
- L7824 `clampBtnPos(el,x,y)`
- L7834 `bindDraggableBtn(el,storeKey)`
- L7919 `bindDrawerGestures()`
- L7956 `animateValue(el,to,suffix='%',digits=0)`
- L7965 `tick(now)`
- L7968 `macroCard(key,name,color)`
- L7969 `renderToday()`
- L7992 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L7994 constante `HOME`
- L7996 `coachCandidates()`
- L8002 `coachIdeas(t,g,ref,meal)`
- L8015 `renderCoach()`
- L8035 `coachPrompt()`
- L8043 `nutrientDetailStandard(key)`
- L8057 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L8063 `upgradeTo12(s,o)`
- L8068 `benfotiamineTotals(entries=effectiveEntries()`
- L8077 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L8079 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L8091 `microStat(m,t=totals()`
- L8096 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L8104 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L8105 `ratioInfo(key,t=totals()`
- L8144 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L8161 constante `RATIO_ENDS`
- L8163 `ratioZones(i)` — v68: cada equilibrio tiene una zona «aceptable» (ni verde ni mala) y su meta visible en la tarjeta.
- L8171 `ratioTone(i)`
- L8176 constante `NEAR_HEAD`
- L8177 `ratioBar(i,big=false)`
- L8186 `ratioNeedBase(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L8204 `needHTML(i,t)`
- L8205 `ratioNeed(i,t=totals()`
- L8209 `adBalance(t=totals()`
- L8236 `hasZncuSupp(d=day()`
- L8239 `toggleZncuSupp()`
- L8267 `renderRatios()`
- L8276 `ratioDetail(key)`
- L8286 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L8303 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L8318 `renderMicroMap()`
- L8322 `nutrientDetailForDay(key)`
- L8327 `editTargetsForm()`
- L8337 `mealData()`
- L8342 `renderMealSegments()`
- L8350 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L8368 constante `FAT_KEYS`
- L8370 `fatData(entries=effectiveEntries()`
- L8376 `energyData(entries=effectiveEntries()`
- L8380 `segmentedBar(items,total,attr)`
- L8384 `renderMealChart()`
- L8389 `renderFat()`
- L8397 `fatDetail(key)`
- L8402 `energyDetail(key)`
- L8409 `portionCandidates(q='')`
- L8414 `openPortion()`
- L8427 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L8442 `templates()`
- L8446 `renderExtra()`
- L8457 `updateExtra(reset=true)`
- L8469 `addExtra(id,amount)`
- L8485 `shakePreview()`
- L8486 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L8501 constante `LENS`
- L8507 `lensKey(key)`
- L8508 `lensHTML(key)`
- L8512 `appendLens(key)`
- L8521 `weekDates()`

### IA en la página: conexión directa o por servidor

- L8531 constante `MEAL_WORD`
- L8532 `mealOfWord(w)`
- L8533 `mealFromText(raw,fallback)`
- L8537 `canonMeal(v,fallback)`
- L8545 `localMeal(raw,meal)`
- L8551 constante `AI_FALLBACK`
- L8552 `applyAIConfig(raw)`
- L8578 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L8579 `callGemini(model,key,prompt,img,signal,think=true)`
- L8597 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L8604 `aiProv(m=$('ai-mode')`
- L8605 `aiBase(mode)`
- L8614 `chatHeaders(mode,key)`
- L8621 `callChat(mode,model,key,prompt,img,signal)` — ChatGPT, Claude, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L8651 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L8659 constante `MODEL_PREF`
- L8660 `pickModel(ids)`
- L8665 `ensureModel(st)`
- L8676 `syncProvider()`
- L8689 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L8723 constante `AI_PREF`
- L8724 `aiConnected()`
- L8725 `syncAI()`
- L8727 `saveAIPrefs()`
- L8728 `loadAIPrefs()`
- L8729 `openAISetup()`
- L8735 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L8742 constante `MACROS`
- L8744 `cleanGoals(o,fallback)`
- L8749 `cleanCompare(o={})`
- L8753 `snapshotDay(d,reference='saved')`
- L8758 `upgradeTo17(s,o)`
- L8763 `entriesFor(d,source=weekSource)`
- L8767 `dayRow(dt,source=weekSource)`
- L8771 `goalsFor(dt)`
- L8777 `metricValue(r,key)`
- L8783 `targetOf(dt,key)`
- L8787 `weekSummary()`
- L8791 `aggregate(key,summary=weekSummary()`
- L8795 `tone(pct,mode='macro')`
- L8802 `pctText(a)`
- L8803 `weekProgress(a,color)`
- L8804 `renderWeekMicros(s)`
- L8816 `ratioAggregate(s,num,den)`
- L8820 `renderWeekRatios(s)`
- L8826 `renderWeekTable(s)`
- L8827 `weeklyDetail(key,oneDate=null)`
- L8836 `weekRatioDetail(key)`
- L8844 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L8850 `openDay(dt)`
- L8888 `withDayGoals(fn)`
- L8893 `renderMicros()`
- L8894 `nutrientDetail(key)`
- L8895 `editTargets()`
- L8896 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L8906 `summaryFor(start)`
- L8910 `ringSVG(pct,color,marker)`
- L8912 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L8916 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L8931 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L8932 `macroTone(p)`
- L8933 `dayMacroPct(dt,k)`
- L8934 `renderWeekly()`
- L8957 `weekDetail(dt,picked)`
- L8965 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L8975 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L8981 `sparkline(pts)`
- L8987 `renderCalendar()`
- L9004 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L9005 `splitMeals(raw)`
- L9015 `localDay(raw,fallback)`
- L9022 `promptDay(raw,fallback)`
- L9023 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L9045 `parseCsv(text)`
- L9060 `hevyDate(value,format='auto')`
- L9077 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L9092 constante `GYM_APPS`
- L9094 `gymSig(headers)`
- L9095 `gymApp(headers)`
- L9096 `hevyMapping()`
- L9097 `gymSaved()`
- L9098 `renderMapping(parsed)`
- L9115 `optionalNum(v,min=0,max=1e7)`
- L9120 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L9127 `buildHevy(parsed,map)`
- L9161 `cleanWorkout(s)`
- L9168 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L9183 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L9184 constante `GP_ALIAS`
- L9194 `gpNorm(s)`
- L9195 `gpKey(name)`
- L9199 `gpF(n,d=0)`
- L9200 `gpDate(d,opt)`
- L9201 `gpMonday(d)`
- L9202 constante `GP_GROUPS`
- L9217 constante `GP_COLORS`
- L9218 `gpGroup(name)`
- L9219 `gpWorkSets(s)`
- L9220 `gpModel()`
- L9244 `gpSessionMetrics(e,sets)`
- L9259 constante `GP_METRICS`
- L9264 `gpMetricsFor(e)`
- L9265 `gpRangeHist(e)`
- L9266 `gpPRs(model)`
- L9289 `gpStatus(e)`
- L9307 `gpNext(e)`
- L9315 `gpChart(e)`
- L9343 `gpPointDetail(e)`
- L9349 `gpRepTable(e)`
- L9356 `gpKpis(model)`
- L9365 `gpWeekData(model,w)` — Datos de una semana de gimnasio (series por músculo y sesiones).
- L9370 `gpWeekLabel(w,short)`
- L9371 `gpWeekly(model)`
- L9390 `gpMuscles(model)`
- L9398 `gpHeat(model)` — v69: «Constancia» — mapa de días entrenados (como antes), con días de la semana, meses, intensidad y detalle al tocar.
- L9418 `gpExList(model)`
- L9425 `gpExDetail(model)`
- L9438 `gpDayFood(dt)`
- L9439 `gpNutrition(model)`
- L9446 `gpRecentPRs(model)`
- L9450 `gpSessions(model)`
- L9456 `gpSessionModal(id)`
- L9467 `gpWeekModal(w)`
- L9474 `gpSelect(key)`
- L9475 `gpClick(e)`
- L9491 `renderGym()`
- L9511 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L9520 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L9526 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L9551 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L9555 `showHelp()`
- L9559 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L9561 `markBackup()`
- L9565 `exportJSON()`
- L9570 `drawBackupReminder()`
- L9580 `applyDensity()`
- L9592 `syncDayComplete()`
- L9595 `drawMeals()` — Comidas del día de un vistazo.
- L9603 `filterLog()` — Buscador de Registro.
- L9616 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L9622 `recentFoods()`
- L9627 `quickChip(e,fav)`
- L9645 `drawQuickFoods()`
- L9674 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L9678 `toggleAddPanel(id)`
- L9690 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L9701 `pasteMessage(text,ok)`
- L9709 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L9720 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L9731 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L9737 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L9758 `storableState()`

### Render único: actualiza toda la página

- L9766 `nearView(el)`
- L9768 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L9772 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L9803 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L9804 constante `REF_TABLE`
- L9811 `refTargets(mode)`
- L9812 `syncMicroMode()`
- L9825 `mealByHour(h=new Date()`
- L9832 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L9843 `dataSummary(s)`
- L9847 `confirmImport(next,name)`
- L9854 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L9860 `checkUpdate()`
- L9865 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L9880 constante `GAP_PREFER`
- L9881 constante `GAP_SKIP`
- L9882 constante `GAP_UNIT`
- L9883 `gapQty(f,x)`
- L9884 `gapFoods(key,gap,ctx)`
- L9903 `weekSources(key,sum)`
- L9909 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L9922 `gapRow(x,open,meal,sum,ctx)`
- L9938 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L9963 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L9964 `isFemale(s=state)`
- L9965 `sexLabel(s=state)`
- L9966 `sexBadge(sex)`
- L9968 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L9969 constante `OPT_FEMALE`
- L9980 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba.
- L9981 `applySexOpt(sex)`
- L9983 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L9988 `cleanPreset(p,fb)`
- L9992 `dayNamesFor(types)`
- L9994 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L10004 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L10012 `profV()`
- L10013 `isTrainDay(i)`
- L10014 `activityName(i)`
- L10015 `dayFaf(i)`
- L10016 `presetDesc(cfg,shake)`
- L10020 `profileDescription()`
- L10028 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L10030 `wizCatalog()`
- L10031 `wizOpen(opts={})`
- L10046 `wizTitle()`
- L10047 `wizPaint(sameStep=true)`
- L10056 `wizSync()`
- L10069 `wizFoodOptions()`
- L10072 `wizPresetSummary(cfg,whey)`
- L10077 `wizPresetHTML(kind)`
- L10085 `wizPreview()`
- L10096 `wizHTML()`
- L10137 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L10221 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L10222 constante `SUPP_CATALOG`
- L10244 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L10245 constante `PEAT_BREAKFAST`
- L10246 constante `PEAT_SHAKE`
- L10248 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L10255 `benfoUser()`
- L10257 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L10273 `ico(n)`
- L10275 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L10284 `showTour(i=0)`
- L10296 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L10297 `hubAction(v)`
- L10305 constante `FORM_URL` — Llegan solas a una hoja de Google (formulario del creador de la app). Sin cuentas ni datos personales.
- L10306 constante `FORM_FIELDS`
- L10307 constante `FB_CATS`
- L10309 `openFeedback()`
- L10313 `feedbackData()`
- L10320 `feedbackText()`
- L10321 `sendFeedback()`
- L10334 `shareFeedback()`
- L10351 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L10358 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L10366 constante `I18N_EN`

### v59: idioma (español / inglés)

- L12017 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L12018 constante `WD_EN`
- L12019 `trOne(s)`
- L12027 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L12028 constante `ES_FOOD_GYM`
- L12065 `trFood(s)`
- L12077 constante `TR_TPL`
- L12111 `trLower(s)`
- L12112 `trTpl(s,attr)`
- L12113 constante `FOOD_SEL`
- L12114 `trText(s,attr=false)`
- L12124 `trNode(n)`
- L12139 `trEl(el)`
- L12147 `trTree(root)`
- L12156 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L12167 `setLang(l,quiet)`
- L12180 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter), solo en la web publicada

- L12189 constante `GC_CODE`
- L12190 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L12200 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L12201 `packMove()`
- L12209 `unpackMove(code)`
- L12218 `moveData()`
- L12228 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L12234 `checkMove(code)`
- L12253 `aiFrameworkLines()` — v69: marco de referencia del informe para IA. Así cualquier IA, aunque no conozca la app ni al usuario, sabe con qué comparar.

### Arranque

