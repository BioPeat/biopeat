# MAPA DEL CÓDIGO · BioPeat v49 (revisión de datos 23)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (483 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-5707; todo el JavaScript en `<script id="app">` (desde la línea 5708).

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

- L5747 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L5748 constante `AZUCAR_N`
- L5749 constante `USDA_N`
- L5755 constante `FOODS`
- L5757 constante `BASE_FAT_FIX`
- L5760 constante `EXTRA`
- L5761 constante `KEYS`
- L5763 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L5765 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.
- L5766 constante `MICRO_NOTE`
- L5768 constante `DAYS`
- L5769 constante `FAF`
- L5773 `number(v,min=0,max=1e6)`
- L5779 `decimalInputs(root=document)`
- L5780 `localDate(d=new Date()`
- L5781 `validDate(s)`
- L5786 `shift(s,n)`
- L5794 constante `CONTEXT`
- L5795 `defaults()`
- L5797 `bmr()`
- L5803 constante `DEF_P` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L5804 `targetFor(d)`
- L5820 `cleanNutrients(o,required=false)`
- L5832 `cleanEntry(e)`
- L5837 `cleanPlan(p)`
- L5841 `planEntry(p)`
- L5850 `seedPlan(d,whichDate)`
- L5854 `ensureDay(d=date)`
- L5861 `effectiveEntries(d=day()`
- L5862 constante `SALTED_IDS`
- L5863 constante `SWEET_RE`
- L5864 `inferFatShares(e,txt=normalize((e?.name||'')`
- L5882 `inferredNutrients(e)`
- L5921 `totals(entries=effectiveEntries()`
- L5930 `change(fn,message='Guardado')`
- L5934 `undo()`
- L5941 `toast(text,canUndo=false)`
- L5949 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L5950 `onClick(fn)`
- L5952 `attempt(fn)`
- L5956 `modal(title,body)`
- L5965 `modalRestore()`
- L5975 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L5976 `modalBack()`
- L5977 `goDate(d)`
- L5984 `renderHeader()`
- L5993 `renderRows(entries)`
- L5997 `entryValues(e)`
- L5998 `renderLog()`
- L6005 `fromFood(id,amount,meal)`
- L6011 `pantryId(name)`
- L6013 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6019 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6028 `recipe(kind)`
- L6034 `summary(entries)`
- L6038 `renderPresetInfo()`
- L6042 `stripCode(raw)`
- L6048 `parseBIO(raw,meal=$('meal-select')`
- L6054 `parseSmart(raw)`
- L6058 constante `COUNT`
- L6061 `nutrientFields(n,prefix='n_')`
- L6062 `readNutrients(form,prefix='n_')`
- L6067 `editEntry(id)`
- L6076 `editFood(id,pending=null)`
- L6081 `usageStats(days=90)`
- L6087 `renderFoods()`
- L6095 `nutrientSources(key)`
- L6102 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6103 `suppSlot(meal)`
- L6104 `renderSupps()`
- L6119 `editPlan(id)`
- L6126 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6145 `makePrompt(meal='Comida',note='')`
- L6150 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6154 `photoPrompt(meal,note)`
- L6157 `resetPhoto()`
- L6168 `openPhoto()`
- L6174 `shrinkPhoto(file)`
- L6177 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6203 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6210 `cleanFood(id,f)`
- L6214 `migrateBase(o)`
- L6233 `download(name,text,type)`
- L6242 `portable()`
- L6266 `syncAppIcons()`
- L6274 `downloadAppIcons()`
- L6311 `storageStatus()`
- L6317 `idbReadWrite(mode,value)`
- L6318 `openDB()`
- L6319 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L6331 `setQuantity(id,value,msg='Cantidad actualizada')`
- L6335 `niceStep(v)`
- L6336 `stepQuantity(id,dir)`
- L6390 `renderAppInfo()`
- L6405 `init()`

### Corrección de la pauta declarada (revisión 11 de los datos)

- L6423 `planFamily(e)`
- L6435 `correctedPlan(plan)`
- L6441 `syncCorrectedDay(s,dt)`
- L6450 `upgradeTo11(s,o)`

### Navegación: una sola página; la barra inferior solo desplaza

