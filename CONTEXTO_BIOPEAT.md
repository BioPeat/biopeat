# CONTEXTO · BioPeat

**Versión actual: v66** (revisión de datos 26)

Documento maestro. Lo lee la IA que programa BioPeat (Gemini «BioPeat Dev» o Claude). Los cambios se entregan en bloques `@@@` y los aplica y prueba `actualizar.html`. **Se actualiza sustituyendo el texto de cada apartado, nunca añadiendo apartados nuevos al final.** Si algo de aquí contradice al código, manda el código; avisa de la diferencia.

## 0. App pública (desde v56)
- **BioPeat la usa cualquiera.** Diego es el creador y el usuario principal, pero **nada suyo está en el código** (desde v58): ni su pauta, ni su desayuno o batido, ni su plan de macros, ni sus nombres de días. Todo eso vive solo en sus datos guardados y se describe en los apartados 1-4 para que la IA lo conozca. Un usuario nuevo: un usuario nuevo empieza con `defaults()` genérico (sin pauta, sin desayuno ni batido fijos, metas genéricas, sin Nesquik ni Haribo) y el **asistente** lo configura (bienvenida, ayuda en cada paso y sugerencias de suplementos de `SUPP_CATALOG`). Al terminar sale la **guía de uso** (`TOUR`, siempre en Más → Guía de uso).
- **Más** (barra inferior, `HUB`): Nutrientes, Tu pauta, Gimnasio, Ajustes, Copia de seguridad y Guía de uso, más un botón ancho que abre el **menú lateral** (logo): Perfiles, Exportar datos para IA y Sugerir una mejora, con **Pregunta a tu IA siempre visible abajo**. No se repiten funciones entre los dos.
- **Asistente, punto de partida** (primera vez y perfil nuevo): «Empezar de cero» o «Lo básico de Peat» (`PEAT_BREAKFAST`, `PEAT_SHAKE` y suplementos `PEAT_BASIC`: D3, K2, E, magnesio y glicina, que se pueden quitar). Suplementos: `SUPP_CATALOG` en dos grupos (`g:'peat'` y `g:'comun'`, con la postura de Peat si los desaconsejaba) y «Añadir otro a mano».
- **Nutrientes → Comparar:** mis metas, referencia UE (EFSA) o EE. UU. (NIH) por sexo (`REF_TABLE`, `refMode`); solo cambia la comparación, nunca las metas.
- **Una mano:** en el móvil las ventanas son hojas que salen desde abajo (se cierran deslizando hacia abajo), «Añadir» es el botón central elevado, y deslizar el recuadro de la fecha cambia de día.
- **Sugerencias de usuarios:** Más → Sugerir una mejora las envía (sin cuentas) al formulario de Google de Diego (`FORM_URL`, `FORM_FIELDS`: tipo, título, descripción, versión) con `fetch` `no-cors`; llegan a una hoja de Google. Diego las ve en `actualizar.html` → Buzón (lee la hoja publicada en CSV), marca las que quiere, copia la petición para la IA y las marca como «Hecha».
- **Idiomas (v59):** español e inglés. Se elige en el paso 1 del asistente (primera vez y perfil nuevo) y en Ajustes (`setLang`, preferencia `bp_lang` del dispositivo; por defecto, el idioma del móvil). Traducción en pantalla con la tabla `I18N_EN`; los datos se guardan siempre en español. La IA responde en el idioma elegido.
- **Lanzamiento (v59):** `inicio.html` es la web de presentación (ES/EN) con instalación, preguntas, **privacidad** (#privacidad) y **aviso legal** (#aviso-legal); contacto biopeatapp@gmail.com. Estadísticas sin cookies con GoatCounter (código `biopeat`, solo en la web publicada). **Mudanza:** Ajustes → «Mudar mis datos a otra dirección» abre la nueva dirección con los datos comprimidos en el enlace (`#bp-move=`) y allí se confirman. Sugerencias con «¿Cómo nos has conocido?» (va en la descripción como «[Origen: …]»).
- **Actualizaciones:** cada `index.html` publicado llega a todos los usuarios (aviso «Hay una versión nueva»). Los datos de cada uno no se tocan.

## 1. Diego y cómo quiere la app
- La app tiene **perfiles**. Cada perfil guarda sus datos aparte y tiene **sexo** (hombre o mujer), objetivo, semana, desayuno, batido y pauta propios. Lo que sigue describe **solo el perfil de Diego** (sus datos guardados), no lo que ve un usuario nuevo.
- 23 años, hombre, 185 cm, ~77,5 kg (editable). Madrid. Escribe rápido y con faltas: entiéndelo por el sentido.
- Trabaja en finanzas y entrena a dos equipos de baloncesto.
- Pesas full body **lunes, miércoles y sábado**; partido el **domingo**; martes, jueves y viernes sin pesas.
- Registra el gimnasio en **HEVY gratis**: exporta un CSV y lo importa en la app (vale el CSV de cualquier app).
- Enfoque **Ray Peat / Georgi Dinkov**, pero la app **no debe ser juzgona ni rígida**: datos claros y sugerencias, sin avisos médicos ni confirmaciones por motivos de salud. Sabe lo que hace con su suplementación y aspirina.
- Gustos: móvil primero, muy visual, gráficos que se tocan, porcentajes que pasan del 100 %, pocas pantallas, añadir con un toque (se puede deshacer). No soporta que se diga «hecho» o «comprobado» si no lo está.

## 2. Metas del día
Se calculan siempre al vuelo con `targetFor(fecha)`. Orden de prioridad: ajuste manual de ese día → metas globales («todos los días» o «entreno/descanso») → plan del perfil. Desde v58 el plan de Diego (tabla de abajo) está guardado en **sus metas «entreno / descanso»** (`upgradeTo26` lo pasó una vez); ya no hay plan personal en el código. Los demás perfiles calculan proteína y grasa con `GOAL_TYPES` (g/kg según objetivo, sexo y día de entreno o descanso) y la energía con la TMB × el FAF del tipo de día (`DAY_TYPES`). Mujer: TMB −161 en vez de +5, **proteína mínima 80 g** y un suelo de calorías para no quedarse corta.

| Día | Actividad | FAF | Proteína | Grasa | Aspirina |
|---|---|---|---|---|---|
| Lunes | Full body | 1,725 | 145 g | 75 g | 500 mg |
| Martes | Pista | 1,5 | 130 g | 65 g | 250 mg |
| Miércoles | Full body | 1,725 | 145 g | 75 g | 500 mg |
| Jueves | Pista + selenio | 1,5 | 130 g | 65 g | 250 mg |
| Viernes | Pista | 1,5 | 130 g | 65 g | 250 mg |
| Sábado | Full body | 1,65 | 145 g | 75 g | 500 mg |
| Domingo | Partido + selenio | 1,75 | 145 g | 75 g | 500 mg |

- Energía = TMB Mifflin-St Jeor (10×peso + 6,25×185 − 5×23 + 5) × FAF, redondeada a 5.
- Proteína y grasa del plan por defecto escalan con el peso (peso / 77,5).
- Hidratos = el resto de la energía, con un **mínimo de 3 g por g de proteína** (C:P ≥ 3). Si no cabe, sube la energía.
- Diego puede cambiar las metas en **Nutrientes → Editar objetivos** (todos los días, entreno/descanso o solo un día) y en **Ajustes → Editar objetivos de macros del día**. «Volver al plan Peat por defecto» lo restablece desde hoy.

## 3. Pauta de suplementos (la de Diego; un usuario nuevo empieza sin pauta)
Se suma sola cada día y cuenta como tomada. Si un día no se toma algo, Diego toca esa toma en «Tu pauta» y deja de contar (tocar otra vez la recupera). Se edita en «Tu pauta → Cambiar mi pauta habitual».

| Momento | Qué | Cantidad | Días |
|---|---|---|---|
| Desayuno | Vitamina D3 | 4.000 UI (100 µg) | todos |
| Desayuno | Vitamina A (retinol) | 10.000 UI (3.000 µg RAE) | todos (la quita a mano si come hígado) |
| Desayuno | K2 MK-4 | 0,5 mg | todos |
| Comida | Vitamina E | 200 UI (134 mg) | todos |
| Comida | Benfotiamina (B1) | 250 mg | todos |
| Comida | Glicina | 5 g | todos |
| Comida | Bisglicinato de magnesio HSN | 2 g de polvo (≈220 mg Mg) | todos |
| Comida | Selenio | 200 µg | jueves y domingo |
| Merienda | Creatina | 5 g | todos (la del batido no se duplica) |
| Merienda | K2 MK-4 | 0,5 mg | todos |
| Merienda | Aspirina, toda la del día | 500 mg L/X/S/D · 250 mg M/J/V | todos |
| Antes de dormir | Glicina | 5 g | todos |
| Antes de dormir | Bisglicinato de magnesio HSN | 2 g de polvo | todos |

La B1 se muestra aparte: mg de benfotiamina frente a su pauta; la tiamina de los alimentos va por separado.

## 4. Comidas habituales (un toque; las de Diego, un usuario nuevo las configura en el asistente)
Se guardan por perfil en `state.v54.breakfast` y `state.v54.shake` y se editan en el asistente (⚙). Las de Diego:
- **Desayuno:** 220 ml leche entera + 21 g Nesquik + 1 plátano (120 g) + 250 ml zumo de naranja.
- **Batido de merienda:** 200 ml leche + 150 ml zumo + 35 g azúcar + 1 plátano + whey 0-40 g (con un control deslizante que muestra el % de proteína del día).
- Durante el entreno o el partido: ositos Haribo con azúcar.

## 5. Reglas Peat / Dinkov de la app
- **PUFA ≤ 4 g/día** (es un máximo, no una meta). **Ca:P ≥ 1,20**. Calcio 2.000 mg. **Hierro ≤ 14 mg** (límite).
- **Zona ideal de cada micro: UNA sola tabla, `OPT`** (en `index.html`, junto a `DEPOSIT`). Cada entrada tiene `kind` (`min` llegar a la meta · `band` entre `lo` y `hi` · `max` tope · `ref` solo referencia), `src` (peat, din, foro, of, tuya) y `ref` (texto que se ve al tocar el nutriente). Helpers: `optInfo()`, `optState()`, `optLine()`. **No crees otras listas de bandas o límites.** Valores actuales: vitamina A banda 3.000-3.800 µg (Peat: 10.000 UI), vitamina D mín. 100 µg (4.000 UI), selenio banda 100-200 µg, yodo banda 150-225 µg, hierro máx. 14 mg, calcio mín. 2.000 mg (Peat/Dinkov 2.000-3.000), **fósforo solo referencia** (importa Ca:P) y sodio sin «te falta». PUFA máx. 4 g. A:D 2-4 : 1 y Zn:Cu ~10 : 1 son referencias de la app sin cifra verificada de Peat.
- **Depósitos (media de 7 días):** A, D, E, B12, folato, selenio, yodo, cobre y hierro. Los días sin registro cuentan 0 (la tarjeta dice «n/7 con registro»; «parcial» solo significa que a algún alimento le falta el dato). El día de hoy no cuenta hasta marcarlo completo: se mide con los 7 días cerrados hasta ayer y la tarjeta indica cuánto suma hoy. El resto son diarios.
- **Grasa saturada:** para la meta de grasa cuenta ×0,5 (`SAT_W`), por ser la grasa que mejor encaja con Peat (coco, mantequilla, lácteos); el PUFA es lo que se vigila. La energía (kcal) cuenta todo.
- Alimentos preferidos para sugerir: leche, queso, zumo de naranja, fruta madura, miel/azúcar, patata, arroz, huevos, marisco, gelatina, carne con caldo. Evitar aceites vegetales.
- **No inventes cifras atribuidas a Peat.** Donde no hay cifra suya, se usa la meta personal.
- **Mujer:** la tabla `OPT_FEMALE` cambia solo lo que tiene fuente (se aplica con `applySexOpt()` en cada `render()`): hierro tope 18 mg (oficial; Peat: el estrógeno hace absorber más hierro, «From PMS to Menopause»), zinc 8 mg (oficial), magnesio 400 mg (Peat/Dinkov; «Nutrition for Women»: corta los calambres menstruales), sodio sin restringir (edema premenstrual), y notas de Peat en vitamina A, E, B2 y calcio. `femaleWhy()` añade una frase de Peat para mujer en los equilibrios. **Peat no dio cifras distintas para mujer en PUFA, Ca:P ni C:P: son las mismas (4 g, 1,2 y 3).** Metas de partida de un perfil nuevo: `NEW_PROFILE_MICRO`.

## 6. Qué hace la app (v59)
Una sola página. Barra inferior **Hoy · Registro · Añadir · Semana · Más** (no cambiar el orden) y botón redondo de **Gimnasio**.
- **Menú lateral** (tocar el logo): Perfiles (tocar = usar; ⚙ = asistente; ✎ renombrar; × borrar; «+ Crear perfil nuevo»), Exportar datos para IA y Pregunta a tu IA. La lista se desplaza sola sin mover la página.
- **Asistente de perfil** (`wizOpen({mode})`, modos `first` / `new` / `edit`): 5 pasos (Tú · Objetivo · Comidas · Suplementos · Resumen con las metas de un día de entreno y uno de descanso). Sale solo al empezar de cero (con botón para restaurar una copia). Al crear un perfil se puede empezar de cero o copiar la despensa y la pauta del perfil activo. Al guardar, las dosis y aportes de la pauta se conservan (si cambias la dosis, el aporte se escala).
- **Hoy:** energía, anillos de macros (% sin tope, «Te faltan X g»), recomendación del día + «Pedir sugerencia a la IA», **Equilibrio del día** (5 tarjetas: Ca:P, PUFA, hidratos:proteína, A:D, Zn:Cu; cada una con semáforo ✓/!, barra con zona verde y «Tú», y una frase sencilla; al tocarla: «¿Por qué importa?» (explicación Peat) y «Cómo llegar hoy» con alimentos y cantidades exactas que se añaden con un toque), comidas del día con «Igual que ayer», «Marcar día completo», «Vista Resumen».
- Al añadir la primera comida de un día, el día anterior se marca solo como completo (v35).
- **Añadir:** texto libre de varias comidas en un mensaje (sin IA si reconoce los alimentos), foto con IA, «Foto en Gemini» (copiar prompt + pegar respuesta `BIOPEAT:`), manual, rápidos/favoritos, desayuno, batido, suplemento extra, Mi despensa (lo que analiza la IA se guarda y se reutiliza).
- **Registro:** buscador, grupos por comida, − / + / ✎ / ×, deshacer, probar una ración, reparto de energía y tipos de grasa.
- **Tus nutrientes:** tres bloques (Escudo Peat: PUFA y hierro · Diarios · Tanques de 7 días), tarjetas o mapa, filtros.
- **Tu pauta:** las tomas de hoy por momento del día (se suman solas; tocar = no tomada hoy), «+ Toma extra», «Lo que te aporta tu pauta» (qué parte de cada meta cubren los suplementos frente a la comida) y el editor de la pauta habitual plegado.
- **Semana:** 4 preguntas numeradas: 1 ¿Cómo voy? (media diaria de los días con comidas frente a la meta, 4 anillos y una frase), 2 Día a día (7 barras de energía; tocar = ficha del día), 3 ¿Qué me falta? (resumen con 4 filtros: te faltan / te pasas / en zona / sin datos; cada hueco se abre al tocarlo y propone alimentos de tu despensa, con vasos o huevos si encajan, que se añaden a hoy con un toque; «Ver N más»; los 25 micros plegados), 4 ¿Voy mejorando? (8 semanas). Debajo, el **calendario**: selector Energía/Proteína/Hidratos/Grasa, media del mes, tendencia (últimos 7 días frente a los 7 anteriores), gráfico de línea del mes y cuadrícula con color por día (verde en rango, ámbar por debajo, violeta por encima, gris sin datos) y 3 barritas de macros; tocar un día = ficha rápida. Opciones de cálculo y tablas, plegadas al final.
- **Gimnasio:** importación del CSV de **cualquier app** (reconoce solas Hevy, Strong, Fitbod, FitNotes y CSV genéricos en inglés o español con `MAP` y `GYM_APPS`; libras→kg, metros→km, fechas DD/MM o MM/DD deducidas, columna «series» que se expande; si no reconoce el formato, el usuario elige una vez la fecha y el ejercicio y se recuerda en `bp_gym_maps`), progresión por peso y repeticiones, 1RM (Epley), récords, volumen, reparto muscular, constancia, nutrición en días de entreno, análisis con IA.
- **Metas genéricas de partida** (usuario nuevo, `MICRO`): vit. E 15 mg, K 120 µg, C 90 mg, B1 1,2 mg, B2 1,3, B3 16, B5 5, B6 1,7, biotina 30 µg, B12 2,4 µg, magnesio 400 mg, potasio 3.500 mg, zinc 11 mg (resto igual). B1 solo se trata como «benfotiamina» si la pauta la incluye (`benfoUser()`).
- **Más → Ajustes:** sexo (♂/♀), botón del asistente, perfil, metas, conexión IA, notas para la IA (+ «Aplicar instrucciones con IA»), estado de la app, copias JSON/HTML (en el móvil se comparten; al restaurar se ve un resumen antes).
- **Avisos:** «Hay una versión nueva» al volver a la app si GitHub tiene una más reciente; aviso sin conexión.

## 7. Conexión con IA (no tocar sin pedirlo)
- Cada usuario conecta **su** IA en Añadir → Conectar IA (`ai-mode`): **Gemini** (`direct`, gratis, por defecto), **ChatGPT** (`openai`), **Claude** (`anthropic`), **OpenRouter**, **otra compatible con OpenAI** (`compat`, con dirección base `ai-base`) o servidor propio (`proxy`). Datos de cada uno en `AI_PROVIDERS`. Sin clave: «Foto en tu chat» copia el prompt para pegarlo en cualquier chat y luego se pega la respuesta `BIOPEAT:`.
- La clave se guarda solo en el móvil si marca «Recordar» (`biopeat_ai24`). **Nunca pongas claves en el código.**
- `requestAI(prompt, img, signal)` es la única puerta: Gemini → `callGemini()` (API estable, `thinkingLevel: 'low'`, cadena con `AI_FALLBACK` gemini-3.1-flash-lite); resto → `callChat()` (formato OpenAI `/chat/completions` o Anthropic `/v1/messages`), 3 intentos. Saturación (429/503, `AI_BUSY`) → reintento con espera y mensaje claro.
- Modelo: Gemini por defecto `gemini-3.8-flash`. En los demás, si el campo está vacío, «Probar conexión» lee la lista de modelos de la cuenta (`listModels()`, `pickModel()`) y elige uno de texto.
- Foto: se reduce a 1.600 px (JPG 0,88) y se analiza componente a componente con `photoPrompt()`. Hace falta un modelo con visión; si no la tiene, se avisa.
- Formato de importación: `BIOPEAT:{...}` o `BIOPEAT:[{...}]` con meal, name, grams, kcal, p, c, f, pufa y los 25 micros. Lo desconocido se omite o va como null, nunca 0.
- Claves de los 25 micros: vitA, vitD, vitE, vitK, vitC, b1, b2, b3, b5, b6, b7, b9, b12, colina, ca, phos, mg, k, na, fe, zn, cu, se, i, mn.

## 8. Datos y publicación
- Los datos viven en el navegador del móvil (`localStorage`, clave `biopeat_pro_v10`). **Nunca se suben a GitHub.**
- Claves guardadas que **no se renombran:** `biopeat_pro_v10`, `biopeat_profiles_v1` (perfiles), compare17, workouts18, favorites22, microTargets17, goalOrigin17, ratioGoals17, macroGoals, targetMode, `v54` (ajustes del perfil: el nombre es histórico) y `profile.sex`.
- Publicada con **GitHub Pages** (rama main) e instalada como app (manifest.json + sw.js). Al subir un index.html nuevo la app se actualiza sola en 1-2 minutos sin perder datos.

## 9. Cómo está hecho el código (resumen técnico)
- Todo en `index.html`: CSS, HTML y un único `<script id="app">`. Sin librerías.
- `change(fn, mensaje)`: única forma de modificar datos (guarda, repinta y permite deshacer).
- `render()`: único punto que repinta. Semana y Gimnasio se pintan al acercarse (`flushLazy`).
- Un solo listener de clic: cada sección registra el suyo con `onClick(fn)`.
- Piezas reutilizables (v34): `ratioInfo(clave)` + `ratioFixes()` (equilibrios), `dayCard(fecha)` (ficha rápida de un día), `monthStats()` + `sparkline()` (tendencias), `macroTone(%)` (colores ok/low/high/none).
- Metas: `targetFor(fecha)` / `dayGoal()` / `goalsFor(fecha)`. No se guardan metas calculadas en los días; solo el ajuste manual `days[fecha].macroGoals`.
- Logo: SVG dentro de `.brand-icon` (ids bp-bg, bp-rim, bp-mark). Iconos del móvil: icon-192.png, icon-512.png e icon-maskable-512.png (Ajustes → «Descargar iconos» los regenera desde el SVG). Colores: azul noche (#16243a) y dorado (#e9bf5c, variables --gold y --gold-soft); verde, ámbar y violeta siguen siendo los colores de estado.
- Migraciones: `migrate()` → `migrateBase` + `upgradeToNN` + `cleanV54()`. Cada `upgradeToNN` se ejecuta una sola vez comprobando `o.appRevision`. `upgradeTo25` repara el magnesio que estropeó el asistente de v54.
- **Prohibido** añadir otro `<script>` o «envolver» funciones (`x=function…`, `window.x=…`): la v54 lo hizo y el perfil de mujer volvía a hombre al recargar. `smoke.py` lo detecta y falla.

## 10. Historial (una línea por versión, máximo 8)
- **v59 · Copilot:** español e inglés (`I18N_EN`, `trTree`, `setLang`, `LOC()`), web `inicio.html` con privacidad y aviso legal, GoatCounter, mudanza de datos por enlace, «¿Cómo nos has conocido?» en sugerencias, IA en el idioma del usuario y modo resumen más compacto arriba.
- **v58 · Copilot:** nada de Diego en el código (su plan de macros pasa a sus metas con `upgradeTo26`; fuera `PLAN`, `DIEGO_V54`, `DEF_P`, Nesquik y Haribo); «Lo básico de Peat» al crear perfil; plantillas Peat de desayuno y batido; 19 suplementos en dos grupos + añadir a mano; comparar nutrientes con UE/EE. UU.; chat de IA fijo abajo del menú y «Más» sin repetir el menú.
- **v57 · Copilot:** sugerencias por formulario de Google (sin cuentas) y buzón que lee la hoja; IA de cualquier proveedor (Gemini, ChatGPT, Claude, OpenRouter, compatible) con `callChat()` y elección de modelo; gimnasio con el CSV de cualquier app (Hevy, Strong, Fitbod, FitNotes, genérico) con detección y formato recordado.
- **v56 · Copilot:** app pública: sin datos de Diego por defecto; asistente con bienvenida, ayuda por paso y sugerencias de suplementos Peat (`SUPP_CATALOG`); guía de uso (`TOUR`); centro Más (`HUB`) con iconos propios (`ICON`/`ico()`); buzón de sugerencias (GitHub issues `[BioPeat]`); hojas inferiores, botón Añadir central y gestos de una mano; aspecto pulido; manifest con accesos directos; `actualizar.html` con archivo enfocado, cambios por partes y buzón.
- **v55 · Copilot:** perfiles integrados en el script principal (sin parches); el perfil de mujer se conserva al recargar; asistente rehecho (5 pasos, resumen, conserva la posición, copia despensa y pauta, sale al empezar de cero) que ya no cambia las dosis de la pauta ni rompe el historial; repara el magnesio estropeado por v54; cifras y notas de mujer con fuente Peat; menú lateral con lista desplazable y chat plegable; `smoke.py` prueba perfiles y prohíbe parches.
- **v51-v54 · Gemini:** menú lateral, perfiles, informe para IA, chat con la IA, sexo hombre/mujer y asistente de perfil (como bloque aparte, integrado en v55).
- **v50 · Copilot:** micronutrientes con una sola tabla de zonas ideales (`OPT`); depósito de 7 días sin «parcial» falsos; «¿Qué me falta?» rehecho; arreglos de fósforo, selenio/yodo/A, colores de la semana y «Ca:P 1,10».
- **v49 · Copilot:** grasa saturada ×0,5 para la meta de grasa (`SAT_W`); depósitos sin el día abierto; `actualizar.html` más tolerante y con errores localizados; GitHub actualiza CONTEXTO y MAPA solo.

## 11. Pendiente / ideas
- Unificar las capas de CSS sin cambiar el aspecto (hay reglas repetidas de varias versiones).
- Gimnasio: aplicar el mismo estilo de «preguntas numeradas» que Semana.
