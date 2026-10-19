import subprocess
branch_name = "prometabolic-update"
title = "feat: Update Prometabolic profile, Epley 1RM, Calendar and Micros"
description = """NOTA DE TRASPASO:
- Implementado el cálculo condicional del Perfil Prometabólico Peat/Dinkov (130P/65F entreno, 115P/60F descanso, Ca:P 1.20, PUFA <= 4g).
- Actualizado `targetFor` y `goalsFor` para respetar estos macros y limpiar estados cacheados.
- Añadidos indicadores de Equilibrio A:D (UI) y Zn:Cu en `#balance-card`.
- Renombrado el Calendario a un sistema de 3 pestañas y sus mini-puntos de colores.
- Implementado el Epley 1RM en las analíticas de progresión del gimnasio con marcado en verde si supera a la sesión anterior.
- Modificado el tope/límite de los micronutrientes: Selenio (óptimo 100-200), Vit A (>3800), Yodo (>225) y Hierro estricto <= 14mg con sus debidos avisos semánticos en `renderWeekMicros` y `renderMicroCards`.
- Añadidos botones "quick chips" de acceso rápido debajo del Header.
- Verificación técnica y tests unitarios confirmados `node verify.js`.
- Version incrementada a v31.
"""
print(f"{branch_name}\n{title}\n{description}")
