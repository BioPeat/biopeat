# AGENTS.md · Reglas para la IA que programa BioPeat

Lo usan el Gem de Gemini «BioPeat Dev» y el proyecto de Claude «BioPeat Dev». Escribe siempre en **español de España**, claro y corto. Diego no programa: nunca le pidas que edite código a mano; él solo copia y pega.

## 0. Cómo funciona el flujo
1. Diego descarga desde `actualizar.html` (Paso 1) un **archivo enfocado**: solo los trozos del script que tienen que ver con su petición, todo el HTML y nada de CSS. Si te falta una función, **no la inventes**: dile su nombre y que descargue otro archivo enfocado que la incluya.
2. Tú respondes con bloques `@@@` (ver apartado 2).
3. Diego los pega en `actualizar.html`, que los aplica a una copia, arranca la app, la recorre entera y comprueba que sus datos se leen igual.
4. Si sale rojo, Diego te pega un mensaje que empieza por **CORREGIR**. Trae el bloque que falla y, si es un error de escritura, la línea, la columna y el trozo de código exacto. Arregla la causa y entrega **solo los bloques que cambian**, con su **mismo número**, dentro de un único bloque de código y empezando por la línea `@@@ SOLO CORREGIDOS` (la página los combina con los anteriores). Si dudas, entrega todos.
5. Si sale verde en un cambio grande, Diego te pega un mensaje que empieza por **REVISAR** (en cambios pequeños puede saltárselo): revísalo como si no lo hubieras escrito tú y contesta «✅ APROBADO» o «❌ HAY QUE CORREGIR» + respuesta nueva.
6. Con «✅ APROBADO», Diego sube el `index.html` nuevo a GitHub.

## 1. Archivos del repositorio
`index.html`, `actualizar.html`, `manifest.json`, `sw.js`, `icon-192.png`, `icon-512.png`, `icon-maskable-512.png`, `AGENTS.md`, `CONTEXTO_BIOPEAT.md`, `MAPA_DEL_CODIGO.md`, `README.md`, `tests/smoke.py`, `tests/datos_prueba.json`, `tools/mapa.py`, `tools/sincronizar_version.py`, `.github/workflows/check.yml`. GitHub regenera solo la versión de `CONTEXTO_BIOPEAT.md` y `MAPA_DEL_CODIGO.md` en cada subida: no los edites para eso.
- Normalmente solo cambias `index.html`. No crees archivos nuevos.

## 2. Cómo editar
- Entrega los cambios como bloques `@@@ BUSCAR n` / `@@@ CAMBIAR POR` / `@@@ FIN`. El texto de BUSCAR se copia **literalmente** del archivo y debe aparecer **exactamente una vez**. `actualizar.html` rechaza cualquier bloque que no cumpla esto.
- Cambios centrados en la tarea. No reescribas ni «limpies» partes que no te han pedido.
- Cada función se define **una sola vez**. Si cambias una función, sustitúyela **en su sitio**; no la dupliques ni la «envuelvas» (`x=function…`, `window.x=…`, `const origX=x`). **Nunca añadas otro `<script>` ni otro `<style>` al final del archivo**: todo va dentro del `<script id="app">` y del `<style>` principal. La v54 lo hizo así y el perfil de mujer volvía a hombre al recargar; `smoke.py` ahora lo rechaza.
- **Para que no falle la comprobación:** prefiere añadir código en funciones nuevas y enganchar con el cambio más pequeño posible; líneas cortas (<150 caracteres); **sin plantillas con backticks anidadas** dentro de `${}` (construye cada trozo en una variable y únelos con `+`); en BUSCAR usa un fragmento corto y único (≤120 caracteres) aunque la línea sea larguísima; antes de entregar cuenta que ( ) { } [ ] comillas y backticks están cerrados.

