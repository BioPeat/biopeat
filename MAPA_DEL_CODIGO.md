# MAPA DEL CÓDIGO · BioPeat v60 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (754 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-5947; todo el JavaScript en `<script id="app">` (desde la línea 5948).

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

- L5997 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L5998 constante `AZUCAR_N`
- L5999 constante `USDA_N`
- L6005 constante `FOODS`
- L6007 constante `BASE_FAT_FIX`
- L6010 constante `EXTRA`
- L6011 constante `KEYS`
- L6013 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L6015 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L6019 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6020 constante `OPT`
- L6038 constante `LIMIT`
- L6039 `optInfo(k,goal)`
- L6046 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6054 `optLine(k,goal,unit)`
- L6061 `optRefHTML(k,goal,unit)`
- L6063 constante `DAYS`
- L6064 constante `FAF`
- L6066 constante `LOC`
- L6070 `number(v,min=0,max=1e6)`
- L6076 `decimalInputs(root=document)`
- L6077 `localDate(d=new Date()`
- L6078 `validDate(s)`
- L6083 `shift(s,n)`
- L6092 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6094 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6100 constante `DAY_TYPES`
- L6101 constante `NEW_V54`
- L6105 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6108 `bmr()` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6114 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6136 `cleanNutrients(o,required=false)`
- L6148 `cleanEntry(e)`
- L6153 `cleanPlan(p)`
- L6157 `planEntry(p)`
- L6166 `seedPlan(d,whichDate)`
- L6170 `ensureDay(d=date)`
- L6177 `effectiveEntries(d=day()`
- L6178 constante `SALTED_IDS`
- L6179 constante `SWEET_RE`
- L6180 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6198 `inferredNutrients(e)`
- L6237 `totals(entries=effectiveEntries()`
- L6246 `change(fn,message='Guardado')`
- L6250 `undo()`
- L6257 `toast(text,canUndo=false)`
- L6265 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6266 `onClick(fn)`
- L6268 `attempt(fn)`
- L6272 `modal(title,body)`
- L6281 `modalRestore()`
- L6291 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6292 `modalBack()`
- L6293 `goDate(d)`
- L6300 `renderHeader()`
- L6311 `renderRows(entries)`
- L6315 `entryValues(e)`
- L6316 `renderLog()`
- L6323 `fromFood(id,amount,meal)`
- L6329 `pantryId(name)`
- L6331 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6337 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6346 `recipe(kind)`
- L6353 `summary(entries)`
- L6357 `renderPresetInfo()`
- L6370 `stripCode(raw)`
- L6376 `parseBIO(raw,meal=$('meal-select')`
- L6382 `parseSmart(raw)`
- L6386 constante `COUNT`
- L6389 `nutrientFields(n,prefix='n_')`
- L6390 `readNutrients(form,prefix='n_')`
- L6395 `editEntry(id)`
- L6404 `editFood(id,pending=null)`
- L6409 `usageStats(days=90)`
- L6415 `renderFoods()`
- L6423 `nutrientSources(key)`
- L6430 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6431 `suppSlot(meal)`
- L6432 `renderSupps()`
- L6447 `editPlan(id)`
- L6454 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6474 `makePrompt(meal='Comida',note='')`
- L6479 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6483 `photoPrompt(meal,note)`
- L6486 `resetPhoto()`
- L6497 `openPhoto()`
- L6503 `shrinkPhoto(file)`
- L6506 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6532 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6539 `cleanFood(id,f)`
- L6543 `migrateBase(o)`
- L6562 `download(name,text,type)`
- L6571 `portable()`
- L6608 `syncAppIcons()`
- L6616 `downloadAppIcons()`
- L6653 constante `PROFILES_KEY`
- L6655 `ensureProfilesStore()`
- L6674 `saveProfilesStore(st)`
- L6678 `syncCurrentProfileToStore(rawStr)`
- L6684 `activeProfileName()`
- L6688 `renderProfilesList()`
- L6730 `switchProfile(id)`
- L6752 `deleteProfileById(id)`
- L6776 `refreshDrawerSummary()`
- L6793 `toggleLeftDrawer(force)`
- L6808 `buildAIExportText(rangeOverride)`
- L7056 `copyAIExport()`
- L7070 `downloadAIExport()`
- L7079 `renderDrawerChat()`
- L7098 `buildDrawerChatPrompt(question)`
- L7110 `askDrawerAI(rawQuestion)`
- L7197 `storageStatus()`
- L7203 `idbReadWrite(mode,value)`
- L7204 `openDB()`
- L7205 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L7218 `setQuantity(id,value,msg='Cantidad actualizada')`
- L7222 `niceStep(v)`
- L7223 `stepQuantity(id,dir)`
- L7277 `renderAppInfo()`
- L7292 `init()`
- L7316 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

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
- L8006 constante `AI_PREF`
- L8007 `aiConnected()`
- L8008 `syncAI()`
- L8010 `saveAIPrefs()`
- L8011 `loadAIPrefs()`
- L8012 `openAISetup()`
- L8018 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L8025 constante `MACROS`
- L8027 `cleanGoals(o,fallback)`
- L8032 `cleanCompare(o={})`
- L8036 `snapshotDay(d,reference='saved')`
- L8041 `upgradeTo17(s,o)`
- L8046 `entriesFor(d,source=weekSource)`
- L8050 `dayRow(dt,source=weekSource)`
- L8054 `goalsFor(dt)`
- L8060 `metricValue(r,key)`
- L8066 `targetOf(dt,key)`
- L8070 `weekSummary()`
- L8074 `aggregate(key,summary=weekSummary()`
- L8078 `tone(pct,mode='macro')`
- L8085 `pctText(a)`
- L8086 `weekProgress(a,color)`
- L8087 `renderWeekMicros(s)`
- L8099 `ratioAggregate(s,num,den)`
- L8103 `renderWeekRatios(s)`
- L8109 `renderWeekTable(s)`
- L8110 `weeklyDetail(key,oneDate=null)`
- L8119 `weekRatioDetail(key)`
- L8127 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L8133 `openDay(dt)`
- L8171 `withDayGoals(fn)`
- L8176 `renderMicros()`
- L8177 `nutrientDetail(key)`
- L8178 `editTargets()`
- L8179 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L8189 `summaryFor(start)`
- L8193 `ringSVG(pct,color,marker)`
- L8195 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L8199 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L8214 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L8215 `macroTone(p)`
- L8216 `dayMacroPct(dt,k)`
- L8217 `renderWeekly()`
- L8240 `weekDetail(dt,picked)`
- L8248 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L8258 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L8264 `sparkline(pts)`
- L8270 `renderCalendar()`
- L8287 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L8288 `splitMeals(raw)`
- L8298 `localDay(raw,fallback)`
- L8305 `promptDay(raw,fallback)`
- L8306 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L8328 `parseCsv(text)`
- L8343 `hevyDate(value,format='auto')`
- L8360 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L8375 constante `GYM_APPS`
- L8377 `gymSig(headers)`
- L8378 `gymApp(headers)`
- L8379 `hevyMapping()`
- L8380 `gymSaved()`
- L8381 `renderMapping(parsed)`
- L8398 `optionalNum(v,min=0,max=1e7)`
- L8403 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L8410 `buildHevy(parsed,map)`
- L8444 `cleanWorkout(s)`
- L8451 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L8466 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L8467 constante `GP_ALIAS`
- L8477 `gpNorm(s)`
- L8478 `gpKey(name)`
- L8482 `gpF(n,d=0)`
- L8483 `gpDate(d,opt)`
- L8484 `gpMonday(d)`
- L8485 constante `GP_GROUPS`
- L8500 constante `GP_COLORS`
- L8501 `gpGroup(name)`
- L8502 `gpWorkSets(s)`
- L8503 `gpModel()`
- L8527 `gpSessionMetrics(e,sets)`
- L8542 constante `GP_METRICS`
- L8547 `gpMetricsFor(e)`
- L8548 `gpRangeHist(e)`
- L8549 `gpPRs(model)`
- L8572 `gpStatus(e)`
- L8590 `gpNext(e)`
- L8598 `gpChart(e)`
- L8626 `gpPointDetail(e)`
- L8632 `gpRepTable(e)`
- L8639 `gpKpis(model)`
- L8647 `gpWeekly(model)`
- L8653 `gpMuscles(model)`
- L8660 `gpHeat(model)`
- L8667 `gpExList(model)`
- L8674 `gpExDetail(model)`
- L8687 `gpDayFood(dt)`
- L8688 `gpNutrition(model)`
- L8695 `gpRecentPRs(model)`
- L8699 `gpSessions(model)`
- L8705 `gpSessionModal(id)`
- L8716 `gpWeekModal(w)`
- L8717 `gpSelect(key)`
- L8718 `gpClick(e)`
- L8730 `renderGym()`
- L8750 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L8759 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L8765 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L8790 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L8794 `showHelp()`
- L8798 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L8800 `markBackup()`
- L8804 `exportJSON()`
- L8809 `drawBackupReminder()`
- L8819 `applyDensity()`
- L8831 `syncDayComplete()`
- L8834 `drawMeals()` — Comidas del día de un vistazo.
- L8842 `filterLog()` — Buscador de Registro.
- L8855 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L8861 `recentFoods()`
- L8866 `quickChip(e,fav)`
- L8884 `drawQuickFoods()`
- L8913 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L8917 `toggleAddPanel(id)`
- L8929 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L8940 `pasteMessage(text,ok)`
- L8948 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L8959 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L8970 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L8976 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L8997 `storableState()`

