# MAPA DEL CÓDIGO · BioPeat v53 (revisión de datos 23)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (549 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-5853; todo el JavaScript en `<script id="app">` (desde la línea 5854).

## Secciones de la página (id)

- `#view-today` — Resumen del día
- `#bp-sum`
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

- L5897 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L5898 constante `AZUCAR_N`
- L5899 constante `USDA_N`
- L5905 constante `FOODS`
- L5907 constante `BASE_FAT_FIX`
- L5910 constante `EXTRA`
- L5911 constante `KEYS`
- L5913 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L5915 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L5919 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L5920 constante `OPT`
- L5938 constante `LIMIT`
- L5939 `optInfo(k,goal)`
- L5944 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L5952 `optLine(k,goal,unit)`
- L5959 `optRefHTML(k,goal,unit)`
- L5961 constante `DAYS`
- L5962 constante `FAF`
- L5966 `number(v,min=0,max=1e6)`
- L5972 `decimalInputs(root=document)`
- L5973 `localDate(d=new Date()`
- L5974 `validDate(s)`
- L5979 `shift(s,n)`
- L5987 constante `CONTEXT`
- L5988 `defaults()`
- L5990 `bmr()`
- L5996 constante `DEF_P` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L5997 `targetFor(d)`
- L6013 `cleanNutrients(o,required=false)`
- L6025 `cleanEntry(e)`
- L6030 `cleanPlan(p)`
- L6034 `planEntry(p)`
- L6043 `seedPlan(d,whichDate)`
- L6047 `ensureDay(d=date)`
- L6054 `effectiveEntries(d=day()`
- L6055 constante `SALTED_IDS`
- L6056 constante `SWEET_RE`
- L6057 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6075 `inferredNutrients(e)`
- L6114 `totals(entries=effectiveEntries()`
- L6123 `change(fn,message='Guardado')`
- L6127 `undo()`
- L6134 `toast(text,canUndo=false)`
- L6142 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6143 `onClick(fn)`
- L6145 `attempt(fn)`
- L6149 `modal(title,body)`
- L6158 `modalRestore()`
- L6168 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6169 `modalBack()`
- L6170 `goDate(d)`
- L6177 `renderHeader()`
- L6188 `renderRows(entries)`
- L6192 `entryValues(e)`
- L6193 `renderLog()`
- L6200 `fromFood(id,amount,meal)`
- L6206 `pantryId(name)`
- L6208 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6214 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6223 `recipe(kind)`
- L6229 `summary(entries)`
- L6233 `renderPresetInfo()`
- L6237 `stripCode(raw)`
- L6243 `parseBIO(raw,meal=$('meal-select')`
- L6249 `parseSmart(raw)`
- L6253 constante `COUNT`
- L6256 `nutrientFields(n,prefix='n_')`
- L6257 `readNutrients(form,prefix='n_')`
- L6262 `editEntry(id)`
- L6271 `editFood(id,pending=null)`
- L6276 `usageStats(days=90)`
- L6282 `renderFoods()`
- L6290 `nutrientSources(key)`
- L6297 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6298 `suppSlot(meal)`
- L6299 `renderSupps()`
- L6314 `editPlan(id)`
- L6321 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6340 `makePrompt(meal='Comida',note='')`
- L6345 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6349 `photoPrompt(meal,note)`
- L6352 `resetPhoto()`
- L6363 `openPhoto()`
- L6369 `shrinkPhoto(file)`
- L6372 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6398 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6405 `cleanFood(id,f)`
- L6409 `migrateBase(o)`
- L6428 `download(name,text,type)`
- L6437 `portable()`
- L6473 `syncAppIcons()`
- L6481 `downloadAppIcons()`
- L6518 constante `PROFILES_KEY`
- L6520 `ensureProfilesStore()`
- L6539 `saveProfilesStore(st)`
- L6543 `syncCurrentProfileToStore(rawStr)`
- L6549 `activeProfileName()`
- L6553 `renderProfilesList()`
- L6594 `switchProfile(id)`
- L6615 `createNewProfile(name,weight,height,age,mode)`
- L6652 `deleteProfileById(id)`
- L6676 `refreshDrawerSummary()`
- L6693 `toggleLeftDrawer(force)`
- L6707 `buildAIExportText(rangeOverride)`
- L6954 `copyAIExport()`
- L6968 `downloadAIExport()`
- L6977 `renderDrawerChat()`
- L6996 `buildDrawerChatPrompt(question)`
- L7008 `askDrawerAI(rawQuestion)`
- L7099 `storageStatus()`
- L7105 `idbReadWrite(mode,value)`
- L7106 `openDB()`
- L7107 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L7120 `setQuantity(id,value,msg='Cantidad actualizada')`
- L7124 `niceStep(v)`
- L7125 `stepQuantity(id,dir)`
- L7179 `renderAppInfo()`
- L7194 `init()`

