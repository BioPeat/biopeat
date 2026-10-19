1. **Modo: rápido** (No se modifican cálculos ni migraciones ni nada core, solo se añade un script `verify.js` de utilidad para el repositorio y se modifica el archivo de instrucciones `AGENTS.md` de acuerdo con el usuario, evitando abrir navegadores en las siguientes tareas).
2. Crear un archivo `verify.js` en la raíz del proyecto.
   - Leerá `index.html`.
   - Comprobará que termine con `</html>`.
   - Extraerá el contenido dentro de `<script id="app">`.
   - Utilizará el módulo `vm` de Node.js (`vm.Script`) para comprobar la sintaxis.
   - Creará un sandbox mínimo simulando `window`, `document`, `localStorage` y otros objetos globales necesarios para que no dé `ReferenceError`.
   - Ejecutará el script y llamará a funciones críticas como `init()` y `migrate()` simulando su ejecución inicial para asegurar que no haya errores inmediatos que den una pantalla blanca (debe completar todo en menos de 1 segundo).
3. Modificar `AGENTS.md`:
   - Cambiar la sección "En CADA tarea" o cómo el sistema valida el código, quitando la obligación de abrir el navegador sin cabeza ("headless browser") en el "Modo Completo".
   - En su lugar, ejecutar únicamente `node verify.js`.
   - Indicar explícitamente que NO se actualicen `CONTEXTO_BIOPEAT.md` ni `MAPA_DEL_CODIGO.md` a menos que la tarea lo pida explícitamente.
4. Pre-commit steps.
5. Hacer submit y push a `main`.
