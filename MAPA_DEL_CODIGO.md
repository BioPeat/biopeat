# MAPA DEL CÓDIGO · BioPeat v69 (revisión de datos 26)

Generado con `python tools/mapa.py`. No lo edites a mano. Las líneas son orientativas: busca siempre por nombre.

`index.html` (831 KB): CSS (`<style>`) y HTML de las secciones en las líneas 1-6338; todo el JavaScript en `<script id="app">` (desde la línea 6339).

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

- L6397 constante `ZERO_MICRO` — Valores de referencia USDA FoodData Central por 100 g (aprox.). Revisa tu etiqueta si difiere.
- L6398 constante `AZUCAR_N`
- L6399 constante `USDA_N`
- L6405 constante `FOODS`
- L6407 constante `BASE_FAT_FIX`
- L6410 constante `EXTRA`
- L6411 constante `KEYS`
- L6413 constante `SAT_W` — Grasa para la meta: la saturada (leche, mantequilla, coco) cuenta SAT_W veces; el resto (mono y PUFA) cuenta entera. La energía (kcal) siempre cuenta todo.
- L6415 constante `DEPOSIT` — Micros de «depósito»: el cuerpo los almacena, así que se valoran con la media de 7 días. «limit»: mejor por debajo.

### Zona ideal de cada micronutriente: UNA sola tabla

- L6419 constante `SRC_NAME` — lo/hi:'goal' usa tu meta personal. src: de dónde sale la cifra. ref: texto que se ve al tocar el nutriente. nogap: no se propone «te falta».
- L6420 constante `OPT`
- L6438 constante `LIMIT`
- L6439 `optInfo(k,goal)`
- L6446 `optState(k,v,goal)` — Estado de un valor frente a su zona: 'none' | 'low' | 'ok' | 'high' | 'ref'
- L6454 `optLine(k,goal,unit)`
- L6461 `optRefHTML(k,goal,unit)`
- L6463 constante `DAYS`
- L6464 constante `FAF`
- L6466 constante `LOC`
- L6470 `number(v,min=0,max=1e6)`
- L6476 `decimalInputs(root=document)`
- L6477 `localDate(d=new Date()`
- L6478 `validDate(s)`
- L6483 `shift(s,n)`
- L6492 constante `CONTEXT` — Contexto libre de cada perfil (lo escribe el usuario en sus notas). Vacío por defecto.
- L6494 constante `GOAL_TYPES` — Ajustes de perfil por defecto (se usan ya en defaults(), por eso van aquí arriba). Detalle en «Perfiles: sexo, objetivo…».
- L6500 constante `DAY_TYPES`
- L6501 constante `NEW_V54`
- L6505 `defaults()` — Usuario nuevo: sin pauta, sin desayuno ni batido fijos y sin alimentos de marca; el asistente lo configura.
- L6508 `bmr()` — Mifflin-St Jeor: +5 en hombre, -161 en mujer.
- L6514 `targetFor(d)` — Prioridad: 1) ajuste manual de ese día (state.days[d].macroGoals) 2) metas globales (targetMode all/split) 3) plan por defecto.
- L6536 `cleanNutrients(o,required=false)`
- L6548 `cleanEntry(e)`
- L6553 `cleanPlan(p)`
- L6557 `planEntry(p)`
- L6566 `seedPlan(d,whichDate)`
- L6570 `ensureDay(d=date)`
- L6577 `effectiveEntries(d=day()`
- L6578 constante `SALTED_IDS`
- L6579 constante `SWEET_RE`
- L6580 `inferFatShares(e,txt=normalize((e?.name||'')`
- L6598 `inferredNutrients(e)`
- L6637 `totals(entries=effectiveEntries()`
- L6646 `change(fn,message='Guardado')`
- L6650 `undo()`
- L6657 `toast(text,canUndo=false)`
- L6665 constante `CLICK_HANDLERS` — Un solo listener de clic para toda la página; cada sección registra su manejador con onClick().
- L6666 `onClick(fn)`
- L6668 `attempt(fn)`
- L6672 `modal(title,body)`
- L6681 `modalRestore()`
- L6691 `afterModal(fn)` — Cierra la ventana y espera a que el historial se asiente antes de desplazar la página.
- L6692 `modalBack()`
- L6693 `goDate(d)`
- L6700 `renderHeader()`
- L6713 `renderRows(entries)`
- L6717 `entryValues(e)`
- L6718 `renderLog()`
- L6725 `fromFood(id,amount,meal)`
- L6731 `pantryId(name)`
- L6733 `rememberFood(e)` — Guarda en Mi despensa (por 100 g) un plato analizado por la IA, para reconocerlo después sin IA.
- L6739 `addEntries(entries,message='Añadido',d=date,opts={})`
- L6748 `recipe(kind)`
- L6755 `summary(entries)`
- L6759 `renderPresetInfo()`
- L6772 `stripCode(raw)`
- L6778 `parseBIO(raw,meal=$('meal-select')`
- L6784 `parseSmart(raw)`
- L6788 constante `COUNT`
- L6791 `nutrientFields(n,prefix='n_')`
- L6792 `readNutrients(form,prefix='n_')`
- L6797 `editEntry(id)`
- L6806 `editFood(id,pending=null)`
- L6811 `usageStats(days=90)`
- L6817 `renderFoods()`
- L6825 `nutrientSources(key)`
- L6832 constante `SUPP_SLOTS` — Tu pauta de hoy: checklist por momento del día. Marcar = toma confirmada; desmarcar = vuelve a prevista.
- L6833 `suppSlot(meal)`
- L6834 `renderSupps()`
- L6849 `editPlan(id)`
- L6856 `renderSettings()`