### Corrección de la pauta declarada (revisión 11 de los datos)

- L7212 `planFamily(e)`
- L7224 `correctedPlan(plan)`
- L7230 `syncCorrectedDay(s,dt)`
- L7239 `upgradeTo11(s,o)`

### Navegación: una sola página; la barra inferior solo desplaza

- L7245 `setNav(v)`
- L7250 `go(v,focus)`
- L7262 `syncDatePill()`
- L7266 `animateValue(el,to,suffix='%',digits=0)`
- L7275 `tick(now)`
- L7278 `macroCard(key,name,color)`
- L7279 `renderToday()`
- L7302 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L7304 constante `HOME`
- L7306 `coachCandidates()`
- L7312 `coachIdeas(t,g,ref,meal)`
- L7325 `renderCoach()`
- L7342 `coachPrompt()`
- L7350 `nutrientDetailStandard(key)`
- L7364 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L7370 `upgradeTo12(s,o)`
- L7375 `benfotiamineTotals(entries=effectiveEntries()`
- L7384 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L7386 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L7398 `microStat(m,t=totals()`
- L7403 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L7411 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L7412 `ratioInfo(key,t=totals()`
- L7447 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L7464 constante `RATIO_ENDS`
- L7465 `ratioBar(i,big=false)`
- L7470 `ratioNeed(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L7487 `needHTML(i,t)`
- L7488 `renderRatios()`
- L7493 `ratioDetail(key)`
- L7503 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L7520 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L7535 `renderMicroMap()`
- L7539 `nutrientDetailForDay(key)`
- L7544 `editTargetsForm()`
- L7554 `mealData()`
- L7559 `renderMealSegments()`
- L7567 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L7577 constante `FAT_KEYS`
- L7579 `fatData(entries=effectiveEntries()`
- L7585 `energyData(entries=effectiveEntries()`
- L7589 `segmentedBar(items,total,attr)`
- L7593 `renderMealChart()`
- L7598 `renderFat()`
- L7606 `fatDetail(key)`
- L7611 `energyDetail(key)`
- L7618 `portionCandidates(q='')`
- L7623 `openPortion()`
- L7636 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L7651 `templates()`
- L7655 `renderExtra()`
- L7666 `updateExtra(reset=true)`
- L7678 `addExtra(id,amount)`
- L7694 `shakePreview()`
- L7695 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L7710 constante `LENS`
- L7716 `lensKey(key)`
- L7717 `lensHTML(key)`
- L7721 `appendLens(key)`
- L7730 `weekDates()`

### IA en la página: conexión directa o por servidor

- L7740 constante `MEAL_WORD`
- L7741 `mealOfWord(w)`
- L7742 `mealFromText(raw,fallback)`
- L7746 `canonMeal(v,fallback)`
- L7754 `localMeal(raw,meal)`
- L7760 constante `AI_FALLBACK`
- L7761 `applyAIConfig(raw)`
- L7787 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L7788 `callGemini(model,key,prompt,img,signal,think=true)`
- L7805 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L7837 constante `AI_PREF`
- L7838 `aiConnected()`
- L7839 `syncAI()`
- L7841 `saveAIPrefs()`
- L7842 `loadAIPrefs()`
- L7843 `openAISetup()`
- L7849 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L7856 constante `MACROS`
- L7858 `cleanGoals(o,fallback)`
- L7863 `cleanCompare(o={})`
- L7867 `snapshotDay(d,reference='saved')`
- L7872 `upgradeTo17(s,o)`
- L7877 `entriesFor(d,source=weekSource)`
- L7881 `dayRow(dt,source=weekSource)`
- L7885 `goalsFor(dt)`
- L7891 `metricValue(r,key)`
- L7897 `targetOf(dt,key)`
- L7901 `weekSummary()`
- L7905 `aggregate(key,summary=weekSummary()`
- L7909 `tone(pct,mode='macro')`
- L7916 `pctText(a)`
- L7917 `weekProgress(a,color)`
- L7918 `renderWeekMicros(s)`
- L7930 `ratioAggregate(s,num,den)`
- L7934 `renderWeekRatios(s)`
- L7940 `renderWeekTable(s)`
- L7941 `weeklyDetail(key,oneDate=null)`
- L7950 `weekRatioDetail(key)`
- L7958 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L7964 `openDay(dt)`
- L8002 `withDayGoals(fn)`
- L8007 `renderMicros()`
- L8008 `nutrientDetail(key)`
- L8009 `editTargets()`
- L8010 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L8020 `summaryFor(start)`
- L8024 `ringSVG(pct,color,marker)`
- L8026 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L8030 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L8045 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L8046 `macroTone(p)`
- L8047 `dayMacroPct(dt,k)`
- L8048 `renderWeekly()`
- L8071 `weekDetail(dt,picked)`
- L8079 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L8089 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L8095 `sparkline(pts)`
- L8101 `renderCalendar()`
- L8118 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L8119 `splitMeals(raw)`
- L8129 `localDay(raw,fallback)`
- L8136 `promptDay(raw,fallback)`
- L8137 `analyzeDay(usePhoto=false)`

### Gimnasio: importación de CSV de HEVY, sesiones y análisis IA

- L8159 `parseCsv(text)`
- L8174 `hevyDate(value,format='auto')`
- L8183 constante `MAP`
- L8184 `hevyMapping()`
- L8185 `renderMapping(parsed)`
- L8192 `optionalNum(v,min=0,max=1e7)`
- L8196 `buildHevy(parsed,map)`
- L8206 `cleanWorkout(s)`
- L8213 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L8228 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L8229 constante `GP_ALIAS`
- L8239 `gpNorm(s)`
- L8240 `gpKey(name)`
- L8244 `gpF(n,d=0)`
- L8245 `gpDate(d,opt)`
- L8246 `gpMonday(d)`
- L8247 constante `GP_GROUPS`
- L8262 constante `GP_COLORS`
- L8263 `gpGroup(name)`
- L8264 `gpWorkSets(s)`
- L8265 `gpModel()`
- L8289 `gpSessionMetrics(e,sets)`
- L8304 constante `GP_METRICS`
- L8309 `gpMetricsFor(e)`
- L8310 `gpRangeHist(e)`
- L8311 `gpPRs(model)`
- L8334 `gpStatus(e)`
- L8352 `gpNext(e)`
- L8360 `gpChart(e)`
- L8388 `gpPointDetail(e)`
- L8394 `gpRepTable(e)`
- L8401 `gpKpis(model)`
- L8409 `gpWeekly(model)`
- L8415 `gpMuscles(model)`
- L8422 `gpHeat(model)`
- L8429 `gpExList(model)`
- L8436 `gpExDetail(model)`
- L8449 `gpDayFood(dt)`
- L8450 `gpNutrition(model)`
- L8457 `gpRecentPRs(model)`
- L8461 `gpSessions(model)`
- L8467 `gpSessionModal(id)`
- L8478 `gpWeekModal(w)`
- L8479 `gpSelect(key)`
- L8480 `gpClick(e)`
- L8492 `renderGym()`
- L8512 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L8521 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L8527 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L8551 `openMoreMenu()` — Menú «Más»: secciones poco frecuentes, sin saturar la barra inferior.
- L8558 `showHelp()`
- L8562 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L8564 `markBackup()`
- L8568 `exportJSON()`
- L8573 `drawBackupReminder()`
- L8583 `applyDensity()`
- L8595 `syncDayComplete()`
- L8598 `drawMeals()` — Comidas del día de un vistazo.
- L8606 `filterLog()` — Buscador de Registro.
- L8619 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L8625 `recentFoods()`
- L8630 `quickChip(e,fav)`
- L8648 `drawQuickFoods()`
- L8677 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L8681 `toggleAddPanel(id)`
- L8693 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L8704 `pasteMessage(text,ok)`
- L8712 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L8723 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L8732 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L8750 `storableState()`

### Render único: actualiza toda la página

- L8758 `nearView(el)`
- L8760 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L8764 `render()`
- L8799 `mealByHour(h=new Date()`
- L8806 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L8816 `dataSummary(s)`
- L8820 `confirmImport(next,name)`
- L8827 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L8833 `checkUpdate()`
- L8838 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L8853 constante `GAP_PREFER`
- L8854 constante `GAP_SKIP`
- L8855 constante `GAP_UNIT`
- L8856 `gapQty(f,x)`
- L8857 `gapFoods(key,gap,ctx)`
- L8876 `weekSources(key,sum)`
- L8882 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L8895 `gapRow(x,open,meal,sum,ctx)`
- L8911 `renderGaps(sum,s)`

### v53: Vista Resumen propia de Hoy (no es la vista normal en pequeño)

- L8934 constante `SUM_SHORT`
- L8935 constante `SUM_MAIN`
- L8936 `sumName(m)`
- L8937 `sumMacro(key,name,val,goal)`
- L8945 `sumMicros(t)`
- L8964 `sumTip(t,g,d)`
- L8977 `renderSummary()`

### Arranque

