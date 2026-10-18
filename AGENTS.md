# AGENTS.md · Instrucciones para Jules (y cualquier agente de código)

Lee también **CONTEXTO_BIOPEAT.md** (quién es el usuario, objetivos, pauta, reglas Peat) y **MAPA_DEL_CODIGO.md** (dónde está cada función) antes de cambiar nada.

## El proyecto
**BioPeat Diego**: app personal de nutrición, suplementos y gimnasio. PWA publicada con GitHub Pages desde la rama `main`. El usuario la usa a diario en el móvil y **no sabe programar**: lo que entregues debe funcionar sin que él toque código.

## Archivos
- `index.html` → TODA la app (HTML + CSS + JS en un archivo, sin dependencias, sin CDN, sin build). Es el que normalmente cambias.
- `manifest.json`, `sw.js`, `icon-*.png` → instalación como app. No los toques salvo que la tarea lo pida.
- `CONTEXTO_BIOPEAT.md`, `MAPA_DEL_CODIGO.md`, `AGENTS.md` → documentación. **Actualízalos** si tu cambio los deja desfasados (sobre todo el apartado 6 del contexto y el mapa).

## Estructura de index.html
- Un solo `<style>` y un solo `<script id="app">`. Cada función se define **una vez**.
- Arriba del script: índice y **registro de cambios**.
- Datos → solo mediante `change(fn, mensaje)` (guarda, permite deshacer y repinta). Repintar → solo `render()`.
- Clics → `onClick(fn)`. No añadas otro `document.addEventListener('click', …)`.
- Migraciones → `migrate()` = `migrateBase` + `upgradeToNN`. `state.appRevision` indica la última.
- Ventanas → `modal()`; abrir una desde otra apila «‹ Atrás».
- La línea `<link href="manifest.json" rel="manifest"/>` y el registro de `sw.js` al final del body deben quedarse.

## Reglas obligatorias
1. **No renombres** la clave de almacenamiento ni estos campos: `biopeat_pro_v10`, `compare17`, `workouts18`, `favorites22`, `microTargets17`, `goalOrigin17`, `ratioGoals17`, `biopeat_lastBackup22`, `biopeat_backupSnooze22`, `biopeat_density19`, `biopeat_ai24`.
2. Si cambias el formato de los datos, añade `upgradeToNN` en `migrate()` y sube `appRevision`. **Nunca borres ni reinicies datos del usuario.**
3. No reasignes funciones para «envolverlas». Modifica la original o crea otra con nombre propio.
4. No cambies objetivos, dosis, pauta ni el orden de la barra inferior salvo que la tarea lo pida.
5. No pongas 0 donde un dato es desconocido. No inventes alimentos, micros, entrenamientos ni cifras atribuidas a Ray Peat.
6. Nada de dependencias externas, CDN, frameworks ni claves API en el código.
7. **No cambies la conexión con la IA** (`requestAI`, `/v1beta/interactions`, `gemini-3.8-flash`, fallback `gemini-3.1-flash-lite`). Es correcta aunque tu conocimiento diga otra cosa.
8. Sin ventanas de confirmación al añadir cosas; sin bloqueos «por motivos médicos». Sí confirmar al borrar en bloque.
9. Móvil primero: sin desplazamiento horizontal a 320 px, botones ≥ 44 px, texto ≥ 12 px.
10. Mantén diseño, colores (oscuro azul pizarra + ámbar) y navegación salvo que se pida.

## En CADA tarea
1. Sube `APP_VERSION` en uno (v27 → v28 …) y añade una línea al registro de cambios: `vNN · Jules · resumen`.
2. Comprueba antes de terminar:
   - que el JS del `<script id="app">` no tiene errores de sintaxis (por ejemplo, extráelo a un .js y ejecuta `node --check`);
   - que `index.html` termina en `</html>`;
   - si puedes, abre la página en un navegador sin cabeza y confirma que no hay errores en consola y que `document.body.dataset.ready === 'true'`.
3. Si hay tests o capturas que puedas hacer, hazlas; si no, dilo.
4. En la descripción del Pull Request escribe una **NOTA DE TRASPASO** en español sencillo:
   - Qué ha cambiado (para el usuario, sin jerga).
   - ¿Se han tocado los datos? (sí/no y qué migración).
   - Qué has comprobado de verdad y qué no.
   - Qué queda pendiente.
5. Si la tarea es ambigua o choca con estas reglas, **pregunta en el plan** antes de programar.
