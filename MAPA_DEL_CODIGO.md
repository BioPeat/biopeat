# MAPA DEL CÓDIGO · BioPeat v54 (revisión de datos 24)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (604 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-5788; todo el JavaScript en `<script id="app">` (desde la línea 5789).

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

- L5832 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L5833 constante `AZUCAR_N`
- L5834 constante `USDA_N`
- L5840 constante `FOODS`
- L5842 constante `BASE_FAT_FIX`
- L5845 constante `EXTRA`
- L5846 constante `KEYS`
- L5848 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L5850 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L5854 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L5855 constante `OPT`
- L5873 constante `LIMIT`
- L5874 `optInfo(k,goal)`
- L5879 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L5887 `optLine(k,goal,unit)`
- L5894 `optRefHTML(k,goal,unit)`
- L5896 constante `DAYS`
- L5897 constante `FAF`
- L5901 `number(v,min=0,max=1e6)`
- L5907 `decimalInputs(root=document)`
- L5908 `localDate(d=new Date()`
- L5909 `validDate(s)`
- L5914 `shift(s,n)`
- L5922 constante `CONTEXT`
- L5923 `defaults()`
- L5925 `bmr()`
- L5931 constante `DEF_P` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L5932 `targetFor(d)`
- L5948 `cleanNutrients(o,required=false)`
- L5960 `cleanEntry(e)`
- L5965 `cleanPlan(p)`
- L5969 `planEntry(p)`
- L5978 `seedPlan(d,whichDate)`
- L5982 `ensureDay(d=date)`
- L5989 `effectiveEntries(d=day()`
- L5990 constante `SALTED_IDS`
- L5991 constante `SWEET_RE`
- L5992 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6010 `inferredNutrients(e)`
- L6049 `totals(entries=effectiveEntries()`
- L6058 `change(fn,message='Guardado')`
- L6062 `undo()`
- L6069 `toast(text,canUndo=false)`
- L6077 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6078 `onClick(fn)`
- L6080 `attempt(fn)`
- L6084 `modal(title,body)`
- L6093 `modalRestore()`
- L6103 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6104 `modalBack()`
- L6105 `goDate(d)`
- L6112 `renderHeader()`
- L6123 `renderRows(entries)`
- L6127 `entryValues(e)`
- L6128 `renderLog()`
- L6135 `fromFood(id,amount,meal)`
- L6141 `pantryId(name)`
- L6143 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6149 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6158 `recipe(kind)`
- L6164 `summary(entries)`
- L6168 `renderPresetInfo()`
- L6172 `stripCode(raw)`
- L6178 `parseBIO(raw,meal=$('meal-select')`
- L6184 `parseSmart(raw)`
- L6188 constante `COUNT`
- L6191 `nutrientFields(n,prefix='n_')`
- L6192 `readNutrients(form,prefix='n_')`
- L6197 `editEntry(id)`
- L6206 `editFood(id,pending=null)`
- L6211 `usageStats(days=90)`
- L6217 `renderFoods()`
- L6225 `nutrientSources(key)`
- L6232 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6233 `suppSlot(meal)`
- L6234 `renderSupps()`
- L6249 `editPlan(id)`
- L6256 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6275 `makePrompt(meal='Comida',note='')`
- L6280 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6284 `photoPrompt(meal,note)`
- L6287 `resetPhoto()`
- L6298 `openPhoto()`
- L6304 `shrinkPhoto(file)`
- L6307 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6333 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6340 `cleanFood(id,f)`
- L6344 `migrateBase(o)`
- L6363 `download(name,text,type)`
- L6372 `portable()`
- L6409 `syncAppIcons()`
- L6417 `downloadAppIcons()`
- L6454 constante `PROFILES_KEY`
- L6456 `ensureProfilesStore()`
- L6475 `saveProfilesStore(st)`
- L6479 `syncCurrentProfileToStore(rawStr)`
- L6485 `activeProfileName()`
- L6489 `renderProfilesList()`
- L6530 `switchProfile(id)`
- L6551 `createNewProfile(name,weight,height,age,mode)`
- L6588 `deleteProfileById(id)`
- L6612 `refreshDrawerSummary()`
- L6629 `toggleLeftDrawer(force)`
- L6644 `buildAIExportText(rangeOverride)`
- L6891 `copyAIExport()`
- L6905 `downloadAIExport()`
- L6914 `renderDrawerChat()`
- L6933 `buildDrawerChatPrompt(question)`
- L6945 `askDrawerAI(rawQuestion)`
- L7036 `storageStatus()`
- L7042 `idbReadWrite(mode,value)`
- L7043 `openDB()`
- L7044 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L7057 `setQuantity(id,value,msg='Cantidad actualizada')`
- L7061 `niceStep(v)`
- L7062 `stepQuantity(id,dir)`
- L7116 `renderAppInfo()`
- L7131 `init()`

### Corrección de la pauta declarada (revisión 11 de los datos)