### IA y fotos: prompt BIOPEAT (ración completa; lo desconocido queda null, nunca 0)

- L6876 `makePrompt(meal='Comida',note='')`
- L6881 `pantryHint()` — Prompt específico de FOTO: un objeto por ingrediente, con tamaño estimado por referencias y tu despensa como base.
- L6885 `photoPrompt(meal,note)`
- L6888 `resetPhoto()`
- L6899 `openPhoto()`
- L6905 `shrinkPhoto(file)`
- L6908 `selectPhoto(file)`

### Datos: validación, migración de copias antiguas, almacenamiento y copias

- L6934 `cleanDayGoals(g)` — Valida un ajuste manual de macros de un día: {p,f} y opcionalmente kcal.
- L6941 `cleanFood(id,f)`
- L6945 `migrateBase(o)`
- L6964 `download(name,text,type)`
- L6973 `portable()`
- L7013 `syncAppIcons()`
- L7021 `downloadAppIcons()`
- L7058 constante `PROFILES_KEY`
- L7060 `ensureProfilesStore()`
- L7079 `saveProfilesStore(st)`
- L7083 `syncCurrentProfileToStore(rawStr)`
- L7089 `activeProfileName()`
- L7093 `renderProfilesList()`
- L7135 `switchProfile(id)`
- L7157 `deleteProfileById(id)`
- L7181 `refreshDrawerSummary()`
- L7198 `toggleLeftDrawer(force)`
- L7213 `buildAIExportText(rangeOverride)`
- L7463 `copyAIExport()`
- L7477 `downloadAIExport()`
- L7486 `renderDrawerChat()`
- L7505 `buildDrawerChatPrompt(question)`
- L7517 `askDrawerAI(rawQuestion)`
- L7604 `storageStatus()`
- L7610 `idbReadWrite(mode,value)`
- L7611 `openDB()`
- L7612 `save()`

### Eventos generales: añadir con un toque, editar, eliminar

- L7625 `setQuantity(id,value,msg='Cantidad actualizada')`
- L7629 `niceStep(v)`
- L7630 `stepQuantity(id,dir)`
- L7684 `renderAppInfo()`
- L7699 `init()`
- L7726 `upgradeTo11(s,o)` — Revisión 11 (antigua): solo marca la revisión. La corrección de la pauta de entonces ya está en los datos.

### Navegación: una sola página; la barra inferior solo desplaza

- L7728 `setNav(v)`
- L7733 `go(v,focus)`
- L7744 constante `THEME_KEY`
- L7745 constante `SUN_SVG`
- L7746 constante `MOON_SVG`
- L7748 `syncThemeUI()`
- L7760 `toggleTheme()`
- L7769 `syncLogoTheme()`
- L7780 `applyMenuBtnState()`
- L7803 `syncDatePill()`
- L7814 `clampBtnPos(el,x,y)`
- L7824 `bindDraggableBtn(el,storeKey)`
- L7909 `bindDrawerGestures()`
- L7946 `animateValue(el,to,suffix='%',digits=0)`
- L7955 `tick(now)`
- L7958 `macroCard(key,name,color)`
- L7959 `renderToday()`
- L7982 `kindTag(k)`

