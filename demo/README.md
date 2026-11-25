# Play the isolation game

[English](README.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md)

[简体中文](README.zh-Hans.md) · [Play online](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html?lang=en) · [D10 diagram](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/d10.html?lang=en)

Download [the self-contained HTML board](index.html) and open it in a browser; no installation is needed. Select a tree and a starting player. You can click a vertex, focus it with Tab and press Enter or Space, or use the legal-move buttons. Switching languages keeps the current game.

Choose **Try the two-move example** for a guided five-vertex game. A dashed purple ring marks the next suggested vertex. After a move, check which vertices were newly covered and how many orange edges disappeared.

Each move covers the chosen vertex and its neighbors and must newly cover an endpoint of an orange edge. A previously covered vertex can still be played if it satisfies that rule. Blue outlines mark every optimal move for the player to move. The number on a legal-move button includes that move and gives the remaining length under optimal play by both sides.

The strategy panel shows the exact starting values for both players and one optimal continuation from the current position. The preview and **Play an optimal move** choose the lowest-numbered vertex to break ties. The board updates after each move and undo.

| Tree | D starts | S starts | What to try |
|---|---:|---:|---|
| P5 | 1 | 2 | Play 2, then the already covered vertex 3. |
| P9 | 3 | 4 | Compare a free D opening with a forced opening at the center, 5. |
| D8 · 22 vertices | 9 | 10 | Check D's value before adding the leaf. |
| D8 · 23 vertices | 10 | 10 | Adding the leaf raises D's value to 10. |

The [D10 diagram](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/d10.html?lang=en) has plus and minus buttons for k and side-by-side values for the tree order, lower bound and ceiling benchmark. The path-length diagram shows the 4 + 2 + 4 edges that attain diameter 10.

The 25 November 2026 browser check completed all eight optimal games and checked every legal move and value on 141,420 reachable states, covering 1,335,806 legal transitions. It also exercised keyboard and pointer play, undo, restart, language switching, and the 320 px and 375 px layouts.

[Python replays](../REPRODUCE.md) · [English home](../README.md)
