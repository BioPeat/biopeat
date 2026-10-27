# BioPeat

App de nutrición gratuita con enfoque Ray Peat / Georgi Dinkov, en un solo archivo (`index.html`), publicada con GitHub Pages e instalable en el móvil. Cualquiera puede usarla: la primera vez un asistente la configura y una guía explica cómo se usa.

- **Datos:** viven solo en el móvil de cada usuario (sin cuenta ni servidor). Nunca se suben aquí.
- **Actualizaciones:** al publicar un `index.html` nuevo, a todos los usuarios les sale «Hay una versión nueva».
- **Sugerencias de usuarios:** llegan solas a una hoja de Google (formulario). Se revisan en `actualizar.html` → Buzón de sugerencias.
- **IA:** cada usuario conecta la suya (Gemini gratis, ChatGPT, Claude, OpenRouter u otra compatible). **Gimnasio:** vale el CSV de cualquier app.
- **Qué es la app y cómo se programa:** `CONTEXTO_BIOPEAT.md` y `AGENTS.md` (reglas para la IA que programa).
- **Dónde está cada cosa en el código:** `MAPA_DEL_CODIGO.md` (lo regenera GitHub solo).
- **Aplicar y comprobar cambios:** `actualizar.html` en la web de la app.
- **Prueba completa:** `python tests/smoke.py` (la ejecuta GitHub en cada subida).
