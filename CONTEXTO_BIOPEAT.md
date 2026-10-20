# CONTEXTO · BioPeat Diego

**Versión actual: v34** (revisión de datos 23)

Documento maestro. Lo leen Gemini (para planificar) y Jules (para programar). **Se actualiza sustituyendo el texto de cada apartado, nunca añadiendo apartados nuevos al final.** Si algo de aquí contradice al código, manda el código; avisa de la diferencia en el Pull Request.

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
- Selenio óptimo 100-200 µg; vitamina A ≤ 3.800 µg; yodo ≤ 225 µg; A:D 2-4 : 1; Zn:Cu ~10 : 1.
- **Depósitos (media de 7 días):** A, D, E, B12, folato, selenio, yodo, cobre y hierro. Los días sin registro cuentan 0. El resto son diarios.
- Alimentos preferidos para sugerir: leche, queso, zumo de naranja, fruta madura, miel/azúcar, patata, arroz, huevos, marisco, gelatina, carne con caldo. Evitar aceites vegetales.
- **No inventes cifras atribuidas a Peat.** Donde no hay cifra suya, se usa la meta personal.

## 6. Qué hace la app (v34)
Una sola página. Barra inferior **Hoy · Registro · Añadir · Semana · Más** (no cambiar el orden) y botón redondo de **Gimnasio**.
- **Hoy:** energía, anillos de macros (% sin tope, «Te faltan X g»), recomendación del día + «Pedir sugerencia a la IA», **Equilibrio del día** (5 tarjetas: Ca:P, PUFA, hidratos:proteína, A:D, Zn:Cu; cada una con semáforo ✓/!, barra con zona verde y «Tú», y una frase sencilla; al tocarla: «¿Por qué importa?» (explicación Peat) y «Cómo llegar hoy» con alimentos y cantidades exactas que se añaden con un toque), comidas del día con «Igual que ayer», «Marcar día completo», «Vista Resumen».
- **Añadir:** texto libre de varias comidas en un mensaje (sin IA si reconoce los alimentos), foto con IA, «Foto en Gemini» (copiar prompt + pegar respuesta `BIOPEAT:`), manual, rápidos/favoritos, desayuno, batido, suplemento extra, Mi despensa (lo que analiza la IA se guarda y se reutiliza).
- **Registro:** buscador, grupos por comida, − / + / ✎ / ×, deshacer, probar una ración, reparto de energía y tipos de grasa.
- **Tus nutrientes:** tres bloques (Escudo Peat: PUFA y hierro · Diarios · Tanques de 7 días), tarjetas o mapa, filtros.
- **Tu pauta:** las tomas de hoy por momento del día (se suman solas; tocar = no tomada hoy), «+ Toma extra», «Lo que te aporta tu pauta» (qué parte de cada meta cubren los suplementos frente a la comida) y el editor de la pauta habitual plegado.
- **Semana:** 4 preguntas numeradas: 1 ¿Cómo voy? (media diaria de los días con comidas frente a la meta, 4 anillos y una frase), 2 Día a día (7 barras de energía; tocar = ficha del día), 3 ¿Qué me falta? (micros por debajo del 90 %, micros por encima de su máximo y 3 equilibrios; los 25 plegados), 4 ¿Voy mejorando? (8 semanas). Debajo, el **calendario**: selector Energía/Proteína/Hidratos/Grasa, media del mes, tendencia (últimos 7 días frente a los 7 anteriores), gráfico de línea del mes y cuadrícula con color por día (verde en rango, ámbar por debajo, violeta por encima, gris sin datos) y 3 barritas de macros; tocar un día = ficha rápida. Opciones de cálculo y tablas, plegadas al final.
- **Gimnasio:** importación CSV de HEVY, progresión por peso y repeticiones, 1RM (Epley), récords, volumen, reparto muscular, constancia, nutrición en días de entreno, análisis con IA.
- **Más → Ajustes:** perfil, metas, conexión IA, notas para la IA (+ «Aplicar instrucciones con IA»), estado de la app, copias JSON/HTML.

