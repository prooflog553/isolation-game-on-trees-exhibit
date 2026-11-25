# 树上的隔离博弈：从直径 9 到直径 10

[English](README.md) · **简体中文** · [日本語](README.ja.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [项目网站](https://prooflog553.github.io/isolation-game-on-trees-exhibit/)

**一棵树有多“长”，会怎样影响一场隔离博弈的手数？** 对这里研究的上取整界，答案恰好藏在直径 9 与 10 之间。

[**阅读论文 PDF**](manuscript/Isolation_Game_Research_Report.pdf) · [**查看 Lean 源码与构建**](formal/README.zh-Hans.md) · [**在线体验**](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html?lang=zh)

## 摘要

隔离博弈中，两名玩家轮流选择顶点；一方试图尽快结束游戏，另一方则尽量延长游戏。对于有 $n$ 个顶点的树，一个自然的问题是：先手的 Dominator 能否总在 $\lceil 3n/7\rceil$ 手内结束？本项目从树的**直径**出发研究这个问题，得到一条精确的直径分界。

当直径至多为 **9** 时，任意有限树在 Dominator 先手下都满足这一上界。当直径为 **10** 时，对每个正整数 $k$，我们构造出一棵有 $210k$ 个顶点的树：无论哪一方先手，双方最优行棋都至少需要 $91k$ 手，而上取整基准仅为 $90k$。因此，反例不仅在直径 10 出现，超出基准的手数也至少随 $k$ 线性增长。

上界证明结合结构归约、有限证书和覆盖任意多普通分支的 14 族策略；下界则来自可扩展的模块化构造及相应策略。仓库提供论文、形式化源码、复算程序和交互展示，供读者沿不同路径核验。

![从直径 9 的上界到直径 10 的反例族](assets/diameter-threshold.svg)

## 问题从哪里来

在普通隔离博弈中，一手覆盖所选顶点和它的邻点；合法的一手必须新覆盖一条原本两端都未覆盖的边的至少一个端点。当所有边都至少有一端被覆盖时，游戏结束。Dominator 力求减少手数，Staller 力求增加手数。树的直径是其顶点间最远距离，按边数计算。

已有研究提出了关于博弈手数的 $3n/7$ 型猜想。本项目最初也尝试研究更强的下取整界；但一个小例子迫使问题发生变化：给一棵 **22 点、直径为 8** 的树的中心添一片叶子，直径不变，Dominator 先手的最优手数却从 **9** 增至 **10**。对于 23 个顶点，下取整界是 9，上取整界是 10。研究于是转向：上取整界能保证到什么直径，又从哪里开始失效？[文献与定理范围](manuscript/SOURCES.zh-Hans.md) · [这棵树的复算](REPRODUCE.zh-Hans.md)

## 结果与证明的范围

| 结果 | 结论 |
|---|---|
| **直径至多 9** | 对每棵有 $n$ 个顶点的有限树，普通博弈从全未覆盖状态开始时，Dominator 先手可在 $\lceil3n/7\rceil$ 手内结束。本项目未证明相同上界适用于 Staller 先手。 |
| **直径恰为 10** | 对每个正整数 $k$，存在一棵 $210k$ 点树，两种先手的博弈值都至少为 $91k$；该树的上取整基准为 $90k$。这里的 $91k$ 是下界，而非声称精确值。 |
| **证明方法** | D9 通过结构归约和有限分类，将问题化到 14 个候选族，再为任意多条普通分支给出策略；D10 通过连接 15 点模块，构造无限反例族。 |

这两项结果共同确定：对于 Dominator 先手，上取整界在树上首次可能失效的直径是 **10**。D10 的下界还覆盖 Staller 先手；这并不意味着本项目同时解决了直径至多 9 时的 Staller 先手情形。[证明与证据导航](EVIDENCE_MAP.zh-Hans.md)

## 从哪里开始

| 如果你想…… | 可以查看 |
|---|---|
| **阅读证明** | [论文全文](manuscript/Isolation_Game_Research_Report.pdf) · [证明导航与 D9 实例](EVIDENCE_MAP.zh-Hans.md) · [文献和定理对照](manuscript/SOURCES.zh-Hans.md) |
| **检查形式化结果** | [D6、D7、D9、D10 的 Lean 源码与构建说明](formal/README.zh-Hans.md) |
| **尝试例子** | [在线棋盘](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html?lang=zh) · [可缩放的 D10 构造](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/d10.html?lang=zh) · [棋盘使用说明](demo/README.zh-Hans.md) |
| **独立复算** | [Python 案例、有限证书和复现步骤](REPRODUCE.zh-Hans.md) |
| **了解研究过程** | [AI 如何解题：失败的开局、反例与证明修订](RESEARCH.zh-Hans.md) |

例如，在五点路径 $1—2—3—4—5$ 上先选择 **2**，再选择已经被覆盖的 **3**，就能看到：已覆盖的顶点在满足合法着条件时仍然可以选择。

档案整理与维护：岑弈（Cen Yi）。[逐材料权利与许可](LICENSE_SCOPE.md)
