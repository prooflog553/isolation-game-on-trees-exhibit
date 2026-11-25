# Isolation Game on Trees

**English** · [简体中文](README.zh-Hans.md) · [Project website](https://prooflog553.github.io/isolation-game-on-trees-exhibit/?lang=en)

**The rounded upper bound holds for Dominator-start play on every tree through diameter 9. An infinite family breaks it at diameter 10 for either starting player.**

[**Full paper (PDF)**](manuscript/Isolation_Game_Research_Report.pdf) · [**Lean source and builds**](formal/README.md) · [**Play online**](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html)

![The diameter threshold from 9 to 10](assets/diameter-threshold.svg)

## What we established

| Result | What it says |
|---|---|
| **Exact diameter threshold** | On every finite tree of order $n$ and diameter at most 9, Dominator can finish in at most $\lceil3n/7\rceil$ moves when starting. |
| **Infinite obstruction with a growing gap** | For each positive integer $k$, a diameter-10 tree on $210k$ vertices requires at least $91k$ moves for either starter under optimal play. The conjectured ceiling is $90k$. |
| **A small example that changed the question** | Adding one leaf preserves diameter 8 and raises the D-start value from 9 to 10. At 23 vertices the floor is 9 and the ceiling is 10. |

## Why it matters

The result pinpoints **where the rounded conjecture first fails on trees**. At the boundary, the counterexample gap grows by at least $k$. The upper-bound proof shows how to use finite certificates in an unbounded minimax problem. Structural reductions limit the exceptional branches, while strategies for 14 families handle arbitrarily many ordinary branches.

The exhibit makes the AI-led research inspectable. Readers can replay the failed center opening, reproduce the one-leaf counterexample, and inspect the Lean proof endpoints. [Research process and failed attempts](RESEARCH.md)

## Explore and reproduce

| Start here | What to open |
|---|---|
| **Paper and proof map** | [Full paper (PDF)](manuscript/Isolation_Game_Research_Report.pdf) · [Proof map and D9 example](EVIDENCE_MAP.md) · [References and theorem scope](manuscript/SOURCES.md) |
| **Formal verification** | [D6, D7, D9 and D10 source and builds](formal/README.md) · [D9 main Lean file](formal/D9/FourteenDiameterNineClosure.lean) · [D10 main Lean file](formal/D10/FinalDiameterCounterexample.lean) |
| **Interactive exhibits** | [Online board](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html) · [Zoomable D10 construction](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/d10.html) · [Offline instructions](demo/README.md) |
| **Independent checks** | [Run the Python replays and finite certificates](REPRODUCE.md) |

Each turn covers the chosen vertex and its neighbors. A move must newly cover an endpoint of an edge with two uncovered endpoints. Dominator wants to finish quickly, and Staller wants to prolong play. On the five-vertex path, choose **2** then **3** to see when an already covered vertex can still be played.

Archive curation and maintenance by Cen Yi (岑弈). [Material-specific rights and notices](LICENSE_SCOPE.md)
