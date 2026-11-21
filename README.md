# BioPeat

App de nutrición bioenergética gratuita con enfoque Ray Peat / Georgi Dinkov, en un solo archivo (`index.html`), publicada con GitHub Pages e instalable como PWA en Android, iPhone y ordenador.

- **Web de presentación:** [inicio.html](inicio.html) (qué es, mockup interactivo de 4 pestañas, instalación inteligente por dispositivo, privacidad RGPD y aviso legal, en español e inglés).
- **Idiomas:** español e inglés (`I18N_EN` y parser bilingüe `parseSmart` ES/EN + Open Food Facts + escáner de códigos de barras con cámara).
- **Privacidad y respaldo cifrado E2EE:** los datos se guardan localmente (`localStorage` + espejo automático en `IndexedDB`) y se cifran en el propio dispositivo con **AES-256-GCM** antes de guardarse opcionalmente en nuestra bóveda zero-knowledge (`cloudflare/worker.js` + D1 UE), con recuperación mediante gestor de contraseñas o enlace secreto `#bp-sync=`. Nunca se suben claves de IA.
- **Sugerencias y estadísticas sin cookies:** llegan automáticamente a Cloudflare D1 mediante `/api/feedback` y `/api/ping`. Se gestionan en el panel privado `/admin` o con Antigravity usando `.agents/skills/revisar-sugerencias/SKILL.md` (y `actualizar.html` enlaza al panel).
- **Marcadores bioenergéticos (opcional):** temperatura, pulso y nivel de energía diarios en Hoy, integrados en el informe para IA y chat.
- **IA:** cada usuario conecta la suya opcionalmente (Gemini o Groq gratis, ChatGPT, Claude, OpenRouter u otra compatible). **Gimnasio:** importa CSV de Hevy, Strong, Fitbod, FitNotes o cualquier app.
- **Qué es la app y cómo se programa:** [CONTEXTO_BIOPEAT.md](CONTEXTO_BIOPEAT.md), [AGENTS.md](AGENTS.md) y [MAPA_DEL_CODIGO.md](MAPA_DEL_CODIGO.md) (lo regenera GitHub automáticamente).
- **Comprobación de seguridad y pruebas:**
  - `python tools/security_check.py` (CSP, `eval`, aislamiento de secretos/claves, SQL parametrizado en Worker).
  - `python tests/smoke.py` (ejecución completa en Chromium headless en cada subida y semanalmente).
