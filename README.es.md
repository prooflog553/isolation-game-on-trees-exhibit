# El juego de aislamiento en árboles

[English](README.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · **Español** · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md)

![Umbral de diámetro entre 9 y 10](assets/diameter-threshold.svg)

**¿Cuánto puede alargarse el juego en un árbol?** Para una cota concreta, el salto del diámetro 9 al 10 cambia la respuesta.

## Cómo se juega

Dos jugadores eligen vértices por turnos. Al elegir un vértice, se marcan ese vértice y todos sus vecinos. Una jugada es válida si marca por primera vez al menos un extremo de una arista que, antes de la jugada, tenía ambos extremos sin marcar. El vértice elegido puede estar ya marcado. El juego acaba cuando no quedan aristas con ambos extremos sin marcar. Dominator intenta minimizar el número de jugadas y Staller, maximizarlo.

Por ejemplo, en el camino 1–2–3–4–5, al jugar 2 se marcan 1, 2 y 3. Jugar después 3 es válido: marca 4, uno de los extremos de la última arista con ambos extremos sin marcar, y termina el juego.

## Qué demostramos

- **Diámetro como máximo 9.** En el juego ordinario, con todos los vértices inicialmente sin marcar y con Dominator como primer jugador, el valor del juego en un árbol finito de $n$ vértices es como máximo $\lceil 3n/7\rceil$. No se ha establecido esa misma cota para el caso en que empieza Staller.
- **Diámetro exactamente 10.** Para cada entero $k\ge1$ hay un árbol de $210k$ vértices cuyo valor del juego es al menos $91k$, empiece quien empiece. La cota anterior daría $\lceil 3(210k)/7\rceil=90k$. No se afirma que el valor sea exactamente $91k$ ni que el contraejemplo de 210 vértices sea el menor posible.

## El giro de la investigación: una sola hoja

Se unen los puntos medios de tres caminos disjuntos de siete vértices a un nuevo vértice central. El árbol obtenido tiene 22 vértices y, si empieza Dominator, el juego dura 9 jugadas con juego óptimo. Añadir una hoja al centro mantiene el diámetro en 8, pero eleva el valor a 10 con 23 vértices. En ese tamaño, la cota redondeada hacia abajo da 9 y falla; al redondear hacia arriba se obtiene 10. Este contraejemplo motivó el cambio de la hipótesis: el cálculo de esos dos árboles no prueba la nueva cota para todos los árboles.

## Del ensayo a la demostración

En el camino de nueve vértices, empezar por el centro obliga a cuatro jugadas con continuación óptima, aunque una apertura libre de Dominator permite terminar en tres. El ejemplo descartó una estrategia general, no la cota que se quería demostrar.

La construcción de diámetro 10 reúne $14k$ módulos de 15 vértices conectando sus centros en estrella. La demostración final controla primero la fase central y después el juego restante. Para diámetro 9, los certificados finitos tratan casos locales y las estrategias para 14 familias admiten un número arbitrario de ramas ordinarias.

La persona responsable orientó la investigación y pidió revisiones críticas; los sistemas de IA propusieron y revisaron construcciones y argumentos. Las reconstrucciones en Python comprueban ejemplos y certificados finitos; Lean comprueba los enunciados formalizados. La historia documentada conserva lagunas.

## Para explorar y verificar

- [Artículo completo (PDF, inglés)](manuscript/Isolation_Game_Research_Report.pdf) · [Mapa de pruebas (inglés)](EVIDENCE_MAP.md)
- [Historia de la investigación (inglés)](RESEARCH.md) · [Instrucciones de reproducción (inglés)](REPRODUCE.md) · [Fuentes y compilaciones de Lean (inglés)](formal/README.md)
- [Tablero interactivo (inglés/chino)](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html) · [Construcción D10 (inglés/chino)](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/d10.html)
- [Licencias y avisos (inglés)](LICENSE_SCOPE.md)


*Edición y mantenimiento del archivo: Cen Yi (岑弈).*