### Recomendación del día: ideas sencillas con lo que hay en casa y lo que sueles comer; IA opcional

- L7984 constante `HOME`
- L7986 `coachCandidates()`
- L7992 `coachIdeas(t,g,ref,meal)`
- L8005 `renderCoach()`
- L8025 `coachPrompt()`
- L8033 `nutrientDetailStandard(key)`
- L8047 `updateMacroPreview()`

### Hoy: anillos de macros, ratios, micros (B1 = benfotiamina aparte)

- L8053 `upgradeTo12(s,o)`
- L8058 `benfotiamineTotals(entries=effectiveEntries()`
- L8067 `dayActive(d)` — Un día cuenta si tiene comidas o alguna toma real (manual o confirmada). Los días sin registro restan: el depósito se vacía.
- L8069 `rollingMicro(key,dt=date,source='all')` — Depósito de 7 días que termina en dt: suma de lo ingerido / (7 × meta). Cada día nuevo entra y el más antiguo sale.
- L8081 `microStat(m,t=totals()`
- L8086 `metric(m)`

### Equilibrio del día: 5 ratios explicados en lenguaje sencillo, con el porqué y cómo llegar

- L8094 constante `RATIO_NAMES` — solver: {num,den,target} → busca cuánto de un alimento hace que num/den alcance target (mantener ≥ target).
- L8095 `ratioInfo(key,t=totals()`
- L8130 `ratioFixes(info,t=totals()` — Alimentos de tu despensa que llevan el ratio a la meta, con la cantidad exacta (ración razonable).
- L8147 constante `RATIO_ENDS`
- L8149 `ratioZones(i)` — v68: cada equilibrio tiene una zona «aceptable» (ni verde ni mala) y su meta visible en la tarjeta.
- L8157 `ratioTone(i)`
- L8162 constante `NEAR_HEAD`
- L8163 `ratioBar(i,big=false)`
- L8172 `ratioNeedBase(i,t=totals()` — v44: qué te falta (o te sobra) en cada equilibrio, con la cantidad que cambia el resultado.
- L8189 `needHTML(i,t)`
- L8190 `ratioNeed(i,t=totals()`
- L8194 `renderRatios()`
- L8201 `ratioDetail(key)`
- L8211 `microCardHTML(m,x,personal)` — Tarjeta de un nutriente: cifra, barra con tu zona ideal en verde y una línea con la zona y de dónde sale.
- L8228 `renderMicrosForDay()` — Tus nutrientes en 3 bloques: Escudo Peat (límites), Diarios y Tanques (depósito 7 días). Respeta el filtro elegido.
- L8243 `renderMicroMap()`
- L8247 `nutrientDetailForDay(key)`
- L8252 `editTargetsForm()`
- L8262 `mealData()`
- L8267 `renderMealSegments()`
- L8275 `mealDetail(index)`

### Registro: origen de la energía, tipos de grasa y «probar una ración»

- L8285 constante `FAT_KEYS`
- L8287 `fatData(entries=effectiveEntries()`
- L8293 `energyData(entries=effectiveEntries()`
- L8297 `segmentedBar(items,total,attr)`
- L8301 `renderMealChart()`
- L8306 `renderFat()`
- L8314 `fatDetail(key)`
- L8319 `energyDetail(key)`
- L8326 `portionCandidates(q='')`
- L8331 `openPortion()`
- L8344 `previewPortion()`

### Añadir: suplementos extra y batido con previsión de proteína

- L8359 `templates()`
- L8363 `renderExtra()`
- L8374 `updateExtra(reset=true)`
- L8386 `addExtra(id,amount)`
- L8402 `shakePreview()`
- L8403 `renderPresets()`

### Contexto Peat al tocar un gráfico (educativo, no clínico)

- L8418 constante `LENS`
- L8424 `lensKey(key)`
- L8425 `lensHTML(key)`
- L8429 `appendLens(key)`
- L8438 `weekDates()`

### IA en la página: conexión directa o por servidor

