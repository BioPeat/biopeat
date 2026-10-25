# CONTEXTO · BioPeat Diego

**Versión actual: v50** (revisión de datos 23)

Documento maestro. Lo lee la IA que programa BioPeat (Gemini «BioPeat Dev» o Claude). Los cambios se entregan en bloques `@@@` y los aplica y prueba `actualizar.html`. **Se actualiza sustituyendo el texto de cada apartado, nunca añadiendo apartados nuevos al final.** Si algo de aquí contradice al código, manda el código; avisa de la diferencia.

## 1. Diego y cómo quiere la app
- 23 años, hombre, 185 cm, ~77,5 kg (editable). Madrid. Escribe rápido y con faltas: entiéndelo por el sentido.
- Trabaja en finanzas y entrena a dos equipos de baloncesto.
- Pesas full body **lunes, miércoles y sábado**; partido el **domingo**; martes, jueves y viernes sin pesas.
- Registra el gimnasio en **HEVY gratis** (sin API): exporta un CSV y lo importa en la app.
- Enfoque **Ray Peat / Georgi Dinkov**, pero la app **no debe ser juzgona ni rígida**: datos claros y sugerencias, sin avisos médicos ni confirmaciones por motivos de salud. Sabe lo que hace con su suplementación y aspirina.
- Gustos: móvil primero, muy visual, gráficos que se tocan, porcentajes que pasan del 100 %, pocas pantallas, añadir con un toque (se puede deshacer). No soporta que se diga «hecho» o «comprobado» si no lo está.

## 2. Metas del día
Se calculan siempre al vuelo con `targetFor(fecha)`. Orden de prioridad: ajuste manual de ese día → metas globales («todos los días» o «entreno/descanso») → plan por defecto.

| Día | Actividad | FAF | Proteína | Grasa | Aspirina |
|---|---|---|---|---|---|
| Lunes | Full body | 1,725 | 145 g | 75 g | 500 mg |
| Martes | Pista | 1,5 | 130 g | 65 g | 250 mg |
| Miércoles | Full body | 1,725 | 145 g | 75 g | 500 mg |
| Jueves | Pista + selenio | 1,5 | 130 g | 65 g | 250 mg |
| Viernes | Pista | 1,5 | 130 g | 65 g | 250 mg |
| Sábado | Full body | 1,65 | 145 g | 75 g | 500 mg |
| Domingo | Partido + selenio | 1,75 | 145 g | 75 g | 500 mg |

- Energía = TMB Mifflin-St Jeor (10×peso + 6,25×185 − 5×23 + 5) × FAF, redondeada a 5.
- Proteína y grasa del plan por defecto escalan con el peso (peso / 77,5).
- Hidratos = el resto de la energía, con un **mínimo de 3 g por g de proteína** (C:P ≥ 3). Si no cabe, sube la energía.
- Diego puede cambiar las metas en **Nutrientes → Editar objetivos** (todos los días, entreno/descanso o solo un día) y en **Ajustes → Editar objetivos de macros del día**. «Volver al plan Peat por defecto» lo restablece desde hoy.

## 3. Pauta de suplementos
Se suma sola cada día y cuenta como tomada. Si un día no se toma algo, Diego toca esa toma en «Tu pauta» y deja de contar (tocar otra vez la recupera). Se edita en «Tu pauta → Cambiar mi pauta habitual».

| Momento | Qué | Cantidad | Días |
|---|---|---|---|
| Desayuno | Vitamina D3 | 4.000 UI (100 µg) | todos |
| Desayuno | Vitamina A (retinol) | 10.000 UI (3.000 µg RAE) | todos (la quita a mano si come hígado) |
| Desayuno | K2 MK-4 | 0,5 mg | todos |
| Comida | Vitamina E | 200 UI (134 mg) | todos |
| Comida | Benfotiamina (B1) | 250 mg | todos |
| Comida | Glicina | 5 g | todos |
| Comida | Bisglicinato de magnesio HSN | 2 g de polvo (≈220 mg Mg) | todos |
| Comida | Selenio | 200 µg | jueves y domingo |
| Merienda | Creatina | 5 g | todos (la del batido no se duplica) |
| Merienda | K2 MK-4 | 0,5 mg | todos |
| Merienda | Aspirina, toda la del día | 500 mg L/X/S/D · 250 mg M/J/V | todos |
| Antes de dormir | Glicina | 5 g | todos |
| Antes de dormir | Bisglicinato de magnesio HSN | 2 g de polvo | todos |