- L7149 `planFamily(e)`
- L7161 `correctedPlan(plan)`
- L7167 `syncCorrectedDay(s,dt)`
- L7176 `upgradeTo11(s,o)`

### Navegación: una sola página; la barra inferior solo desplaza

- L7182 `setNav(v)`
- L7187 `go(v,focus)`
- L7199 `syncDatePill()`
- L7203 `animateValue(el,to,suffix='%',digits=0)`
- L7212 `tick(now)`
- L7215 `macroCard(key,name,color)`
- L7216 `renderToday()`
- L7239 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L7241 constante `HOME`
- L7243 `coachCandidates()`
- L7249 `coachIdeas(t,g,ref,meal)`
- L7262 `renderCoach()`
- L7279 `coachPrompt()`
- L7287 `nutrientDetailStandard(key)`
- L7301 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L7307 `upgradeTo12(s,o)`
- L7312 `benfotiamineTotals(entries=effectiveEntries()`
- L7321 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L7323 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L7335 `microStat(m,t=totals()`
- L7340 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L7348 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L7349 `ratioInfo(key,t=totals()`
- L7384 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L7401 constante `RATIO_ENDS`
- L7402 `ratioBar(i,big=false)`
- L7407 `ratioNeed(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L7424 `needHTML(i,t)`
- L7425 `renderRatios()`
- L7430 `ratioDetail(key)`
- L7440 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L7457 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L7472 `renderMicroMap()`
- L7476 `nutrientDetailForDay(key)`
- L7481 `editTargetsForm()`
- L7491 `mealData()`
- L7496 `renderMealSegments()`
- L7504 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L7514 constante `FAT_KEYS`
- L7516 `fatData(entries=effectiveEntries()`
- L7522 `energyData(entries=effectiveEntries()`
- L7526 `segmentedBar(items,total,attr)`
- L7530 `renderMealChart()`
- L7535 `renderFat()`
- L7543 `fatDetail(key)`
- L7548 `energyDetail(key)`
- L7555 `portionCandidates(q='')`
- L7560 `openPortion()`
- L7573 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L7588 `templates()`
- L7592 `renderExtra()`
- L7603 `updateExtra(reset=true)`
- L7615 `addExtra(id,amount)`
- L7631 `shakePreview()`
- L7632 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L7647 constante `LENS`
- L7653 `lensKey(key)`
- L7654 `lensHTML(key)`
- L7658 `appendLens(key)`
- L7667 `weekDates()`

### IA en la página: conexión directa o por servidor

- L7677 constante `MEAL_WORD`
- L7678 `mealOfWord(w)`
- L7679 `mealFromText(raw,fallback)`
- L7683 `canonMeal(v,fallback)`
- L7691 `localMeal(raw,meal)`
- L7697 constante `AI_FALLBACK`
- L7698 `applyAIConfig(raw)`
- L7724 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L7725 `callGemini(model,key,prompt,img,signal,think=true)`
- L7742 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L7774 constante `AI_PREF`
- L7775 `aiConnected()`
- L7776 `syncAI()`
- L7778 `saveAIPrefs()`
- L7779 `loadAIPrefs()`
- L7780 `openAISetup()`
- L7786 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L7793 constante `MACROS`
- L7795 `cleanGoals(o,fallback)`
- L7800 `cleanCompare(o={})`
- L7804 `snapshotDay(d,reference='saved')`
- L7809 `upgradeTo17(s,o)`
- L7814 `entriesFor(d,source=weekSource)`
- L7818 `dayRow(dt,source=weekSource)`
- L7822 `goalsFor(dt)`
- L7828 `metricValue(r,key)`
- L7834 `targetOf(dt,key)`
- L7838 `weekSummary()`
- L7842 `aggregate(key,summary=weekSummary()`
- L7846 `tone(pct,mode='macro')`
- L7853 `pctText(a)`
- L7854 `weekProgress(a,color)`
- L7855 `renderWeekMicros(s)`
- L7867 `ratioAggregate(s,num,den)`
- L7871 `renderWeekRatios(s)`
- L7877 `renderWeekTable(s)`
- L7878 `weeklyDetail(key,oneDate=null)`
- L7887 `weekRatioDetail(key)`
- L7895 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L7901 `openDay(dt)`
- L7939 `withDayGoals(fn)`
- L7944 `renderMicros()`
- L7945 `nutrientDetail(key)`
- L7946 `editTargets()`
- L7947 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L7957 `summaryFor(start)`
- L7961 `ringSVG(pct,color,marker)`
- L7963 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L7967 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L7982 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L7983 `macroTone(p)`
- L7984 `dayMacroPct(dt,k)`
- L7985 `renderWeekly()`
- L8008 `weekDetail(dt,picked)`
- L8016 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L8026 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L8032 `sparkline(pts)`
- L8038 `renderCalendar()`
- L8055 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L8056 `splitMeals(raw)`
- L8066 `localDay(raw,fallback)`
- L8073 `promptDay(raw,fallback)`
- L8074 `analyzeDay(usePhoto=false)`

### Gimnasio: importación de CSV de HEVY, sesiones y análisis IA

- L8096 `parseCsv(text)`
- L8111 `hevyDate(value,format='auto')`
- L8120 constante `MAP`
- L8121 `hevyMapping()`
- L8122 `renderMapping(parsed)`
- L8129 `optionalNum(v,min=0,max=1e7)`
- L8133 `buildHevy(parsed,map)`
- L8143 `cleanWorkout(s)`
- L8150 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L8165 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L8166 constante `GP_ALIAS`
- L8176 `gpNorm(s)`
- L8177 `gpKey(name)`
- L8181 `gpF(n,d=0)`
- L8182 `gpDate(d,opt)`
- L8183 `gpMonday(d)`
- L8184 constante `GP_GROUPS`
- L8199 constante `GP_COLORS`
- L8200 `gpGroup(name)`
- L8201 `gpWorkSets(s)`
- L8202 `gpModel()`
- L8226 `gpSessionMetrics(e,sets)`
- L8241 constante `GP_METRICS`
- L8246 `gpMetricsFor(e)`
- L8247 `gpRangeHist(e)`
- L8248 `gpPRs(model)`
- L8271 `gpStatus(e)`
- L8289 `gpNext(e)`
- L8297 `gpChart(e)`
- L8325 `gpPointDetail(e)`
- L8331 `gpRepTable(e)`
- L8338 `gpKpis(model)`
- L8346 `gpWeekly(model)`
- L8352 `gpMuscles(model)`
- L8359 `gpHeat(model)`
- L8366 `gpExList(model)`
- L8373 `gpExDetail(model)`
- L8386 `gpDayFood(dt)`
- L8387 `gpNutrition(model)`
- L8394 `gpRecentPRs(model)`
- L8398 `gpSessions(model)`
- L8404 `gpSessionModal(id)`
- L8415 `gpWeekModal(w)`
- L8416 `gpSelect(key)`
- L8417 `gpClick(e)`
- L8429 `renderGym()`
- L8449 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L8458 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L8464 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L8488 `openMoreMenu()` — Menú «Más»: secciones poco frecuentes, sin saturar la barra inferior.
- L8495 `showHelp()`
- L8499 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L8501 `markBackup()`
- L8505 `exportJSON()`
- L8510 `drawBackupReminder()`
- L8520 `applyDensity()`
- L8532 `syncDayComplete()`
- L8535 `drawMeals()` — Comidas del día de un vistazo.
- L8543 `filterLog()` — Buscador de Registro.
- L8556 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L8562 `recentFoods()`
- L8567 `quickChip(e,fav)`
- L8585 `drawQuickFoods()`
- L8614 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L8618 `toggleAddPanel(id)`
- L8630 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L8641 `pasteMessage(text,ok)`
- L8649 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L8660 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L8669 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L8687 `storableState()`

### Render único: actualiza toda la página

- L8695 `nearView(el)`
- L8697 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L8701 `render()`
- L8736 `mealByHour(h=new Date()`
- L8743 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L8753 `dataSummary(s)`
- L8757 `confirmImport(next,name)`
- L8764 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L8770 `checkUpdate()`
- L8775 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L8790 constante `GAP_PREFER`
- L8791 constante `GAP_SKIP`
- L8792 constante `GAP_UNIT`
- L8793 `gapQty(f,x)`
- L8794 `gapFoods(key,gap,ctx)`
- L8813 `weekSources(key,sum)`
- L8819 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L8832 `gapRow(x,open,meal,sum,ctx)`
- L8848 `renderGaps(sum,s)`

### Arranque


### 1. REFERENCIAS RAY PEAT DIFERENCIADAS HOMBRE / MUJER

- L8932 constante `PEAT_SEX_TARGETS`
- L8965 constante `GOAL_TYPES`
- L8972 `getSex(st=state)`
- L8973 `isFemale(st=state)`
- L8974 `sexLabel(st=state)`
- L8976 `defaultV54ForDiego()`
- L8989 `ensureV54State(s=state,profId)`
- L9024 `applySexReferences(sex,resetTargets=false,s=state)`
- L9112 `presetItemsDesc(cfg,isShake=false)`
- L9224 `ensureWomenPeatCard()`
- L9241 `injectProfileSexControls()`

### 5. ASISTENTE INTERACTIVO EN 5 PASOS (ACTUALIZACIÓN IN-PLACE SIN ROMPER HISTORIAL)

- L9347 constante `WIZ_SUPPS_CATALOG`
- L9367 `buildWizardDraft(opts={})`
- L9412 `calcItemsSummary(items,extraWhey=0)`
- L9426 `foodOptionsHTML()`
- L9433 `showOrUpdateWizardModal(title,html)` — Actualiza el contenido del modal sin acumular entradas en history.pushState cuando ya está abierto
- L9445 `renderWizardStep()`
- L9608 `syncWizardInputs()`
- L9626 `commitWizard()`
- L9943 `bootV54()`