- L8448 constante `MEAL_WORD`
- L8449 `mealOfWord(w)`
- L8450 `mealFromText(raw,fallback)`
- L8454 `canonMeal(v,fallback)`
- L8462 `localMeal(raw,meal)`
- L8468 constante `AI_FALLBACK`
- L8469 `applyAIConfig(raw)`
- L8495 `aiError(msg,extra={})` — Si el modelo elegido tarda o falla (tiempo, 429, 5xx, 404), se reintenta solo con AI_FALLBACK.
- L8496 `callGemini(model,key,prompt,img,signal,think=true)`
- L8514 constante `AI_PROVIDERS` — Proveedores de IA: Gemini (gratis), ChatGPT, Claude, OpenRouter, cualquier API compatible con OpenAI, o servidor propio.
- L8521 `aiProv(m=$('ai-mode')`
- L8522 `aiBase(mode)`
- L8531 `chatHeaders(mode,key)`
- L8538 `callChat(mode,model,key,prompt,img,signal)` — ChatGPT, Claude, OpenRouter y APIs compatibles. Mismo contrato que callGemini: devuelve texto o lanza aiError (retry si merece reintento).
- L8568 `listModels(mode,key)` — Lista de modelos de la cuenta (para elegir uno sin saber su nombre exacto).
- L8576 constante `MODEL_PREF`
- L8577 `pickModel(ids)`
- L8582 `ensureModel(st)`
- L8593 `syncProvider()`
- L8606 `requestAI(prompt,img,signal,modelOverride='',onStep=null)`
- L8640 constante `AI_PREF`
- L8641 `aiConnected()`
- L8642 `syncAI()`
- L8644 `saveAIPrefs()`
- L8645 `loadAIPrefs()`
- L8646 `openAISetup()`
- L8652 `upgradeTo16(s,o)`

### Semana: totales, 25 micros, ratios, mapa por día

- L8659 constante `MACROS`
- L8661 `cleanGoals(o,fallback)`
- L8666 `cleanCompare(o={})`
- L8670 `snapshotDay(d,reference='saved')`
- L8675 `upgradeTo17(s,o)`
- L8680 `entriesFor(d,source=weekSource)`
- L8684 `dayRow(dt,source=weekSource)`
- L8688 `goalsFor(dt)`
- L8694 `metricValue(r,key)`
- L8700 `targetOf(dt,key)`
- L8704 `weekSummary()`
- L8708 `aggregate(key,summary=weekSummary()`
- L8712 `tone(pct,mode='macro')`
- L8719 `pctText(a)`
- L8720 `weekProgress(a,color)`
- L8721 `renderWeekMicros(s)`
- L8733 `ratioAggregate(s,num,den)`
- L8737 `renderWeekRatios(s)`
- L8743 `renderWeekTable(s)`
- L8744 `weeklyDetail(key,oneDate=null)`
- L8753 `weekRatioDetail(key)`
- L8761 `shiftMonth(n)` — Calendar: compare explicit personal goals, never classify health or infer unrecorded days.
- L8767 `openDay(dt)`
- L8805 `withDayGoals(fn)`
- L8810 `renderMicros()`
- L8811 `nutrientDetail(key)`
- L8812 `editTargets()`
- L8813 `revealSection(id)`

### Semana: resumen rápido y tendencia de ocho semanas

- L8823 `summaryFor(start)`
- L8827 `ringSVG(pct,color,marker)`
- L8829 `trendData()` — Vista rápida de la semana: 4 anillos de macros, micros y ratios, y una tira de 7 días con colores.
- L8833 `renderTrends()`

### Semana y calendario (v34): 4 preguntas claras + calendario con tendencia

- L8848 constante `MACRO4` — 1 ¿Cómo voy? (media diaria frente a tu meta) · 2 Día a día · 3 Lo que más falta · 4 Tendencia. Luego el calendario.
- L8849 `macroTone(p)`
- L8850 `dayMacroPct(dt,k)`
- L8851 `renderWeekly()`
- L8874 `weekDetail(dt,picked)`
- L8882 `dayCard(dt)` — Ficha rápida de un día: 4 barras de macros + ratios en palabras. Se usa en Semana y en Calendario.
- L8892 `monthStats(month,key)` — Estadística de un mes para una métrica: % diario frente a la meta y media.
- L8898 `sparkline(pts)`
- L8904 `renderCalendar()`
- L8921 constante `MEALS` — One message can describe multiple meals; all-or-nothing import, no forced single meal.
- L8922 `splitMeals(raw)`
- L8932 `localDay(raw,fallback)`
- L8939 `promptDay(raw,fallback)`
- L8940 `analyzeDay(usePhoto=false)`

### Gimnasio: importación del CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes…), sesiones y análisis IA