## 3. Reglas del código (su incumplimiento rompió v30-v32)
- **Metas del día:** usa siempre `targetFor(fecha)`, `dayGoal()` o `goalsFor(fecha)`. **Nunca** guardes metas calculadas dentro de `state.days[fecha]`. El único ajuste por día permitido es `state.days[fecha].macroGoals = {p, f, kcal?}`.
- **Cambiar datos:** solo dentro de `change(() => { ... }, 'mensaje')`. No llames a `save()` ni a `render()` tras un `change`.
- **Migraciones de datos guardados:** crea `upgradeToNN(s, o)` que empiece con `if((Number(o.appRevision)||0) >= NN) return;`, llámala en `migrate()` y sube `APP_REVISION` a NN. Nunca hagas cambios de datos que se repitan en cada arranque.
- **Claves guardadas que no se renombran:** `biopeat_pro_v10`, `biopeat_profiles_v1`, compare17, workouts18, favorites22, microTargets17, goalOrigin17, ratioGoals17, macroGoals, targetMode, `v54`, `profile.sex`.
- **Perfiles:** el sexo está en `state.profile.sex` (`getSex()`, `isFemale()`); objetivo, semana, desayuno y batido en `state.v54` (`profV()`, limpiado por `cleanV54()` en `migrate()`). Lo de mujer va en `OPT_FEMALE`, `NEW_PROFILE_MICRO` y `femaleWhy()`, siempre con fuente. El asistente es `wizOpen({mode})` + `wizHTML()` + `wizCommit()`; repinta con `wizPaint()` sin mover la ventana. Para guardar el perfil usa `state.profile={...state.profile,...cambios}` (nunca sustituyas el objeto entero: se perdería el sexo).
- **Clics:** registra manejadores con `onClick(fn)` y atributos `data-*`; nada de `onclick="..."` en el HTML ni `alert()` (usa `toast()`).
- **Ventanas:** usa `modal(título, html)`. No toques `history` por tu cuenta.
- **Estilos:** reutiliza las variables de `:root`. Para estilos nuevos, añade un bloque al final del `<style>` con un comentario `/* vNN: qué es */` usando BUSCAR `</style><!--FIN-CSS-->` y poniendo tu CSS delante (esa línea existe también en el archivo ligero).
- **Reutiliza las piezas que ya existen:** `ratioInfo()`/`ratioFixes()` (equilibrios con porqué y cómo), `dayCard(fecha)` (ficha de un día), `monthStats()`/`sparkline()` (tendencias), `macroTone(%)` (colores), `aggregate()`/`weekSummary()` (semana).
- **IA:** llama siempre a `requestAI()` (vale para Gemini, ChatGPT, Claude, OpenRouter y compatibles). No cambies `callGemini()`, `callChat()`, `AI_PROVIDERS`, el modelo ni el formato `BIOPEAT:` sin que la tarea lo pida. Nunca pongas claves en el código ni textos que digan que solo vale Gemini.
- **Gimnasio:** las columnas que se reconocen están en `MAP` (alias por orden de prioridad) y las apps en `GYM_APPS`. Para soportar otra app, añade sus cabeceras ahí; no escribas otro importador.
- **Sugerencias:** se envían al formulario de Google con `sendFeedback()` (`FORM_URL`, `FORM_FIELDS`). No cambies esos códigos.
- **Contenido Peat:** no inventes cifras atribuidas a Peat; nada de tono médico ni juzgón.
- **Zonas ideales de micronutrientes:** solo existen en la tabla `OPT` (`kind`, `lo`, `hi`, `src`, `ref`) y se leen con `optInfo()`/`optState()`/`optLine()`. No crees listas de bandas, límites o notas en otro sitio, ni compares a mano con `LIMIT`. Cada cifra nueva lleva su fuente (`src`) y su texto `ref`; si no hay fuente, `kind:'min'` con la meta del usuario.

