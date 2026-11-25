# Isolation Game on Trees: From Diameter 9 to 10

**English** · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Português](README.pt.md) · [Project website](https://prooflog553.github.io/isolation-game-on-trees-exhibit/?lang=en)

**How does the diameter of a tree constrain the length of an isolation game?** For a proposed ceiling bound, the answer turns on the passage from diameter 9 to diameter 10.

[**Read the paper (PDF)**](manuscript/Isolation_Game_Research_Report.pdf) · [**Explore the Lean sources and builds**](formal/README.md) · [**Play online**](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html?lang=en)

## Abstract

In the isolation game, two players choose vertices in turn: one aims to finish quickly, while the other tries to prolong play. For a tree on $n$ vertices, can Dominator, moving first, always finish within $\lceil 3n/7\rceil$ moves? This project studies that question through the **diameter** of the tree and identifies an exact threshold.

For every finite tree of diameter at most **9**, the ceiling bound holds when Dominator starts. At diameter **10**, for every positive integer $k$, we construct a tree on $210k$ vertices that requires at least $91k$ moves under optimal play, whichever player starts; its ceiling benchmark is only $90k$. Thus the counterexample appears at diameter 10, and its excess over the benchmark grows by at least $k$.

The upper-bound proof combines structural reductions, finite certificates and strategies for 14 families with arbitrarily many ordinary branches. The lower bound uses a scalable modular construction and a corresponding strategy. The repository brings together the paper, formal sources, replays and interactive exhibits so that readers can examine the result from several directions.

![From the diameter-9 upper bound to the diameter-10 counterexample family](assets/diameter-threshold.svg)

## The question

In the ordinary isolation game, a move covers the chosen vertex and its neighbors. It is legal only if it newly covers an endpoint of an edge whose endpoints were both uncovered before the move. The game ends when every edge has a covered endpoint. Dominator minimizes the number of moves; Staller maximizes it. A tree's diameter is the greatest distance between two vertices, measured in edges.

Earlier work posed conjectures of the $3n/7$ form for game length. This project initially investigated the stronger floor bound, but a small example changed the question. Add one leaf at the center of a **22-vertex, diameter-8** tree: its diameter stays the same, while its optimal Dominator-start value rises from **9** to **10**. At 23 vertices the floor is 9 and the ceiling is 10. The investigation then asked how far the ceiling bound extends, and where it first fails. [References and theorem scope](manuscript/SOURCES.md) · [Replay the example](REPRODUCE.md)

## Results and scope

| Result | Statement |
|---|---|
| **Diameter at most 9** | On every finite tree with $n$ vertices, in ordinary play from an initially uncovered position, Dominator can finish within $\lceil3n/7\rceil$ moves when starting. This project does not establish the same bound for Staller starts. |
| **Diameter exactly 10** | For every positive integer $k$, a tree on $210k$ vertices has game value at least $91k$ for either starting player; its ceiling benchmark is $90k$. The number $91k$ is a lower bound, not a claim of exact value. |
| **Proof approach** | D9 uses structural reductions and finite classification to reach 14 candidate families, then supplies strategies for arbitrarily many ordinary branches. D10 connects 15-vertex modules to form an infinite counterexample family. |

Together, the two results show that **10 is the first diameter at which the rounded Dominator-start bound can fail on a tree**. The D10 lower bound also covers Staller starts; it does not settle the Staller-start upper bound through diameter 9. [Proof and evidence map](EVIDENCE_MAP.md)

## Explore the work

| If you want to… | Start here |
|---|---|
| **Read the proofs** | [Full paper](manuscript/Isolation_Game_Research_Report.pdf) · [Proof map and D9 example](EVIDENCE_MAP.md) · [References and theorem scope](manuscript/SOURCES.md) |
| **Inspect formal verification** | [Lean sources and build instructions for D6, D7, D9 and D10](formal/README.md) |
| **Try the examples** | [Online board](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html?lang=en) · [Zoomable D10 construction](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/d10.html?lang=en) · [Board instructions](demo/README.md) |
| **Reproduce checks** | [Python examples, finite certificates and reproduction guide](REPRODUCE.md) |
| **Follow the research** | [How AI worked through failed openings, counterexamples and proof revisions](RESEARCH.md) |

For a quick example, play **2** and then the already covered vertex **3** on the path $1—2—3—4—5$. A covered vertex remains playable whenever the legality condition is met.

Archive curation and maintenance by Cen Yi (岑弈). [Material-specific rights and notices](LICENSE_SCOPE.md)