- L8962 `parseCsv(text)`
- L8977 `hevyDate(value,format='auto')`
- L8994 constante `MAP` — Columnas que se reconocen solas (Hevy, Strong, Fitbod, FitNotes, Jefit y CSV genéricos en inglés o español). El orden marca la prioridad.
- L9009 constante `GYM_APPS`
- L9011 `gymSig(headers)`
- L9012 `gymApp(headers)`
- L9013 `hevyMapping()`
- L9014 `gymSaved()`
- L9015 `renderMapping(parsed)`
- L9032 `optionalNum(v,min=0,max=1e7)`
- L9037 `durSec(v)` — Segundos a partir de «45», «1:30», «01:02:03» o «1h 5m 3s».
- L9044 `buildHevy(parsed,map)`
- L9078 `cleanWorkout(s)`
- L9085 `analyzeGym()`

### Gimnasio: progresión por peso y repeticiones, buscador y gráficos interactivos

- L9100 constante `GP` — Lee state.workouts18 (formato existente). No modifica los entrenamientos salvo «Eliminar sesión».
- L9101 constante `GP_ALIAS`
- L9111 `gpNorm(s)`
- L9112 `gpKey(name)`
- L9116 `gpF(n,d=0)`
- L9117 `gpDate(d,opt)`
- L9118 `gpMonday(d)`
- L9119 constante `GP_GROUPS`
- L9134 constante `GP_COLORS`
- L9135 `gpGroup(name)`
- L9136 `gpWorkSets(s)`
- L9137 `gpModel()`
- L9161 `gpSessionMetrics(e,sets)`
- L9176 constante `GP_METRICS`
- L9181 `gpMetricsFor(e)`
- L9182 `gpRangeHist(e)`
- L9183 `gpPRs(model)`
- L9206 `gpStatus(e)`
- L9224 `gpNext(e)`
- L9232 `gpChart(e)`
- L9260 `gpPointDetail(e)`
- L9266 `gpRepTable(e)`
- L9273 `gpKpis(model)`
- L9282 `gpWeekData(model,w)` — Datos de una semana de gimnasio (series por músculo y sesiones).
- L9287 `gpWeekLabel(w,short)`
- L9288 `gpWeekly(model)`
- L9307 `gpMuscles(model)`
- L9315 `gpHeat(model)` — v69: «Constancia» — mapa de días entrenados (como antes), con días de la semana, meses, intensidad y detalle al tocar.
- L9335 `gpExList(model)`
- L9342 `gpExDetail(model)`
- L9355 `gpDayFood(dt)`
- L9356 `gpNutrition(model)`
- L9363 `gpRecentPRs(model)`
- L9367 `gpSessions(model)`
- L9373 `gpSessionModal(id)`
- L9384 `gpWeekModal(w)`
- L9391 `gpSelect(key)`
- L9392 `gpClick(e)`
- L9408 `renderGym()`
- L9428 `upgradeTo19(s,o)` — v26: calcio 1.500 → 2.000 mg (Peat/Dinkov) solo donde seguía el valor antiguo por defecto; el pasado no se toca.
- L9437 `upgradeTo20(s,o)` — v27: azúcar con micros a 0, fichas USDA para las vacías, sin campos de día que no se usan.
- L9443 `upgradeTo18(s,o)`

### Herramientas de uso diario: menú Más, comidas de un vistazo, buscador, repetir comida, rápidos, copias

- L9468 `openMoreMenu()` — Menú «Más»: todo lo que no está en la barra, en botones grandes al alcance del pulgar.
- L9472 `showHelp()`
- L9476 constante `BACKUP_KEY` — Copias JSON: una sola función para todos los botones.
- L9478 `markBackup()`
- L9482 `exportJSON()`
- L9487 `drawBackupReminder()`
- L9497 `applyDensity()`
- L9509 `syncDayComplete()`
- L9512 `drawMeals()` — Comidas del día de un vistazo.
- L9520 `filterLog()` — Buscador de Registro.
- L9533 `clampNotes()` — Textos largos: dos líneas y «ver más».
- L9539 `recentFoods()`
- L9544 `quickChip(e,fav)`
- L9562 `drawQuickFoods()`
- L9591 `syncAddTools()` — Botones de «¿Qué has comido?»: un panel abierto cada vez.
- L9595 `toggleAddPanel(id)`
- L9607 `extractBiopeat(raw)` — Pegar la respuesta de Gemini: localiza el bloque BIOPEAT o el JSON dentro del texto.
- L9618 `pasteMessage(text,ok)`
- L9626 `copyGoals(s,o)` — Copia las metas globales guardadas (antes de v33 se perdían al recargar).
- L9637 `upgradeTo23(s,o)` — Ahora: vuelve al plan por defecto (145P/75G entreno, 130P/65G descanso), Ca:P 1,20, PUFA 4 g, C:P 3, y referencias de ratio en cada día.
- L9648 `upgradeTo25(s,o)` — Se repara con la ficha HSN (1,5 g de polvo = 165 mg de magnesio, es decir 110 mg por gramo), en la pauta y en los días guardados.
- L9654 `migrate(o)`

