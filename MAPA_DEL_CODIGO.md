# MAPA DEL CÓDIGO · BioPeat v55 (revisión de datos 25)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (577 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-5846; todo el JavaScript en `<script id="app">` (desde la línea 5847).

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

- L5891 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L5892 constante `AZUCAR_N`
- L5893 constante `USDA_N`
- L5899 constante `FOODS`
- L5901 constante `BASE_FAT_FIX`
- L5904 constante `EXTRA`
- L5905 constante `KEYS`
- L5907 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L5909 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L5913 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L5914 constante `OPT`
- L5932 constante `LIMIT`
- L5933 `optInfo(k,goal)`
- L5938 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L5946 `optLine(k,goal,unit)`
- L5953 `optRefHTML(k,goal,unit)`
- L5955 constante `DAYS`
- L5956 constante `FAF`
- L5960 `number(v,min=0,max=1e6)`
- L5966 `decimalInputs(root=document)`
- L5967 `localDate(d=new Date()`
- L5968 `validDate(s)`
- L5973 `shift(s,n)`
- L5981 constante `CONTEXT`
- L5983 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L5989 constante `DAY_TYPES`
- L5990 constante `DIEGO_V54`
- L5993 constante `NEW_V54`
- L5996 `defaults()`
- L5999 `bmr()` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6006 constante `DEF_P` — Plan de macros personal de Diego (useDiegoPlan); el resto de perfiles usa GOAL_TYPES.
- L6007 `targetFor(d)`
- L6030 `cleanNutrients(o,required=false)`
- L6042 `cleanEntry(e)`
- L6047 `cleanPlan(p)`
- L6051 `planEntry(p)`
- L6060 `seedPlan(d,whichDate)`
- L6064 `ensureDay(d=date)`
- L6071 `effectiveEntries(d=day()`
- L6072 constante `SALTED_IDS`
- L6073 constante `SWEET_RE`
- L6074 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6092 `inferredNutrients(e)`
- L6131 `totals(entries=effectiveEntries()`
- L6140 `change(fn,message='Guardado')`
- L6144 `undo()`
- L6151 `toast(text,canUndo=false)`
- L6159 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6160 `onClick(fn)`
- L6162 `attempt(fn)`
- L6166 `modal(title,body)`
- L6175 `modalRestore()`
- L6185 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6186 `modalBack()`
- L6187 `goDate(d)`
- L6194 `renderHeader()`
- L6205 `renderRows(entries)`
- L6209 `entryValues(e)`
- L6210 `renderLog()`
- L6217 `fromFood(id,amount,meal)`
- L6223 `pantryId(name)`
- L6225 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6231 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6240 `recipe(kind)`
- L6247 `summary(entries)`
- L6251 `renderPresetInfo()`
- L6263 `stripCode(raw)`
- L6269 `parseBIO(raw,meal=$('meal-select')`
- L6275 `parseSmart(raw)`
- L6279 constante `COUNT`
- L6282 `nutrientFields(n,prefix='n_')`
- L6283 `readNutrients(form,prefix='n_')`
- L6288 `editEntry(id)`
- L6297 `editFood(id,pending=null)`
- L6302 `usageStats(days=90)`
- L6308 `renderFoods()`
- L6316 `nutrientSources(key)`
- L6323 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6324 `suppSlot(meal)`
- L6325 `renderSupps()`
- L6340 `editPlan(id)`
- L6347 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6367 `makePrompt(meal='Comida',note='')`
- L6372 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6376 `photoPrompt(meal,note)`
- L6379 `resetPhoto()`
- L6390 `openPhoto()`
- L6396 `shrinkPhoto(file)`
- L6399 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6425 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6432 `cleanFood(id,f)`
- L6436 `migrateBase(o)`
- L6455 `download(name,text,type)`
- L6464 `portable()`
- L6501 `syncAppIcons()`
- L6509 `downloadAppIcons()`
- L6546 constante `PROFILES_KEY`
- L6548 `ensureProfilesStore()`
- L6567 `saveProfilesStore(st)`
- L6571 `syncCurrentProfileToStore(rawStr)`
- L6577 `activeProfileName()`
- L6581 `renderProfilesList()`
- L6623 `switchProfile(id)`
- L6645 `deleteProfileById(id)`
- L6669 `refreshDrawerSummary()`
- L6686 `toggleLeftDrawer(force)`
- L6701 `buildAIExportText(rangeOverride)`
- L6949 `copyAIExport()`
- L6963 `downloadAIExport()`
- L6972 `renderDrawerChat()`
- L6991 `buildDrawerChatPrompt(question)`
- L7003 `askDrawerAI(rawQuestion)`
- L7090 `storageStatus()`
- L7096 `idbReadWrite(mode,value)`
- L7097 `openDB()`
- L7098 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L7111 `setQuantity(id,value,msg='Cantidad actualizada')`
- L7115 `niceStep(v)`
- L7116 `stepQuantity(id,dir)`
- L7170 `renderAppInfo()`
- L7185 `init()`

