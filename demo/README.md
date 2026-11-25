# Play the isolation game / 体验隔离博弈

[Play online / 在线玩一局](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html) · [D10 diagram / 构造图解](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/d10.html)

Download [the self-contained HTML board](index.html) and open it in a browser. Select a tree and a starting player. The language selector keeps your current game. You can click a vertex, focus it and press Enter or Space, or use the legal-move buttons.

下载[单文件棋盘](index.html)后用浏览器打开，无需安装。选择树和先手。切换中英文会保留棋局。可以点击顶点，用 Tab 聚焦后按 Enter 或空格，也可以使用合法着按钮。

Play covers the chosen vertex and its neighbors. A move is legal when it covers an endpoint of an orange edge. Previously covered vertices are playable when they satisfy that rule. Blue outlines mark all optimal moves for the player to move.

一手覆盖所选顶点及其邻点，必须覆盖一条橙色边的端点。已覆盖顶点满足这个条件也能走。蓝框标出当前一方的全部最优着。合法着按钮的数字包含这一步，表示双方随后都最优时还需多少手。

The right panel shows the two exact opening values and one optimal continuation for both sides from the current position. The preview and **Play an optimal move** use the lowest-numbered move to resolve ties. The board updates after every move and undo.

策略区同时显示 D、S 各自先手的空局最优值，以及当前局面下的一条最优续局。预览和「走一步最优着」遇到并列时取顶点编号最小的一手。

| 树 / Tree | D 先手 / D starts | S 先手 / S starts | 可以试什么 / What to try |
| --- | ---: | ---: | --- |
| P5 | 1 | 2 | 先选 2，再选已经覆盖的 3。 / Play 2, then the already covered vertex 3. |
| P9 | 3 | 4 | D 自由首着可三手结束。强制从中心 5 起手要四手。 / Compare the free D opening with forcing vertex 5. |
| D8 · 22 点 / vertices | 9 | 10 | 对照添叶前的 D 先手值。 / Check D's value before adding the leaf. |
| D8 · 23 点 / vertices | 10 | 10 | 加一片叶后，D 先手最优值变为 10。 / The extra leaf raises D's value to 10. |

The 25 November browser check completed all eight optimal games and checked every legal move and value on 141,420 reachable states, covering 1,335,806 legal transitions. It also exercised keyboard play, pointer play, undo, restart, language switching, and the 320 px and 375 px layouts.

[Python 复算 / Python replays](../REPRODUCE.md) · [中文首页](../README.zh-Hans.md) · [English home](../README.md)
