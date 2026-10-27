# MAPA DEL CÓDIGO · BioPeat v57 (revisión de datos 25)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (612 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-5918; todo el JavaScript en `<script id="app">` (desde la línea 5919).

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

- L5965 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L5966 constante `AZUCAR_N`
- L5967 constante `USDA_N`
- L5973 constante `FOODS`
- L5975 constante `BASE_FAT_FIX`
- L5978 constante `EXTRA`
- L5979 constante `KEYS`
- L5981 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L5983 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L5987 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L5988 constante `OPT`
- L6006 constante `LIMIT`
- L6007 `optInfo(k,goal)`
- L6012 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6020 `optLine(k,goal,unit)`
- L6027 `optRefHTML(k,goal,unit)`
- L6029 constante `DAYS`
- L6030 constante `FAF`
- L6034 `number(v,min=0,max=1e6)`
- L6040 `decimalInputs(root=document)`
- L6041 `localDate(d=new Date()`
- L6042 `validDate(s)`
- L6047 `shift(s,n)`
- L6056 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6058 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6064 constante `DAY_TYPES`
- L6065 constante `DIEGO_V54`
- L6068 constante `NEW_V54`
- L6072 constante `GENERIC_SKIP` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6073 `defaults()`
- L6076 `bmr()` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6083 constante `DEF_P` — Plan de macros personal de Diego (useDiegoPlan); el resto de perfiles usa GOAL_TYPES.
- L6084 `targetFor(d)`
- L6107 `cleanNutrients(o,required=false)`
- L6119 `cleanEntry(e)`
- L6124 `cleanPlan(p)`
- L6128 `planEntry(p)`
- L6137 `seedPlan(d,whichDate)`
- L6141 `ensureDay(d=date)`
- L6148 `effectiveEntries(d=day()`
- L6149 constante `SALTED_IDS`
- L6150 constante `SWEET_RE`
- L6151 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6169 `inferredNutrients(e)`
- L6208 `totals(entries=effectiveEntries()`
- L6217 `change(fn,message='Guardado')`
- L6221 `undo()`
- L6228 `toast(text,canUndo=false)`
- L6236 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6237 `onClick(fn)`
- L6239 `attempt(fn)`
- L6243 `modal(title,body)`
- L6252 `modalRestore()`
- L6262 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6263 `modalBack()`
- L6264 `goDate(d)`
- L6271 `renderHeader()`
- L6282 `renderRows(entries)`
- L6286 `entryValues(e)`
- L6287 `renderLog()`
- L6294 `fromFood(id,amount,meal)`
- L6300 `pantryId(name)`
- L6302 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6308 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6317 `recipe(kind)`
- L6324 `summary(entries)`
- L6328 `renderPresetInfo()`
- L6341 `stripCode(raw)`
- L6347 `parseBIO(raw,meal=$('meal-select')`
- L6353 `parseSmart(raw)`
- L6357 constante `COUNT`
- L6360 `nutrientFields(n,prefix='n_')`
- L6361 `readNutrients(form,prefix='n_')`
- L6366 `editEntry(id)`
- L6375 `editFood(id,pending=null)`
- L6380 `usageStats(days=90)`
- L6386 `renderFoods()`
- L6394 `nutrientSources(key)`
- L6401 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6402 `suppSlot(meal)`
- L6403 `renderSupps()`
- L6418 `editPlan(id)`
- L6425 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6445 `makePrompt(meal='Comida',note='')`
- L6450 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6454 `photoPrompt(meal,note)`
- L6457 `resetPhoto()`
- L6468 `openPhoto()`
- L6474 `shrinkPhoto(file)`
- L6477 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6503 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6510 `cleanFood(id,f)`
- L6514 `migrateBase(o)`
- L6533 `download(name,text,type)`
- L6542 `portable()`
- L6579 `syncAppIcons()`
- L6587 `downloadAppIcons()`
- L6624 constante `PROFILES_KEY`
- L6626 `ensureProfilesStore()`
- L6645 `saveProfilesStore(st)`
- L6649 `syncCurrentProfileToStore(rawStr)`
- L6655 `activeProfileName()`
- L6659 `renderProfilesList()`
- L6701 `switchProfile(id)`
- L6723 `deleteProfileById(id)`
- L6747 `refreshDrawerSummary()`
- L6764 `toggleLeftDrawer(force)`
- L6779 `buildAIExportText(rangeOverride)`
- L7027 `copyAIExport()`
- L7041 `downloadAIExport()`
- L7050 `renderDrawerChat()`
- L7069 `buildDrawerChatPrompt(question)`
- L7081 `askDrawerAI(rawQuestion)`
- L7168 `storageStatus()`
- L7174 `idbReadWrite(mode,value)`
- L7175 `openDB()`
- L7176 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L7189 `setQuantity(id,value,msg='Cantidad actualizada')`
- L7193 `niceStep(v)`
- L7194 `stepQuantity(id,dir)`
- L7248 `renderAppInfo()`
- L7263 `init()`

### Corrección de la pauta declarada (revisión 11 de los datos)

- L7285 `planFamily(e)`
- L7297 `correctedPlan(plan)`
- L7303 `syncCorrectedDay(s,dt)`
- L7312 `upgradeTo11(s,o)`

### Navegación: una sola página; la barra inferior solo desplaza