### Corrección de la pauta declarada (revisión 11 de los datos)

- L7206 `planFamily(e)`
- L7218 `correctedPlan(plan)`
- L7224 `syncCorrectedDay(s,dt)`
- L7233 `upgradeTo11(s,o)`

### Navegación: una sola página; la barra inferior solo desplaza

- L7239 `setNav(v)`
- L7244 `go(v,focus)`
- L7256 `syncDatePill()`
- L7260 `animateValue(el,to,suffix='%',digits=0)`
- L7269 `tick(now)`
- L7272 `macroCard(key,name,color)`
- L7273 `renderToday()`
- L7296 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L7298 constante `HOME`
- L7300 `coachCandidates()`
- L7306 `coachIdeas(t,g,ref,meal)`
- L7319 `renderCoach()`
- L7337 `coachPrompt()`
- L7345 `nutrientDetailStandard(key)`
- L7359 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L7365 `upgradeTo12(s,o)`
- L7370 `benfotiamineTotals(entries=effectiveEntries()`
- L7379 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L7381 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L7393 `microStat(m,t=totals()`
- L7398 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L7406 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L7407 `ratioInfo(key,t=totals()`
- L7442 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L7459 constante `RATIO_ENDS`
- L7460 `ratioBar(i,big=false)`
- L7465 `ratioNeed(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L7482 `needHTML(i,t)`
- L7483 `renderRatios()`
- L7488 `ratioDetail(key)`
- L7498 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L7515 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L7530 `renderMicroMap()`
- L7534 `nutrientDetailForDay(key)`
- L7539 `editTargetsForm()`
- L7549 `mealData()`
- L7554 `renderMealSegments()`
- L7562 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L7572 constante `FAT_KEYS`
- L7574 `fatData(entries=effectiveEntries()`
- L7580 `energyData(entries=effectiveEntries()`
- L7584 `segmentedBar(items,total,attr)`
- L7588 `renderMealChart()`
- L7593 `renderFat()`
- L7601 `fatDetail(key)`
- L7606 `energyDetail(key)`
- L7613 `portionCandidates(q='')`
- L7618 `openPortion()`
- L7631 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L7646 `templates()`
- L7650 `renderExtra()`
- L7661 `updateExtra(reset=true)`
- L7673 `addExtra(id,amount)`
- L7689 `shakePreview()`
- L7690 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L7705 constante `LENS`
- L7711 `lensKey(key)`
- L7712 `lensHTML(key)`
- L7716 `appendLens(key)`
- L7725 `weekDates()`

### IA en la página: conexión directa o por servidor

- L7735 constante `MEAL_WORD`
- L7736 `mealOfWord(w)`
- L7737 `mealFromText(raw,fallback)`
- L7741 `canonMeal(v,fallback)`
- L7749 `localMeal(raw,meal)`
- L7755 constante `AI_FALLBACK`
- L7756 `applyAIConfig(raw)`
- L7782 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L7783 `callGemini(model,key,prompt,img,signal,think=true)`
- L7800 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L7832 constante `AI_PREF`
- L7833 `aiConnected()`
- L7834 `syncAI()`
- L7836 `saveAIPrefs()`
- L7837 `loadAIPrefs()`
- L7838 `openAISetup()`
- L7844 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L7851 constante `MACROS`
- L7853 `cleanGoals(o,fallback)`
- L7858 `cleanCompare(o={})`
- L7862 `snapshotDay(d,reference='saved')`
- L7867 `upgradeTo17(s,o)`
- L7872 `entriesFor(d,source=weekSource)`
- L7876 `dayRow(dt,source=weekSource)`
- L7880 `goalsFor(dt)`
- L7886 `metricValue(r,key)`
- L7892 `targetOf(dt,key)`
- L7896 `weekSummary()`
- L7900 `aggregate(key,summary=weekSummary()`
- L7904 `tone(pct,mode='macro')`
- L7911 `pctText(a)`
- L7912 `weekProgress(a,color)`
- L7913 `renderWeekMicros(s)`
- L7925 `ratioAggregate(s,num,den)`
- L7929 `renderWeekRatios(s)`
- L7935 `renderWeekTable(s)`
- L7936 `weeklyDetail(key,oneDate=null)`
- L7945 `weekRatioDetail(key)`
- L7953 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L7959 `openDay(dt)`
- L7997 `withDayGoals(fn)`
- L8002 `renderMicros()`
- L8003 `nutrientDetail(key)`
- L8004 `editTargets()`
- L8005 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L8015 `summaryFor(start)`
- L8019 `ringSVG(pct,color,marker)`
- L8021 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L8025 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L8040 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L8041 `macroTone(p)`
- L8042 `dayMacroPct(dt,k)`
- L8043 `renderWeekly()`
- L8066 `weekDetail(dt,picked)`
- L8074 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L8084 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L8090 `sparkline(pts)`
- L8096 `renderCalendar()`
- L8113 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L8114 `splitMeals(raw)`
- L8124 `localDay(raw,fallback)`
- L8131 `promptDay(raw,fallback)`
- L8132 `analyzeDay(usePhoto=false)`

### Gimnasio: importación de CSV de HEVY, sesiones y análisis IA

- L8154 `parseCsv(text)`
- L8169 `hevyDate(value,format='auto')`
- L8178 constante `MAP`
- L8179 `hevyMapping()`
- L8180 `renderMapping(parsed)`
- L8187 `optionalNum(v,min=0,max=1e7)`
- L8191 `buildHevy(parsed,map)`
- L8201 `cleanWorkout(s)`
- L8208 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L8223 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L8224 constante `GP_ALIAS`
- L8234 `gpNorm(s)`
- L8235 `gpKey(name)`
- L8239 `gpF(n,d=0)`
- L8240 `gpDate(d,opt)`
- L8241 `gpMonday(d)`
- L8242 constante `GP_GROUPS`
- L8257 constante `GP_COLORS`
- L8258 `gpGroup(name)`
- L8259 `gpWorkSets(s)`
- L8260 `gpModel()`
- L8284 `gpSessionMetrics(e,sets)`
- L8299 constante `GP_METRICS`
- L8304 `gpMetricsFor(e)`
- L8305 `gpRangeHist(e)`
- L8306 `gpPRs(model)`
- L8329 `gpStatus(e)`
- L8347 `gpNext(e)`
- L8355 `gpChart(e)`
- L8383 `gpPointDetail(e)`
- L8389 `gpRepTable(e)`
- L8396 `gpKpis(model)`
- L8404 `gpWeekly(model)`
- L8410 `gpMuscles(model)`
- L8417 `gpHeat(model)`
- L8424 `gpExList(model)`
- L8431 `gpExDetail(model)`
- L8444 `gpDayFood(dt)`
- L8445 `gpNutrition(model)`
- L8452 `gpRecentPRs(model)`
- L8456 `gpSessions(model)`
- L8462 `gpSessionModal(id)`
- L8473 `gpWeekModal(w)`
- L8474 `gpSelect(key)`
- L8475 `gpClick(e)`
- L8487 `renderGym()`
- L8507 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L8516 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L8522 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L8546 `openMoreMenu()` — Menú «Más»: secciones poco frecuentes, sin saturar la barra inferior.
- L8553 `showHelp()`
- L8557 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L8559 `markBackup()`
- L8563 `exportJSON()`
- L8568 `drawBackupReminder()`
- L8578 `applyDensity()`
- L8590 `syncDayComplete()`
- L8593 `drawMeals()` — Comidas del día de un vistazo.
- L8601 `filterLog()` — Buscador de Registro.
- L8614 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L8620 `recentFoods()`
- L8625 `quickChip(e,fav)`
- L8643 `drawQuickFoods()`
- L8672 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L8676 `toggleAddPanel(id)`
- L8688 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L8699 `pasteMessage(text,ok)`
- L8707 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L8718 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L8729 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L8735 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L8755 `storableState()`

### Render único: actualiza toda la página

- L8763 `nearView(el)`
- L8765 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L8769 `render()`
- L8805 `mealByHour(h=new Date()`
- L8812 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L8822 `dataSummary(s)`
- L8826 `confirmImport(next,name)`
- L8833 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L8839 `checkUpdate()`
- L8844 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L8859 constante `GAP_PREFER`
- L8860 constante `GAP_SKIP`
- L8861 constante `GAP_UNIT`
- L8862 `gapQty(f,x)`
- L8863 `gapFoods(key,gap,ctx)`
- L8882 `weekSources(key,sum)`
- L8888 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L8901 `gapRow(x,open,meal,sum,ctx)`
- L8917 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L8942 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L8943 `isFemale(s=state)`
- L8944 `sexLabel(s=state)`
- L8945 `sexBadge(sex)`
- L8947 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L8948 constante `OPT_FEMALE`
- L8959 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo (las de Diego incluyen sus suplementos). Mujer: hierro, zinc y magnesio de las fuentes de arriba.
- L8960 `applySexOpt(sex)`
- L8962 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L8967 `cleanPreset(p,fb)`
- L8971 `dayNamesFor(types)`
- L8973 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas de Diego) se usan los de Diego.
- L8982 `profV()`
- L8983 `isTrainDay(i)`
- L8984 `activityName(i)`
- L8985 `dayFaf(i)`
- L8986 `presetDesc(cfg,shake)`
- L8990 `profileDescription()`
- L8998 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L8999 constante `WIZ_EXTRA`
- L9004 `wizCatalog()`
- L9005 `wizOpen(opts={})`
- L9020 `wizTitle()`
- L9021 `wizPaint(sameStep=true)`
- L9030 `wizSync()`
- L9043 `wizFoodOptions()`
- L9046 `wizPresetSummary(cfg,whey)`
- L9051 `wizPresetHTML(kind)`
- L9059 `wizPreview()`
- L9071 `wizHTML()`
- L9106 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### Arranque

