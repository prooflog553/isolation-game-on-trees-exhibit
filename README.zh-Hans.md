# 树上的隔离博弈

[English](README.md) · **简体中文** · [日本語](README.ja.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [项目网站](https://prooflog553.github.io/isolation-game-on-trees-exhibit/)

**Dominator 先手时，上取整界对直径至多 9 的所有树成立。到了直径 10，一个无限反例族在两种先手下都超过这条界。**

[**读完整论文 PDF**](manuscript/Isolation_Game_Research_Report.pdf) · [**看 Lean 源码与构建说明**](formal/README.zh-Hans.md) · [**在线玩一局**](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html)

[**了解 AI 的研究过程**](RESEARCH.zh-Hans.md) 从失败的中心首着讲起，经过一片叶子迫使改题、反例直径从 12 降到 10，最后补上 D9 证明的缺口。每个转折都附有复算或证明入口。

![上取整界的精确直径门槛，从 9 到 10](assets/diameter-threshold.svg)

## 主要结果

| 结果 | 它说明什么 |
|---|---|
| **确定精确的直径门槛** | 对任何一棵有 $n$ 个顶点、直径至多 9 的有限树，Dominator 先手可在 $\lceil3n/7\rceil$ 手内结束。 |
| **构造超界幅度会增长的无限反例族** | 每个正整数 $k$ 都给出一棵 $210k$ 点、直径恰为 10 的树。两种先手都至少需要 $91k$ 手，上取整基准是 $90k$。 |
| **找到改变研究方向的小反例** | 给一棵 22 点树添一片叶子，直径仍为 8，但 Dominator 先手值从 9 升到 10。23 点时下取整界为 9，上取整界为 10。 |

## 这项工作的意义

**它解释了上取整猜想在树上最早从哪里失效。** 直径 9 的证明把无限范围的问题拆成可穷尽的局部证书，以及覆盖任意多普通分支的 14 族策略。直径 10 的构造则给出可扩展的失败机制，超出基准的手数至少随 $k$ 线性增长。

读者可以在棋盘上试失败的开局，用 Python 核验精确值，再从论文和 Lean 查看一般定理。研究记录同时交代人何时要求查错或批准改题，AI 提出了哪些构造和修订。

## 阅读、体验与复现

| 想做什么 | 入口 |
|---|---|
| **读论文与证明** | [完整论文 PDF](manuscript/Isolation_Game_Research_Report.pdf) · [D9 实例和证明导航](EVIDENCE_MAP.zh-Hans.md) · [文献与定理范围](manuscript/SOURCES.zh-Hans.md) |
| **看 Lean 代码** | [D6、D7、D9、D10 源码包和构建说明](formal/README.zh-Hans.md) · [D9 主证明文件](formal/D9/FourteenDiameterNineClosure.lean) · [D10 主定理文件](formal/D10/FinalDiameterCounterexample.lean) |
| **体验游戏与构造** | [在线棋盘与最优策略](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html) · [D10 可缩放构造](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/d10.html) · [离线使用说明](demo/README.zh-Hans.md) |
| **自行跑程序** | [Python 案例与有限证书](REPRODUCE.zh-Hans.md) |

每手覆盖所选点和它的邻点，且须新覆盖一条原本两端都未覆盖的边的端点。Dominator 尽快结束，Staller 尽量拖长。在五点路径上先选 **2** 再选 **3**，即可验证已覆盖的顶点何时还能走。

档案整理与维护由岑弈（Cen Yi）负责。[逐材料权利与许可](LICENSE_SCOPE.md)