### Guardado: no se almacenan días que solo contienen la pauta automática sin cambios

- L9675 `storableState()`

### Render único: actualiza toda la página

- L9683 `nearView(el)`
- L9685 `flushLazy(force='')` — Semana y Gimnasio son las partes más pesadas: se repintan cuando están cerca de la pantalla o al ir a ellas.
- L9689 `render()`

### v58: referencias oficiales para comparar (adultos 19-50 años)

- L9720 constante `REF_NAMES` — Solo sirven para comparar: no cambian tus metas. B1 y B3 de la EFSA van por energía; aquí se usan para unas 2.400 kcal (hombre) y 2.000 kcal (mujer).
- L9721 constante `REF_TABLE`
- L9728 `refTargets(mode)`
- L9729 `syncMicroMode()`
- L9742 `mealByHour(h=new Date()`
- L9749 `syncMealByHour()`

### v43: restaurar copia con resumen, compartir copia, aviso de versión nueva y sin conexión

- L9760 `dataSummary(s)`
- L9764 `confirmImport(next,name)`
- L9771 `shareOrDownload(name,text,type)` — En el móvil abre «Compartir» (WhatsApp, Drive, correo…); en el ordenador descarga el archivo.
- L9777 `checkUpdate()`
- L9782 `showUpdate(v)`

### v50: «¿Qué me falta?» de Semana

- L9797 constante `GAP_PREFER`
- L9798 constante `GAP_SKIP`
- L9799 constante `GAP_UNIT`
- L9800 `gapQty(f,x)`
- L9801 `gapFoods(key,gap,ctx)`
- L9820 `weekSources(key,sum)`
- L9826 `gapRows(sum)` — Estado de cada micro esta semana: media diaria frente a su zona (con un 10 % de margen en lo que falta).
- L9839 `gapRow(x,open,meal,sum,ctx)`
- L9855 `renderGaps(sum,s)`

### Perfiles: sexo, objetivo, semana, comidas habituales y asistente

- L9880 `getSex(s=state)` — «v54» es solo el nombre histórico de la clave guardada: no se renombra.
- L9881 `isFemale(s=state)`
- L9882 `sexLabel(s=state)`
- L9883 `sexBadge(sex)`
- L9885 constante `OPT_BASE` — Cambios por sexo sobre la tabla OPT (mismo formato). Solo se cambia lo que tiene fuente; el resto es igual para los dos.
- L9886 constante `OPT_FEMALE`
- L9897 constante `NEW_PROFILE_MICRO` — Metas de partida de un perfil nuevo. Mujer: hierro, zinc y magnesio de las fuentes de arriba.
- L9898 `applySexOpt(sex)`
- L9900 `femaleWhy(key)` — Equilibrios del día: frase extra para mujer, con su fuente.
- L9905 `cleanPreset(p,fb)`
- L9909 `dayNamesFor(types)`
- L9911 `cleanV54(v,sex)` — Limpia los ajustes del perfil guardados. Sin datos (copias antiguas) se usan los de un perfil nuevo.
- L9921 `upgradeTo26(s,o)` — Si el perfil lo usaba, sus cifras pasan a sus metas guardadas (entreno/descanso) y la energía se calcula igual que antes.
- L9929 `profV()`
- L9930 `isTrainDay(i)`
- L9931 `activityName(i)`
- L9932 `dayFaf(i)`
- L9933 `presetDesc(cfg,shake)`
- L9937 `profileDescription()`
- L9945 constante `WIZ_STEPS` — Un único borrador «wiz». Se pinta dentro de la ventana normal (modal) y se repinta sin perder la posición.
- L9947 `wizCatalog()`
- L9948 `wizOpen(opts={})`
- L9963 `wizTitle()`
- L9964 `wizPaint(sameStep=true)`
- L9973 `wizSync()`
- L9986 `wizFoodOptions()`
- L9989 `wizPresetSummary(cfg,whey)`
- L9994 `wizPresetHTML(kind)`
- L10002 `wizPreview()`
- L10013 `wizHTML()`
- L10054 `wizCommit()` — Guarda el borrador. Las dosis y valores de la pauta se conservan; si cambias la dosis, el aporte se escala en proporción.

