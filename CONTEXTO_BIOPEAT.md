# CONTEXTO COMPLETO · BioPeat Diego

Documento maestro del proyecto. Lo leen **Gemini** (para pensar y redactar tareas) y **Jules** (para programarlas). Si algo de aquí contradice al código, manda el código; avisa de la diferencia.

---

## 1. Quién es el usuario y qué busca
- **Diego**, 23 años, hombre, 185 cm, ~77,5 kg (editable en la app). Madrid (España). Escribe en español de España, de forma rápida y con faltas; entiéndelo por el sentido.
- Trabaja en finanzas y entrena a dos equipos federados de baloncesto.
- **Entrenamiento:** full body lunes, miércoles y sábado (70–85 min, 2 series efectivas al fallo, RIR 0-1); partido de baloncesto el domingo; martes, jueves y viernes sin pesas (trabajo + pista).
- Registra sus entrenamientos en **HEVY (plan gratuito, sin API)**: exporta un CSV y lo importa en la app.
- **Enfoque nutricional:** acercarse lo máximo posible a las ideas de **Ray Peat** y **Georgi Dinkov** (bioenergética, prometabólico), pero **sin que la app sea juzgona ni rígida**. Prefiere ver datos claros y sugerencias, no avisos médicos ni bloqueos. Sabe lo que hace con su suplementación y aspirina: **no le restrinjas ni le pidas confirmaciones por motivos médicos.**
- **Cómo le gusta trabajar:** cambios iterativos, mucho visual, gráficos interactivos, porcentajes que pueden pasar del 100 %, pocas pantallas, móvil primero, sin ventanas de confirmación al añadir (se añade con un toque y se puede deshacer/editar). Es muy sensible a que se le diga que algo está hecho o comprobado cuando no lo está.

## 2. Objetivos diarios (calculados en la app con `targetFor`)
- TMB Mifflin-St Jeor: 10×peso + 6,25×185 − 5×23 + 5 (≈1.821 kcal con 77,5 kg).
- kcal = TMB × FAF del día, redondeado a 5. Proteína y grasa fijas por día (escalan con el peso); hidratos = el resto.

| Día | Actividad | FAF | Proteína | Grasa | Aspirina |
|---|---|---|---|---|---|
| Lunes | Full body pesado | 1,725 | 165 g | 90 g | 500 mg |
| Martes | Descanso / pista | 1,5 | 150 g | 85 g | 250 mg |
| Miércoles | Full body potencia | 1,725 | 165 g | 90 g | 500 mg |
| Jueves | Descanso / pista + selenio | 1,5 | 150 g | 85 g | 250 mg |
| Viernes | Descanso / pista | 1,5 | 150 g | 85 g | 250 mg |
| Sábado | Full body frecuencia | 1,65 | 160 g | 90 g | 500 mg |
| Domingo | Partido + selenio | 1,75 | 160 g | 85 g | 500 mg |

## 3. Pauta de suplementos (se añade sola cada día como «prevista»; editable en «Tu pauta»)
| Momento | Qué | Cantidad | Días |
|---|---|---|---|
| Desayuno | Vitamina D3 | 4.000 UI (100 µg) | todos |
| Desayuno | Vitamina A (retinol) | 10.000 UI (3.000 µg RAE) | todos (Diego la omite si come hígado; no se automatiza) |
| Desayuno | K2 MK-4 | 0,5 mg | todos |
| Comida | Vitamina E | 200 UI (134 mg) | todos |
| Comida | Benfotiamina (B1) | 250 mg | todos |
| Comida | Glicina | 5 g | todos |
| Comida | Bisglicinato de magnesio HSN | **2 g de polvo** (no de Mg elemental) | todos |
| Comida | Selenio | 200 µg | jueves y domingo |
| Merienda (con el batido) | Creatina | 5 g | todos |
| Merienda | K2 MK-4 | 0,5 mg | todos |
| Merienda | **Aspirina, toda la del día en una toma** | 500 mg L/X/S/D · 250 mg M/J/V | todos |
| Antes de dormir | Glicina | 5 g | todos |
| Antes de dormir | Bisglicinato de magnesio HSN | 2 g de polvo | todos |