La B1 se muestra aparte: mg de benfotiamina frente a su pauta; la tiamina de los alimentos va por separado.

## 4. Comidas habituales (un toque)
- **Desayuno:** 220 ml leche entera + 21 g Nesquik + 1 plátano (120 g) + 250 ml zumo de naranja.
- **Batido de merienda:** 200 ml leche + 150 ml zumo + 35 g azúcar + 1 plátano + whey 0-40 g (con un control deslizante que muestra el % de proteína del día).
- Durante el entreno o el partido: ositos Haribo con azúcar.

## 5. Reglas Peat / Dinkov de la app
- **PUFA ≤ 4 g/día** (es un máximo, no una meta). **Ca:P ≥ 1,20**. Calcio 2.000 mg. **Hierro ≤ 14 mg** (límite).
- **Zona ideal de cada micro: UNA sola tabla, `OPT`** (en `index.html`, junto a `DEPOSIT`). Cada entrada tiene `kind` (`min` llegar a la meta · `band` entre `lo` y `hi` · `max` tope · `ref` solo referencia), `src` (peat, din, foro, of, tuya) y `ref` (texto que se ve al tocar el nutriente). Helpers: `optInfo()`, `optState()`, `optLine()`. **No crees otras listas de bandas o límites.** Valores actuales: vitamina A banda 3.000-3.800 µg (Peat: 10.000 UI), vitamina D mín. 100 µg (4.000 UI), selenio banda 100-200 µg, yodo banda 150-225 µg, hierro máx. 14 mg, calcio mín. 2.000 mg (Peat/Dinkov 2.000-3.000), **fósforo solo referencia** (importa Ca:P) y sodio sin «te falta». PUFA máx. 4 g. A:D 2-4 : 1 y Zn:Cu ~10 : 1 son referencias de la app sin cifra verificada de Peat.
- **Depósitos (media de 7 días):** A, D, E, B12, folato, selenio, yodo, cobre y hierro. Los días sin registro cuentan 0 (la tarjeta dice «n/7 con registro»; «parcial» solo significa que a algún alimento le falta el dato). El día de hoy no cuenta hasta marcarlo completo: se mide con los 7 días cerrados hasta ayer y la tarjeta indica cuánto suma hoy. El resto son diarios.
- **Grasa saturada:** para la meta de grasa cuenta ×0,5 (`SAT_W`), por ser la grasa que mejor encaja con Peat (coco, mantequilla, lácteos); el PUFA es lo que se vigila. La energía (kcal) cuenta todo.
- Alimentos preferidos para sugerir: leche, queso, zumo de naranja, fruta madura, miel/azúcar, patata, arroz, huevos, marisco, gelatina, carne con caldo. Evitar aceites vegetales.
- **No inventes cifras atribuidas a Peat.** Donde no hay cifra suya, se usa la meta personal.

