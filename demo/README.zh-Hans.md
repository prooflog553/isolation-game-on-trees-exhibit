# 体验隔离博弈

[English](README.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md)

[English](README.md) · [在线棋盘](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html) · [D10 构造图](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/d10.html)

下载[单文件棋盘](index.html)，用浏览器打开即可，无需安装。选择树和先手后，可以点击顶点，也可以用 Tab 键聚焦顶点，再按 Enter 或空格，或者使用合法着按钮。切换中英文时，当前棋局会保留。

每手覆盖所选顶点及其邻点，并且必须新覆盖一条橙色边的端点。已经覆盖的顶点只要满足这一条件，仍然可以选择。蓝框标出当前一方的全部最优着。合法着按钮上的数字包含这一步，表示双方此后都按最优策略行棋时，还需要多少手。

策略区显示两种先手的空局最优值，以及从当前局面出发的一条双方最优续局。预览和“走一步最优着”在出现并列时选择编号最小的顶点。每次落子或悔棋后，棋盘都会更新。

| 树 | D 先手 | S 先手 | 可以试什么 |
|---|---:|---:|---|
| P5 | 1 | 2 | 先选 2，再选已经覆盖的 3。 |
| P9 | 3 | 4 | 对比 D 自由选择首着与固定从中心 5 起手。 |
| D8 · 22 点 | 9 | 10 | 查看添叶前的 D 先手值。 |
| D8 · 23 点 | 10 | 10 | 加一片叶后，D 先手值升为 10。 |

2026 年 11 月 25 日的浏览器检查完成了八种最优对局，并检查了 141,420 个可达状态中的每一步合法着法和对应值，共涉及 1,335,806 个合法转移。检查还覆盖了键盘与鼠标操作、悔棋、重新开始、语言切换，以及 320 和 375 像素宽的布局。

[Python 复算](../REPRODUCE.zh-Hans.md) · [中文首页](../README.zh-Hans.md)