- L7318 `setNav(v)`
- L7323 `go(v,focus)`
- L7335 `syncDatePill()`
- L7339 `animateValue(el,to,suffix='%',digits=0)`
- L7348 `tick(now)`
- L7351 `macroCard(key,name,color)`
- L7352 `renderToday()`
- L7375 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L7377 constante `HOME`
- L7379 `coachCandidates()`
- L7385 `coachIdeas(t,g,ref,meal)`
- L7398 `renderCoach()`
- L7416 `coachPrompt()`
- L7424 `nutrientDetailStandard(key)`
- L7438 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L7444 `upgradeTo12(s,o)`
- L7449 `benfotiamineTotals(entries=effectiveEntries()`
- L7458 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L7460 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L7472 `microStat(m,t=totals()`
- L7477 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L7485 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L7486 `ratioInfo(key,t=totals()`
- L7521 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L7538 constante `RATIO_ENDS`
- L7539 `ratioBar(i,big=false)`
- L7544 `ratioNeed(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L7561 `needHTML(i,t)`
- L7562 `renderRatios()`
- L7567 `ratioDetail(key)`
- L7577 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L7594 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L7609 `renderMicroMap()`
- L7613 `nutrientDetailForDay(key)`
- L7618 `editTargetsForm()`
- L7628 `mealData()`
- L7633 `renderMealSegments()`
- L7641 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L7651 constante `FAT_KEYS`
- L7653 `fatData(entries=effectiveEntries()`
- L7659 `energyData(entries=effectiveEntries()`
- L7663 `segmentedBar(items,total,attr)`
- L7667 `renderMealChart()`
- L7672 `renderFat()`
- L7680 `fatDetail(key)`
- L7685 `energyDetail(key)`
- L7692 `portionCandidates(q='')`
- L7697 `openPortion()`
- L7710 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L7725 `templates()`
- L7729 `renderExtra()`
- L7740 `updateExtra(reset=true)`
- L7752 `addExtra(id,amount)`
- L7768 `shakePreview()`
- L7769 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L7784 constante `LENS`
- L7790 `lensKey(key)`
- L7791 `lensHTML(key)`
- L7795 `appendLens(key)`
- L7804 `weekDates()`

### IA en la página: conexión directa o por servidor

- L7814 constante `MEAL_WORD`
- L7815 `mealOfWord(w)`
- L7816 `mealFromText(raw,fallback)`
- L7820 `canonMeal(v,fallback)`
- L7828 `localMeal(raw,meal)`
- L7834 constante `AI_FALLBACK`
- L7835 `applyAIConfig(raw)`
- L7861 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L7862 `callGemini(model,key,prompt,img,signal,think=true)`
- L7880 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L7887 `aiProv(m=$('ai-mode')`
- L7888 `aiBase(mode)`
- L7897 `chatHeaders(mode,key)`
- L7904 `callChat(mode,model,key,prompt,img,signal)` — ChatGPT, Claude, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L7934 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L7942 constante `MODEL_PREF`
- L7943 `pickModel(ids)`
- L7948 `ensureModel(st)`
- L7959 `syncProvider()`
- L7972 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
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

- L8995 `storableState()`

### Render único: actualiza toda la página

- L9003 `nearView(el)`
- L9005 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L9009 `render()`
- L9045 `mealByHour(h=new Date()`
- L9052 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L9063 `dataSummary(s)`
- L9067 `confirmImport(next,name)`
- L9074 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L9080 `checkUpdate()`
- L9085 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L9100 constante `GAP_PREFER`
- L9101 constante `GAP_SKIP`
- L9102 constante `GAP_UNIT`
- L9103 `gapQty(f,x)`
- L9104 `gapFoods(key,gap,ctx)`
- L9123 `weekSources(key,sum)`
- L9129 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L9142 `gapRow(x,open,meal,sum,ctx)`
- L9158 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L9183 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L9184 `isFemale(s=state)`
- L9185 `sexLabel(s=state)`
- L9186 `sexBadge(sex)`
- L9188 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L9189 constante `OPT_FEMALE`
- L9200 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo (las de Diego incluyen sus suplementos). Mujer: hierro, zinc y magnesio de las fuentes de arriba.
- L9201 `applySexOpt(sex)`
- L9203 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L9208 `cleanPreset(p,fb)`
- L9212 `dayNamesFor(types)`
- L9214 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas de Diego) se usan los de Diego.
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
- L9308 `wizHTML()`
- L9343 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L9424 constante `ALL_DAYS` — Sugerencias genéricas (enfoque Peat y seguidores) para el paso «Suplementos» del asistente. No son recomendaciones médicas: el usuario elige y ajusta la dosis.
- L9425 constante `SUPP_CATALOG`
- L9440 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L9447 `benfoUser()`
- L9449 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L9465 `ico(n)`
- L9467 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L9476 `showTour(i=0)`
- L9488 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L9489 `hubAction(v)`
- L9500 constante `FORM_URL` — Llegan solas a una hoja de Google (formulario de Diego). Sin cuentas ni datos personales.
- L9501 constante `FORM_FIELDS`
- L9502 constante `FB_CATS`
- L9504 `openFeedback()`
- L9508 `feedbackData()`
- L9514 `feedbackText()`
- L9515 `sendFeedback()`
- L9528 `shareFeedback()`
- L9545 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L9552 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### Arranque