### Render único: actualiza toda la página

- L9005 `nearView(el)`
- L9007 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L9011 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L9042 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L9043 constante `REF_TABLE`
- L9050 `refTargets(mode)`
- L9051 `syncMicroMode()`
- L9064 `mealByHour(h=new Date()`
- L9071 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L9082 `dataSummary(s)`
- L9086 `confirmImport(next,name)`
- L9093 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L9099 `checkUpdate()`
- L9104 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L9119 constante `GAP_PREFER`
- L9120 constante `GAP_SKIP`
- L9121 constante `GAP_UNIT`
- L9122 `gapQty(f,x)`
- L9123 `gapFoods(key,gap,ctx)`
- L9142 `weekSources(key,sum)`
- L9148 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L9161 `gapRow(x,open,meal,sum,ctx)`
- L9177 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L9202 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L9203 `isFemale(s=state)`
- L9204 `sexLabel(s=state)`
- L9205 `sexBadge(sex)`
- L9207 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L9208 constante `OPT_FEMALE`
- L9219 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba.
- L9220 `applySexOpt(sex)`
- L9222 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L9227 `cleanPreset(p,fb)`
- L9231 `dayNamesFor(types)`
- L9233 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L9243 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L9251 `profV()`
- L9252 `isTrainDay(i)`
- L9253 `activityName(i)`
- L9254 `dayFaf(i)`
- L9255 `presetDesc(cfg,shake)`
- L9259 `profileDescription()`
- L9267 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L9269 `wizCatalog()`
- L9270 `wizOpen(opts={})`
- L9285 `wizTitle()`
- L9286 `wizPaint(sameStep=true)`
- L9295 `wizSync()`
- L9308 `wizFoodOptions()`
- L9311 `wizPresetSummary(cfg,whey)`
- L9316 `wizPresetHTML(kind)`
- L9324 `wizPreview()`
- L9335 `wizHTML()`
- L9376 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L9460 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L9461 constante `SUPP_CATALOG`
- L9483 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L9484 constante `PEAT_BREAKFAST`
- L9485 constante `PEAT_SHAKE`
- L9487 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L9494 `benfoUser()`
- L9496 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L9512 `ico(n)`
- L9514 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L9523 `showTour(i=0)`
- L9535 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L9536 `hubAction(v)`
- L9544 constante `FORM_URL` — Llegan solas a una hoja de Google (formulario del creador de la app). Sin cuentas ni datos personales.
- L9545 constante `FORM_FIELDS`
- L9546 constante `FB_CATS`
- L9548 `openFeedback()`
- L9552 `feedbackData()`
- L9559 `feedbackText()`
- L9560 `sendFeedback()`
- L9573 `shareFeedback()`
- L9590 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L9597 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L9605 constante `I18N_EN`

### v59: idioma (español / inglés)

- L11181 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L11182 constante `WD_EN`
- L11183 `trOne(s)`
- L11191 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L11192 constante `ES_FOOD_GYM`
- L11229 `trFood(s)`
- L11241 constante `TR_TPL`
- L11275 `trLower(s)`
- L11276 `trTpl(s,attr)`
- L11277 constante `FOOD_SEL`
- L11278 `trText(s,attr=false)`
- L11288 `trNode(n)`
- L11303 `trEl(el)`
- L11311 `trTree(root)`
- L11320 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L11331 `setLang(l,quiet)`
- L11344 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter), solo en la web publicada

- L11353 constante `GC_CODE`
- L11354 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L11364 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L11365 `packMove()`
- L11373 `unpackMove(code)`
- L11382 `moveData()`
- L11392 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L11398 `checkMove(code)`

### Arranque

