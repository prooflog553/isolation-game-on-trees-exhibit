# Jugar al juego de aislamiento

[English](README.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md)

[English](README.md) · [Inicio en español](../README.es.md) · [Tablero en línea](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html) · [Construcción D10](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/d10.html)

Descarga el [tablero HTML autónomo](index.html) y ábrelo en un navegador, sin instalar nada. Elige un árbol y quién empieza. Puedes pulsar un vértice, seleccionarlo con Tab y usar Enter o la barra espaciadora, o emplear los botones de jugadas válidas. El tablero conserva la partida al cambiar entre inglés y chino.

Cada jugada cubre el vértice elegido y sus vecinos; debe cubrir por primera vez un extremo de una arista naranja. Se puede elegir un vértice ya cubierto si cumple esa condición. Los contornos azules señalan todas las jugadas óptimas del jugador de turno. El número de cada botón incluye esa jugada e indica cuántas quedan si ambos jugadores actúan de forma óptima.

El panel de estrategia muestra los valores iniciales para ambos jugadores y una continuación óptima desde la posición actual. Cuando hay empate, la vista previa y la opción de jugar una jugada óptima eligen el vértice de menor número.

| Árbol | Empieza D | Empieza S | Qué probar |
|---|---:|---:|---|
| P5 | 1 | 2 | Juega 2 y después el vértice 3, ya cubierto. |
| P9 | 3 | 4 | Compara la apertura libre de D con la apertura obligatoria en el centro 5. |
| D8 · 22 vértices | 9 | 10 | Comprueba el valor de D antes de añadir la hoja. |
| D8 · 23 vértices | 10 | 10 | Al añadir una hoja, el valor de D sube a 10. |

La comprobación en navegador del 25 de noviembre de 2026 completó las ocho partidas óptimas y revisó 141.420 estados alcanzables y 1.335.806 transiciones legales. También probó teclado, puntero, deshacer, reinicio, cambio de idioma y diseños de 320 y 375 píxeles.

[Guía de reproducción (inglés)](../REPRODUCE.md)
