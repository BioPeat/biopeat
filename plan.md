Modo: completo
Motivo: Modificaremos la presentación central de `renderSupps`, `renderMicrosForDay` y `renderWeekly`. También tocaremos lógica de UI sobre variables como PUFA, Hierro y los depósitos. Debemos garantizar que la vista Resumen funcione mediante clases CSS (bp-compact).

1.  **Vista Resumen vs Vista Explicaciones (CSS & UI)**
    *   I will use `replace_with_git_merge_diff` to modify `index.html`. It will replace `function applyDensity()` to handle `#bp-density, #bp-density-today` toggles.
    *   It will modify `renderToday` to inject the toggle HTML element:
        ```html
        <div class="bp-density-toggle" style="margin-bottom:8px;text-align:right;">
          <button id="bp-density-today" class="btn small ghost" onclick="compactView=!compactView;applyDensity();prefs.set('biopeat_density19',compactView?'compact':'comfortable');toast(compactView?'Modo resumen: solo datos y gráficos.':'Explicaciones visibles de nuevo.');"></button>
        </div>
        ```
    *   It will modify `renderRatios` to inject `<p class="ratio-explanation" style="display:none;...>` which will be shown via CSS in detailed mode (not `bp-compact`).
    *   I will verify with `run_in_bash_session` running `grep -n "bp-density-today" index.html`.

2.  **Modificar `renderSupps` ("Tu pauta")**
    *   I will use `replace_with_git_merge_diff` on `index.html` to rewrite `renderSupps()`. The new body will categorize `entries` (where `kind !== 'food'`) by `slot` (Desayuno, Comida, Merienda, Antes de dormir).
    *   It will construct HTML with an `h3` for each slot, a checkbox for each item (using `e.confirmed`), and a `<button class="btn btn-emerald" onclick="confirmAllSupps()">Confirmar las previstas de hoy</button>` at the end.
    *   I will write the implementation of `confirmAllSupps()` via `replace_with_git_merge_diff`.
    *   I will verify using `run_in_bash_session` `sed -n '/function renderSupps/,/^}/p' index.html`.

3.  **Modificar `renderMicrosForDay` ("Tus nutrientes")**
    *   I will use `replace_with_git_merge_diff` on `index.html` to rewrite `renderMicrosForDay()`.
    *   I will implement logic inside it to split `MICRO` into: `Escudo` (PUFA, fe), `Tanques` (vitA, vitD, vitE, b12, b9, se, i, cu), and `Diarios` (the rest).
    *   I will generate specific HTML blocks for each section (`<h3>🛡️ Escudo Peat...`).
    *   I will verify using `run_in_bash_session` `sed -n '/function renderMicrosForDay/,/^}/p' index.html`.

4.  **Modificar `renderWeekly` ("Tu semana")**
    *   I will use `replace_with_git_merge_diff` on `index.html` to modify `renderWeekTable(s)`.
    *   I will change:
        `$('week-table').innerHTML='<table><caption>Totales...';`
        to:
        `$('week-table').innerHTML='<details><summary>Ver tabla detallada de los 25 nutrientes por día</summary><table><caption>Totales...</table></details>';`
    *   I will verify using `run_in_bash_session` `grep -A 5 "function renderWeekTable" index.html`.

5.  **Actualizar documentos y verificar tests**
    *   I will use `replace_with_git_merge_diff` to add specific sentences to `CONTEXTO_BIOPEAT.md` and `MAPA_DEL_CODIGO.md` explaining the 3-block micros layout and the grouped supps.
    *   I will use `replace_with_git_merge_diff` to update `index.html` setting `const APP_VERSION = 'v32';` and prepending a `<p><b>v32:</b> Diferenciación clara de pauta y nutrientes...</p>` to the changelog.
    *   I will verify using `run_in_bash_session` `grep "v32" index.html`.
    *   I will run `node verify.js` and verify it passes.

6.  **Pre-commit steps**
    *   Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.

7.  **Submit the change**
    *   Use the submit tool to push the changes.

