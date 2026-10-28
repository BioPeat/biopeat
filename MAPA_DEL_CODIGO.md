# MAPA DEL CÓDIGO · BioPeat v59 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (732 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-5947; todo el JavaScript en `<script id="app">` (desde la línea 5948).

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

- L5996 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L5997 constante `AZUCAR_N`
- L5998 constante `USDA_N`
- L6004 constante `FOODS`
- L6006 constante `BASE_FAT_FIX`
- L6009 constante `EXTRA`
- L6010 constante `KEYS`
- L6012 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L6014 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L6018 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6019 constante `OPT`
- L6037 constante `LIMIT`
- L6038 `optInfo(k,goal)`
- L6045 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6053 `optLine(k,goal,unit)`
- L6060 `optRefHTML(k,goal,unit)`
- L6062 constante `DAYS`
- L6063 constante `FAF`
- L6065 constante `LOC`
- L6069 `number(v,min=0,max=1e6)`
- L6075 `decimalInputs(root=document)`
- L6076 `localDate(d=new Date()`
- L6077 `validDate(s)`
- L6082 `shift(s,n)`
- L6091 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6093 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6099 constante `DAY_TYPES`
- L6100 constante `NEW_V54`
- L6104 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6107 `bmr()` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6113 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6135 `cleanNutrients(o,required=false)`
- L6147 `cleanEntry(e)`
- L6152 `cleanPlan(p)`
- L6156 `planEntry(p)`
- L6165 `seedPlan(d,whichDate)`
- L6169 `ensureDay(d=date)`
- L6176 `effectiveEntries(d=day()`
- L6177 constante `SALTED_IDS`
- L6178 constante `SWEET_RE`
- L6179 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6197 `inferredNutrients(e)`
- L6236 `totals(entries=effectiveEntries()`
- L6245 `change(fn,message='Guardado')`
- L6249 `undo()`
- L6256 `toast(text,canUndo=false)`
- L6264 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6265 `onClick(fn)`
- L6267 `attempt(fn)`
- L6271 `modal(title,body)`
- L6280 `modalRestore()`
- L6290 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6291 `modalBack()`
- L6292 `goDate(d)`
- L6299 `renderHeader()`
- L6310 `renderRows(entries)`
- L6314 `entryValues(e)`
- L6315 `renderLog()`
- L6322 `fromFood(id,amount,meal)`
- L6328 `pantryId(name)`
- L6330 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6336 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6345 `recipe(kind)`
- L6352 `summary(entries)`
- L6356 `renderPresetInfo()`
- L6369 `stripCode(raw)`
- L6375 `parseBIO(raw,meal=$('meal-select')`
- L6381 `parseSmart(raw)`
- L6385 constante `COUNT`
- L6388 `nutrientFields(n,prefix='n_')`
- L6389 `readNutrients(form,prefix='n_')`
- L6394 `editEntry(id)`
- L6403 `editFood(id,pending=null)`
- L6408 `usageStats(days=90)`
- L6414 `renderFoods()`
- L6422 `nutrientSources(key)`
- L6429 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6430 `suppSlot(meal)`
- L6431 `renderSupps()`
- L6446 `editPlan(id)`
- L6453 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6473 `makePrompt(meal='Comida',note='')`
- L6478 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6482 `photoPrompt(meal,note)`
- L6485 `resetPhoto()`
- L6496 `openPhoto()`
- L6502 `shrinkPhoto(file)`
- L6505 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6531 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6538 `cleanFood(id,f)`
- L6542 `migrateBase(o)`
- L6561 `download(name,text,type)`
- L6570 `portable()`
- L6607 `syncAppIcons()`
- L6615 `downloadAppIcons()`
- L6652 constante `PROFILES_KEY`
- L6654 `ensureProfilesStore()`
- L6673 `saveProfilesStore(st)`
- L6677 `syncCurrentProfileToStore(rawStr)`
- L6683 `activeProfileName()`
- L6687 `renderProfilesList()`
- L6729 `switchProfile(id)`
- L6751 `deleteProfileById(id)`
- L6775 `refreshDrawerSummary()`
- L6792 `toggleLeftDrawer(force)`
- L6807 `buildAIExportText(rangeOverride)`
- L7055 `copyAIExport()`
- L7069 `downloadAIExport()`
- L7078 `renderDrawerChat()`
- L7097 `buildDrawerChatPrompt(question)`
- L7109 `askDrawerAI(rawQuestion)`
- L7196 `storageStatus()`
- L7202 `idbReadWrite(mode,value)`
- L7203 `openDB()`
- L7204 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L7217 `setQuantity(id,value,msg='Cantidad actualizada')`
- L7221 `niceStep(v)`
- L7222 `stepQuantity(id,dir)`
- L7276 `renderAppInfo()`
- L7291 `init()`
- L7315 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L7317 `setNav(v)`
- L7322 `go(v,focus)`
- L7334 `syncDatePill()`
- L7338 `animateValue(el,to,suffix='%',digits=0)`
- L7347 `tick(now)`
- L7350 `macroCard(key,name,color)`
- L7351 `renderToday()`
- L7374 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L7376 constante `HOME`
- L7378 `coachCandidates()`
- L7384 `coachIdeas(t,g,ref,meal)`
- L7397 `renderCoach()`
- L7415 `coachPrompt()`
- L7423 `nutrientDetailStandard(key)`
- L7437 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L7443 `upgradeTo12(s,o)`
- L7448 `benfotiamineTotals(entries=effectiveEntries()`
- L7457 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L7459 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L7471 `microStat(m,t=totals()`
- L7476 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L7484 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L7485 `ratioInfo(key,t=totals()`
- L7520 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L7537 constante `RATIO_ENDS`
- L7538 `ratioBar(i,big=false)`
- L7543 `ratioNeed(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L7560 `needHTML(i,t)`
- L7561 `renderRatios()`
- L7566 `ratioDetail(key)`
- L7576 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L7593 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L7608 `renderMicroMap()`
- L7612 `nutrientDetailForDay(key)`
- L7617 `editTargetsForm()`
- L7627 `mealData()`
- L7632 `renderMealSegments()`
- L7640 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L7650 constante `FAT_KEYS`
- L7652 `fatData(entries=effectiveEntries()`
- L7658 `energyData(entries=effectiveEntries()`
- L7662 `segmentedBar(items,total,attr)`
- L7666 `renderMealChart()`
- L7671 `renderFat()`
- L7679 `fatDetail(key)`
- L7684 `energyDetail(key)`
- L7691 `portionCandidates(q='')`
- L7696 `openPortion()`
- L7709 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L7724 `templates()`
- L7728 `renderExtra()`
- L7739 `updateExtra(reset=true)`
- L7751 `addExtra(id,amount)`
- L7767 `shakePreview()`
- L7768 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L7783 constante `LENS`
- L7789 `lensKey(key)`
- L7790 `lensHTML(key)`
- L7794 `appendLens(key)`
- L7803 `weekDates()`

### IA en la página: conexión directa o por servidor

- L7813 constante `MEAL_WORD`
- L7814 `mealOfWord(w)`
- L7815 `mealFromText(raw,fallback)`
- L7819 `canonMeal(v,fallback)`
- L7827 `localMeal(raw,meal)`
- L7833 constante `AI_FALLBACK`
- L7834 `applyAIConfig(raw)`
- L7860 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L7861 `callGemini(model,key,prompt,img,signal,think=true)`
- L7879 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L7886 `aiProv(m=$('ai-mode')`
- L7887 `aiBase(mode)`
- L7896 `chatHeaders(mode,key)`
- L7903 `callChat(mode,model,key,prompt,img,signal)` — ChatGPT, Claude, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L7933 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L7941 constante `MODEL_PREF`
- L7942 `pickModel(ids)`
- L7947 `ensureModel(st)`
- L7958 `syncProvider()`
- L7971 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L8005 constante `AI_PREF`
- L8006 `aiConnected()`
- L8007 `syncAI()`
- L8009 `saveAIPrefs()`
- L8010 `loadAIPrefs()`
- L8011 `openAISetup()`
- L8017 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L8024 constante `MACROS`
- L8026 `cleanGoals(o,fallback)`
- L8031 `cleanCompare(o={})`
- L8035 `snapshotDay(d,reference='saved')`
- L8040 `upgradeTo17(s,o)`
- L8045 `entriesFor(d,source=weekSource)`
- L8049 `dayRow(dt,source=weekSource)`
- L8053 `goalsFor(dt)`
- L8059 `metricValue(r,key)`
- L8065 `targetOf(dt,key)`
- L8069 `weekSummary()`
- L8073 `aggregate(key,summary=weekSummary()`
- L8077 `tone(pct,mode='macro')`
- L8084 `pctText(a)`
- L8085 `weekProgress(a,color)`
- L8086 `renderWeekMicros(s)`
- L8098 `ratioAggregate(s,num,den)`
- L8102 `renderWeekRatios(s)`
- L8108 `renderWeekTable(s)`
- L8109 `weeklyDetail(key,oneDate=null)`
- L8118 `weekRatioDetail(key)`
- L8126 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L8132 `openDay(dt)`
- L8170 `withDayGoals(fn)`
- L8175 `renderMicros()`
- L8176 `nutrientDetail(key)`
- L8177 `editTargets()`
- L8178 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L8188 `summaryFor(start)`
- L8192 `ringSVG(pct,color,marker)`
- L8194 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L8198 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L8213 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L8214 `macroTone(p)`
- L8215 `dayMacroPct(dt,k)`
- L8216 `renderWeekly()`
- L8239 `weekDetail(dt,picked)`
- L8247 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L8257 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L8263 `sparkline(pts)`
- L8269 `renderCalendar()`
- L8286 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L8287 `splitMeals(raw)`
- L8297 `localDay(raw,fallback)`
- L8304 `promptDay(raw,fallback)`
- L8305 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L8327 `parseCsv(text)`
- L8342 `hevyDate(value,format='auto')`
- L8359 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L8374 constante `GYM_APPS`
- L8376 `gymSig(headers)`
- L8377 `gymApp(headers)`
- L8378 `hevyMapping()`
- L8379 `gymSaved()`
- L8380 `renderMapping(parsed)`
- L8397 `optionalNum(v,min=0,max=1e7)`
- L8402 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L8409 `buildHevy(parsed,map)`
- L8443 `cleanWorkout(s)`
- L8450 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L8465 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L8466 constante `GP_ALIAS`
- L8476 `gpNorm(s)`
- L8477 `gpKey(name)`
- L8481 `gpF(n,d=0)`
- L8482 `gpDate(d,opt)`
- L8483 `gpMonday(d)`
- L8484 constante `GP_GROUPS`
- L8499 constante `GP_COLORS`
- L8500 `gpGroup(name)`
- L8501 `gpWorkSets(s)`
- L8502 `gpModel()`
- L8526 `gpSessionMetrics(e,sets)`
- L8541 constante `GP_METRICS`
- L8546 `gpMetricsFor(e)`
- L8547 `gpRangeHist(e)`
- L8548 `gpPRs(model)`
- L8571 `gpStatus(e)`
- L8589 `gpNext(e)`
- L8597 `gpChart(e)`
- L8625 `gpPointDetail(e)`
- L8631 `gpRepTable(e)`
- L8638 `gpKpis(model)`
- L8646 `gpWeekly(model)`
- L8652 `gpMuscles(model)`
- L8659 `gpHeat(model)`
- L8666 `gpExList(model)`
- L8673 `gpExDetail(model)`
- L8686 `gpDayFood(dt)`
- L8687 `gpNutrition(model)`
- L8694 `gpRecentPRs(model)`
- L8698 `gpSessions(model)`
- L8704 `gpSessionModal(id)`
- L8715 `gpWeekModal(w)`
- L8716 `gpSelect(key)`
- L8717 `gpClick(e)`
- L8729 `renderGym()`
- L8749 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L8758 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L8764 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L8789 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L8793 `showHelp()`
- L8797 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L8799 `markBackup()`
- L8803 `exportJSON()`
- L8808 `drawBackupReminder()`
- L8818 `applyDensity()`
- L8830 `syncDayComplete()`
- L8833 `drawMeals()` — Comidas del día de un vistazo.
- L8841 `filterLog()` — Buscador de Registro.
- L8854 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L8860 `recentFoods()`
- L8865 `quickChip(e,fav)`
- L8883 `drawQuickFoods()`
- L8912 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L8916 `toggleAddPanel(id)`
- L8928 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L8939 `pasteMessage(text,ok)`
- L8947 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L8958 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L8969 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L8975 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L8996 `storableState()`

### Render único: actualiza toda la página

- L9004 `nearView(el)`
- L9006 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L9010 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L9040 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L9041 constante `REF_TABLE`
- L9048 `refTargets(mode)`
- L9049 `syncMicroMode()`
- L9062 `mealByHour(h=new Date()`
- L9069 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L9080 `dataSummary(s)`
- L9084 `confirmImport(next,name)`
- L9091 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L9097 `checkUpdate()`
- L9102 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L9117 constante `GAP_PREFER`
- L9118 constante `GAP_SKIP`
- L9119 constante `GAP_UNIT`
- L9120 `gapQty(f,x)`
- L9121 `gapFoods(key,gap,ctx)`
- L9140 `weekSources(key,sum)`
- L9146 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L9159 `gapRow(x,open,meal,sum,ctx)`
- L9175 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L9200 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L9201 `isFemale(s=state)`
- L9202 `sexLabel(s=state)`
- L9203 `sexBadge(sex)`
- L9205 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L9206 constante `OPT_FEMALE`
- L9217 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba.
- L9218 `applySexOpt(sex)`
- L9220 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L9225 `cleanPreset(p,fb)`
- L9229 `dayNamesFor(types)`
- L9231 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L9241 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L9249 `profV()`
- L9250 `isTrainDay(i)`
- L9251 `activityName(i)`
- L9252 `dayFaf(i)`
- L9253 `presetDesc(cfg,shake)`
- L9257 `profileDescription()`
- L9265 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L9267 `wizCatalog()`
- L9268 `wizOpen(opts={})`
- L9283 `wizTitle()`
- L9284 `wizPaint(sameStep=true)`
- L9293 `wizSync()`
- L9306 `wizFoodOptions()`
- L9309 `wizPresetSummary(cfg,whey)`
- L9314 `wizPresetHTML(kind)`
- L9322 `wizPreview()`
- L9333 `wizHTML()`
- L9374 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L9458 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L9459 constante `SUPP_CATALOG`
- L9481 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L9482 constante `PEAT_BREAKFAST`
- L9483 constante `PEAT_SHAKE`
- L9485 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L9492 `benfoUser()`
- L9494 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L9510 `ico(n)`
- L9512 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L9521 `showTour(i=0)`
- L9533 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L9534 `hubAction(v)`
- L9543 constante `FORM_URL` — Llegan solas a una hoja de Google (formulario del creador de la app). Sin cuentas ni datos personales.
- L9544 constante `FORM_FIELDS`
- L9545 constante `FB_CATS`
- L9547 `openFeedback()`
- L9551 `feedbackData()`
- L9558 `feedbackText()`
- L9559 `sendFeedback()`
- L9572 `shareFeedback()`
- L9589 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L9596 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L9604 constante `I18N_EN`

### v59: idioma (español / inglés)

- L10927 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L10928 constante `WD_EN`
- L10929 `trOne(s)`
- L10937 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L10938 constante `TR_TPL`
- L10954 `trLower(s)`
- L10955 `trTpl(s,attr)`
- L10956 `trText(s,attr=false)`
- L10962 `trNode(n)`
- L10976 `trEl(el)`
- L10984 `trTree(root)`
- L10993 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L11004 `setLang(l,quiet)`
- L11016 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter), solo en la web publicada

- L11025 constante `GC_CODE`
- L11026 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L11036 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L11037 `packMove()`
- L11045 `unpackMove(code)`
- L11054 `moveData()`
- L11064 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L11070 `checkMove(code)`

### Arranque

