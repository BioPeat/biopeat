# MAPA DEL CÓDIGO · BioPeat v72 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (862 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-6345; todo el JavaScript en `<script id="app">` (desde la línea 6346).

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

- L6407 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L6408 constante `AZUCAR_N`
- L6409 constante `USDA_N`
- L6415 constante `FOODS`
- L6417 constante `BASE_FAT_FIX`
- L6420 constante `EXTRA`
- L6421 constante `KEYS`
- L6423 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L6425 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L6429 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6430 constante `OPT`
- L6451 constante `LIMIT`
- L6452 `optInfo(k,goal)`
- L6459 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6467 `optLine(k,goal,unit)`
- L6474 `optRefHTML(k,goal,unit)`
- L6476 constante `DAYS`
- L6477 constante `FAF`
- L6479 constante `LOC`
- L6483 `number(v,min=0,max=1e6)`
- L6489 `decimalInputs(root=document)`
- L6490 `localDate(d=new Date()`
- L6491 `validDate(s)`
- L6496 `shift(s,n)`
- L6505 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6507 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6513 constante `DAY_TYPES`
- L6514 constante `NEW_V54`
- L6518 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6521 `bmr()` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6527 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6549 `cleanNutrients(o,required=false)`
- L6561 `cleanEntry(e)`
- L6566 `cleanPlan(p)`
- L6570 `planEntry(p)`
- L6579 `seedPlan(d,whichDate)`
- L6583 `ensureDay(d=date)`
- L6590 `effectiveEntries(d=day()`
- L6591 constante `SALTED_IDS`
- L6592 constante `SWEET_RE`
- L6593 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6611 `inferredNutrients(e)`
- L6650 `totals(entries=effectiveEntries()`
- L6659 `change(fn,message='Guardado')`
- L6663 `undo()`
- L6670 `toast(text,canUndo=false)`
- L6678 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6679 `onClick(fn)`
- L6681 `attempt(fn)`
- L6685 `modal(title,body)`
- L6694 `modalRestore()`
- L6704 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6705 `modalBack()`
- L6706 `goDate(d)`
- L6713 `renderHeader()`
- L6726 `renderRows(entries)`
- L6730 `entryValues(e)`
- L6731 `renderLog()`
- L6738 `fromFood(id,amount,meal)`
- L6744 `pantryId(name)`
- L6746 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6752 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6761 `recipe(kind)`
- L6768 `summary(entries)`
- L6772 `renderPresetInfo()`
- L6785 `stripCode(raw)`
- L6791 `parseBIO(raw,meal=$('meal-select')`
- L6797 `parseSmart(raw)`
- L6801 constante `COUNT`
- L6804 `nutrientFields(n,prefix='n_')`
- L6805 `readNutrients(form,prefix='n_')`
- L6810 `editEntry(id)`
- L6819 `editFood(id,pending=null)`
- L6824 `usageStats(days=90)`
- L6830 `renderFoods()`
- L6838 `nutrientSources(key)`
- L6845 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6846 `suppSlot(meal)`
- L6847 `renderSupps()`
- L6862 `editPlan(id)`
- L6869 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6889 `makePrompt(meal='Comida',note='')`
- L6894 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6898 `photoPrompt(meal,note)`
- L6901 `resetPhoto()`
- L6912 `openPhoto()`
- L6918 `shrinkPhoto(file)`
- L6921 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6947 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6954 `cleanFood(id,f)`
- L6958 `migrateBase(o)`
- L6977 `download(name,text,type)`
- L6986 `portable()`
- L7027 `syncAppIcons()`
- L7035 `downloadAppIcons()`
- L7072 constante `PROFILES_KEY`
- L7074 `ensureProfilesStore()`
- L7094 `resetProfileSessionUI()`
- L7101 `saveProfilesStore(st)`
- L7110 `syncCurrentProfileToStore(rawStr)`
- L7116 `activeProfileName()`
- L7120 `renderProfilesList()`
- L7162 `switchProfile(id)`
- L7184 `deleteProfileById(id)`
- L7209 `refreshDrawerSummary()`
- L7226 `toggleLeftDrawer(force)`
- L7241 `buildAIExportText(rangeOverride)`
- L7492 `copyAIExport()`
- L7506 `downloadAIExport()`
- L7515 `renderDrawerChat()`
- L7534 `buildDrawerChatContext()`
- L7571 `buildDrawerChatPrompt(question)`
- L7583 `askDrawerAI(rawQuestion)`
- L7670 `storageStatus()`
- L7676 `idbReadWrite(mode,value,key='current')`
- L7677 `openDB()`
- L7678 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L7691 `setQuantity(id,value,msg='Cantidad actualizada')`
- L7695 `niceStep(v)`
- L7696 `stepQuantity(id,dir)`
- L7750 `renderAppInfo()`
- L7765 `init()`
- L7793 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L7795 `setNav(v)`
- L7800 `go(v,focus)`
- L7811 constante `THEME_KEY`
- L7812 constante `SUN_SVG`
- L7813 constante `MOON_SVG`
- L7815 `syncThemeUI()`
- L7827 `toggleTheme()`
- L7836 `syncLogoTheme()`
- L7847 `applyMenuBtnState()`
- L7870 `syncDatePill()`
- L7883 `clampBtnPos(el,x,y)`
- L7893 `bindDraggableBtn(el,storeKey)`
- L7978 `bindDrawerGestures()`
- L8015 `animateValue(el,to,suffix='%',digits=0)`
- L8024 `tick(now)`
- L8027 `macroCard(key,name,color)`
- L8028 `renderToday()`
- L8051 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L8053 constante `HOME`
- L8055 `coachCandidates()`
- L8061 `coachIdeas(t,g,ref,meal)`
- L8074 `renderCoach()`
- L8094 `coachPrompt()`
- L8103 `nutrientDetailStandard(key)`
- L8117 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L8123 `upgradeTo12(s,o)`
- L8128 `benfotiamineTotals(entries=effectiveEntries()`
- L8137 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L8139 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L8151 `microStat(m,t=totals()`
- L8156 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L8164 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L8165 `ratioInfo(key,t=totals()`
- L8204 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L8221 constante `RATIO_ENDS`
- L8223 `ratioZones(i)` — v68: cada equilibrio tiene una zona «aceptable» (ni verde ni mala) y su meta visible en la tarjeta.
- L8231 `ratioTone(i)`
- L8236 constante `NEAR_HEAD`
- L8237 `ratioBar(i,big=false)`
- L8246 `ratioNeedBase(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L8264 `needHTML(i,t)`
- L8265 `ratioNeed(i,t=totals()`
- L8269 `adBalance(t=totals()`
- L8296 `zncuSuppKey()`
- L8297 `zncuSuppCfg()`
- L8319 `zncuDoseLabel(zn,cu)`
- L8322 `hasZncuSupp(d=day()`
- L8327 `toggleZncuSupp()`
- L8347 `openZncuConfig()`
- L8353 `renderRatios()`
- L8364 `ratioDetail(key)`
- L8381 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L8398 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L8413 `renderMicroMap()`
- L8417 `nutrientDetailForDay(key)`
- L8422 `editTargetsForm()`
- L8432 `mealData()`
- L8437 `renderMealSegments()`
- L8445 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L8480 constante `FAT_KEYS`
- L8482 `fatData(entries=effectiveEntries()`
- L8488 `energyData(entries=effectiveEntries()`
- L8492 `segmentedBar(items,total,attr)`
- L8496 `renderMealChart()`
- L8501 `renderFat()`
- L8509 `fatDetail(key)`
- L8514 `energyDetail(key)`
- L8521 `portionCandidates(q='')`
- L8526 `openPortion()`
- L8539 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L8554 `templates()`
- L8558 `renderExtra()`
- L8569 `updateExtra(reset=true)`
- L8581 `addExtra(id,amount)`
- L8597 `shakePreview()`
- L8598 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L8613 constante `LENS`
- L8619 `lensKey(key)`
- L8620 `lensHTML(key)`
- L8624 `appendLens(key)`
- L8633 `weekDates()`

### IA en la página: conexión directa o por servidor

- L8643 constante `MEAL_WORD`
- L8644 `mealOfWord(w)`
- L8645 `mealFromText(raw,fallback)`
- L8649 `canonMeal(v,fallback)`
- L8657 `localMeal(raw,meal)`
- L8663 constante `AI_FALLBACK`
- L8664 constante `GEMINI_DEFAULTS`
- L8665 `applyAIConfig(raw)`
- L8691 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L8692 `callGemini(model,key,prompt,img,signal,opts={})`
- L8715 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L8722 `aiProv(m=$('ai-mode')`
- L8723 `aiBase(mode)`
- L8732 `chatHeaders(mode,key)`
- L8739 `callChat(mode,model,key,prompt,img,signal,opts={})` — ChatGPT, Claude, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L8773 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L8788 constante `MODEL_PREF`
- L8789 `pickModel(ids)`
- L8794 `ensureModel(st)`
- L8810 `syncProvider()`
- L8826 `requestAI(prompt,img,signal,modelOverride='',onStep=null,opts={})`
- L8860 constante `AI_PREF`
- L8861 `aiConnected()`
- L8862 `syncAI()`
- L8864 `saveAIPrefs()`
- L8865 `loadAIPrefs()`
- L8866 `openAISetup()`
- L8872 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L8879 constante `MACROS`
- L8881 `cleanGoals(o,fallback)`
- L8886 `cleanCompare(o={})`
- L8890 `snapshotDay(d,reference='saved')`
- L8895 `upgradeTo17(s,o)`
- L8900 `entriesFor(d,source=weekSource)`
- L8904 `dayRow(dt,source=weekSource)`
- L8908 `goalsFor(dt)`
- L8914 `metricValue(r,key)`
- L8920 `targetOf(dt,key)`
- L8924 `weekSummary()`
- L8928 `aggregate(key,summary=weekSummary()`
- L8932 `tone(pct,mode='macro')`
- L8939 `pctText(a)`
- L8940 `weekProgress(a,color)`
- L8941 `renderWeekMicros(s)`
- L8953 `ratioAggregate(s,num,den)`
- L8957 `renderWeekRatios(s)`
- L8963 `renderWeekTable(s)`
- L8964 `weeklyDetail(key,oneDate=null)`
- L8973 `weekRatioDetail(key)`
- L8981 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L8987 `openDay(dt)`
- L9025 `withDayGoals(fn)`
- L9030 `renderMicros()`
- L9031 `nutrientDetail(key)`
- L9032 `editTargets()`
- L9033 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L9043 `summaryFor(start)`
- L9047 `ringSVG(pct,color,marker)`
- L9049 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L9053 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L9070 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L9071 `macroTone(p)`
- L9072 `dayMacroPct(dt,k)`
- L9073 `renderWeekly()`
- L9096 `weekDetail(dt,picked)`
- L9104 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L9114 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L9120 `sparkline(pts)`
- L9126 `renderCalendar()`
- L9143 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L9144 `splitMeals(raw)`
- L9154 `localDay(raw,fallback)`
- L9161 `promptDay(raw,fallback)`
- L9162 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L9184 `parseCsv(text)`
- L9199 `hevyDate(value,format='auto')`
- L9216 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L9231 constante `GYM_APPS`
- L9233 `gymSig(headers)`
- L9234 `gymApp(headers)`
- L9235 `hevyMapping()`
- L9236 `gymSaved()`
- L9237 `renderMapping(parsed)`
- L9254 `optionalNum(v,min=0,max=1e7)`
- L9259 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L9266 `buildHevy(parsed,map)`
- L9300 `cleanWorkout(s)`
- L9307 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L9322 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L9323 constante `GP_ALIAS`
- L9333 `gpNorm(s)`
- L9334 `gpKey(name)`
- L9338 `gpF(n,d=0)`
- L9339 `gpDate(d,opt)`
- L9340 `gpMonday(d)`
- L9341 constante `GP_GROUPS`
- L9356 constante `GP_COLORS`
- L9357 `gpGroup(name)`
- L9358 `gpWorkSets(s)`
- L9359 `gpModel()`
- L9383 `gpSessionMetrics(e,sets)`
- L9398 constante `GP_METRICS`
- L9403 `gpMetricsFor(e)`
- L9404 `gpRangeHist(e)`
- L9405 `gpPRs(model)`
- L9428 `gpStatus(e)`
- L9446 `gpNext(e)`
- L9454 `gpChart(e)`
- L9482 `gpPointDetail(e)`
- L9488 `gpRepTable(e)`
- L9495 `gpKpis(model)`
- L9504 `gpWeekData(model,w)` — Datos de una semana de gimnasio (series por músculo y sesiones).
- L9509 `gpWeekLabel(w,short)`
- L9510 `gpWeekly(model)`
- L9529 `gpMuscles(model)`
- L9537 `gpHeat(model)` — v69: «Constancia» — mapa de días entrenados (como antes), con días de la semana, meses, intensidad y detalle al tocar.
- L9557 `gpExList(model)`
- L9564 `gpExDetail(model)`
- L9577 `gpDayFood(dt)`
- L9578 `gpNutrition(model)`
- L9585 `gpRecentPRs(model)`
- L9589 `gpSessions(model)`
- L9595 `gpSessionModal(id)`
- L9606 `gpWeekModal(w)`
- L9613 `gpSelect(key)`
- L9614 `gpClick(e)`
- L9630 `renderGym()`
- L9650 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L9659 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L9665 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L9690 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L9694 `showHelp()`
- L9698 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L9700 `markBackup()`
- L9704 `exportJSON()`
- L9709 `drawBackupReminder()`
- L9719 `applyDensity()`
- L9731 `syncDayComplete()`
- L9734 `drawMeals()` — Comidas del día de un vistazo.
- L9742 `filterLog()` — Buscador de Registro.
- L9755 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L9761 `recentFoods()`
- L9766 `quickChip(e,fav)`
- L9784 `drawQuickFoods()`
- L9813 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L9817 `toggleAddPanel(id)`
- L9829 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L9840 `pasteMessage(text,ok)`
- L9848 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L9859 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L9870 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L9876 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L9897 `storableState()`

### Render único: actualiza toda la página

- L9905 `nearView(el)`
- L9907 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L9911 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L9942 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L9943 constante `REF_TABLE`
- L9950 `refTargets(mode)`
- L9951 `syncMicroMode()`
- L9964 `mealByHour(h=new Date()`
- L9971 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L9982 `dataSummary(s)`
- L9986 `confirmImport(next,name)`
- L9993 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L9999 `checkUpdate()`
- L10004 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L10019 constante `GAP_PREFER`
- L10020 constante `GAP_SKIP`
- L10021 constante `GAP_UNIT`
- L10022 `gapQty(f,x)`
- L10023 `gapFoods(key,gap,ctx)`
- L10042 `weekSources(key,sum)`
- L10048 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L10061 `gapRow(x,open,meal,sum,ctx)`
- L10077 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L10102 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L10103 `isFemale(s=state)`
- L10104 `sexLabel(s=state)`
- L10105 `sexBadge(sex)`
- L10107 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L10108 constante `OPT_FEMALE`
- L10119 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba.
- L10120 `applySexOpt(sex)`
- L10122 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L10127 `cleanPreset(p,fb)`
- L10131 `dayNamesFor(types)`
- L10133 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L10143 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L10151 `profV()`
- L10152 `isTrainDay(i)`
- L10153 `activityName(i)`
- L10154 `dayFaf(i)`
- L10155 `presetDesc(cfg,shake)`
- L10159 `profileDescription()`
- L10167 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L10169 `wizCatalog()`
- L10170 `wizOpen(opts={})`
- L10185 `wizTitle()`
- L10186 `wizPaint(sameStep=true)`
- L10195 `wizSync()`
- L10208 `wizFoodOptions()`
- L10211 `wizPresetSummary(cfg,whey)`
- L10216 `wizPresetHTML(kind)`
- L10224 `wizPreview()`
- L10235 `wizHTML()`
- L10276 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L10360 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L10361 constante `SUPP_CATALOG`
- L10383 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L10384 constante `PEAT_BREAKFAST`
- L10385 constante `PEAT_SHAKE`
- L10387 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L10394 `benfoUser()`
- L10396 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L10412 `ico(n)`
- L10414 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L10423 `showTour(i=0)`
- L10435 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L10436 `hubAction(v)`
- L10444 constante `FORM_URL` — Llegan solas a una hoja de Google (formulario del creador de la app). Sin cuentas ni datos personales.
- L10445 constante `FORM_FIELDS`
- L10446 constante `FB_CATS`
- L10448 `openFeedback()`
- L10452 `feedbackData()`
- L10459 `feedbackText()`
- L10460 `sendFeedback()`
- L10473 `shareFeedback()`
- L10490 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L10497 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L10505 constante `I18N_EN`

### v59: idioma (español / inglés)

- L12201 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L12202 constante `WD_EN`
- L12203 `trOne(s)`
- L12211 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L12212 constante `ES_FOOD_GYM`
- L12249 `trFood(s)`
- L12261 constante `TR_TPL`
- L12300 `trLower(s)`
- L12301 `trTpl(s,attr)`
- L12302 constante `FOOD_SEL`
- L12303 `trText(s,attr=false)`
- L12313 `trNode(n)`
- L12332 `trEl(el)`
- L12345 `trTree(root)`
- L12354 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L12368 `setLang(l,quiet)`
- L12381 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter), solo en la web publicada

- L12390 constante `GC_CODE`
- L12391 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L12401 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L12402 `packMove()`
- L12410 `unpackMove(code)`
- L12419 `moveData()`
- L12429 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L12435 `checkMove(code)`
- L12454 `aiFrameworkLines()` — v69: marco de referencia del informe para IA. Así cualquier IA, aunque no conozca la app ni al usuario, sabe con qué comparar.

### Arranque