### v56: app pública — sugerencias de suplementos, guía de uso, centro «Más», buzón de sugerencias y gestos de una mano

- L10138 constante `ALL_DAYS` — No son recomendaciones médicas: el usuario elige y ajusta la dosis a su etiqueta. También puede añadir cualquier otro a mano.
- L10139 constante `SUPP_CATALOG`
- L10161 constante `PEAT_BASIC` — «Lo básico de Peat» al crear un perfil: comidas habituales y suplementos que suele recomendar su entorno (se pueden quitar en el paso 4).
- L10162 constante `PEAT_BREAKFAST`
- L10163 constante `PEAT_SHAKE`
- L10165 constante `WIZ_HELP` — Ayuda corta que sale arriba de cada paso del asistente.
- L10172 `benfoUser()`
- L10174 constante `ICON` — Iconos de línea propios (se ven igual en todos los móviles, a diferencia de los emojis).
- L10190 `ico(n)`
- L10192 constante `TOUR` — ----- Guía de uso (sale al terminar el asistente y siempre en Más → Guía de uso) -----
- L10201 `showTour(i=0)`
- L10213 constante `HUB` — ----- Centro «Más»: todo a un toque del pulgar -----
- L10214 `hubAction(v)`
- L10222 constante `FORM_URL` — Llegan solas a una hoja de Google (formulario del creador de la app). Sin cuentas ni datos personales.
- L10223 constante `FORM_FIELDS`
- L10224 constante `FB_CATS`
- L10226 `openFeedback()`
- L10230 `feedbackData()`
- L10237 `feedbackText()`
- L10238 `sendFeedback()`
- L10251 `shareFeedback()`
- L10268 `bindSheetSwipe()` — Deslizar la ventana hacia abajo desde su cabecera la cierra.
- L10275 `bindDateSwipe()` — Deslizar el recuadro de la fecha a izquierda o derecha cambia de día.

### v59: traducciones al inglés (una por línea; el texto en español con # en lugar de las cifras)

- L10283 constante `I18N_EN`

### v59: idioma (español / inglés)

- L11915 constante `NUM_RE` — Para un texto nuevo: añade su línea a I18N_EN (está justo encima). Lo que no esté en la tabla se queda en español.
- L11916 constante `WD_EN`
- L11917 `trOne(s)`
- L11925 constante `TR_VERB` — Plantillas para etiquetas con un nombre dentro («Editar Leche entera»). Solo se usan si el nombre se traduce o en atributos (aria-label…).
- L11926 constante `ES_FOOD_GYM`
- L11963 `trFood(s)`
- L11975 constante `TR_TPL`
- L12009 `trLower(s)`
- L12010 `trTpl(s,attr)`
- L12011 constante `FOOD_SEL`
- L12012 `trText(s,attr=false)`
- L12022 `trNode(n)`
- L12037 `trEl(el)`
- L12045 `trTree(root)`
- L12054 `untrTree(root)` — Vuelve al español sin recargar: restaura los textos originales guardados.
- L12065 `setLang(l,quiet)`
- L12078 `langPickerHTML()`

### v59: estadísticas sin cookies (GoatCounter), solo en la web publicada

- L12087 constante `GC_CODE`
- L12088 `startStats()`

### v59: mudanza de datos a otra dirección web (por ejemplo, un dominio propio)

- L12098 constante `MOVE_TAG` — Los datos viven en el navegador y van ligados a la dirección. Esto los empaqueta, comprimidos, en el enlace de la nueva dirección.
- L12099 `packMove()`
- L12107 `unpackMove(code)`
- L12116 `moveData()`
- L12126 `takeMoveCode()` — Se lee y se quita del enlace al arrancar (antes de abrir ninguna ventana, para que «Atrás» no lo devuelva).
- L12132 `checkMove(code)`
- L12151 `aiFrameworkLines()` — v69: marco de referencia del informe para IA. Así cualquier IA, aunque no conozca la app ni al usuario, sabe con qué comparar.

### Arranque

