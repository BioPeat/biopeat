# AGENTS.md · Reglas para Jules (y cualquier agente que toque este repositorio)

Este es el **único** archivo de instrucciones para agentes. No crees otros (`agents.md`, `.jules/`, `plan.md`, notas…).
Escribe siempre en **español de España**, claro y corto. Diego no programa: nunca le pidas que edite código a mano.

## 0. MODO AUTÓNOMO (lo más importante)
Diego solo te da el mensaje inicial. **No vuelve a escribirte.** Por eso:
- **No pidas aprobación ni confirmación** de nada: ni del plan, ni de decisiones, ni de pasos intermedios. Presenta el plan y empieza a ejecutarlo directamente.
- **No hagas preguntas.** Si algo es ambiguo, elige la opción más sencilla que cumpla el objetivo y explícalo en «Pendiente o dudas» del Pull Request.
- **No te pares a mitad.** Trabaja hasta el final: código → pruebas en verde → documentos → **Pull Request abierto**. Una tarea sin Pull Request es una tarea fallida.
- Si una comprobación falla por tu cambio, arréglalo tú y vuelve a ejecutar la prueba (repite hasta `TODO OK`).
- Si de verdad es imposible terminar una parte, termina el resto, deja esa parte sin tocar y abre igualmente el Pull Request con el título empezando por `[PARCIAL]` y la explicación en «Pendiente o dudas».
- Si la tarea trae varias peticiones numeradas, haz **todas** en el mismo Pull Request.

## 1. Antes de empezar
1. Lee `CONTEXTO_BIOPEAT.md` (qué quiere Diego) y `MAPA_DEL_CODIGO.md` (dónde está cada cosa). Busca en el código **por nombre**, no por número de línea.
2. Prepara el entorno de pruebas (una vez por sesión):
   `pip install playwright && python -m playwright install --with-deps chromium`
3. Ejecuta `python tests/smoke.py`. Si ya falla antes de tocar nada, sigue con la tarea y avísalo en el Pull Request.

## 2. Archivos permitidos (no puede haber ninguno más)
`index.html`, `manifest.json`, `sw.js`, `icon-192.png`, `icon-512.png`, `icon-maskable-512.png`, `AGENTS.md`, `CONTEXTO_BIOPEAT.md`, `MAPA_DEL_CODIGO.md`, `README.md`, `.gitignore`, `tests/smoke.py`, `tests/datos_prueba.json`, `tools/mapa.py`, `.github/workflows/check.yml`.
- **Prohibido subir** scripts temporales (`fix_*.py`, `patch-*.js`, `check-*.js`, `extracted.js`…), copias de datos de Diego o planes. Si necesitas un script auxiliar, créalo en `/tmp`. No uses `git add -f`.
- La prueba falla si hay archivos de más.

## 3. Cómo editar
- Edita `index.html` **directamente** con tu herramienta de edición. Si usas un script de «buscar y reemplazar», comprueba que el texto aparecía **exactamente una vez** y que el cambio se aplicó.
- Cambios centrados en la tarea. No reescribas ni «limpies» partes que no te han pedido.
- Cada función se define **una sola vez**. Si cambias una función, sustitúyela; no la dupliques ni la «envuelvas».

