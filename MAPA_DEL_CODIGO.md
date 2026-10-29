# MAPA DEL CÓDIGO · BioPeat v61 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (761 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-5992; todo el JavaScript en `<script id="app">` (desde la línea 5993).

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

- L6043 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L6044 constante `AZUCAR_N`
- L6045 constante `USDA_N`
- L6051 constante `FOODS`
- L6053 constante `BASE_FAT_FIX`
- L6056 constante `EXTRA`
- L6057 constante `KEYS`
- L6059 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L6061 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L6065 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6066 constante `OPT`
- L6084 constante `LIMIT`
- L6085 `optInfo(k,goal)`
- L6092 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6100 `optLine(k,goal,unit)`
- L6107 `optRefHTML(k,goal,unit)`
- L6109 constante `DAYS`
- L6110 constante `FAF`
- L6112 constante `LOC`
- L6116 `number(v,min=0,max=1e6)`
- L6122 `decimalInputs(root=document)`
- L6123 `localDate(d=new Date()`
- L6124 `validDate(s)`
- L6129 `shift(s,n)`
- L6138 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6140 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6146 constante `DAY_TYPES`
- L6147 constante `NEW_V54`
- L6151 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6154 `bmr()` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6160 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6182 `cleanNutrients(o,required=false)`
- L6194 `cleanEntry(e)`
- L6199 `cleanPlan(p)`
- L6203 `planEntry(p)`
- L6212 `seedPlan(d,whichDate)`
- L6216 `ensureDay(d=date)`
- L6223 `effectiveEntries(d=day()`
- L6224 constante `SALTED_IDS`
- L6225 constante `SWEET_RE`
- L6226 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6244 `inferredNutrients(e)`
- L6283 `totals(entries=effectiveEntries()`
- L6292 `change(fn,message='Guardado')`
- L6296 `undo()`
- L6303 `toast(text,canUndo=false)`
- L6311 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6312 `onClick(fn)`
- L6314 `attempt(fn)`
- L6318 `modal(title,body)`
- L6327 `modalRestore()`
- L6337 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6338 `modalBack()`
- L6339 `goDate(d)`
- L6346 `renderHeader()`
- L6357 `renderRows(entries)`
- L6361 `entryValues(e)`
- L6362 `renderLog()`
- L6369 `fromFood(id,amount,meal)`
- L6375 `pantryId(name)`
- L6377 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6383 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6392 `recipe(kind)`
- L6399 `summary(entries)`
- L6403 `renderPresetInfo()`
- L6416 `stripCode(raw)`
- L6422 `parseBIO(raw,meal=$('meal-select')`
- L6428 `parseSmart(raw)`
- L6432 constante `COUNT`
- L6435 `nutrientFields(n,prefix='n_')`
- L6436 `readNutrients(form,prefix='n_')`
- L6441 `editEntry(id)`
- L6450 `editFood(id,pending=null)`
- L6455 `usageStats(days=90)`
- L6461 `renderFoods()`
- L6469 `nutrientSources(key)`
- L6476 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6477 `suppSlot(meal)`
- L6478 `renderSupps()`
- L6493 `editPlan(id)`
- L6500 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6520 `makePrompt(meal='Comida',note='')`
- L6525 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6529 `photoPrompt(meal,note)`
- L6532 `resetPhoto()`
- L6543 `openPhoto()`
- L6549 `shrinkPhoto(file)`
- L6552 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6578 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6585 `cleanFood(id,f)`
- L6589 `migrateBase(o)`
- L6608 `download(name,text,type)`
- L6617 `portable()`
- L6654 `syncAppIcons()`
- L6662 `downloadAppIcons()`
- L6699 constante `PROFILES_KEY`
- L6701 `ensureProfilesStore()`
- L6720 `saveProfilesStore(st)`
- L6724 `syncCurrentProfileToStore(rawStr)`
- L6730 `activeProfileName()`
- L6734 `renderProfilesList()`
- L6776 `switchProfile(id)`
- L6798 `deleteProfileById(id)`
- L6822 `refreshDrawerSummary()`
- L6839 `toggleLeftDrawer(force)`
- L6854 `buildAIExportText(rangeOverride)`
- L7102 `copyAIExport()`
- L7116 `downloadAIExport()`
- L7125 `renderDrawerChat()`
- L7144 `buildDrawerChatPrompt(question)`
- L7156 `askDrawerAI(rawQuestion)`
- L7243 `storageStatus()`
- L7249 `idbReadWrite(mode,value)`
- L7250 `openDB()`
- L7251 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L7264 `setQuantity(id,value,msg='Cantidad actualizada')`
- L7268 `niceStep(v)`
- L7269 `stepQuantity(id,dir)`
- L7323 `renderAppInfo()`
- L7338 `init()`
- L7362 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L7364 `setNav(v)`
- L7369 `go(v,focus)`
- L7381 `syncDatePill()`
- L7385 `animateValue(el,to,suffix='%',digits=0)`
- L7394 `tick(now)`
- L7397 `macroCard(key,name,color)`
- L7398 `renderToday()`
- L7421 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L7423 constante `HOME`
- L7425 `coachCandidates()`
- L7431 `coachIdeas(t,g,ref,meal)`
- L7444 `renderCoach()`
- L7462 `coachPrompt()`
- L7470 `nutrientDetailStandard(key)`
- L7484 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L7490 `upgradeTo12(s,o)`
- L7495 `benfotiamineTotals(entries=effectiveEntries()`
- L7504 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L7506 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L7518 `microStat(m,t=totals()`
- L7523 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L7531 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L7532 `ratioInfo(key,t=totals()`
- L7567 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L7584 constante `RATIO_ENDS`
- L7585 `ratioBar(i,big=false)`
- L7590 `ratioNeed(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L7607 `needHTML(i,t)`
- L7608 `renderRatios()`
- L7613 `ratioDetail(key)`
- L7623 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L7640 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L7655 `renderMicroMap()`
- L7659 `nutrientDetailForDay(key)`
- L7664 `editTargetsForm()`
- L7674 `mealData()`
- L7679 `renderMealSegments()`
- L7687 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L7697 constante `FAT_KEYS`
- L7699 `fatData(entries=effectiveEntries()`
- L7705 `energyData(entries=effectiveEntries()`
- L7709 `segmentedBar(items,total,attr)`
- L7713 `renderMealChart()`
- L7718 `renderFat()`
- L7726 `fatDetail(key)`
- L7731 `energyDetail(key)`
- L7738 `portionCandidates(q='')`
- L7743 `openPortion()`
- L7756 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L7771 `templates()`
- L7775 `renderExtra()`
- L7786 `updateExtra(reset=true)`
- L7798 `addExtra(id,amount)`
- L7814 `shakePreview()`
- L7815 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L7830 constante `LENS`
- L7836 `lensKey(key)`
- L7837 `lensHTML(key)`
- L7841 `appendLens(key)`
- L7850 `weekDates()`

### IA en la página: conexión directa o por servidor

- L7860 constante `MEAL_WORD`
- L7861 `mealOfWord(w)`
- L7862 `mealFromText(raw,fallback)`
- L7866 `canonMeal(v,fallback)`
- L7874 `localMeal(raw,meal)`
- L7880 constante `AI_FALLBACK`
- L7881 `applyAIConfig(raw)`
- L7907 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L7908 `callGemini(model,key,prompt,img,signal,think=true)`
- L7926 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L7933 `aiProv(m=$('ai-mode')`
- L7934 `aiBase(mode)`
- L7943 `chatHeaders(mode,key)`
- L7950 `callChat(mode,model,key,prompt,img,signal)` — ChatGPT, Claude, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L7980 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L7988 constante `MODEL_PREF`
- L7989 `pickModel(ids)`
- L7994 `ensureModel(st)`
- L8005 `syncProvider()`
- L8018 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L8052 constante `AI_PREF`
- L8053 `aiConnected()`
- L8054 `syncAI()`
- L8056 `saveAIPrefs()`
- L8057 `loadAIPrefs()`
- L8058 `openAISetup()`
- L8064 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L8071 constante `MACROS`
- L8073 `cleanGoals(o,fallback)`
- L8078 `cleanCompare(o={})`
- L8082 `snapshotDay(d,reference='saved')`
- L8087 `upgradeTo17(s,o)`
- L8092 `entriesFor(d,source=weekSource)`
- L8096 `dayRow(dt,source=weekSource)`
- L8100 `goalsFor(dt)`
- L8106 `metricValue(r,key)`
- L8112 `targetOf(dt,key)`
- L8116 `weekSummary()`
- L8120 `aggregate(key,summary=weekSummary()`
- L8124 `tone(pct,mode='macro')`
- L8131 `pctText(a)`
- L8132 `weekProgress(a,color)`
- L8133 `renderWeekMicros(s)`
- L8145 `ratioAggregate(s,num,den)`
- L8149 `renderWeekRatios(s)`
- L8155 `renderWeekTable(s)`
- L8156 `weeklyDetail(key,oneDate=null)`
- L8165 `weekRatioDetail(key)`
- L8173 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L8179 `openDay(dt)`
- L8217 `withDayGoals(fn)`
- L8222 `renderMicros()`
- L8223 `nutrientDetail(key)`
- L8224 `editTargets()`
- L8225 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L8235 `summaryFor(start)`
- L8239 `ringSVG(pct,color,marker)`
- L8241 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L8245 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L8260 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L8261 `macroTone(p)`
- L8262 `dayMacroPct(dt,k)`
- L8263 `renderWeekly()`
- L8286 `weekDetail(dt,picked)`
- L8294 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L8304 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L8310 `sparkline(pts)`
- L8316 `renderCalendar()`
- L8333 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L8334 `splitMeals(raw)`
- L8344 `localDay(raw,fallback)`
- L8351 `promptDay(raw,fallback)`
- L8352 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L8374 `parseCsv(text)`
- L8389 `hevyDate(value,format='auto')`
- L8406 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L8421 constante `GYM_APPS`
- L8423 `gymSig(headers)`
- L8424 `gymApp(headers)`
- L8425 `hevyMapping()`
- L8426 `gymSaved()`
- L8427 `renderMapping(parsed)`
- L8444 `optionalNum(v,min=0,max=1e7)`
- L8449 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L8456 `buildHevy(parsed,map)`
- L8490 `cleanWorkout(s)`
- L8497 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L8512 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L8513 constante `GP_ALIAS`
- L8523 `gpNorm(s)`
- L8524 `gpKey(name)`
- L8528 `gpF(n,d=0)`
- L8529 `gpDate(d,opt)`
- L8530 `gpMonday(d)`
- L8531 constante `GP_GROUPS`
- L8546 constante `GP_COLORS`
- L8547 `gpGroup(name)`
- L8548 `gpWorkSets(s)`
- L8549 `gpModel()`
- L8573 `gpSessionMetrics(e,sets)`
- L8588 constante `GP_METRICS`
- L8593 `gpMetricsFor(e)`
- L8594 `gpRangeHist(e)`
- L8595 `gpPRs(model)`
- L8618 `gpStatus(e)`
- L8636 `gpNext(e)`
- L8644 `gpChart(e)`
- L8672 `gpPointDetail(e)`
- L8678 `gpRepTable(e)`
- L8685 `gpKpis(model)`
- L8693 `gpWeekly(model)`
- L8699 `gpMuscles(model)`
- L8706 `gpHeat(model)`
- L8713 `gpExList(model)`
- L8720 `gpExDetail(model)`
- L8733 `gpDayFood(dt)`
- L8734 `gpNutrition(model)`
- L8741 `gpRecentPRs(model)`
- L8745 `gpSessions(model)`
- L8751 `gpSessionModal(id)`
- L8762 `gpWeekModal(w)`
- L8763 `gpSelect(key)`
- L8764 `gpClick(e)`
- L8776 `renderGym()`
- L8796 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L8805 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L8811 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L8836 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L8840 `showHelp()`
- L8844 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L8846 `markBackup()`
- L8850 `exportJSON()`
- L8855 `drawBackupReminder()`
- L8865 `applyDensity()`
- L8877 `syncDayComplete()`
- L8880 `drawMeals()` — Comidas del día de un vistazo.
- L8888 `filterLog()` — Buscador de Registro.
- L8901 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L8907 `recentFoods()`
- L8912 `quickChip(e,fav)`
- L8930 `drawQuickFoods()`
- L8959 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L8963 `toggleAddPanel(id)`
- L8975 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L8986 `pasteMessage(text,ok)`
- L8994 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L9005 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L9016 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L9022 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L9043 `storableState()`

### Render único: actualiza toda la página

- L9051 `nearView(el)`
- L9053 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L9057 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L9088 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L9089 constante `REF_TABLE`
- L9096 `refTargets(mode)`
- L9097 `syncMicroMode()`
- L9110 `mealByHour(h=new Date()`
- L9117 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L9128 `dataSummary(s)`
- L9132 `confirmImport(next,name)`
- L9139 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L9145 `checkUpdate()`
- L9150 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L9165 constante `GAP_PREFER`
- L9166 constante `GAP_SKIP`
- L9167 constante `GAP_UNIT`
- L9168 `gapQty(f,x)`
- L9169 `gapFoods(key,gap,ctx)`
- L9188 `weekSources(key,sum)`
- L9194 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L9207 `gapRow(x,open,meal,sum,ctx)`
- L9223 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L9248 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L9249 `isFemale(s=state)`
- L9250 `sexLabel(s=state)`
- L9251 `sexBadge(sex)`
- L9253 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L9254 constante `OPT_FEMALE`
- L9265 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba.
- L9266 `applySexOpt(sex)`
- L9268 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L9273 `cleanPreset(p,fb)`
- L9277 `dayNamesFor(types)`
- L9279 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L9289 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L9297 `profV()`
- L9298 `isTrainDay(i)`
- L9299 `activityName(i)`
- L9300 `dayFaf(i)`
- L9301 `presetDesc(cfg,shake)`
- L9305 `profileDescription()`
- L9313 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L9315 `wizCatalog()`
- L9316 `wizOpen(opts={})`
- L9331 `wizTitle()`
- L9332 `wizPaint(sameStep=true)`
- L9341 `wizSync()`
- L9354 `wizFoodOptions()`
- L9357 `wizPresetSummary(cfg,whey)`
- L9362 `wizPresetHTML(kind)`
- L9370 `wizPreview()`
- L9381 `wizHTML()`
- L9422 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L9506 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L9507 constante `SUPP_CATALOG`
- L9529 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L9530 constante `PEAT_BREAKFAST`
- L9531 constante `PEAT_SHAKE`
- L9533 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L9540 `benfoUser()`
- L9542 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L9558 `ico(n)`
- L9560 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L9569 `showTour(i=0)`
- L9581 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L9582 `hubAction(v)`
- L9590 constante `FORM_URL` — Llegan solas a una hoja de Google (formulario del creador de la app). Sin cuentas ni datos personales.
- L9591 constante `FORM_FIELDS`
- L9592 constante `FB_CATS`
- L9594 `openFeedback()`
- L9598 `feedbackData()`
- L9605 `feedbackText()`
- L9606 `sendFeedback()`
- L9619 `shareFeedback()`
- L9636 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L9643 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L9651 constante `I18N_EN`

### v59: idioma (español / inglés)

- L11227 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L11228 constante `WD_EN`
- L11229 `trOne(s)`
- L11237 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L11238 constante `ES_FOOD_GYM`
- L11275 `trFood(s)`
- L11287 constante `TR_TPL`
- L11321 `trLower(s)`
- L11322 `trTpl(s,attr)`
- L11323 constante `FOOD_SEL`
- L11324 `trText(s,attr=false)`
- L11334 `trNode(n)`
- L11349 `trEl(el)`
- L11357 `trTree(root)`
- L11366 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L11377 `setLang(l,quiet)`
- L11390 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter), solo en la web publicada

- L11399 constante `GC_CODE`
- L11400 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L11410 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L11411 `packMove()`
- L11419 `unpackMove(code)`
- L11428 `moveData()`
- L11438 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L11444 `checkMove(code)`

### Arranque

