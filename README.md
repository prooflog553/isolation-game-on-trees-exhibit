# Isolation Game on Trees

**English** · [简体中文](README.zh-Hans.md)

How long can Staller keep an isolation game going on a tree? When Dominator starts, the ceiling of $3n/7$ bounds the game through diameter 9. At diameter 10, an infinite family exceeds that ceiling for either starter.

## A five-minute introduction

| Start here | What you will find |
|---|---|
| [Play the game](demo/README.md) | Download the browser board, choose either starter, and see the optimal moves |
| [See the graphs behind the proofs](EVIDENCE_MAP.md) | A concrete D9 proof case and a zoomable D10 construction |
| [Read the report](manuscript/Isolation_Game_Research_Report.pdf) | The mathematical arguments and [published references](manuscript/SOURCES.md) |
| [Reproduce the calculations](REPRODUCE.md) | Python replays and finite certificates |
| [Follow the research](RESEARCH.md) | Failed strategies, counterexamples and proof repairs |

## How to play

Players take turns choosing a vertex. Each move covers that vertex and its neighbors. A move is legal if it newly covers an endpoint of an edge whose two endpoints were uncovered. The game ends when there are no such edges. Dominator tries to finish quickly and Staller tries to prolong play.

On `1—2—3—4—5`, choose **2**. The only edge with both ends uncovered is now **4—5**. Choose **3**, which is already covered, to cover **4** and finish the game. [Try it on the board](demo/README.md)

A tree's diameter is its greatest distance between vertices, measured in edges. For every positive integer $k$, the diameter-10 construction has $210k$ vertices and requires at least $91k$ moves under optimal play for each starter. Its rounded benchmark is $90k$. [See the construction](demo/d10.html)

Archive curation and maintenance by Cen Yi (岑弈). [Material-specific rights and notices](LICENSE_SCOPE.md)
