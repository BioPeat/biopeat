# MAPA DEL CÓDIGO · BioPeat v50 (revisión de datos 23)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (492 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-5725; todo el JavaScript en `<script id="app">` (desde la línea 5726).

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

- L5766 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L5767 constante `AZUCAR_N`
- L5768 constante `USDA_N`
- L5774 constante `FOODS`
- L5776 constante `BASE_FAT_FIX`
- L5779 constante `EXTRA`
- L5780 constante `KEYS`
- L5782 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L5784 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L5788 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L5789 constante `OPT`
- L5807 constante `LIMIT`
- L5808 `optInfo(k,goal)`
- L5813 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L5821 `optLine(k,goal,unit)`
- L5828 `optRefHTML(k,goal,unit)`
- L5830 constante `DAYS`
- L5831 constante `FAF`
- L5835 `number(v,min=0,max=1e6)`
- L5841 `decimalInputs(root=document)`
- L5842 `localDate(d=new Date()`
- L5843 `validDate(s)`
- L5848 `shift(s,n)`
- L5856 constante `CONTEXT`
- L5857 `defaults()`
- L5859 `bmr()`
- L5865 constante `DEF_P` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L5866 `targetFor(d)`
- L5882 `cleanNutrients(o,required=false)`
- L5894 `cleanEntry(e)`
- L5899 `cleanPlan(p)`
- L5903 `planEntry(p)`
- L5912 `seedPlan(d,whichDate)`
- L5916 `ensureDay(d=date)`
- L5923 `effectiveEntries(d=day()`
- L5924 constante `SALTED_IDS`
- L5925 constante `SWEET_RE`
- L5926 `inferFatShares(e,txt=normalize((e?.name||'')`
- L5944 `inferredNutrients(e)`
- L5983 `totals(entries=effectiveEntries()`
- L5992 `change(fn,message='Guardado')`
- L5996 `undo()`
- L6003 `toast(text,canUndo=false)`
- L6011 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6012 `onClick(fn)`
- L6014 `attempt(fn)`
- L6018 `modal(title,body)`
- L6027 `modalRestore()`
- L6037 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6038 `modalBack()`
- L6039 `goDate(d)`
- L6046 `renderHeader()`
- L6055 `renderRows(entries)`
- L6059 `entryValues(e)`
- L6060 `renderLog()`
- L6067 `fromFood(id,amount,meal)`
- L6073 `pantryId(name)`
- L6075 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6081 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6090 `recipe(kind)`
- L6096 `summary(entries)`
- L6100 `renderPresetInfo()`
- L6104 `stripCode(raw)`
- L6110 `parseBIO(raw,meal=$('meal-select')`
- L6116 `parseSmart(raw)`
- L6120 constante `COUNT`
- L6123 `nutrientFields(n,prefix='n_')`
- L6124 `readNutrients(form,prefix='n_')`
- L6129 `editEntry(id)`
- L6138 `editFood(id,pending=null)`
- L6143 `usageStats(days=90)`
- L6149 `renderFoods()`
- L6157 `nutrientSources(key)`
- L6164 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6165 `suppSlot(meal)`
- L6166 `renderSupps()`
- L6181 `editPlan(id)`
- L6188 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6207 `makePrompt(meal='Comida',note='')`
- L6212 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6216 `photoPrompt(meal,note)`
- L6219 `resetPhoto()`
- L6230 `openPhoto()`
- L6236 `shrinkPhoto(file)`
- L6239 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6265 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6272 `cleanFood(id,f)`
- L6276 `migrateBase(o)`
- L6295 `download(name,text,type)`
- L6304 `portable()`
- L6328 `syncAppIcons()`
- L6336 `downloadAppIcons()`
- L6373 `storageStatus()`
- L6379 `idbReadWrite(mode,value)`
- L6380 `openDB()`
- L6381 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L6393 `setQuantity(id,value,msg='Cantidad actualizada')`
- L6397 `niceStep(v)`
- L6398 `stepQuantity(id,dir)`
- L6452 `renderAppInfo()`
- L6467 `init()`

### Corrección de la pauta declarada (revisión 11 de los datos)

- L6485 `planFamily(e)`
- L6497 `correctedPlan(plan)`
- L6503 `syncCorrectedDay(s,dt)`
- L6512 `upgradeTo11(s,o)`

