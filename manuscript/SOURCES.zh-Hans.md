# 文献与定理范围

[English](SOURCES.md) · [研究报告](Isolation_Game_Research_Report.pdf) · [证据导航](../EVIDENCE_MAP.zh-Hans.md)

## 参考文献

[1] B. Brešar, T. Dravec, D. P. Johnston, K. Kuenzel, and D. F. Rall, *Isolation game on graphs*, Graphs Combin. **42** (2026), no. 2, Paper No. 30. [DOI 10.1007/s00373-026-03030-y](https://doi.org/10.1007/s00373-026-03030-y)

[2] C. Bujtás, T. Dravec, M. A. Henning, and S. Klavžar, *Bounds on the game isolation number and exact values for paths and cycles*, Discrete Math. Theor. Comput. Sci. **28** (2026), no. 2, Paper No. 33. [DOI 10.46298/dmtcs.16132](https://doi.org/10.46298/dmtcs.16132)

[3] M. A. Henning and D. F. Rall, *Total isolation game in graphs*, arXiv:2601.03363v1, 6 January 2026. [Cited version](https://arxiv.org/abs/2601.03363v1)

文献 [1，猜想 3.3] 和 [2，猜想 5.1] 对不含 $K_2$ 连通分量的图提出了适用于两种先手的上取整界。文献 [2，猜想 5.4] 对至少有三个顶点的树提出 Dominator 先手的不取整 $3n/7$ 界；由于博弈值是整数，这等价于下取整界。文献 [2，猜想 5.3] 假设最小度数为 2。[3] 的全隔离博弈使用开邻域；本报告研究的普通博弈使用闭邻域。

## 项目结果与已核验的 Lean 定理

所有条目均针对初始标记和历史为空的有限简单树。[Lean 复现说明](../formal/README.zh-Hans.md)提供四个构建输入、定理检查和模块对照表。

| 结果 | 结论 | 核验定理 |
|---|---|---|
| D6 | $n\ge3$、直径至多为 6 时，Dominator 先手值至多为 $\lfloor(2n+1)/5\rfloor\le3n/7$。 | `IsolationGame.tree_diameter_six_bound` |
| D7 | $n\ge3$、直径至多为 7 时，Dominator 先手值至多为 $\lfloor3n/7\rfloor$。 | `IsolationGame.DiameterSeven.tree_diameter_seven_bound` |
| D9 | 直径至多为 9 时，Dominator 先手值至多为 $\lceil3n/7\rceil$。 | `IsolationGame.FourteenDiameterNineClosure.diameter_nine_ordinary_ceil_formula` 和 `actual_empty_marks_and_history`。[报告定理 0.1](Isolation_Game_Research_Report.pdf#page=4) |
| D10 | 对每个 $k\ge1$，存在一棵直径为 10、含 $210k$ 个顶点的树，两种先手的值均至少为 $91k$，其上取整基准为 $90k$。 | `CounterexampleConcreteFinal.model_complete_counterexample`。[附录 B](Isolation_Game_Research_Report.pdf#page=59) |

D6 和 D7 在各自的直径范围内建立了树的不取整界；D8 例子区分了下取整界与上取整界。D9 和 D10 合起来确定了上取整的 Dominator 先手界可能失效的最小直径。D10 对两种先手均反驳了 [1] 和 [2] 的上取整猜想，并在 Dominator 先手时反驳了 [2] 中关于树的猜想。这些树含有叶子，因此该构造不涉及最小度数为 2 的猜想。
