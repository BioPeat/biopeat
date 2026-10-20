# AGENTS.md · Reglas para Jules (y cualquier agente que toque este repositorio)

Este es el **único** archivo de instrucciones para agentes. No crees otros (`agents.md`, `.jules/`, `plan.md`, notas…).
Escribe siempre en **español de España**, claro y corto. Diego no programa: nunca le pidas que edite código a mano.

## 0. Antes de empezar
1. Lee `CONTEXTO_BIOPEAT.md` (qué quiere Diego) y `MAPA_DEL_CODIGO.md` (dónde está cada cosa). Busca en el código **por nombre**, no por número de línea.
2. Prepara el entorno de pruebas (una vez por sesión):
   `pip install playwright && python -m playwright install --with-deps chromium`
3. Ejecuta `python tests/smoke.py`. Debe terminar en `TODO OK` **antes** de cambiar nada. Si no, avisa en el Pull Request.

## 1. Archivos permitidos (no puede haber ninguno más)
`index.html`, `manifest.json`, `sw.js`, `icon-192.png`, `icon-512.png`, `icon-maskable-512.png`, `AGENTS.md`, `CONTEXTO_BIOPEAT.md`, `MAPA_DEL_CODIGO.md`, `README.md`, `.gitignore`, `tests/smoke.py`, `tests/datos_prueba.json`, `tools/mapa.py`, `.github/workflows/check.yml`.

- **Prohibido subir** scripts temporales (`fix_*.py`, `patch-*.js`, `check-*.js`, `extracted.js`…), copias de datos de Diego (`*.json` con sus registros) o planes. Si necesitas un script auxiliar, créalo fuera del repositorio (por ejemplo en `/tmp`). `.gitignore` ya los ignora; no uses `git add -f`.
- La prueba falla si hay archivos de más.

## 2. Cómo editar
- Edita `index.html` **directamente** con tu herramienta de edición. No uses scripts de «buscar y reemplazar» que fallan en silencio. Si aun así usas uno, comprueba que el texto aparecía **exactamente una vez** y que el cambio se aplicó.
- Cambios pequeños y centrados en la tarea. No reescribas ni «limpies» partes que no te han pedido.
- Cada función se define **una sola vez**. Si cambias una función, sustitúyela; no la dupliques ni la «envuelvas» reasignándola.

## 3. Reglas del código (importantes: su incumplimiento rompió v30-v32)
- **Metas del día:** usa siempre `targetFor(fecha)`, `dayGoal()` o `goalsFor(fecha)`. **Nunca** guardes metas calculadas dentro de `state.days[fecha]`. El único ajuste por día permitido es `state.days[fecha].macroGoals = {p, f, kcal?}`.
- **Cambiar datos:** solo dentro de `change(() => { ... }, 'mensaje')`. No llames a `save()` ni a `render()` por tu cuenta tras un `change`.
- **Migraciones de datos guardados:** crea `upgradeToNN(s, o)` que empiece con `if((Number(o.appRevision)||0) >= NN) return;`, llámala en `migrate()` y sube `APP_REVISION` a NN. Nunca hagas cambios de datos que se repitan en cada arranque.
- **Claves guardadas que no se renombran:** `biopeat_pro_v10`, compare17, workouts18, favorites22, microTargets17, goalOrigin17, ratioGoals17, macroGoals, targetMode.
- **Clics:** registra manejadores con `onClick(fn)` o atributos `data-*`; no uses `onclick="..."` en el HTML ni `alert()` (usa `toast()`).
- **Ventanas:** usa `modal(título, html)`. No toques `history` por tu cuenta.
- **Estilos:** reutiliza las variables de `:root` (`--bg-card`, `--text-muted`…). Para estilos nuevos, añade un bloque al final del `<style>` con un comentario `/* vNN: qué es */`.
- **IA:** no cambies la conexión, el modelo ni el formato `BIOPEAT:` sin que la tarea lo pida. Nunca pongas claves en el código.
- **Contenido Peat:** no inventes cifras atribuidas a Peat; nada de tono médico ni juzgón.

## 4. Al terminar (obligatorio, en este orden)
1. **Versión:** sube `APP_VERSION` en una unidad (`'v33'` → `'v34'`). Una versión por Pull Request.
2. **Registro de cambios del script:** en el comentario inicial de `<script id="app">`, añade arriba una línea `vNN · Jules · resumen`. Máximo 6 líneas: borra la más antigua.
3. **`CONTEXTO_BIOPEAT.md`:** cambia «Versión actual» y **sustituye** el texto de los apartados afectados (normalmente el 6). En el apartado 10 añade una línea arriba y deja como máximo 8. **No añadas apartados nuevos ni bloques al final.**
4. **Mapa:** ejecuta `python tools/mapa.py` (no edites `MAPA_DEL_CODIGO.md` a mano).
5. **Prueba:** si añades una función visible, añade una comprobación en `tests/smoke.py` (sección 5 o 6). No debilites ni borres comprobaciones para que pase; si una comprobación está mal, explícalo.
6. Ejecuta `python tests/smoke.py` → debe decir `TODO OK`. **No abras el Pull Request si falla.**

## 5. Descripción del Pull Request (copia este formato)
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

## 6. Si la tarea no está clara
Haz lo más sencillo que cumpla el objetivo y explica tu decisión en «Pendiente o dudas». Solo pregunta si de verdad no puedes avanzar.
