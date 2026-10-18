# AGENTS.md · Instrucciones para Jules (y cualquier agente de código)

## ⚡ VELOCIDAD: MODO RÁPIDO POR DEFECTO
El usuario quiere cambios rápidos. Salvo que la tarea diga «MODO COMPLETO»:
- **No instales nada** (ni npm, ni Playwright, ni navegadores, ni dependencias). No crees archivos de tests.
- **No abras la app en un navegador sin cabeza** ni hagas capturas.
- Lee solo lo necesario: `MAPA_DEL_CODIGO.md` para localizar la función y después esa zona de `index.html` (búscala por nombre). No leas el archivo entero si no hace falta.
- Haz el cambio mínimo que cumpla la tarea. Plan corto (3-5 pasos).
- Única comprobación obligatoria (tarda segundos):
  `python3 -c "import re;s=open('index.html',encoding='utf-8').read();open('/tmp/a.js','w',encoding='utf-8').write(re.search(r'<script id=\"app\">([\s\S]*?)</script>',s).group(1));assert s.rstrip().endswith('</html>')" && node --check /tmp/a.js`
- Si un paso se atasca más de 2 minutos, abandónalo, termina con lo que tengas y explícalo en la nota.
- Las tareas de **solo análisis** se responden en el chat, sin plan largo, sin ejecutar nada y sin Pull Request.

Solo con «MODO COMPLETO» en la tarea: además abre la página con un navegador sin cabeza, comprueba que no hay errores en consola y que `document.body.dataset.ready === 'true'`, y prueba a 320 px.

## El proyecto
**BioPeat Diego**: app personal de nutrición, suplementos y gimnasio. PWA publicada con GitHub Pages desde `main`. El usuario la usa en el móvil y **no sabe programar**. Contexto completo en `CONTEXTO_BIOPEAT.md`; índice de funciones en `MAPA_DEL_CODIGO.md`.

## Archivos
- `index.html` → TODA la app (HTML + CSS + JS, sin dependencias ni build). Es el que normalmente cambias.
- `manifest.json`, `sw.js`, `icon-*.png` → instalación como app. No los toques salvo que se pida.
- `CONTEXTO_BIOPEAT.md`, `MAPA_DEL_CODIGO.md` → actualízalos solo si tu cambio añade, quita o renombra funciones o secciones.

## Estructura de index.html
- Un solo `<style>` y un solo `<script id="app">`. Cada función se define una vez.
- Datos → solo con `change(fn, mensaje)`. Repintar → solo `render()`. Clics → `onClick(fn)`.
- Migraciones → `migrate()` = `migrateBase` + `upgradeToNN` (sube `state.appRevision`).
- Ventanas → `modal()`. Texto variable en HTML → siempre con `esc()`.
- No quites `<link href="manifest.json" rel="manifest"/>` ni el registro de `sw.js` del final.

## Reglas obligatorias
1. No renombres: `biopeat_pro_v10`, `compare17`, `workouts18`, `favorites22`, `microTargets17`, `goalOrigin17`, `ratioGoals17`, `biopeat_lastBackup22`, `biopeat_backupSnooze22`, `biopeat_density19`, `biopeat_ai24`.
2. Si cambias el formato de datos, añade `upgradeToNN`. Nunca borres ni reinicies datos.
3. No reasignes funciones para «envolverlas».
4. No cambies objetivos, dosis, pauta ni el orden de la barra inferior salvo que se pida.
5. No pongas 0 en datos desconocidos ni inventes cifras atribuidas a Ray Peat.
6. Nada de dependencias, CDN ni claves API en el código.
7. No cambies la conexión con la IA (`requestAI`, `/v1beta/interactions`, `gemini-3.8-flash`, fallback `gemini-3.1-flash-lite`), ni el guardado opcional de la clave en localStorage: son intencionados.
8. Sin confirmaciones al añadir ni bloqueos «médicos».
9. Móvil primero: sin desplazamiento horizontal a 320 px, botones ≥ 44 px.
10. Mantén diseño, colores y navegación salvo que se pida.

## Al terminar cada tarea con cambios
1. Sube `APP_VERSION` en uno y añade al registro de cambios: `vNN · Jules · resumen`.
2. Ejecuta la comprobación rápida de arriba.
3. Descripción del Pull Request = **NOTA DE TRASPASO** breve en español: qué cambia para el usuario · ¿datos tocados? · qué has comprobado · pendiente.
