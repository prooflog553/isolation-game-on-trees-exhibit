# Sources and theorem scope

[Research report](Isolation_Game_Research_Report.pdf) · [Evidence map](../EVIDENCE_MAP.md) · [简体中文](SOURCES.zh-Hans.md)

## References

[1] B. Brešar, T. Dravec, D. P. Johnston, K. Kuenzel, and D. F. Rall, *Isolation game on graphs*, Graphs Combin. **42** (2026), no. 2, Paper No. 30. [DOI 10.1007/s00373-026-03030-y](https://doi.org/10.1007/s00373-026-03030-y)

[2] C. Bujtás, T. Dravec, M. A. Henning, and S. Klavžar, *Bounds on the game isolation number and exact values for paths and cycles*, Discrete Math. Theor. Comput. Sci. **28** (2026), no. 2, Paper No. 33. [DOI 10.46298/dmtcs.16132](https://doi.org/10.46298/dmtcs.16132)

[3] M. A. Henning and D. F. Rall, *Total isolation game in graphs*, arXiv:2601.03363v1, 6 January 2026. [Cited version](https://arxiv.org/abs/2601.03363v1)

[1, Conj. 3.3] and [2, Conj. 5.1] ask for the ceiling bound for both starters on graphs with no $K_2$ component. [2, Conj. 5.4] asks for the unrounded $3n/7$ bound for Dominator starts on trees with at least three vertices. For an integer game value, this is the same as the floor bound. [2, Conj. 5.3] assumes minimum degree two. [3] uses open neighborhoods in the total isolation game. The present report concerns the ordinary game, which uses closed neighborhoods.

## Project results and verified Lean endpoints

All rows concern finite simple trees with empty initial marks and history. The [Lean companion](../formal/README.md) provides the four build inputs, theorem checks and module crosswalks.

| Result | Claim | Checked endpoint |
|---|---|---|
| D6 | With $n\ge3$ and diameter at most 6, the D-start value is at most $\lfloor(2n+1)/5\rfloor\le3n/7$. | `IsolationGame.tree_diameter_six_bound` |
| D7 | With $n\ge3$ and diameter at most 7, the D-start value is at most $\lfloor3n/7\rfloor$. | `IsolationGame.DiameterSeven.tree_diameter_seven_bound` |
| D9 | With diameter at most 9, the D-start value is at most $\lceil3n/7\rceil$. | `IsolationGame.FourteenDiameterNineClosure.diameter_nine_ordinary_ceil_formula` and `actual_empty_marks_and_history`. [Report Theorem 0.1](Isolation_Game_Research_Report.pdf#page=4) |
| D10 | For every $k\ge1$, a tree has diameter 10, order $210k$, and both values at least $91k$. Its ceiling benchmark is $90k$. | `CounterexampleConcreteFinal.model_complete_counterexample`. [Appendix B](Isolation_Game_Research_Report.pdf#page=59) |

D6 and D7 establish the unrounded tree bound within their diameter ranges. The D8 example separates the floor and ceiling bounds. D9 and D10 together identify the first diameter at which the rounded D-start bound can fail. D10 refutes the ceiling conjecture in [1] and [2] for both starters and the tree conjecture in [2] for Dominator starts. Its trees have leaves, so the minimum-degree-two conjecture falls outside this construction's scope.