## 6. Qué hace la app (v37)
Una sola página. Barra inferior **Hoy · Registro · Añadir · Semana · Más** (no cambiar el orden) y botón redondo de **Gimnasio**.
- **Hoy:** energía, anillos de macros (% sin tope, «Te faltan X g»), recomendación del día + «Pedir sugerencia a la IA», **Equilibrio del día** (5 tarjetas: Ca:P, PUFA, hidratos:proteína, A:D, Zn:Cu; cada una con semáforo ✓/!, barra con zona verde y «Tú», y una frase sencilla; al tocarla: «¿Por qué importa?» (explicación Peat) y «Cómo llegar hoy» con alimentos y cantidades exactas que se añaden con un toque), comidas del día con «Igual que ayer», «Marcar día completo», «Vista Resumen».
- Al añadir la primera comida de un día, el día anterior se marca solo como completo (v35).
- **Añadir:** texto libre de varias comidas en un mensaje (sin IA si reconoce los alimentos), foto con IA, «Foto en Gemini» (copiar prompt + pegar respuesta `BIOPEAT:`), manual, rápidos/favoritos, desayuno, batido, suplemento extra, Mi despensa (lo que analiza la IA se guarda y se reutiliza).
- **Registro:** buscador, grupos por comida, − / + / ✎ / ×, deshacer, probar una ración, reparto de energía y tipos de grasa.
- **Tus nutrientes:** tres bloques (Escudo Peat: PUFA y hierro · Diarios · Tanques de 7 días), tarjetas o mapa, filtros.
- **Tu pauta:** las tomas de hoy por momento del día (se suman solas; tocar = no tomada hoy), «+ Toma extra», «Lo que te aporta tu pauta» (qué parte de cada meta cubren los suplementos frente a la comida) y el editor de la pauta habitual plegado.
- **Semana:** 4 preguntas numeradas: 1 ¿Cómo voy? (media diaria de los días con comidas frente a la meta, 4 anillos y una frase), 2 Día a día (7 barras de energía; tocar = ficha del día), 3 ¿Qué me falta? (resumen con 4 filtros: te faltan / te pasas / en zona / sin datos; cada hueco se abre al tocarlo y propone alimentos de tu despensa, con vasos o huevos si encajan, que se añaden a hoy con un toque; «Ver N más»; los 25 micros plegados), 4 ¿Voy mejorando? (8 semanas). Debajo, el **calendario**: selector Energía/Proteína/Hidratos/Grasa, media del mes, tendencia (últimos 7 días frente a los 7 anteriores), gráfico de línea del mes y cuadrícula con color por día (verde en rango, ámbar por debajo, violeta por encima, gris sin datos) y 3 barritas de macros; tocar un día = ficha rápida. Opciones de cálculo y tablas, plegadas al final.
- **Gimnasio:** importación CSV de HEVY, progresión por peso y repeticiones, 1RM (Epley), récords, volumen, reparto muscular, constancia, nutrición en días de entreno, análisis con IA.
- **Más → Ajustes:** perfil, metas, conexión IA, notas para la IA (+ «Aplicar instrucciones con IA»), estado de la app, copias JSON/HTML (en el móvil se comparten; al restaurar se ve un resumen antes).
- **Avisos:** «Hay una versión nueva» al volver a la app si GitHub tiene una más reciente; aviso sin conexión.

## 7. Conexión con IA (no tocar sin pedirlo)
- Clave de Gemini API del propio Diego, guardada solo en el móvil si marca «Recordar». **Nunca pongas claves en el código.**
- POST `https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent` (API estable) con `thinkingConfig.thinkingLevel: 'low'` para responder rápido. Funciones: `callGemini()` y `requestAI()`.
- Modelo por defecto gemini-3.8-flash. requestAI() prueba en orden: modelo elegido ×2 y gemini-3.1-flash-lite (AI_FALLBACK) ×2, esperando entre intentos. Si un intento tarda más de 30 s (foto) o 20 s (texto) salta directo al modelo rápido. Saturación (429/503, AI_BUSY) → reintento con espera y, al final, mensaje claro. Tiempo máximo total de una foto: 65 s. «Probar conexión» elige el modelo que responde.
- Foto: se reduce a 1.600 px (JPG 0,88) y se analiza componente a componente con `photoPrompt()` (usa los 40 alimentos más habituales de Mi despensa).
- Formato de importación: `BIOPEAT:{...}` o `BIOPEAT:[{...}]` con meal, name, grams, kcal, p, c, f, pufa y los 25 micros. Lo desconocido se omite o va como null, nunca 0.
- Claves de los 25 micros: vitA, vitD, vitE, vitK, vitC, b1, b2, b3, b5, b6, b7, b9, b12, colina, ca, phos, mg, k, na, fe, zn, cu, se, i, mn.

## 8. Datos y publicación
- Los datos viven en el navegador del móvil (`localStorage`, clave `biopeat_pro_v10`). **Nunca se suben a GitHub.**
- Claves guardadas que **no se renombran:** `biopeat_pro_v10`, compare17, workouts18, favorites22, microTargets17, goalOrigin17, ratioGoals17, macroGoals, targetMode.
- Publicada con **GitHub Pages** (rama main) e instalada como app (manifest.json + sw.js). Al subir un index.html nuevo la app se actualiza sola en 1-2 minutos sin perder datos.

