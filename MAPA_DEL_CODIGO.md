# MAPA DEL CÓDIGO · BioPeat v62 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (773 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-6045; todo el JavaScript en `<script id="app">` (desde la línea 6046).

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

- L6097 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L6098 constante `AZUCAR_N`
- L6099 constante `USDA_N`
- L6105 constante `FOODS`
- L6107 constante `BASE_FAT_FIX`
- L6110 constante `EXTRA`
- L6111 constante `KEYS`
- L6113 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L6115 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L6119 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6120 constante `OPT`
- L6138 constante `LIMIT`
- L6139 `optInfo(k,goal)`
- L6146 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6154 `optLine(k,goal,unit)`
- L6161 `optRefHTML(k,goal,unit)`
- L6163 constante `DAYS`
- L6164 constante `FAF`
- L6166 constante `LOC`
- L6170 `number(v,min=0,max=1e6)`
- L6176 `decimalInputs(root=document)`
- L6177 `localDate(d=new Date()`
- L6178 `validDate(s)`
- L6183 `shift(s,n)`
- L6192 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6194 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6200 constante `DAY_TYPES`
- L6201 constante `NEW_V54`
- L6205 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6208 `bmr()` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6214 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6236 `cleanNutrients(o,required=false)`
- L6248 `cleanEntry(e)`
- L6253 `cleanPlan(p)`
- L6257 `planEntry(p)`
- L6266 `seedPlan(d,whichDate)`
- L6270 `ensureDay(d=date)`
- L6277 `effectiveEntries(d=day()`
- L6278 constante `SALTED_IDS`
- L6279 constante `SWEET_RE`
- L6280 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6298 `inferredNutrients(e)`
- L6337 `totals(entries=effectiveEntries()`
- L6346 `change(fn,message='Guardado')`
- L6350 `undo()`
- L6357 `toast(text,canUndo=false)`
- L6365 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6366 `onClick(fn)`
- L6368 `attempt(fn)`
- L6372 `modal(title,body)`
- L6381 `modalRestore()`
- L6391 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6392 `modalBack()`
- L6393 `goDate(d)`
- L6400 `renderHeader()`
- L6412 `renderRows(entries)`
- L6416 `entryValues(e)`
- L6417 `renderLog()`
- L6424 `fromFood(id,amount,meal)`
- L6430 `pantryId(name)`
- L6432 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6438 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6447 `recipe(kind)`
- L6454 `summary(entries)`
- L6458 `renderPresetInfo()`
- L6471 `stripCode(raw)`
- L6477 `parseBIO(raw,meal=$('meal-select')`
- L6483 `parseSmart(raw)`
- L6487 constante `COUNT`
- L6490 `nutrientFields(n,prefix='n_')`
- L6491 `readNutrients(form,prefix='n_')`
- L6496 `editEntry(id)`
- L6505 `editFood(id,pending=null)`
- L6510 `usageStats(days=90)`
- L6516 `renderFoods()`
- L6524 `nutrientSources(key)`
- L6531 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6532 `suppSlot(meal)`
- L6533 `renderSupps()`
- L6548 `editPlan(id)`
- L6555 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6575 `makePrompt(meal='Comida',note='')`
- L6580 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6584 `photoPrompt(meal,note)`
- L6587 `resetPhoto()`
- L6598 `openPhoto()`
- L6604 `shrinkPhoto(file)`
- L6607 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6633 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6640 `cleanFood(id,f)`
- L6644 `migrateBase(o)`
- L6663 `download(name,text,type)`
- L6672 `portable()`
- L6709 `syncAppIcons()`
- L6717 `downloadAppIcons()`
- L6754 constante `PROFILES_KEY`
- L6756 `ensureProfilesStore()`
- L6775 `saveProfilesStore(st)`
- L6779 `syncCurrentProfileToStore(rawStr)`
- L6785 `activeProfileName()`
- L6789 `renderProfilesList()`
- L6831 `switchProfile(id)`
- L6853 `deleteProfileById(id)`
- L6877 `refreshDrawerSummary()`
- L6894 `toggleLeftDrawer(force)`
- L6909 `buildAIExportText(rangeOverride)`
- L7157 `copyAIExport()`
- L7171 `downloadAIExport()`
- L7180 `renderDrawerChat()`
- L7199 `buildDrawerChatPrompt(question)`
- L7211 `askDrawerAI(rawQuestion)`
- L7298 `storageStatus()`
- L7304 `idbReadWrite(mode,value)`
- L7305 `openDB()`
- L7306 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L7319 `setQuantity(id,value,msg='Cantidad actualizada')`
- L7323 `niceStep(v)`
- L7324 `stepQuantity(id,dir)`
- L7378 `renderAppInfo()`
- L7393 `init()`
- L7417 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L7419 `setNav(v)`
- L7424 `go(v,focus)`
- L7435 constante `THEME_KEY`
- L7436 constante `SUN_SVG`
- L7437 constante `MOON_SVG`
- L7439 `syncThemeUI()`
- L7451 `toggleTheme()`
- L7459 `syncDatePill()`
- L7463 `animateValue(el,to,suffix='%',digits=0)`
- L7472 `tick(now)`
- L7475 `macroCard(key,name,color)`
- L7476 `renderToday()`
- L7499 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L7501 constante `HOME`
- L7503 `coachCandidates()`
- L7509 `coachIdeas(t,g,ref,meal)`
- L7522 `renderCoach()`
- L7540 `coachPrompt()`
- L7548 `nutrientDetailStandard(key)`
- L7562 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L7568 `upgradeTo12(s,o)`
- L7573 `benfotiamineTotals(entries=effectiveEntries()`
- L7582 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L7584 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L7596 `microStat(m,t=totals()`
- L7601 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L7609 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L7610 `ratioInfo(key,t=totals()`
- L7645 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L7662 constante `RATIO_ENDS`
- L7663 `ratioBar(i,big=false)`
- L7668 `ratioNeed(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L7685 `needHTML(i,t)`
- L7686 `renderRatios()`
- L7691 `ratioDetail(key)`
- L7701 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L7718 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L7733 `renderMicroMap()`
- L7737 `nutrientDetailForDay(key)`
- L7742 `editTargetsForm()`
- L7752 `mealData()`
- L7757 `renderMealSegments()`
- L7765 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L7775 constante `FAT_KEYS`
- L7777 `fatData(entries=effectiveEntries()`
- L7783 `energyData(entries=effectiveEntries()`
- L7787 `segmentedBar(items,total,attr)`
- L7791 `renderMealChart()`
- L7796 `renderFat()`
- L7804 `fatDetail(key)`
- L7809 `energyDetail(key)`
- L7816 `portionCandidates(q='')`
- L7821 `openPortion()`
- L7834 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L7849 `templates()`
- L7853 `renderExtra()`
- L7864 `updateExtra(reset=true)`
- L7876 `addExtra(id,amount)`
- L7892 `shakePreview()`
- L7893 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L7908 constante `LENS`
- L7914 `lensKey(key)`
- L7915 `lensHTML(key)`
- L7919 `appendLens(key)`
- L7928 `weekDates()`

### IA en la página: conexión directa o por servidor

- L7938 constante `MEAL_WORD`
- L7939 `mealOfWord(w)`
- L7940 `mealFromText(raw,fallback)`
- L7944 `canonMeal(v,fallback)`
- L7952 `localMeal(raw,meal)`
- L7958 constante `AI_FALLBACK`
- L7959 `applyAIConfig(raw)`
- L7985 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L7986 `callGemini(model,key,prompt,img,signal,think=true)`
- L8004 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L8011 `aiProv(m=$('ai-mode')`
- L8012 `aiBase(mode)`
- L8021 `chatHeaders(mode,key)`
- L8028 `callChat(mode,model,key,prompt,img,signal)` — ChatGPT, Claude, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L8058 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L8066 constante `MODEL_PREF`
- L8067 `pickModel(ids)`
- L8072 `ensureModel(st)`
- L8083 `syncProvider()`
- L8096 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L8130 constante `AI_PREF`
- L8131 `aiConnected()`
- L8132 `syncAI()`
- L8134 `saveAIPrefs()`
- L8135 `loadAIPrefs()`
- L8136 `openAISetup()`
- L8142 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L8149 constante `MACROS`
- L8151 `cleanGoals(o,fallback)`
- L8156 `cleanCompare(o={})`
- L8160 `snapshotDay(d,reference='saved')`
- L8165 `upgradeTo17(s,o)`
- L8170 `entriesFor(d,source=weekSource)`
- L8174 `dayRow(dt,source=weekSource)`
- L8178 `goalsFor(dt)`
- L8184 `metricValue(r,key)`
- L8190 `targetOf(dt,key)`
- L8194 `weekSummary()`
- L8198 `aggregate(key,summary=weekSummary()`
- L8202 `tone(pct,mode='macro')`
- L8209 `pctText(a)`
- L8210 `weekProgress(a,color)`
- L8211 `renderWeekMicros(s)`
- L8223 `ratioAggregate(s,num,den)`
- L8227 `renderWeekRatios(s)`
- L8233 `renderWeekTable(s)`
- L8234 `weeklyDetail(key,oneDate=null)`
- L8243 `weekRatioDetail(key)`
- L8251 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L8257 `openDay(dt)`
- L8295 `withDayGoals(fn)`
- L8300 `renderMicros()`
- L8301 `nutrientDetail(key)`
- L8302 `editTargets()`
- L8303 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L8313 `summaryFor(start)`
- L8317 `ringSVG(pct,color,marker)`
- L8319 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L8323 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L8338 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L8339 `macroTone(p)`
- L8340 `dayMacroPct(dt,k)`
- L8341 `renderWeekly()`
- L8364 `weekDetail(dt,picked)`
- L8372 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L8382 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L8388 `sparkline(pts)`
- L8394 `renderCalendar()`
- L8411 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L8412 `splitMeals(raw)`
- L8422 `localDay(raw,fallback)`
- L8429 `promptDay(raw,fallback)`
- L8430 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L8452 `parseCsv(text)`
- L8467 `hevyDate(value,format='auto')`
- L8484 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L8499 constante `GYM_APPS`
- L8501 `gymSig(headers)`
- L8502 `gymApp(headers)`
- L8503 `hevyMapping()`
- L8504 `gymSaved()`
- L8505 `renderMapping(parsed)`
- L8522 `optionalNum(v,min=0,max=1e7)`
- L8527 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L8534 `buildHevy(parsed,map)`
- L8568 `cleanWorkout(s)`
- L8575 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L8590 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L8591 constante `GP_ALIAS`
- L8601 `gpNorm(s)`
- L8602 `gpKey(name)`
- L8606 `gpF(n,d=0)`
- L8607 `gpDate(d,opt)`
- L8608 `gpMonday(d)`
- L8609 constante `GP_GROUPS`
- L8624 constante `GP_COLORS`
- L8625 `gpGroup(name)`
- L8626 `gpWorkSets(s)`
- L8627 `gpModel()`
- L8651 `gpSessionMetrics(e,sets)`
- L8666 constante `GP_METRICS`
- L8671 `gpMetricsFor(e)`
- L8672 `gpRangeHist(e)`
- L8673 `gpPRs(model)`
- L8696 `gpStatus(e)`
- L8714 `gpNext(e)`
- L8722 `gpChart(e)`
- L8750 `gpPointDetail(e)`
- L8756 `gpRepTable(e)`
- L8763 `gpKpis(model)`
- L8771 `gpWeekly(model)`
- L8777 `gpMuscles(model)`
- L8784 `gpHeat(model)`
- L8791 `gpExList(model)`
- L8798 `gpExDetail(model)`
- L8811 `gpDayFood(dt)`
- L8812 `gpNutrition(model)`
- L8819 `gpRecentPRs(model)`
- L8823 `gpSessions(model)`
- L8829 `gpSessionModal(id)`
- L8840 `gpWeekModal(w)`
- L8841 `gpSelect(key)`
- L8842 `gpClick(e)`
- L8854 `renderGym()`
- L8874 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L8883 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L8889 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L8914 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L8918 `showHelp()`
- L8922 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L8924 `markBackup()`
- L8928 `exportJSON()`
- L8933 `drawBackupReminder()`
- L8943 `applyDensity()`
- L8955 `syncDayComplete()`
- L8958 `drawMeals()` — Comidas del día de un vistazo.
- L8966 `filterLog()` — Buscador de Registro.
- L8979 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L8985 `recentFoods()`
- L8990 `quickChip(e,fav)`
- L9008 `drawQuickFoods()`
- L9037 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L9041 `toggleAddPanel(id)`
- L9053 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L9064 `pasteMessage(text,ok)`
- L9072 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L9083 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L9094 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L9100 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L9121 `storableState()`

### Render único: actualiza toda la página

- L9129 `nearView(el)`
- L9131 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L9135 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L9166 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L9167 constante `REF_TABLE`
- L9174 `refTargets(mode)`
- L9175 `syncMicroMode()`
- L9188 `mealByHour(h=new Date()`
- L9195 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L9206 `dataSummary(s)`
- L9210 `confirmImport(next,name)`
- L9217 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L9223 `checkUpdate()`
- L9228 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L9243 constante `GAP_PREFER`
- L9244 constante `GAP_SKIP`
- L9245 constante `GAP_UNIT`
- L9246 `gapQty(f,x)`
- L9247 `gapFoods(key,gap,ctx)`
- L9266 `weekSources(key,sum)`
- L9272 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L9285 `gapRow(x,open,meal,sum,ctx)`
- L9301 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L9326 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L9327 `isFemale(s=state)`
- L9328 `sexLabel(s=state)`
- L9329 `sexBadge(sex)`
- L9331 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L9332 constante `OPT_FEMALE`
- L9343 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba.
- L9344 `applySexOpt(sex)`
- L9346 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L9351 `cleanPreset(p,fb)`
- L9355 `dayNamesFor(types)`
- L9357 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L9367 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L9375 `profV()`
- L9376 `isTrainDay(i)`
- L9377 `activityName(i)`
- L9378 `dayFaf(i)`
- L9379 `presetDesc(cfg,shake)`
- L9383 `profileDescription()`
- L9391 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L9393 `wizCatalog()`
- L9394 `wizOpen(opts={})`
- L9409 `wizTitle()`
- L9410 `wizPaint(sameStep=true)`
- L9419 `wizSync()`
- L9432 `wizFoodOptions()`
- L9435 `wizPresetSummary(cfg,whey)`
- L9440 `wizPresetHTML(kind)`
- L9448 `wizPreview()`
- L9459 `wizHTML()`
- L9500 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L9584 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L9585 constante `SUPP_CATALOG`
- L9607 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L9608 constante `PEAT_BREAKFAST`
- L9609 constante `PEAT_SHAKE`
- L9611 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L9618 `benfoUser()`
- L9620 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L9636 `ico(n)`
- L9638 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L9647 `showTour(i=0)`
- L9659 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L9660 `hubAction(v)`
- L9668 constante `FORM_URL` — Llegan solas a una hoja de Google (formulario del creador de la app). Sin cuentas ni datos personales.
- L9669 constante `FORM_FIELDS`
- L9670 constante `FB_CATS`
- L9672 `openFeedback()`
- L9676 `feedbackData()`
- L9683 `feedbackText()`
- L9684 `sendFeedback()`
- L9697 `shareFeedback()`
- L9714 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L9721 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L9729 constante `I18N_EN`

### v59: idioma (español / inglés)

- L11305 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L11306 constante `WD_EN`
- L11307 `trOne(s)`
- L11315 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L11316 constante `ES_FOOD_GYM`
- L11353 `trFood(s)`
- L11365 constante `TR_TPL`
- L11399 `trLower(s)`
- L11400 `trTpl(s,attr)`
- L11401 constante `FOOD_SEL`
- L11402 `trText(s,attr=false)`
- L11412 `trNode(n)`
- L11427 `trEl(el)`
- L11435 `trTree(root)`
- L11444 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L11455 `setLang(l,quiet)`
- L11468 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter), solo en la web publicada

- L11477 constante `GC_CODE`
- L11478 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L11488 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L11489 `packMove()`
- L11497 `unpackMove(code)`
- L11506 `moveData()`
- L11516 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L11522 `checkMove(code)`

### Arranque

