# MAPA DEL CÓDIGO · BioPeat v64 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (791 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-6190; todo el JavaScript en `<script id="app">` (desde la línea 6191).

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

- L6244 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L6245 constante `AZUCAR_N`
- L6246 constante `USDA_N`
- L6252 constante `FOODS`
- L6254 constante `BASE_FAT_FIX`
- L6257 constante `EXTRA`
- L6258 constante `KEYS`
- L6260 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L6262 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L6266 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6267 constante `OPT`
- L6285 constante `LIMIT`
- L6286 `optInfo(k,goal)`
- L6293 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6301 `optLine(k,goal,unit)`
- L6308 `optRefHTML(k,goal,unit)`
- L6310 constante `DAYS`
- L6311 constante `FAF`
- L6313 constante `LOC`
- L6317 `number(v,min=0,max=1e6)`
- L6323 `decimalInputs(root=document)`
- L6324 `localDate(d=new Date()`
- L6325 `validDate(s)`
- L6330 `shift(s,n)`
- L6339 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6341 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6347 constante `DAY_TYPES`
- L6348 constante `NEW_V54`
- L6352 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6355 `bmr()` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6361 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6383 `cleanNutrients(o,required=false)`
- L6395 `cleanEntry(e)`
- L6400 `cleanPlan(p)`
- L6404 `planEntry(p)`
- L6413 `seedPlan(d,whichDate)`
- L6417 `ensureDay(d=date)`
- L6424 `effectiveEntries(d=day()`
- L6425 constante `SALTED_IDS`
- L6426 constante `SWEET_RE`
- L6427 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6445 `inferredNutrients(e)`
- L6484 `totals(entries=effectiveEntries()`
- L6493 `change(fn,message='Guardado')`
- L6497 `undo()`
- L6504 `toast(text,canUndo=false)`
- L6512 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6513 `onClick(fn)`
- L6515 `attempt(fn)`
- L6519 `modal(title,body)`
- L6528 `modalRestore()`
- L6538 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6539 `modalBack()`
- L6540 `goDate(d)`
- L6547 `renderHeader()`
- L6559 `renderRows(entries)`
- L6563 `entryValues(e)`
- L6564 `renderLog()`
- L6571 `fromFood(id,amount,meal)`
- L6577 `pantryId(name)`
- L6579 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6585 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6594 `recipe(kind)`
- L6601 `summary(entries)`
- L6605 `renderPresetInfo()`
- L6618 `stripCode(raw)`
- L6624 `parseBIO(raw,meal=$('meal-select')`
- L6630 `parseSmart(raw)`
- L6634 constante `COUNT`
- L6637 `nutrientFields(n,prefix='n_')`
- L6638 `readNutrients(form,prefix='n_')`
- L6643 `editEntry(id)`
- L6652 `editFood(id,pending=null)`
- L6657 `usageStats(days=90)`
- L6663 `renderFoods()`
- L6671 `nutrientSources(key)`
- L6678 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6679 `suppSlot(meal)`
- L6680 `renderSupps()`
- L6695 `editPlan(id)`
- L6702 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6722 `makePrompt(meal='Comida',note='')`
- L6727 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6731 `photoPrompt(meal,note)`
- L6734 `resetPhoto()`
- L6745 `openPhoto()`
- L6751 `shrinkPhoto(file)`
- L6754 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6780 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6787 `cleanFood(id,f)`
- L6791 `migrateBase(o)`
- L6810 `download(name,text,type)`
- L6819 `portable()`
- L6856 `syncAppIcons()`
- L6864 `downloadAppIcons()`
- L6901 constante `PROFILES_KEY`
- L6903 `ensureProfilesStore()`
- L6922 `saveProfilesStore(st)`
- L6926 `syncCurrentProfileToStore(rawStr)`
- L6932 `activeProfileName()`
- L6936 `renderProfilesList()`
- L6978 `switchProfile(id)`
- L7000 `deleteProfileById(id)`
- L7024 `refreshDrawerSummary()`
- L7041 `toggleLeftDrawer(force)`
- L7056 `buildAIExportText(rangeOverride)`
- L7304 `copyAIExport()`
- L7318 `downloadAIExport()`
- L7327 `renderDrawerChat()`
- L7346 `buildDrawerChatPrompt(question)`
- L7358 `askDrawerAI(rawQuestion)`
- L7445 `storageStatus()`
- L7451 `idbReadWrite(mode,value)`
- L7452 `openDB()`
- L7453 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L7466 `setQuantity(id,value,msg='Cantidad actualizada')`
- L7470 `niceStep(v)`
- L7471 `stepQuantity(id,dir)`
- L7525 `renderAppInfo()`
- L7540 `init()`
- L7564 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L7566 `setNav(v)`
- L7571 `go(v,focus)`
- L7582 constante `THEME_KEY`
- L7583 constante `SUN_SVG`
- L7584 constante `MOON_SVG`
- L7586 `syncThemeUI()`
- L7598 `toggleTheme()`
- L7606 `syncDatePill()`
- L7610 `animateValue(el,to,suffix='%',digits=0)`
- L7619 `tick(now)`
- L7622 `macroCard(key,name,color)`
- L7623 `renderToday()`
- L7646 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L7648 constante `HOME`
- L7650 `coachCandidates()`
- L7656 `coachIdeas(t,g,ref,meal)`
- L7669 `renderCoach()`
- L7687 `coachPrompt()`
- L7695 `nutrientDetailStandard(key)`
- L7709 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L7715 `upgradeTo12(s,o)`
- L7720 `benfotiamineTotals(entries=effectiveEntries()`
- L7729 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L7731 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L7743 `microStat(m,t=totals()`
- L7748 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L7756 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L7757 `ratioInfo(key,t=totals()`
- L7792 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L7809 constante `RATIO_ENDS`
- L7810 `ratioBar(i,big=false)`
- L7815 `ratioNeed(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L7832 `needHTML(i,t)`
- L7833 `renderRatios()`
- L7838 `ratioDetail(key)`
- L7848 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L7865 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L7880 `renderMicroMap()`
- L7884 `nutrientDetailForDay(key)`
- L7889 `editTargetsForm()`
- L7899 `mealData()`
- L7904 `renderMealSegments()`
- L7912 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L7922 constante `FAT_KEYS`
- L7924 `fatData(entries=effectiveEntries()`
- L7930 `energyData(entries=effectiveEntries()`
- L7934 `segmentedBar(items,total,attr)`
- L7938 `renderMealChart()`
- L7943 `renderFat()`
- L7951 `fatDetail(key)`
- L7956 `energyDetail(key)`
- L7963 `portionCandidates(q='')`
- L7968 `openPortion()`
- L7981 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L7996 `templates()`
- L8000 `renderExtra()`
- L8011 `updateExtra(reset=true)`
- L8023 `addExtra(id,amount)`
- L8039 `shakePreview()`
- L8040 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L8055 constante `LENS`
- L8061 `lensKey(key)`
- L8062 `lensHTML(key)`
- L8066 `appendLens(key)`
- L8075 `weekDates()`

### IA en la página: conexión directa o por servidor

- L8085 constante `MEAL_WORD`
- L8086 `mealOfWord(w)`
- L8087 `mealFromText(raw,fallback)`
- L8091 `canonMeal(v,fallback)`
- L8099 `localMeal(raw,meal)`
- L8105 constante `AI_FALLBACK`
- L8106 `applyAIConfig(raw)`
- L8132 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L8133 `callGemini(model,key,prompt,img,signal,think=true)`
- L8151 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L8158 `aiProv(m=$('ai-mode')`
- L8159 `aiBase(mode)`
- L8168 `chatHeaders(mode,key)`
- L8175 `callChat(mode,model,key,prompt,img,signal)` — ChatGPT, Claude, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L8205 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L8213 constante `MODEL_PREF`
- L8214 `pickModel(ids)`
- L8219 `ensureModel(st)`
- L8230 `syncProvider()`
- L8243 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L8277 constante `AI_PREF`
- L8278 `aiConnected()`
- L8279 `syncAI()`
- L8281 `saveAIPrefs()`
- L8282 `loadAIPrefs()`
- L8283 `openAISetup()`
- L8289 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L8296 constante `MACROS`
- L8298 `cleanGoals(o,fallback)`
- L8303 `cleanCompare(o={})`
- L8307 `snapshotDay(d,reference='saved')`
- L8312 `upgradeTo17(s,o)`
- L8317 `entriesFor(d,source=weekSource)`
- L8321 `dayRow(dt,source=weekSource)`
- L8325 `goalsFor(dt)`
- L8331 `metricValue(r,key)`
- L8337 `targetOf(dt,key)`
- L8341 `weekSummary()`
- L8345 `aggregate(key,summary=weekSummary()`
- L8349 `tone(pct,mode='macro')`
- L8356 `pctText(a)`
- L8357 `weekProgress(a,color)`
- L8358 `renderWeekMicros(s)`
- L8370 `ratioAggregate(s,num,den)`
- L8374 `renderWeekRatios(s)`
- L8380 `renderWeekTable(s)`
- L8381 `weeklyDetail(key,oneDate=null)`
- L8390 `weekRatioDetail(key)`
- L8398 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L8404 `openDay(dt)`
- L8442 `withDayGoals(fn)`
- L8447 `renderMicros()`
- L8448 `nutrientDetail(key)`
- L8449 `editTargets()`
- L8450 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L8460 `summaryFor(start)`
- L8464 `ringSVG(pct,color,marker)`
- L8466 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L8470 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L8485 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L8486 `macroTone(p)`
- L8487 `dayMacroPct(dt,k)`
- L8488 `renderWeekly()`
- L8511 `weekDetail(dt,picked)`
- L8519 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L8529 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L8535 `sparkline(pts)`
- L8541 `renderCalendar()`
- L8558 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L8559 `splitMeals(raw)`
- L8569 `localDay(raw,fallback)`
- L8576 `promptDay(raw,fallback)`
- L8577 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L8599 `parseCsv(text)`
- L8614 `hevyDate(value,format='auto')`
- L8631 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L8646 constante `GYM_APPS`
- L8648 `gymSig(headers)`
- L8649 `gymApp(headers)`
- L8650 `hevyMapping()`
- L8651 `gymSaved()`
- L8652 `renderMapping(parsed)`
- L8669 `optionalNum(v,min=0,max=1e7)`
- L8674 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L8681 `buildHevy(parsed,map)`
- L8715 `cleanWorkout(s)`
- L8722 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L8737 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L8738 constante `GP_ALIAS`
- L8748 `gpNorm(s)`
- L8749 `gpKey(name)`
- L8753 `gpF(n,d=0)`
- L8754 `gpDate(d,opt)`
- L8755 `gpMonday(d)`
- L8756 constante `GP_GROUPS`
- L8771 constante `GP_COLORS`
- L8772 `gpGroup(name)`
- L8773 `gpWorkSets(s)`
- L8774 `gpModel()`
- L8798 `gpSessionMetrics(e,sets)`
- L8813 constante `GP_METRICS`
- L8818 `gpMetricsFor(e)`
- L8819 `gpRangeHist(e)`
- L8820 `gpPRs(model)`
- L8843 `gpStatus(e)`
- L8861 `gpNext(e)`
- L8869 `gpChart(e)`
- L8897 `gpPointDetail(e)`
- L8903 `gpRepTable(e)`
- L8910 `gpKpis(model)`
- L8918 `gpWeekly(model)`
- L8924 `gpMuscles(model)`
- L8931 `gpHeat(model)`
- L8938 `gpExList(model)`
- L8945 `gpExDetail(model)`
- L8958 `gpDayFood(dt)`
- L8959 `gpNutrition(model)`
- L8966 `gpRecentPRs(model)`
- L8970 `gpSessions(model)`
- L8976 `gpSessionModal(id)`
- L8987 `gpWeekModal(w)`
- L8988 `gpSelect(key)`
- L8989 `gpClick(e)`
- L9001 `renderGym()`
- L9021 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L9030 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L9036 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L9061 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L9065 `showHelp()`
- L9069 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L9071 `markBackup()`
- L9075 `exportJSON()`
- L9080 `drawBackupReminder()`
- L9090 `applyDensity()`
- L9102 `syncDayComplete()`
- L9105 `drawMeals()` — Comidas del día de un vistazo.
- L9113 `filterLog()` — Buscador de Registro.
- L9126 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L9132 `recentFoods()`
- L9137 `quickChip(e,fav)`
- L9155 `drawQuickFoods()`
- L9184 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L9188 `toggleAddPanel(id)`
- L9200 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L9211 `pasteMessage(text,ok)`
- L9219 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L9230 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L9241 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L9247 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L9268 `storableState()`

### Render único: actualiza toda la página

- L9276 `nearView(el)`
- L9278 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L9282 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L9313 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L9314 constante `REF_TABLE`
- L9321 `refTargets(mode)`
- L9322 `syncMicroMode()`
- L9335 `mealByHour(h=new Date()`
- L9342 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L9353 `dataSummary(s)`
- L9357 `confirmImport(next,name)`
- L9364 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L9370 `checkUpdate()`
- L9375 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L9390 constante `GAP_PREFER`
- L9391 constante `GAP_SKIP`
- L9392 constante `GAP_UNIT`
- L9393 `gapQty(f,x)`
- L9394 `gapFoods(key,gap,ctx)`
- L9413 `weekSources(key,sum)`
- L9419 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L9432 `gapRow(x,open,meal,sum,ctx)`
- L9448 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L9473 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L9474 `isFemale(s=state)`
- L9475 `sexLabel(s=state)`
- L9476 `sexBadge(sex)`
- L9478 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L9479 constante `OPT_FEMALE`
- L9490 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba.
- L9491 `applySexOpt(sex)`
- L9493 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L9498 `cleanPreset(p,fb)`
- L9502 `dayNamesFor(types)`
- L9504 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L9514 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L9522 `profV()`
- L9523 `isTrainDay(i)`
- L9524 `activityName(i)`
- L9525 `dayFaf(i)`
- L9526 `presetDesc(cfg,shake)`
- L9530 `profileDescription()`
- L9538 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L9540 `wizCatalog()`
- L9541 `wizOpen(opts={})`
- L9556 `wizTitle()`
- L9557 `wizPaint(sameStep=true)`
- L9566 `wizSync()`
- L9579 `wizFoodOptions()`
- L9582 `wizPresetSummary(cfg,whey)`
- L9587 `wizPresetHTML(kind)`
- L9595 `wizPreview()`
- L9606 `wizHTML()`
- L9647 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L9731 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L9732 constante `SUPP_CATALOG`
- L9754 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L9755 constante `PEAT_BREAKFAST`
- L9756 constante `PEAT_SHAKE`
- L9758 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L9765 `benfoUser()`
- L9767 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L9783 `ico(n)`
- L9785 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L9794 `showTour(i=0)`
- L9806 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L9807 `hubAction(v)`
- L9815 constante `FORM_URL` — Llegan solas a una hoja de Google (formulario del creador de la app). Sin cuentas ni datos personales.
- L9816 constante `FORM_FIELDS`
- L9817 constante `FB_CATS`
- L9819 `openFeedback()`
- L9823 `feedbackData()`
- L9830 `feedbackText()`
- L9831 `sendFeedback()`
- L9844 `shareFeedback()`
- L9861 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L9868 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L9876 constante `I18N_EN`

### v59: idioma (español / inglés)

- L11452 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L11453 constante `WD_EN`
- L11454 `trOne(s)`
- L11462 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L11463 constante `ES_FOOD_GYM`
- L11500 `trFood(s)`
- L11512 constante `TR_TPL`
- L11546 `trLower(s)`
- L11547 `trTpl(s,attr)`
- L11548 constante `FOOD_SEL`
- L11549 `trText(s,attr=false)`
- L11559 `trNode(n)`
- L11574 `trEl(el)`
- L11582 `trTree(root)`
- L11591 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L11602 `setLang(l,quiet)`
- L11615 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter), solo en la web publicada

- L11624 constante `GC_CODE`
- L11625 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L11635 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L11636 `packMove()`
- L11644 `unpackMove(code)`
- L11653 `moveData()`
- L11663 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L11669 `checkMove(code)`

### Arranque

