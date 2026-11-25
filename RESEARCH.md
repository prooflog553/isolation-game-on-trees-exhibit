# How AI worked through the Isolation Game on Trees

[简体中文](RESEARCH.zh-Hans.md) · [Project home](README.md) · [Full paper](manuscript/Isolation_Game_Research_Report.pdf) · [Lean source](formal/README.md)

The investigation began with an attempt to prove a move bound. A failed opening strategy forced a change in proof approach. A one-leaf counterexample then forced a change in the question itself. AI developed a counterexample family at diameter 10 and closed the general upper bound through diameter 9. The account below paraphrases surviving research exchanges and separates what was reported at the time from what readers can verify today.

## 1. A nine-vertex path defeats the center opening

A tree center is close to every vertex, so starting there looks natural. Records from 11 September already show the strategy meeting exceptions. On 13 September, the human asked for counterexamples first, specifically whether starting at the center could cost an extra move.

AI reported the nine-vertex path. Starting at vertex 5 takes four moves under optimal continuation. A free Dominator opening at vertex 2 or 3 finishes in three. The result removed a proof shortcut and left the real upper-bound obligation in place. A successful proof would have to find a sufficiently good opening for every tree in scope.

**Try it.** Select `P9` and compare vertices 5 and 2, or run the exact solver for all nine first moves. [Online board](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html) · [Replay script](ai-cases/check_ai_case_p9_d8.py)

## 2. One extra leaf overturns the original bound

On 29 September, the human asked AI to challenge two local lemmas and then test shallow leaves near the center. AI reported that the lemmas survived under their stated conditions and produced a counterexample to the original target.

Join the midpoints of three disjoint seven-vertex paths to a common center. This gives a 22-vertex tree of diameter 8. Attach one leaf to the center. The diameter is still 8, but the optimal Dominator-start value rises from 9 to 10. The floor at order 23 is 9. AI proposed switching to the ceiling, and the human approved the change on 30 September. The ceiling for this same tree is 10.

**Verify it.** The replay generates both trees, checks their diameters and solves their free and center-forced openings. [One-leaf diagram](assets/d8-one-leaf.svg) · [Reproduction commands](REPRODUCE.md)

## 3. From diameter 12 to diameter 10

On 30 September, an AI reply already described a diameter-12 family built with 23-vertex modules. In the surviving account of tests joining two modules, 10 of 21 connection classes were completed. The other 11 reached time or state limits and were recorded as unresolved. The public replays do not reproduce that historical search.

The human approved continuing the investigation. In the earliest recovered D10 exchange, the concrete construction appeared in the AI reply. It replaced the larger modules with 15-vertex ones. Each module has its own center, joined to the midpoints of two seven-vertex paths. Linking the existing centers of $14k$ modules into a star adds only edges. This gives $210k$ vertices and a longest path of $4+2+4=10$ edges.

That reply gave the Dominator-start lower bound of $91k$. The final proof controls the center phase before comparing the remaining endpoint game. It establishes at least $91k$ moves for either starter, against the ceiling $90k$. When the D10 construction appears in the surviving record, the general D9 upper bound is still open. [Interactive construction](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/d10.html) · [Appendix B](manuscript/Isolation_Game_Research_Report.pdf#page=59) · [D10 Lean theorem](formal/D10/FinalDiameterCounterexample.lean)

## 4. Where the D9 proof broke and how it was repaired

D9 must allow arbitrarily many ordinary branches. A 30 September exchange gives an exact negative control on two premarked forests. Adding one seven-vertex path changes the Dominator-start value from 9 to 13 and the Staller-start value from 10 to 13. The example defeats a blanket three-move rule for adding such a path. The theorem concerns ordinary play on connected trees from an empty start.

The human requested an adversarial review of the candidate proof. The first review called for major revision. It found that leaves of some finite certificates still depended on incomplete mathematical rules. It also challenged the step from bounded calculations to arbitrarily many branches. In the revision, AI supplied conditions for the rules and established budgets for 14 candidate families at every allowed multiplicity. For example, `r00` has $14+7(p+q)$ vertices and a proved budget of $6+3(p+q)$ moves for arbitrary nonnegative $p,q$.

The finite check covers the local structure, and the strategy proof handles the unbounded parameters. The later Lean build checks the resulting diameter-at-most-9 ceiling for ordinary Dominator-start play. The corresponding universal Staller-start ceiling remains open in this work. [Replay the negative control](ai-cases/check_ai_case_d9.py) · [Family budgets on p. 55](manuscript/Isolation_Game_Research_Report.pdf#page=55) · [D9 Lean build and theorem evidence](formal/README.md)

## A formalization correction in D7

For a 16-vertex tree, the actual residual game maps to an auxiliary graph with two adjacent roots. The premarked root has one attached arm and corresponds to `x`. Marking `y` changes the game state. AI corrected the correspondence. A later formal revision proved the small-order bound that an earlier assembly had assumed and supplied it inside the project. The two changes address different proof obligations. [D7 source project](formal/D7-L3.zip) · [D7 theorem entry](formal/README.md)

## What readers can check

| Evidence | Question it answers |
|---|---|
| The paraphrased exchanges and revision record | Who set the next task, what AI proposed, and what changed after a failure |
| Browser play and exact Python replays | The value of a specific opening, counterexample or negative control |
| Paper, finite certificates and Lean | The scope of the final theorems and how the finite and unbounded parts fit together |

The earliest proposal of the center-opening idea, any earlier D10 draft and the complete trial sequence have gaps. The surviving records support the turning points presented here. [Reproduction and verification guide](REPRODUCE.md)
