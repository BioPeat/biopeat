---
name: revisar-sugerencias
description: Consulta, analiza y gestiona las sugerencias reales de usuarios guardadas en Cloudflare D1 (biopeat-db) y actualiza su estado tras la decisión del creador.
---

# Revisar sugerencias de BioPeat (Cloudflare D1)

Cuando Diego pregunte por las sugerencias o mejoras enviadas por los usuarios de BioPeat:

1. **Consultar `biopeat-db` vía MCP `cloudflare_cloudflare`** (`execute` sobre `account_id = "a38b0dc7b72539c49cf44f2617ef396f"` y `database_id` de `cloudflare/config.json`):
   ```sql
   SELECT id, created_at, category, title, body, app_version, lang, view_name, device, origin, status, ai_notes
   FROM feedback
   ORDER BY CASE WHEN status='new' THEN 0 WHEN status='triaged' THEN 1 WHEN status='accepted' THEN 2 ELSE 3 END, id DESC
   LIMIT 100;
   ```
   También puedes consultar estadísticas rápidas si aporta contexto:
   ```sql
   SELECT status, COUNT(*) AS n FROM feedback GROUP BY status;
   ```

2. **Analizar cada sugerencia pendiente (`new` / `triaged`)**:
   - Evaluar utilidad real para usuarios internacionales de BioPeat.
   - Evaluar esfuerzo y riesgo técnico en `index.html` (reglas de `AGENTS.md`: single-script, claves protegidas, coste 0 €).
   - Evaluar encaje con la filosofía Ray Peat / Georgi Dinkov (sin medicalizar ni inventar cifras).
   - Detectar duplicados o spam.

3. **Presentar a Diego un resumen claro en español de España**:
   - Agrupar en: **Recomendadas para aplicar**, **Opcionales / a valorar** y **Descartables / spam** (con ID, título, resumen, motivo y esfuerzo).
   - Preguntar cuáles quiere aplicar o descartar.

4. **Tras su confirmación**:
   - Aplicar en el código las aceptadas, verificar con `tools/security_check.py` y `tests/smoke.py`.
   - Actualizar `status` (`accepted`, `done` o `rejected`) y `ai_notes` en D1 usando queries SQL parametrizadas vía `cloudflare_cloudflare:execute`.