- Ficha HSN: 1,5 g de polvo ≈ 165 mg de Mg elemental (≈110 mg Mg/g de polvo). 4 g/día de polvo es lo que toma Diego; no lo cambies.
- La aspirina se puede registrar siempre que quiera, cualquier día y cantidad.
- La **B1** se muestra aparte: mg de benfotiamina frente a su pauta, y tiamina de alimentos por separado (no se suman 1:1).

## 4. Comidas habituales (botones de 1 toque)
- **Desayuno:** 220 ml leche entera + 21 g Nesquik (3 cucharadas) + 1 plátano (120 g) + 250 ml zumo de naranja exprimido. ≈433 kcal.
- **Batido de merienda:** 200 ml leche entera + 150 ml zumo de naranja + 35 g azúcar + 5 g creatina + 1 plátano (120 g) + **whey 0–40 g** con slider que muestra en directo cómo queda el % de proteína del día. La creatina del batido no se duplica con la de la pauta.
- Intra-entreno/partido: ositos Haribo con azúcar a demanda (por 100 g: 343 kcal, 77 g hidratos, 6,9 g proteína, 0 PUFA).

## 5. Reglas nutricionales Peat / Dinkov en la app
- **PUFA:** límite personal <= 4,0 g/día. Es un **máximo**, no una meta.
- **Calcio : fósforo:** referencia ≥ 1,10 : 1 (editable). Calcio objetivo **2.000 mg** (Peat/Dinkov hablan de 2.000–3.000 mg, sobre todo de leche y queso).
- **Hidratos : proteína:** se muestra como «g de hidratos por cada g de proteína» frente al reparto del plan del día (±20 % verde).
- **Hierro:** es un **límite** (mejor por debajo, <= 14 mg).
- Prioridades de alimentos para sugerencias: leche, queso, zumo de naranja, fruta madura, miel/azúcar, patata, arroz, huevos, marisco, gelatina, carne con caldo; evitar aceites vegetales y PUFA.
- **Micros «depósito» (se valoran con 7 días):** A, D, E, B12, folato (B9), selenio, yodo, cobre y hierro. El depósito se llena con lo que se toma y cada día sale el más antiguo; los días sin registro cuentan 0. El resto (calcio, fósforo, magnesio, potasio, sodio, zinc, manganeso, C, B1–B7, colina, K) son diarios.
- Donde no hay cifra documentada de Peat, se mantiene la meta personal de Diego. **No inventes cifras atribuidas a Peat.**

### Los 25 micronutrientes (claves del JSON)
vitA, vitD, vitE, vitK, vitC, b1, b2, b3, b5, b6, b7, b9, b12, colina, ca, phos, mg, k, na, fe, zn, cu, se, i, mn.
Extras: kcal, p, c, f, pufa, retinol, fiber, sugars, freeSugar, satFat, monoFat, glycine, creatine, benfotiamine.