## 7. Conexión con IA (no tocar sin pedirlo)
- Clave de Gemini API del propio Diego, guardada solo en el móvil si marca «Recordar». **Nunca pongas claves en el código.**
- POST `https://generativelanguage.googleapis.com/v1beta/interactions`. Modelo por defecto `gemini-3.8-flash`; con error 429 pasa solo a `gemini-3.1-flash-lite`.
- Formato de importación: `BIOPEAT:{...}` o `BIOPEAT:[{...}]` con meal, name, grams, kcal, p, c, f, pufa y los 25 micros. Lo desconocido se omite o va como null, nunca 0.
- Claves de los 25 micros: vitA, vitD, vitE, vitK, vitC, b1, b2, b3, b5, b6, b7, b9, b12, colina, ca, phos, mg, k, na, fe, zn, cu, se, i, mn.

## 8. Datos y publicación
- Los datos viven en el navegador del móvil (`localStorage`, clave `biopeat_pro_v10`). **Nunca se suben a GitHub.**
- Claves guardadas que **no se renombran:** `biopeat_pro_v10`, compare17, workouts18, favorites22, microTargets17, goalOrigin17, ratioGoals17, macroGoals, targetMode.
- Publicada con **GitHub Pages** (rama main) e instalada como app (manifest.json + sw.js). Al aceptar un Pull Request la app se actualiza sola en 1-2 minutos sin perder datos.

## 9. Cómo está hecho el código (resumen técnico)
- Todo en `index.html`: CSS, HTML y un único `<script id="app">`. Sin librerías.
- `change(fn, mensaje)`: única forma de modificar datos (guarda, repinta y permite deshacer).
- `render()`: único punto que repinta. Semana y Gimnasio se pintan al acercarse (`flushLazy`).
- Un solo listener de clic: cada sección registra el suyo con `onClick(fn)`.
- Piezas reutilizables (v34): `ratioInfo(clave)` + `ratioFixes()` (equilibrios), `dayCard(fecha)` (ficha rápida de un día), `monthStats()` + `sparkline()` (tendencias), `macroTone(%)` (colores ok/low/high/none).
- Metas: `targetFor(fecha)` / `dayGoal()` / `goalsFor(fecha)`. No se guardan metas calculadas en los días; solo el ajuste manual `days[fecha].macroGoals`.
- Migraciones: `migrate()` → `migrateBase` + `upgradeToNN`. Cada `upgradeToNN` se ejecuta una sola vez comprobando `o.appRevision`.

## 10. Historial (una línea por versión, máximo 8)
- **v34 · Copilot:** equilibrio del día fácil de entender (semáforo, frase, porqué Peat y alimentos exactos para corregirlo); «Tu pauta» simplificada (se suma sola, tocar = no tomada) con «Lo que te aporta tu pauta»; Semana en 4 preguntas; calendario con métrica elegible, media, tendencia y ficha rápida del día. Flujo Gemini → Jules autónomo.
- **v33 · Copilot:** reparación de v30-v32. Arreglado: no se leían los macros y casi nada se guardaba (las metas se borraban en cada arranque); las metas personales se perdían al recargar; la pauta salía toda en «Otros»; el formulario de objetivos ignoraba los macros; tarjetas de nutrientes que abrían dos ventanas; A:D y Zn:Cu abrían la ventana equivocada; «Atrás» podía sacar de la app; textos como «2 platanos» o «y 100 g» no se reconocían. Plan por defecto 145/75 y 130/65. Repositorio limpio, prueba automática y reglas nuevas para agentes.
- **v30-v32 · Jules:** perfil Peat/Dinkov, simulador Ca:P y C:P, tanques de 7 días, vista resumen, 1RM Epley.
- **v25-v29 · Copilot/Jules:** gimnasio HEVY, recomendación del día, depósitos, despensa automática, foto con IA.

## 11. Pendiente / ideas
- Unificar las capas de CSS sin cambiar el aspecto (hay reglas repetidas de varias versiones).
- Gimnasio: aplicar el mismo estilo de «preguntas numeradas» que Semana.