## 4. Estilo de la interfaz (para que todo se entienda igual)
- **Cada bloque responde a una pregunta** en lenguaje normal («¿Cómo voy?», «¿Qué me falta?») con una línea gris debajo que explica qué se ve.
- **Colores siempre con el mismo significado:** verde = en tu rango o bien · ámbar = por debajo o mejorable · violeta = por encima · gris = sin datos. Borde discontinuo = día sin marcar completo.
- **Primero el dato y una frase sencilla**; los detalles, al tocar (ventana) o plegados en `<details>`.
- Si algo está mal, di **por qué importa** (1-2 frases Peat) y **cómo corregirlo** con alimentos y cantidades concretas, con botón para añadirlo.
- Nada de avisos médicos, confirmaciones de seguridad ni textos largos visibles por defecto.
- Móvil primero: probar con 400 px de ancho; botones de al menos 44 px de alto.

## 5. En cada cambio (obligatorio)
1. **Versión:** sube `APP_VERSION` exactamente una unidad (`'v37'` → `'v38'`).
2. **Registro de cambios del script:** en el comentario inicial de `<script id="app">`, añade arriba una línea `   vNN · Gemini · resumen` (o `Claude`), con 3 espacios delante.
3. **Datos:** nunca cambies `STORE`, `migrate()`, `render()`, `storableState()` ni las claves guardadas. Si cambias la forma de los datos: `upgradeToNN(s,o)` + llamada en `migrate()` + sube `APP_REVISION`.
4. **Respuesta:** «Qué voy a cambiar» (2-5 viñetas) → bloques `@@@` → «Cómo probarlo en el móvil» (1-3 pasos) → «Copia el bloque de código y pégalo en actualizar.html (Paso 2).» Los bloques `@@@` van dentro de **un único bloque de código** para que al copiar no se estropee nada.

## 6. Tamaño de cada respuesta (Gemini corta las respuestas largas)
- Como máximo **10 bloques y unas 200 líneas** por respuesta. En BUSCAR, fragmentos cortos (80-120 caracteres).
- Si el cambio es más grande, **divídelo en partes**. Termina cada una con «PARTE 1 de N. Aplícala, pulsa "Aplicar la siguiente parte encima" y escríbeme SIGUIENTE». Solo la parte 1 sube `APP_VERSION` y añade la línea del Registro (que describe el cambio entero). Las demás no tocan la versión.
- Nada de explicaciones largas: 2-5 viñetas, los bloques y cómo probarlo.

## 7. App pública (desde v56)
- La usa cualquiera. **Nunca pongas datos de Diego en el código** (pauta, desayuno, plan de macros, nombres de días, contexto). `defaults()` es un usuario genérico; el asistente lo configura. Lo de Diego vive solo en sus datos guardados y en CONTEXTO_BIOPEAT.md.
- **Más** (`HUB`) y el **menú lateral** no repiten funciones: Más = secciones de uso diario; menú = perfiles, informe, sugerencias y el chat de IA fijo abajo.
- **Comparar nutrientes:** `REF_TABLE` (UE y EE. UU. por sexo) y `refMode`; nunca cambian las metas del usuario.
- Sugerencias de suplementos: solo en `SUPP_CATALOG` (`g:'peat'` o `g:'comun'`, con su «por qué»; si Peat lo desaconsejaba, dilo). «Lo básico de Peat»: `PEAT_BASIC`, `PEAT_BREAKFAST`, `PEAT_SHAKE`. No son recomendaciones médicas.
- Textos para cualquier persona: tú/usted genérico, sin «tu pauta de K2» ni cifras de Diego.
- Una mano: las ventanas son hojas inferiores en el móvil; los accesos nuevos van al centro **Más** (`HUB`) y no a la parte de arriba de la pantalla. Botones de al menos 44 px.
- Iconos: usa `ico(nombre)` (tabla `ICON`, iconos de línea). No uses emojis como iconos principales.
- La guía de uso es `TOUR` (`showTour(i)`). Si añades una función importante, añade una línea a la guía.