- L6456 `setNav(v)`
- L6461 `go(v,focus)`
- L6473 `syncDatePill()`
- L6477 `animateValue(el,to,suffix='%',digits=0)`
- L6486 `tick(now)`
- L6489 `macroCard(key,name,color)`
- L6490 `renderToday()`
- L6513 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L6515 constante `HOME`
- L6517 `coachCandidates()`
- L6523 `coachIdeas(t,g,ref,meal)`
- L6536 `renderCoach()`
- L6553 `coachPrompt()`
- L6561 `nutrientDetailStandard(key)`
- L6575 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L6581 `upgradeTo12(s,o)`
- L6586 `benfotiamineTotals(entries=effectiveEntries()`
- L6595 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L6597 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L6609 `microStat(m,t=totals()`
- L6614 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L6622 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L6623 `ratioInfo(key,t=totals()`
- L6658 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L6675 constante `RATIO_ENDS`
- L6676 `ratioBar(i,big=false)`
- L6681 `ratioNeed(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L6698 `needHTML(i,t)`
- L6699 `renderRatios()`
- L6704 `ratioDetail(key)`
- L6714 constante `MICRO_BANDS` — Tarjeta de un nutriente. Límites (máx): verde por debajo. Selenio: banda óptima 100-200 µg.
- L6715 `microCardHTML(m,x,personal)`
- L6725 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L6740 `renderMicroMap()`
- L6744 `nutrientDetailForDay(key)`
- L6749 `editTargetsForm()`
- L6759 `mealData()`
- L6764 `renderMealSegments()`
- L6772 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L6782 constante `FAT_KEYS`
- L6783 constante `FAT_PROFILES`
- L6785 `fatData(entries=effectiveEntries()`
- L6791 `energyData(entries=effectiveEntries()`
- L6795 `segmentedBar(items,total,attr)`
- L6799 `renderMealChart()`
- L6804 `renderFat()`
- L6812 `fatDetail(key)`
- L6817 `energyDetail(key)`
- L6824 `portionCandidates(q='')`
- L6829 `openPortion()`
- L6842 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L6857 `templates()`
- L6861 `renderExtra()`
- L6872 `updateExtra(reset=true)`
- L6884 `addExtra(id,amount)`
- L6900 `shakePreview()`
- L6901 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L6916 constante `LENS`
- L6922 `lensKey(key)`
- L6923 `lensHTML(key)`
- L6927 `appendLens(key)`
- L6936 `weekDates()`

### IA en la página: conexión directa o por servidor

- L6946 constante `MEAL_WORD`
- L6947 `mealOfWord(w)`
- L6948 `mealFromText(raw,fallback)`
- L6952 `canonMeal(v,fallback)`
- L6960 `localMeal(raw,meal)`
- L6966 constante `AI_FALLBACK`
- L6967 `applyAIConfig(raw)`
- L6993 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L6994 `callGemini(model,key,prompt,img,signal,think=true)`
- L7011 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L7043 constante `AI_PREF`
- L7044 `aiConnected()`
- L7045 `syncAI()`
- L7047 `saveAIPrefs()`
- L7048 `loadAIPrefs()`
- L7049 `openAISetup()`
- L7055 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L7062 constante `MACROS`
- L7064 `cleanGoals(o,fallback)`
- L7069 `cleanCompare(o={})`
- L7073 `snapshotDay(d,reference='saved')`
- L7078 `upgradeTo17(s,o)`
- L7083 `entriesFor(d,source=weekSource)`
- L7087 `dayRow(dt,source=weekSource)`
- L7091 `goalsFor(dt)`
- L7097 `metricValue(r,key)`
- L7103 `targetOf(dt,key)`
- L7107 `weekSummary()`
- L7111 `aggregate(key,summary=weekSummary()`
- L7115 `tone(pct,mode='macro')`
- L7122 `pctText(a)`
- L7123 `weekProgress(a,color)`
- L7124 `renderWeekMicros(s)`
- L7148 `ratioAggregate(s,num,den)`
- L7152 `renderWeekRatios(s)`
- L7158 `renderWeekTable(s)`
- L7159 `weeklyDetail(key,oneDate=null)`
- L7167 `weekRatioDetail(key)`
- L7175 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L7181 `openDay(dt)`
- L7219 `withDayGoals(fn)`
- L7224 `renderMicros()`
- L7225 `nutrientDetail(key)`
- L7226 `editTargets()`
- L7227 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L7237 `summaryFor(start)`
- L7241 `ringSVG(pct,color,marker)`
- L7243 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L7247 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L7262 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L7263 `macroTone(p)`
- L7264 `dayMacroPct(dt,k)`
- L7265 `renderWeekly()`
- L7288 `weekDetail(dt,picked)`
- L7296 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L7306 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L7312 `sparkline(pts)`
- L7318 `renderCalendar()`
- L7335 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L7336 `splitMeals(raw)`
- L7346 `localDay(raw,fallback)`
- L7353 `promptDay(raw,fallback)`
- L7354 `analyzeDay(usePhoto=false)`

### Gimnasio: importación de CSV de HEVY, sesiones y análisis IA

- L7376 `parseCsv(text)`
- L7391 `hevyDate(value,format='auto')`
- L7400 constante `MAP`
- L7401 `hevyMapping()`
- L7402 `renderMapping(parsed)`
- L7409 `optionalNum(v,min=0,max=1e7)`
- L7413 `buildHevy(parsed,map)`
- L7423 `cleanWorkout(s)`
- L7430 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L7445 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L7446 constante `GP_ALIAS`
- L7456 `gpNorm(s)`
- L7457 `gpKey(name)`
- L7461 `gpF(n,d=0)`
- L7462 `gpDate(d,opt)`
- L7463 `gpMonday(d)`
- L7464 constante `GP_GROUPS`
- L7479 constante `GP_COLORS`
- L7480 `gpGroup(name)`
- L7481 `gpWorkSets(s)`
- L7482 `gpModel()`
- L7506 `gpSessionMetrics(e,sets)`
- L7521 constante `GP_METRICS`
- L7526 `gpMetricsFor(e)`
- L7527 `gpRangeHist(e)`
- L7528 `gpPRs(model)`
- L7551 `gpStatus(e)`
- L7569 `gpNext(e)`
- L7577 `gpChart(e)`
- L7605 `gpPointDetail(e)`
- L7611 `gpRepTable(e)`
- L7618 `gpKpis(model)`
- L7626 `gpWeekly(model)`
- L7632 `gpMuscles(model)`
- L7639 `gpHeat(model)`
- L7646 `gpExList(model)`
- L7653 `gpExDetail(model)`
- L7666 `gpDayFood(dt)`
- L7667 `gpNutrition(model)`
- L7674 `gpRecentPRs(model)`
- L7678 `gpSessions(model)`
- L7684 `gpSessionModal(id)`
- L7695 `gpWeekModal(w)`
- L7696 `gpSelect(key)`
- L7697 `gpClick(e)`
- L7709 `renderGym()`
- L7729 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L7738 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L7744 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L7768 `openMoreMenu()` — Menú «Más»: secciones poco frecuentes, sin saturar la barra inferior.
- L7775 `showHelp()`
- L7779 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L7781 `markBackup()`
- L7785 `exportJSON()`
- L7790 `drawBackupReminder()`
- L7800 `applyDensity()`
- L7812 `syncDayComplete()`
- L7815 `drawMeals()` — Comidas del día de un vistazo.
- L7823 `filterLog()` — Buscador de Registro.
- L7836 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L7842 `recentFoods()`
- L7847 `quickChip(e,fav)`
- L7865 `drawQuickFoods()`
- L7894 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L7898 `toggleAddPanel(id)`
- L7910 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L7921 `pasteMessage(text,ok)`
- L7929 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L7940 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L7949 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L7967 `storableState()`

### Render único: actualiza toda la página

- L7975 `nearView(el)`
- L7977 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L7981 `render()`
- L8016 `mealByHour(h=new Date()`
- L8023 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L8033 `dataSummary(s)`
- L8037 `confirmImport(next,name)`
- L8044 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L8050 `checkUpdate()`
- L8055 `showUpdate(v)`

### v49: «¿Qué me falta?» de Semana

- L8069 constante `GAP_PREFER` — Alimentos que se proponen para cubrir un hueco (solo los que ya tienes en Mi despensa). Primero los de la lista Peat, los más ligeros primero.
- L8070 constante `GAP_SKIP`
- L8071 `gapFoods(key,gap)`
- L8091 `weekGaps(sum)`
- L8096 `gapCard(x)`
- L8101 `renderGaps(sum,s)`

### Arranque