## 4. Reglas del código (su incumplimiento rompió v30-v32)
- **Metas del día:** usa siempre `targetFor(fecha)`, `dayGoal()` o `goalsFor(fecha)`. **Nunca** guardes metas calculadas dentro de `state.days[fecha]`. El único ajuste por día permitido es `state.days[fecha].macroGoals = {p, f, kcal?}`.
- **Cambiar datos:** solo dentro de `change(() => { ... }, 'mensaje')`. No llames a `save()` ni a `render()` tras un `change`.
- **Migraciones de datos guardados:** crea `upgradeToNN(s, o)` que empiece con `if((Number(o.appRevision)||0) >= NN) return;`, llámala en `migrate()` y sube `APP_REVISION` a NN. Nunca hagas cambios de datos que se repitan en cada arranque.
- **Claves guardadas que no se renombran:** `biopeat_pro_v10`, compare17, workouts18, favorites22, microTargets17, goalOrigin17, ratioGoals17, macroGoals, targetMode.
- **Clics:** registra manejadores con `onClick(fn)` y atributos `data-*`; nada de `onclick="..."` en el HTML ni `alert()` (usa `toast()`).
- **Ventanas:** usa `modal(título, html)`. No toques `history` por tu cuenta.
- **Estilos:** reutiliza las variables de `:root`. Para estilos nuevos, añade un bloque al final del `<style>` con un comentario `/* vNN: qué es */`.
- **Reutiliza las piezas que ya existen:** `ratioInfo()`/`ratioFixes()` (equilibrios con porqué y cómo), `dayCard(fecha)` (ficha de un día), `monthStats()`/`sparkline()` (tendencias), `macroTone(%)` (colores), `aggregate()`/`weekSummary()` (semana).
- **IA:** no cambies la conexión, el modelo ni el formato `BIOPEAT:` sin que la tarea lo pida. Nunca pongas claves en el código.
- **Contenido Peat:** no inventes cifras atribuidas a Peat; nada de tono médico ni juzgón.

## 5. Estilo de la interfaz (para que todo se entienda igual)
- **Cada bloque responde a una pregunta** en lenguaje normal («¿Cómo voy?», «¿Qué me falta?») con una línea gris debajo que explica qué se ve.
- **Colores siempre con el mismo significado:** verde = en tu rango o bien · ámbar = por debajo o mejorable · violeta = por encima · gris = sin datos. Borde discontinuo = día sin marcar completo.
- **Primero el dato y una frase sencilla**; los detalles, al tocar (ventana) o plegados en `<details>`.
- Si algo está mal, di **por qué importa** (1-2 frases Peat) y **cómo corregirlo** con alimentos y cantidades concretas, con botón para añadirlo.
- Nada de avisos médicos, confirmaciones de seguridad ni textos largos visibles por defecto.
- Móvil primero: probar con 400 px de ancho; botones de al menos 44 px de alto.

## 6. Al terminar (obligatorio, en este orden)
1. **Versión:** sube `APP_VERSION` en una unidad (`'v34'` → `'v35'`). Una versión por Pull Request.
2. **Registro de cambios del script:** en el comentario inicial de `<script id="app">`, añade arriba una línea `vNN · Jules · resumen`. Máximo 6 líneas: borra la más antigua.
3. **`CONTEXTO_BIOPEAT.md`:** cambia «Versión actual» y **sustituye** el texto de los apartados afectados (normalmente el 6). En el apartado 10 añade una línea arriba y deja como máximo 8. **No añadas apartados nuevos ni bloques al final.**
4. **Mapa:** ejecuta `python tools/mapa.py` (no edites `MAPA_DEL_CODIGO.md` a mano).
5. **Prueba:** si añades o cambias algo visible, añade una comprobación en `tests/smoke.py` (secciones 5, 5b o 6). No debilites ni borres comprobaciones para que pase; si una ya no tiene sentido porque la tarea cambia ese comportamiento, sustitúyela por otra equivalente y explícalo.
6. Ejecuta `python tests/smoke.py` → debe decir `TODO OK`.
7. **Abre el Pull Request** (publica la rama y crea el PR) sin esperar a nadie.

## 7. Descripción del Pull Request (copia este formato)
```
## Qué cambia (para Diego, en 1-3 frases sencillas)
...
## Cómo probarlo en el móvil
1. ...
## Prueba automática
TODO OK (python tests/smoke.py)
## RESUMEN PARA GEMINI
Versión: vNN → vNN+1
Hecho: ...
Funciones/ID tocados: ...
Pendiente o dudas: ... (o «nada»)
```
