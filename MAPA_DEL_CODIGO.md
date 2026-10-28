# MAPA DEL CÓDIGO · BioPeat v58 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (612 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-5929; todo el JavaScript en `<script id="app">` (desde la línea 5930).

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

- L5977 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L5978 constante `AZUCAR_N`
- L5979 constante `USDA_N`
- L5985 constante `FOODS`
- L5987 constante `BASE_FAT_FIX`
- L5990 constante `EXTRA`
- L5991 constante `KEYS`
- L5993 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L5995 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L5999 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6000 constante `OPT`
- L6018 constante `LIMIT`
- L6019 `optInfo(k,goal)`
- L6026 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6034 `optLine(k,goal,unit)`
- L6041 `optRefHTML(k,goal,unit)`
- L6043 constante `DAYS`
- L6044 constante `FAF`
- L6048 `number(v,min=0,max=1e6)`
- L6054 `decimalInputs(root=document)`
- L6055 `localDate(d=new Date()`
- L6056 `validDate(s)`
- L6061 `shift(s,n)`
- L6070 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6072 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6078 constante `DAY_TYPES`
- L6079 constante `NEW_V54`
- L6083 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6086 `bmr()` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6092 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6114 `cleanNutrients(o,required=false)`
- L6126 `cleanEntry(e)`
- L6131 `cleanPlan(p)`
- L6135 `planEntry(p)`
- L6144 `seedPlan(d,whichDate)`
- L6148 `ensureDay(d=date)`
- L6155 `effectiveEntries(d=day()`
- L6156 constante `SALTED_IDS`
- L6157 constante `SWEET_RE`
- L6158 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6176 `inferredNutrients(e)`
- L6215 `totals(entries=effectiveEntries()`
- L6224 `change(fn,message='Guardado')`
- L6228 `undo()`
- L6235 `toast(text,canUndo=false)`
- L6243 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6244 `onClick(fn)`
- L6246 `attempt(fn)`
- L6250 `modal(title,body)`
- L6259 `modalRestore()`
- L6269 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6270 `modalBack()`
- L6271 `goDate(d)`
- L6278 `renderHeader()`
- L6289 `renderRows(entries)`
- L6293 `entryValues(e)`
- L6294 `renderLog()`
- L6301 `fromFood(id,amount,meal)`
- L6307 `pantryId(name)`
- L6309 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6315 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6324 `recipe(kind)`
- L6331 `summary(entries)`
- L6335 `renderPresetInfo()`
- L6348 `stripCode(raw)`
- L6354 `parseBIO(raw,meal=$('meal-select')`
- L6360 `parseSmart(raw)`
- L6364 constante `COUNT`
- L6367 `nutrientFields(n,prefix='n_')`
- L6368 `readNutrients(form,prefix='n_')`
- L6373 `editEntry(id)`
- L6382 `editFood(id,pending=null)`
- L6387 `usageStats(days=90)`
- L6393 `renderFoods()`
- L6401 `nutrientSources(key)`
- L6408 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6409 `suppSlot(meal)`
- L6410 `renderSupps()`
- L6425 `editPlan(id)`
- L6432 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6452 `makePrompt(meal='Comida',note='')`
- L6457 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6461 `photoPrompt(meal,note)`
- L6464 `resetPhoto()`
- L6475 `openPhoto()`
- L6481 `shrinkPhoto(file)`
- L6484 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6510 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6517 `cleanFood(id,f)`
- L6521 `migrateBase(o)`
- L6540 `download(name,text,type)`
- L6549 `portable()`
- L6586 `syncAppIcons()`
- L6594 `downloadAppIcons()`
- L6631 constante `PROFILES_KEY`
- L6633 `ensureProfilesStore()`
- L6652 `saveProfilesStore(st)`
- L6656 `syncCurrentProfileToStore(rawStr)`
- L6662 `activeProfileName()`
- L6666 `renderProfilesList()`
- L6708 `switchProfile(id)`
- L6730 `deleteProfileById(id)`
- L6754 `refreshDrawerSummary()`
- L6771 `toggleLeftDrawer(force)`
- L6786 `buildAIExportText(rangeOverride)`
- L7034 `copyAIExport()`
- L7048 `downloadAIExport()`
- L7057 `renderDrawerChat()`
- L7076 `buildDrawerChatPrompt(question)`
- L7088 `askDrawerAI(rawQuestion)`
- L7175 `storageStatus()`
- L7181 `idbReadWrite(mode,value)`
- L7182 `openDB()`
- L7183 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L7196 `setQuantity(id,value,msg='Cantidad actualizada')`
- L7200 `niceStep(v)`
- L7201 `stepQuantity(id,dir)`
- L7255 `renderAppInfo()`
- L7270 `init()`
- L7292 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L7294 `setNav(v)`
- L7299 `go(v,focus)`
- L7311 `syncDatePill()`
- L7315 `animateValue(el,to,suffix='%',digits=0)`
- L7324 `tick(now)`
- L7327 `macroCard(key,name,color)`
- L7328 `renderToday()`
- L7351 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L7353 constante `HOME`
- L7355 `coachCandidates()`
- L7361 `coachIdeas(t,g,ref,meal)`
- L7374 `renderCoach()`
- L7392 `coachPrompt()`
- L7400 `nutrientDetailStandard(key)`
- L7414 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L7420 `upgradeTo12(s,o)`
- L7425 `benfotiamineTotals(entries=effectiveEntries()`
- L7434 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L7436 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L7448 `microStat(m,t=totals()`
- L7453 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L7461 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L7462 `ratioInfo(key,t=totals()`
- L7497 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L7514 constante `RATIO_ENDS`
- L7515 `ratioBar(i,big=false)`
- L7520 `ratioNeed(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L7537 `needHTML(i,t)`
- L7538 `renderRatios()`
- L7543 `ratioDetail(key)`
- L7553 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L7570 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L7585 `renderMicroMap()`
- L7589 `nutrientDetailForDay(key)`
- L7594 `editTargetsForm()`
- L7604 `mealData()`
- L7609 `renderMealSegments()`
- L7617 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L7627 constante `FAT_KEYS`
- L7629 `fatData(entries=effectiveEntries()`
- L7635 `energyData(entries=effectiveEntries()`
- L7639 `segmentedBar(items,total,attr)`
- L7643 `renderMealChart()`
- L7648 `renderFat()`
- L7656 `fatDetail(key)`
- L7661 `energyDetail(key)`
- L7668 `portionCandidates(q='')`
- L7673 `openPortion()`
- L7686 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L7701 `templates()`
- L7705 `renderExtra()`
- L7716 `updateExtra(reset=true)`
- L7728 `addExtra(id,amount)`
- L7744 `shakePreview()`
- L7745 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L7760 constante `LENS`
- L7766 `lensKey(key)`
- L7767 `lensHTML(key)`
- L7771 `appendLens(key)`
- L7780 `weekDates()`

### IA en la página: conexión directa o por servidor

- L7790 constante `MEAL_WORD`
- L7791 `mealOfWord(w)`
- L7792 `mealFromText(raw,fallback)`
- L7796 `canonMeal(v,fallback)`
- L7804 `localMeal(raw,meal)`
- L7810 constante `AI_FALLBACK`
- L7811 `applyAIConfig(raw)`
- L7837 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L7838 `callGemini(model,key,prompt,img,signal,think=true)`
- L7856 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L7863 `aiProv(m=$('ai-mode')`
- L7864 `aiBase(mode)`
- L7873 `chatHeaders(mode,key)`
- L7880 `callChat(mode,model,key,prompt,img,signal)` — ChatGPT, Claude, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L7910 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L7918 constante `MODEL_PREF`
- L7919 `pickModel(ids)`
- L7924 `ensureModel(st)`
- L7935 `syncProvider()`
- L7948 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L7981 constante `AI_PREF`
- L7982 `aiConnected()`
- L7983 `syncAI()`
- L7985 `saveAIPrefs()`
- L7986 `loadAIPrefs()`
- L7987 `openAISetup()`
- L7993 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L8000 constante `MACROS`
- L8002 `cleanGoals(o,fallback)`
- L8007 `cleanCompare(o={})`
- L8011 `snapshotDay(d,reference='saved')`
- L8016 `upgradeTo17(s,o)`
- L8021 `entriesFor(d,source=weekSource)`
- L8025 `dayRow(dt,source=weekSource)`
- L8029 `goalsFor(dt)`
- L8035 `metricValue(r,key)`
- L8041 `targetOf(dt,key)`
- L8045 `weekSummary()`
- L8049 `aggregate(key,summary=weekSummary()`
- L8053 `tone(pct,mode='macro')`
- L8060 `pctText(a)`
- L8061 `weekProgress(a,color)`
- L8062 `renderWeekMicros(s)`
- L8074 `ratioAggregate(s,num,den)`
- L8078 `renderWeekRatios(s)`
- L8084 `renderWeekTable(s)`
- L8085 `weeklyDetail(key,oneDate=null)`
- L8094 `weekRatioDetail(key)`
- L8102 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L8108 `openDay(dt)`
- L8146 `withDayGoals(fn)`
- L8151 `renderMicros()`
- L8152 `nutrientDetail(key)`
- L8153 `editTargets()`
- L8154 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L8164 `summaryFor(start)`
- L8168 `ringSVG(pct,color,marker)`
- L8170 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L8174 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L8189 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L8190 `macroTone(p)`
- L8191 `dayMacroPct(dt,k)`
- L8192 `renderWeekly()`
- L8215 `weekDetail(dt,picked)`
- L8223 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L8233 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L8239 `sparkline(pts)`
- L8245 `renderCalendar()`
- L8262 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L8263 `splitMeals(raw)`
- L8273 `localDay(raw,fallback)`
- L8280 `promptDay(raw,fallback)`
- L8281 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L8303 `parseCsv(text)`
- L8318 `hevyDate(value,format='auto')`
- L8335 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L8350 constante `GYM_APPS`
- L8352 `gymSig(headers)`
- L8353 `gymApp(headers)`
- L8354 `hevyMapping()`
- L8355 `gymSaved()`
- L8356 `renderMapping(parsed)`
- L8373 `optionalNum(v,min=0,max=1e7)`
- L8378 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L8385 `buildHevy(parsed,map)`
- L8419 `cleanWorkout(s)`
- L8426 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L8441 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L8442 constante `GP_ALIAS`
- L8452 `gpNorm(s)`
- L8453 `gpKey(name)`
- L8457 `gpF(n,d=0)`
- L8458 `gpDate(d,opt)`
- L8459 `gpMonday(d)`
- L8460 constante `GP_GROUPS`
- L8475 constante `GP_COLORS`
- L8476 `gpGroup(name)`
- L8477 `gpWorkSets(s)`
- L8478 `gpModel()`
- L8502 `gpSessionMetrics(e,sets)`
- L8517 constante `GP_METRICS`
- L8522 `gpMetricsFor(e)`
- L8523 `gpRangeHist(e)`
- L8524 `gpPRs(model)`
- L8547 `gpStatus(e)`
- L8565 `gpNext(e)`
- L8573 `gpChart(e)`
- L8601 `gpPointDetail(e)`
- L8607 `gpRepTable(e)`
- L8614 `gpKpis(model)`
- L8622 `gpWeekly(model)`
- L8628 `gpMuscles(model)`
- L8635 `gpHeat(model)`
- L8642 `gpExList(model)`
- L8649 `gpExDetail(model)`
- L8662 `gpDayFood(dt)`
- L8663 `gpNutrition(model)`
- L8670 `gpRecentPRs(model)`
- L8674 `gpSessions(model)`
- L8680 `gpSessionModal(id)`
- L8691 `gpWeekModal(w)`
- L8692 `gpSelect(key)`
- L8693 `gpClick(e)`
- L8705 `renderGym()`
- L8725 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L8734 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L8740 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L8765 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L8769 `showHelp()`
- L8773 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L8775 `markBackup()`
- L8779 `exportJSON()`
- L8784 `drawBackupReminder()`
- L8794 `applyDensity()`
- L8806 `syncDayComplete()`
- L8809 `drawMeals()` — Comidas del día de un vistazo.
- L8817 `filterLog()` — Buscador de Registro.
- L8830 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L8836 `recentFoods()`
- L8841 `quickChip(e,fav)`
- L8859 `drawQuickFoods()`
- L8888 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L8892 `toggleAddPanel(id)`
- L8904 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L8915 `pasteMessage(text,ok)`
- L8923 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L8934 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L8945 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L8951 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L8972 `storableState()`

### Render único: actualiza toda la página

- L8980 `nearView(el)`
- L8982 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L8986 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L9016 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L9017 constante `REF_TABLE`
- L9024 `refTargets(mode)`
- L9025 `syncMicroMode()`
- L9036 `mealByHour(h=new Date()`
- L9043 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L9054 `dataSummary(s)`
- L9058 `confirmImport(next,name)`
- L9065 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L9071 `checkUpdate()`
- L9076 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L9091 constante `GAP_PREFER`
- L9092 constante `GAP_SKIP`
- L9093 constante `GAP_UNIT`
- L9094 `gapQty(f,x)`
- L9095 `gapFoods(key,gap,ctx)`
- L9114 `weekSources(key,sum)`
- L9120 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L9133 `gapRow(x,open,meal,sum,ctx)`
- L9149 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L9174 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L9175 `isFemale(s=state)`
- L9176 `sexLabel(s=state)`
- L9177 `sexBadge(sex)`
- L9179 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L9180 constante `OPT_FEMALE`
- L9191 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba.
- L9192 `applySexOpt(sex)`
- L9194 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L9199 `cleanPreset(p,fb)`
- L9203 `dayNamesFor(types)`
- L9205 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L9215 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L9223 `profV()`
- L9224 `isTrainDay(i)`
- L9225 `activityName(i)`
- L9226 `dayFaf(i)`
- L9227 `presetDesc(cfg,shake)`
- L9231 `profileDescription()`
- L9239 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L9241 `wizCatalog()`
- L9242 `wizOpen(opts={})`
- L9257 `wizTitle()`
- L9258 `wizPaint(sameStep=true)`
- L9267 `wizSync()`
- L9280 `wizFoodOptions()`
- L9283 `wizPresetSummary(cfg,whey)`
- L9288 `wizPresetHTML(kind)`
- L9296 `wizPreview()`
- L9307 `wizHTML()`
- L9348 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L9432 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L9433 constante `SUPP_CATALOG`
- L9455 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L9456 constante `PEAT_BREAKFAST`
- L9457 constante `PEAT_SHAKE`
- L9459 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L9466 `benfoUser()`
- L9468 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L9484 `ico(n)`
- L9486 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L9495 `showTour(i=0)`
- L9507 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L9508 `hubAction(v)`
- L9517 constante `FORM_URL` — Llegan solas a una hoja de Google (formulario del creador de la app). Sin cuentas ni datos personales.
- L9518 constante `FORM_FIELDS`
- L9519 constante `FB_CATS`
- L9521 `openFeedback()`
- L9525 `feedbackData()`
- L9531 `feedbackText()`
- L9532 `sendFeedback()`
- L9545 `shareFeedback()`
- L9562 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L9569 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### Arranque