### Navegación: una sola página; la barra inferior solo desplaza

- L6518 `setNav(v)`
- L6523 `go(v,focus)`
- L6535 `syncDatePill()`
- L6539 `animateValue(el,to,suffix='%',digits=0)`
- L6548 `tick(now)`
- L6551 `macroCard(key,name,color)`
- L6552 `renderToday()`
- L6575 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L6577 constante `HOME`
- L6579 `coachCandidates()`
- L6585 `coachIdeas(t,g,ref,meal)`
- L6598 `renderCoach()`
- L6615 `coachPrompt()`
- L6623 `nutrientDetailStandard(key)`
- L6637 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L6643 `upgradeTo12(s,o)`
- L6648 `benfotiamineTotals(entries=effectiveEntries()`
- L6657 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L6659 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L6671 `microStat(m,t=totals()`
- L6676 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L6684 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L6685 `ratioInfo(key,t=totals()`
- L6720 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L6737 constante `RATIO_ENDS`
- L6738 `ratioBar(i,big=false)`
- L6743 `ratioNeed(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L6760 `needHTML(i,t)`
- L6761 `renderRatios()`
- L6766 `ratioDetail(key)`
- L6776 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L6793 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L6808 `renderMicroMap()`
- L6812 `nutrientDetailForDay(key)`
- L6817 `editTargetsForm()`
- L6827 `mealData()`
- L6832 `renderMealSegments()`
- L6840 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L6850 constante `FAT_KEYS`
- L6852 `fatData(entries=effectiveEntries()`
- L6858 `energyData(entries=effectiveEntries()`
- L6862 `segmentedBar(items,total,attr)`
- L6866 `renderMealChart()`
- L6871 `renderFat()`
- L6879 `fatDetail(key)`
- L6884 `energyDetail(key)`
- L6891 `portionCandidates(q='')`
- L6896 `openPortion()`
- L6909 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L6924 `templates()`
- L6928 `renderExtra()`
- L6939 `updateExtra(reset=true)`
- L6951 `addExtra(id,amount)`
- L6967 `shakePreview()`
- L6968 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L6983 constante `LENS`
- L6989 `lensKey(key)`
- L6990 `lensHTML(key)`
- L6994 `appendLens(key)`
- L7003 `weekDates()`

### IA en la página: conexión directa o por servidor

- L7013 constante `MEAL_WORD`
- L7014 `mealOfWord(w)`
- L7015 `mealFromText(raw,fallback)`
- L7019 `canonMeal(v,fallback)`
- L7027 `localMeal(raw,meal)`
- L7033 constante `AI_FALLBACK`
- L7034 `applyAIConfig(raw)`
- L7060 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L7061 `callGemini(model,key,prompt,img,signal,think=true)`
- L7078 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L7110 constante `AI_PREF`
- L7111 `aiConnected()`
- L7112 `syncAI()`
- L7114 `saveAIPrefs()`
- L7115 `loadAIPrefs()`
- L7116 `openAISetup()`
- L7122 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L7129 constante `MACROS`
- L7131 `cleanGoals(o,fallback)`
- L7136 `cleanCompare(o={})`
- L7140 `snapshotDay(d,reference='saved')`
- L7145 `upgradeTo17(s,o)`
- L7150 `entriesFor(d,source=weekSource)`
- L7154 `dayRow(dt,source=weekSource)`
- L7158 `goalsFor(dt)`
- L7164 `metricValue(r,key)`
- L7170 `targetOf(dt,key)`
- L7174 `weekSummary()`
- L7178 `aggregate(key,summary=weekSummary()`
- L7182 `tone(pct,mode='macro')`
- L7189 `pctText(a)`
- L7190 `weekProgress(a,color)`
- L7191 `renderWeekMicros(s)`
- L7203 `ratioAggregate(s,num,den)`
- L7207 `renderWeekRatios(s)`
- L7213 `renderWeekTable(s)`
- L7214 `weeklyDetail(key,oneDate=null)`
- L7223 `weekRatioDetail(key)`
- L7231 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L7237 `openDay(dt)`
- L7275 `withDayGoals(fn)`
- L7280 `renderMicros()`
- L7281 `nutrientDetail(key)`
- L7282 `editTargets()`
- L7283 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L7293 `summaryFor(start)`
- L7297 `ringSVG(pct,color,marker)`
- L7299 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L7303 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L7318 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L7319 `macroTone(p)`
- L7320 `dayMacroPct(dt,k)`
- L7321 `renderWeekly()`
- L7344 `weekDetail(dt,picked)`
- L7352 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L7362 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L7368 `sparkline(pts)`
- L7374 `renderCalendar()`
- L7391 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L7392 `splitMeals(raw)`
- L7402 `localDay(raw,fallback)`
- L7409 `promptDay(raw,fallback)`
- L7410 `analyzeDay(usePhoto=false)`

### Gimnasio: importación de CSV de HEVY, sesiones y análisis IA

- L7432 `parseCsv(text)`
- L7447 `hevyDate(value,format='auto')`
- L7456 constante `MAP`
- L7457 `hevyMapping()`
- L7458 `renderMapping(parsed)`
- L7465 `optionalNum(v,min=0,max=1e7)`
- L7469 `buildHevy(parsed,map)`
- L7479 `cleanWorkout(s)`
- L7486 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L7501 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L7502 constante `GP_ALIAS`
- L7512 `gpNorm(s)`
- L7513 `gpKey(name)`
- L7517 `gpF(n,d=0)`
- L7518 `gpDate(d,opt)`
- L7519 `gpMonday(d)`
- L7520 constante `GP_GROUPS`
- L7535 constante `GP_COLORS`
- L7536 `gpGroup(name)`
- L7537 `gpWorkSets(s)`
- L7538 `gpModel()`
- L7562 `gpSessionMetrics(e,sets)`
- L7577 constante `GP_METRICS`
- L7582 `gpMetricsFor(e)`
- L7583 `gpRangeHist(e)`
- L7584 `gpPRs(model)`
- L7607 `gpStatus(e)`
- L7625 `gpNext(e)`
- L7633 `gpChart(e)`
- L7661 `gpPointDetail(e)`
- L7667 `gpRepTable(e)`
- L7674 `gpKpis(model)`
- L7682 `gpWeekly(model)`
- L7688 `gpMuscles(model)`
- L7695 `gpHeat(model)`
- L7702 `gpExList(model)`
- L7709 `gpExDetail(model)`
- L7722 `gpDayFood(dt)`
- L7723 `gpNutrition(model)`
- L7730 `gpRecentPRs(model)`
- L7734 `gpSessions(model)`
- L7740 `gpSessionModal(id)`
- L7751 `gpWeekModal(w)`
- L7752 `gpSelect(key)`
- L7753 `gpClick(e)`
- L7765 `renderGym()`
- L7785 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L7794 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L7800 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L7824 `openMoreMenu()` — Menú «Más»: secciones poco frecuentes, sin saturar la barra inferior.
- L7831 `showHelp()`
- L7835 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L7837 `markBackup()`
- L7841 `exportJSON()`
- L7846 `drawBackupReminder()`
- L7856 `applyDensity()`
- L7868 `syncDayComplete()`
- L7871 `drawMeals()` — Comidas del día de un vistazo.
- L7879 `filterLog()` — Buscador de Registro.
- L7892 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L7898 `recentFoods()`
- L7903 `quickChip(e,fav)`
- L7921 `drawQuickFoods()`
- L7950 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L7954 `toggleAddPanel(id)`
- L7966 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L7977 `pasteMessage(text,ok)`
- L7985 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L7996 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L8005 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L8023 `storableState()`

### Render único: actualiza toda la página

- L8031 `nearView(el)`
- L8033 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L8037 `render()`
- L8072 `mealByHour(h=new Date()`
- L8079 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L8089 `dataSummary(s)`
- L8093 `confirmImport(next,name)`
- L8100 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L8106 `checkUpdate()`
- L8111 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L8126 constante `GAP_PREFER`
- L8127 constante `GAP_SKIP`
- L8128 constante `GAP_UNIT`
- L8129 `gapQty(f,x)`
- L8130 `gapFoods(key,gap,ctx)`
- L8149 `weekSources(key,sum)`
- L8155 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L8168 `gapRow(x,open,meal,sum,ctx)`
- L8184 `renderGaps(sum,s)`

### Arranque