## 6. Qué hace la app hoy (v28)
Una sola página con desplazamiento; barra inferior **Hoy · Registro · Añadir · Semana · Más** (solo desplaza; **no cambiar este orden**) y botón flotante redondo de **Gimnasio** siempre visible.
- **Hoy:** energía con %, recomendación del día (ideas sencillas + botón «Pedir sugerencia a la IA» que aprende de lo que suele comer), anillos de macros con % sin tope y «Te quedan X g», equilibrio del día (Ca:P, PUFA, C:P), comidas del día con «Igual que ayer», «Marcar día completo», aviso de copia de seguridad, «Modo resumen».
- **Añadir:** «¿Qué has comido?» (texto libre de varias comidas en un mensaje → se reparte en desayuno/comida/merienda/cena), **Foto aquí** (IA directa; la foto y el texto se vacían tras analizar), **Foto en Gemini** (copiar prompt + pegar respuesta `BIOPEAT:`), Manual, «Tus rápidos»/favoritos, desayuno, batido, suplemento extra, **Mi despensa** (lo que analiza la IA se guarda solo y se reutiliza sin IA).
- **Registro:** buscador, grupos plegables por comida, − / + / ✎ / ×, deshacer, probar una ración (con buscador), reparto de energía y tipos de grasa.
- **25 micros:** mapa y tarjetas, depósitos con barras de 7 días.
- **Tu pauta:** automática, ✓ para confirmar tomas, «Confirmar las previstas de hoy», editor, aspirina.
- **Semana:** 4 anillos semanales, micros y ratios, tira de 7 días por colores, tendencia de 8 semanas, desglose plegado, calendario editable.
- **Gimnasio:** importación CSV de HEVY (lb→kg, asistidos, nombres unificados, reps anómalas), buscador de ejercicios, progresión por **peso y repeticiones**, 1RM, récords, volumen semanal, reparto muscular, constancia, nutrición en días de entreno vs descanso, análisis con IA.
- **Más → Ajustes:** perfil, metas, conexión IA, notas para la IA, estado de la app, copias JSON/HTML, fuentes de Peat.

## 7. Conexión con IA (no tocar)
- Modo directo con la clave de Gemini API del usuario (Interactions API, `POST https://generativelanguage.googleapis.com/v1beta/interactions`). Modelo por defecto `gemini-3.8-flash`; si devuelve 429 pasa solo a `gemini-3.1-flash-lite`. También hay modo servidor propio. La clave solo se guarda en el dispositivo si el usuario marca «Recordar». **Nunca pongas claves en el código.**
- Formato de importación: `BIOPEAT:{...}` o `BIOPEAT:[{...}]` con `meal, name, grams, kcal, p, c, f, pufa` y los 25 micros con las claves de arriba. Lo desconocido se omite (no se pone 0).

## 8. Datos y despliegue
- Datos en el navegador del móvil (`localStorage` clave `biopeat_pro_v10`, con alternativas). **Nunca** se suben a GitHub.
- La app está publicada en **GitHub Pages** desde la rama `main` del repositorio `biopeat` y se instala como PWA (manifest.json + sw.js). Al cambiar `index.html` la app se actualiza sola sin perder datos, siempre que no cambie la dirección ni se renombren los campos protegidos.

## 9. Historial resumido
v10–v19: primeras versiones con Gemini/Copilot. v20: una sola página. v22: Añadir unificado, favoritos, aviso de copia. v23: reescritura en una sola capa. v24: conexión IA desde el móvil, modo resumen, Mis alimentos. v25: Gimnasio nuevo. v26: correcciones de Gemini, recomendación, ventanas con «Atrás», depósitos, calcio 2.000. v27: recomendación sencilla + IA, despensa automática, depósitos que se llenan y vacían, semana visual, −/+, fallback de modelo.

**Pendiente conocido:** unificar las capas de CSS sin cambiar el aspecto (hacerlo con capturas antes/después).


## v32 UI Changes
- La vista de 'Tus nutrientes' se divide en 3 bloques: Escudo Peat (Límites máximos), Vitaminas y Minerales Diarios, y Tanques de Reserva (Depósitos 7 días) para simplificar y dar contexto visual.
- La vista de 'Tu pauta' (suplementos) ahora es un checklist limpio agrupado por momentos del día (Desayuno, Comida, Merienda, Antes de dormir).
- Se ha introducido un conmutador explícito entre 'Vista Resumen' y 'Vista con Explicaciones Peat' (toggle CSS `bp-compact`).
- En 'Tu semana', la tabla detallada de 25 nutrientes se pliega en un `<details>` por defecto para simplificar el panel.