## 9. Cómo está hecho el código (resumen técnico)
- Todo en `index.html`: CSS, HTML y un único `<script id="app">`. Sin librerías.
- `change(fn, mensaje)`: única forma de modificar datos (guarda, repinta y permite deshacer).
- `render()`: único punto que repinta. Semana y Gimnasio se pintan al acercarse (`flushLazy`).
- Un solo listener de clic: cada sección registra el suyo con `onClick(fn)`.
- Piezas reutilizables (v34): `ratioInfo(clave)` + `ratioFixes()` (equilibrios), `dayCard(fecha)` (ficha rápida de un día), `monthStats()` + `sparkline()` (tendencias), `macroTone(%)` (colores ok/low/high/none).
- Metas: `targetFor(fecha)` / `dayGoal()` / `goalsFor(fecha)`. No se guardan metas calculadas en los días; solo el ajuste manual `days[fecha].macroGoals`.
- Logo: SVG dentro de `.brand-icon` (ids bp-bg, bp-rim, bp-mark). Iconos del móvil: icon-192.png, icon-512.png e icon-maskable-512.png (Ajustes → «Descargar iconos» los regenera desde el SVG). Colores: azul noche (#16243a) y dorado (#e9bf5c, variables --gold y --gold-soft); verde, ámbar y violeta siguen siendo los colores de estado.
- Migraciones: `migrate()` → `migrateBase` + `upgradeToNN`. Cada `upgradeToNN` se ejecuta una sola vez comprobando `o.appRevision`.

## 10. Historial (una línea por versión, máximo 8)
- **v50 · Copilot:** micronutrientes con una sola tabla de zonas ideales (`OPT`: fuente a la vista en cada tarjeta, franja verde en la barra, referencias Peat/Dinkov/foros/oficial); depósito de 7 días sin avisos «parcial» falsos; «¿Qué me falta?» rehecho (resumen con filtros, filas que se abren, alimentos con un toque y cantidades en vasos o huevos); arreglados: el fósforo se valoraba como meta y salía como «te falta», las tarjetas de selenio/yodo/vitamina A se contradecían (máx. y banda a la vez), colores de la semana sin CSS y el texto antiguo «Ca:P 1,10».
- **v49 · Copilot:** la grasa saturada cuenta ×0,5 para la meta de grasa (constante `SAT_W`; la meta no cambia y los kcal cuentan todo); «¿Qué me falta?» de Semana rehecho (3 micros que más faltan con alimentos que se añaden con un toque, equilibrios solo si están fuera de rango); depósitos de 7 días: hoy no cuenta hasta cerrar el día, yodo con banda óptima 100-225 µg y notas Peat/Dinkov revisadas; `actualizar.html` localiza bloques con espacios o comillas distintos, indica bloque/línea/columna de los errores de escritura y admite correcciones parciales; GitHub regenera solo la versión de CONTEXTO y el MAPA.
- **v43 · Copilot:** la IA reintenta sola si Gemini está saturado (2 intentos con el modelo elegido y 2 con el rápido, con espera) y da un mensaje claro; aviso «Hay una versión nueva»; restaurar copia muestra antes un resumen; en el móvil la copia se comparte (WhatsApp, Drive…); aviso sin conexión; prueba automática en GitHub (.github/workflows/check.yml).
- **v42 · Copilot:** logo nuevo (B dorada en línea con una P dorada maciza dentro y punto dorado, fondo azul noche), iconos PNG reales para el móvil (normal y maskable) y tema de la app en azul noche y dorado.
- **v38-v41 · Claude/Gemini:** primeros logos B+P y botón para descargar los iconos.
- **v37 · Copilot:** IA rápida y fiable: API estable, razonamiento bajo, respaldo automático a gemini-3.1-flash-lite si tarda, «Probar conexión» elige el modelo que funciona. Flujo nuevo: la IA entrega bloques `@@@` y `actualizar.html` los prueba (sin Jules).
- **v36 · Gemini:** el botón del plan Peat por defecto indica si ya lo usas.
- **v35 · Copilot:** el día anterior se marca completo al añadir comida; foto por ingredientes con despensa, contador y errores claros.

## 11. Pendiente / ideas
- Unificar las capas de CSS sin cambiar el aspecto (hay reglas repetidas de varias versiones).
- Gimnasio: aplicar el mismo estilo de «preguntas numeradas» que Semana.
