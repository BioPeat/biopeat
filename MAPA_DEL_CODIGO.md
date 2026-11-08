# MAPA DEL CÓDIGO · BioPeat v70 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (834 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-6346; todo el JavaScript en `<script id="app">` (desde la línea 6347).

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

- L6406 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L6407 constante `AZUCAR_N`
- L6408 constante `USDA_N`
- L6414 constante `FOODS`
- L6416 constante `BASE_FAT_FIX`
- L6419 constante `EXTRA`
- L6420 constante `KEYS`
- L6422 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L6424 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L6428 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6429 constante `OPT`
- L6447 constante `LIMIT`
- L6448 `optInfo(k,goal)`
- L6455 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6463 `optLine(k,goal,unit)`
- L6470 `optRefHTML(k,goal,unit)`
- L6472 constante `DAYS`
- L6473 constante `FAF`
- L6475 constante `LOC`
- L6479 `number(v,min=0,max=1e6)`
- L6485 `decimalInputs(root=document)`
- L6486 `localDate(d=new Date()`
- L6487 `validDate(s)`
- L6492 `shift(s,n)`
- L6501 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6503 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6509 constante `DAY_TYPES`
- L6510 constante `NEW_V54`
- L6514 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6517 `bmr()` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6523 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6545 `cleanNutrients(o,required=false)`
- L6557 `cleanEntry(e)`
- L6562 `cleanPlan(p)`
- L6566 `planEntry(p)`
- L6575 `seedPlan(d,whichDate)`
- L6579 `ensureDay(d=date)`
- L6586 `effectiveEntries(d=day()`
- L6587 constante `SALTED_IDS`
- L6588 constante `SWEET_RE`
- L6589 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6607 `inferredNutrients(e)`
- L6646 `totals(entries=effectiveEntries()`
- L6655 `change(fn,message='Guardado')`
- L6659 `undo()`
- L6666 `toast(text,canUndo=false)`
- L6674 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6675 `onClick(fn)`
- L6677 `attempt(fn)`
- L6681 `modal(title,body)`
- L6690 `modalRestore()`
- L6700 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6701 `modalBack()`
- L6702 `goDate(d)`
- L6709 `renderHeader()`
- L6722 `renderRows(entries)`
- L6726 `entryValues(e)`
- L6727 `renderLog()`
- L6734 `fromFood(id,amount,meal)`
- L6740 `pantryId(name)`
- L6742 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6748 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6757 `recipe(kind)`
- L6764 `summary(entries)`
- L6768 `renderPresetInfo()`
- L6781 `stripCode(raw)`
- L6787 `parseBIO(raw,meal=$('meal-select')`
- L6793 `parseSmart(raw)`
- L6797 constante `COUNT`
- L6800 `nutrientFields(n,prefix='n_')`
- L6801 `readNutrients(form,prefix='n_')`
- L6806 `editEntry(id)`
- L6815 `editFood(id,pending=null)`
- L6820 `usageStats(days=90)`
- L6826 `renderFoods()`
- L6834 `nutrientSources(key)`
- L6841 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6842 `suppSlot(meal)`
- L6843 `renderSupps()`
- L6858 `editPlan(id)`
- L6865 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6885 `makePrompt(meal='Comida',note='')`
- L6890 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6894 `photoPrompt(meal,note)`
- L6897 `resetPhoto()`
- L6908 `openPhoto()`
- L6914 `shrinkPhoto(file)`
- L6917 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6943 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6950 `cleanFood(id,f)`
- L6954 `migrateBase(o)`
- L6973 `download(name,text,type)`
- L6982 `portable()`
- L7022 `syncAppIcons()`
- L7030 `downloadAppIcons()`
- L7067 constante `PROFILES_KEY`
- L7069 `ensureProfilesStore()`
- L7088 `saveProfilesStore(st)`
- L7092 `syncCurrentProfileToStore(rawStr)`
- L7098 `activeProfileName()`
- L7102 `renderProfilesList()`
- L7144 `switchProfile(id)`
- L7166 `deleteProfileById(id)`
- L7190 `refreshDrawerSummary()`
- L7207 `toggleLeftDrawer(force)`
- L7222 `buildAIExportText(rangeOverride)`
- L7472 `copyAIExport()`
- L7486 `downloadAIExport()`
- L7495 `renderDrawerChat()`
- L7514 `buildDrawerChatPrompt(question)`
- L7526 `askDrawerAI(rawQuestion)`
- L7613 `storageStatus()`
- L7619 `idbReadWrite(mode,value)`
- L7620 `openDB()`
- L7621 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L7634 `setQuantity(id,value,msg='Cantidad actualizada')`
- L7638 `niceStep(v)`
- L7639 `stepQuantity(id,dir)`
- L7693 `renderAppInfo()`
- L7708 `init()`
- L7735 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L7737 `setNav(v)`
- L7742 `go(v,focus)`
- L7753 constante `THEME_KEY`
- L7754 constante `SUN_SVG`
- L7755 constante `MOON_SVG`
- L7757 `syncThemeUI()`
- L7769 `toggleTheme()`
- L7778 `syncLogoTheme()`
- L7789 `applyMenuBtnState()`
- L7812 `syncDatePill()`
- L7823 `clampBtnPos(el,x,y)`
- L7833 `bindDraggableBtn(el,storeKey)`
- L7918 `bindDrawerGestures()`
- L7955 `animateValue(el,to,suffix='%',digits=0)`
- L7964 `tick(now)`
- L7967 `macroCard(key,name,color)`
- L7968 `renderToday()`
- L7991 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L7993 constante `HOME`
- L7995 `coachCandidates()`
- L8001 `coachIdeas(t,g,ref,meal)`
- L8014 `renderCoach()`
- L8034 `coachPrompt()`
- L8042 `nutrientDetailStandard(key)`
- L8056 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L8062 `upgradeTo12(s,o)`
- L8067 `benfotiamineTotals(entries=effectiveEntries()`
- L8076 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L8078 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L8090 `microStat(m,t=totals()`
- L8095 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L8103 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L8104 `ratioInfo(key,t=totals()`
- L8139 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L8156 constante `RATIO_ENDS`
- L8158 `ratioZones(i)` — v68: cada equilibrio tiene una zona «aceptable» (ni verde ni mala) y su meta visible en la tarjeta.
- L8166 `ratioTone(i)`
- L8171 constante `NEAR_HEAD`
- L8172 `ratioBar(i,big=false)`
- L8181 `ratioNeedBase(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L8198 `needHTML(i,t)`
- L8199 `ratioNeed(i,t=totals()`
- L8203 `hasZncuSupp(d=day()`
- L8206 `toggleZncuSupp()`
- L8234 `renderRatios()`
- L8243 `ratioDetail(key)`
- L8253 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L8270 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L8285 `renderMicroMap()`
- L8289 `nutrientDetailForDay(key)`
- L8294 `editTargetsForm()`
- L8304 `mealData()`
- L8309 `renderMealSegments()`
- L8317 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L8335 constante `FAT_KEYS`
- L8337 `fatData(entries=effectiveEntries()`
- L8343 `energyData(entries=effectiveEntries()`
- L8347 `segmentedBar(items,total,attr)`
- L8351 `renderMealChart()`
- L8356 `renderFat()`
- L8364 `fatDetail(key)`
- L8369 `energyDetail(key)`
- L8376 `portionCandidates(q='')`
- L8381 `openPortion()`
- L8394 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L8409 `templates()`
- L8413 `renderExtra()`
- L8424 `updateExtra(reset=true)`
- L8436 `addExtra(id,amount)`
- L8452 `shakePreview()`
- L8453 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L8468 constante `LENS`
- L8474 `lensKey(key)`
- L8475 `lensHTML(key)`
- L8479 `appendLens(key)`
- L8488 `weekDates()`

### IA en la página: conexión directa o por servidor

- L8498 constante `MEAL_WORD`
- L8499 `mealOfWord(w)`
- L8500 `mealFromText(raw,fallback)`
- L8504 `canonMeal(v,fallback)`
- L8512 `localMeal(raw,meal)`
- L8518 constante `AI_FALLBACK`
- L8519 `applyAIConfig(raw)`
- L8545 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L8546 `callGemini(model,key,prompt,img,signal,think=true)`
- L8564 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L8571 `aiProv(m=$('ai-mode')`
- L8572 `aiBase(mode)`
- L8581 `chatHeaders(mode,key)`
- L8588 `callChat(mode,model,key,prompt,img,signal)` — ChatGPT, Claude, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L8618 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L8626 constante `MODEL_PREF`
- L8627 `pickModel(ids)`
- L8632 `ensureModel(st)`
- L8643 `syncProvider()`
- L8656 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L8690 constante `AI_PREF`
- L8691 `aiConnected()`
- L8692 `syncAI()`
- L8694 `saveAIPrefs()`
- L8695 `loadAIPrefs()`
- L8696 `openAISetup()`
- L8702 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L8709 constante `MACROS`
- L8711 `cleanGoals(o,fallback)`
- L8716 `cleanCompare(o={})`
- L8720 `snapshotDay(d,reference='saved')`
- L8725 `upgradeTo17(s,o)`
- L8730 `entriesFor(d,source=weekSource)`
- L8734 `dayRow(dt,source=weekSource)`
- L8738 `goalsFor(dt)`
- L8744 `metricValue(r,key)`
- L8750 `targetOf(dt,key)`
- L8754 `weekSummary()`
- L8758 `aggregate(key,summary=weekSummary()`
- L8762 `tone(pct,mode='macro')`
- L8769 `pctText(a)`
- L8770 `weekProgress(a,color)`
- L8771 `renderWeekMicros(s)`
- L8783 `ratioAggregate(s,num,den)`
- L8787 `renderWeekRatios(s)`
- L8793 `renderWeekTable(s)`
- L8794 `weeklyDetail(key,oneDate=null)`
- L8803 `weekRatioDetail(key)`
- L8811 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L8817 `openDay(dt)`
- L8855 `withDayGoals(fn)`
- L8860 `renderMicros()`
- L8861 `nutrientDetail(key)`
- L8862 `editTargets()`
- L8863 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L8873 `summaryFor(start)`
- L8877 `ringSVG(pct,color,marker)`
- L8879 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L8883 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L8898 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L8899 `macroTone(p)`
- L8900 `dayMacroPct(dt,k)`
- L8901 `renderWeekly()`
- L8924 `weekDetail(dt,picked)`
- L8932 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L8942 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L8948 `sparkline(pts)`
- L8954 `renderCalendar()`
- L8971 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L8972 `splitMeals(raw)`
- L8982 `localDay(raw,fallback)`
- L8989 `promptDay(raw,fallback)`
- L8990 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L9012 `parseCsv(text)`
- L9027 `hevyDate(value,format='auto')`
- L9044 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L9059 constante `GYM_APPS`
- L9061 `gymSig(headers)`
- L9062 `gymApp(headers)`
- L9063 `hevyMapping()`
- L9064 `gymSaved()`
- L9065 `renderMapping(parsed)`
- L9082 `optionalNum(v,min=0,max=1e7)`
- L9087 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L9094 `buildHevy(parsed,map)`
- L9128 `cleanWorkout(s)`
- L9135 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L9150 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L9151 constante `GP_ALIAS`
- L9161 `gpNorm(s)`
- L9162 `gpKey(name)`
- L9166 `gpF(n,d=0)`
- L9167 `gpDate(d,opt)`
- L9168 `gpMonday(d)`
- L9169 constante `GP_GROUPS`
- L9184 constante `GP_COLORS`
- L9185 `gpGroup(name)`
- L9186 `gpWorkSets(s)`
- L9187 `gpModel()`
- L9211 `gpSessionMetrics(e,sets)`
- L9226 constante `GP_METRICS`
- L9231 `gpMetricsFor(e)`
- L9232 `gpRangeHist(e)`
- L9233 `gpPRs(model)`
- L9256 `gpStatus(e)`
- L9274 `gpNext(e)`
- L9282 `gpChart(e)`
- L9310 `gpPointDetail(e)`
- L9316 `gpRepTable(e)`
- L9323 `gpKpis(model)`
- L9332 `gpWeekData(model,w)` — Datos de una semana de gimnasio (series por músculo y sesiones).
- L9337 `gpWeekLabel(w,short)`
- L9338 `gpWeekly(model)`
- L9357 `gpMuscles(model)`
- L9365 `gpHeat(model)` — v69: «Constancia» — mapa de días entrenados (como antes), con días de la semana, meses, intensidad y detalle al tocar.
- L9385 `gpExList(model)`
- L9392 `gpExDetail(model)`
- L9405 `gpDayFood(dt)`
- L9406 `gpNutrition(model)`
- L9413 `gpRecentPRs(model)`
- L9417 `gpSessions(model)`
- L9423 `gpSessionModal(id)`
- L9434 `gpWeekModal(w)`
- L9441 `gpSelect(key)`
- L9442 `gpClick(e)`
- L9458 `renderGym()`
- L9478 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L9487 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L9493 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L9518 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L9522 `showHelp()`
- L9526 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L9528 `markBackup()`
- L9532 `exportJSON()`
- L9537 `drawBackupReminder()`
- L9547 `applyDensity()`
- L9559 `syncDayComplete()`
- L9562 `drawMeals()` — Comidas del día de un vistazo.
- L9570 `filterLog()` — Buscador de Registro.
- L9583 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L9589 `recentFoods()`
- L9594 `quickChip(e,fav)`
- L9612 `drawQuickFoods()`
- L9641 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L9645 `toggleAddPanel(id)`
- L9657 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L9668 `pasteMessage(text,ok)`
- L9676 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L9687 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L9698 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L9704 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L9725 `storableState()`

### Render único: actualiza toda la página

- L9733 `nearView(el)`
- L9735 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L9739 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L9770 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L9771 constante `REF_TABLE`
- L9778 `refTargets(mode)`
- L9779 `syncMicroMode()`
- L9792 `mealByHour(h=new Date()`
- L9799 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L9810 `dataSummary(s)`
- L9814 `confirmImport(next,name)`
- L9821 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L9827 `checkUpdate()`
- L9832 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L9847 constante `GAP_PREFER`
- L9848 constante `GAP_SKIP`
- L9849 constante `GAP_UNIT`
- L9850 `gapQty(f,x)`
- L9851 `gapFoods(key,gap,ctx)`
- L9870 `weekSources(key,sum)`
- L9876 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L9889 `gapRow(x,open,meal,sum,ctx)`
- L9905 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L9930 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L9931 `isFemale(s=state)`
- L9932 `sexLabel(s=state)`
- L9933 `sexBadge(sex)`
- L9935 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L9936 constante `OPT_FEMALE`
- L9947 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba.
- L9948 `applySexOpt(sex)`
- L9950 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L9955 `cleanPreset(p,fb)`
- L9959 `dayNamesFor(types)`
- L9961 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L9971 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L9979 `profV()`
- L9980 `isTrainDay(i)`
- L9981 `activityName(i)`
- L9982 `dayFaf(i)`
- L9983 `presetDesc(cfg,shake)`
- L9987 `profileDescription()`
- L9995 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L9997 `wizCatalog()`
- L9998 `wizOpen(opts={})`
- L10013 `wizTitle()`
- L10014 `wizPaint(sameStep=true)`
- L10023 `wizSync()`
- L10036 `wizFoodOptions()`
- L10039 `wizPresetSummary(cfg,whey)`
- L10044 `wizPresetHTML(kind)`
- L10052 `wizPreview()`
- L10063 `wizHTML()`
- L10104 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L10188 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L10189 constante `SUPP_CATALOG`
- L10211 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L10212 constante `PEAT_BREAKFAST`
- L10213 constante `PEAT_SHAKE`
- L10215 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L10222 `benfoUser()`
- L10224 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L10240 `ico(n)`
- L10242 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L10251 `showTour(i=0)`
- L10263 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L10264 `hubAction(v)`
- L10272 constante `FORM_URL` — Llegan solas a una hoja de Google (formulario del creador de la app). Sin cuentas ni datos personales.
- L10273 constante `FORM_FIELDS`
- L10274 constante `FB_CATS`
- L10276 `openFeedback()`
- L10280 `feedbackData()`
- L10287 `feedbackText()`
- L10288 `sendFeedback()`
- L10301 `shareFeedback()`
- L10318 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L10325 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L10333 constante `I18N_EN`

### v59: idioma (español / inglés)

- L11974 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L11975 constante `WD_EN`
- L11976 `trOne(s)`
- L11984 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L11985 constante `ES_FOOD_GYM`
- L12022 `trFood(s)`
- L12034 constante `TR_TPL`
- L12068 `trLower(s)`
- L12069 `trTpl(s,attr)`
- L12070 constante `FOOD_SEL`
- L12071 `trText(s,attr=false)`
- L12081 `trNode(n)`
- L12096 `trEl(el)`
- L12104 `trTree(root)`
- L12113 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L12124 `setLang(l,quiet)`
- L12137 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter), solo en la web publicada

- L12146 constante `GC_CODE`
- L12147 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L12157 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L12158 `packMove()`
- L12166 `unpackMove(code)`
- L12175 `moveData()`
- L12185 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L12191 `checkMove(code)`
- L12210 `aiFrameworkLines()` — v69: marco de referencia del informe para IA. Así cualquier IA, aunque no conozca la app ni al usuario, sabe con qué comparar.

### Arranque

