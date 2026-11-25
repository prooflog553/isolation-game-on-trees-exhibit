# Evidence map / 证据导航

[English home](README.md) · [中文首页](README.zh-Hans.md) · [Python and certificates / 复算](REPRODUCE.md)

The report links below use the PDF page numbers of the 71-page reading edition. The results concern the ordinary game with no vertices covered at the start.

| Result / 结论 | Where to read or test / 核验入口 |
|---|---|
| D6 and D7 establish the unrounded Dominator-start bound for trees of order at least 3 in their respective diameter ranges. | [Statement and literature crosswalk](manuscript/SOURCES.md) |
| D8 has a 23-vertex counterexample to the unrounded bound. | [Exact figure](assets/d8-one-leaf.svg) · [Python replay](REPRODUCE.md) |
| Through diameter 9, Dominator can finish within $\lceil3n/7\rceil$ moves when starting. | [Theorem 0.1](manuscript/Isolation_Game_Research_Report.pdf#page=3) · [Chapter 12](manuscript/Isolation_Game_Research_Report.pdf#page=53) |
| At diameter 10, both starters can exceed the ceiling for infinitely many orders. | [Appendix B](manuscript/Isolation_Game_Research_Report.pdf#page=58) · [Zoomable construction](demo/d10.html) |

## A concrete D9 proof case / D9 证明中的一棵树

The proof reduces a minimum-order counterexample to 14 candidate families. Each family still allows arbitrary numbers of ordinary branches. In family `r00`, two adjacent centers carry a one-vertex `t00` branch and an eleven-vertex `t08` branch. When $p=q=0$, the tree has 14 vertices. Adding $p$ and $q$ ordinary seven-vertex branches gives $14+7(p+q)$ vertices. The `r00` budget is $6+3(p+q)$ moves, equal to the target ceiling. [Chapter 12 budget table](manuscript/Isolation_Game_Research_Report.pdf#page=55)

图中有两个相邻的中心，分别接 1 点和 11 点分支，共 14 点。普通分支每添一条增加 7 点，第 12 章逐族手数预算也随之增加 3 手。有限证书负责局部策略和结构分类，一般证明负责任意大的分支数量。

![D9 family r00 at p=q=0](assets/d9-r00.svg)

## The diameter-10 family / 直径 10 的反例族

Each module joins the midpoints of two disjoint seven-vertex paths to one shared center. Joining the centers of $14k$ modules into a star gives $210k$ vertices. A path between the farthest tips in distinct leaf modules uses $4+2+4=10$ edges. Appendix B proves a lower bound of $91k$ moves for either starter, against the ceiling $90k$.

[Change the parameter or zoom the diagram / 调整参数与缩放](demo/d10.html)

![A 15-vertex module](assets/d10-module.svg)
