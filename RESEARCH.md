# Research process / 研究过程

[English home](README.md) · [中文首页](README.zh-Hans.md) · [Reproduce the checks / 运行复算](REPRODUCE.md)

AI systems proposed strategies and constructions, developed mathematical arguments, wrote verification code, and challenged proofs. The human chose the research goals, decided which routes to pursue and requested adversarial checks. The report describes these roles on p. 2. [Research report](manuscript/Isolation_Game_Research_Report.pdf#page=2)

AI 参与构造、证明、代码与技术审查。人确定研究目标，取舍路线，并要求对抗性核验。下表保留几次影响结论的失败与修正。早期过程的原始证据仍有缺页。

| What was tried / 尝试 | What the check changed / 核验后的修正 |
|---|---|
| Start at the center / 中心首着 | On the nine-vertex path, playing the center takes four moves. The optimal free Dominator opening takes three. 九点路径已足以推翻通用中心开局规则。 |
| Use the unrounded bound / 沿用不取整的界 | Adding one central leaf gives a diameter-8 tree of order 23 whose D-start value is 10. The floor is 9 and the ceiling is 10. 一片叶子使下取整界失效，研究转向上取整界。 |
| Identify the D7 local position / 对应 D7 的局部状态 | The correct marked root is `x`. The final Lean statement also discharges the small-order obligation. 根的位置和小阶前提分别修正。 |
| Apply a universal seven-vertex move budget / 直接套用七点增量规则 | The D9 replay exhibits marked forests where adding the branch increases the D-start value by four. The final D9 proof handles arbitrary branch counts through family-specific budgets. 局部合并规则需要条件，最终证明逐族处理任意参数。 |
| Build a scalable diameter-10 obstruction / 构造可扩展的直径 10 反例 | Join 15-vertex modules by their centers in a star. The proof gives a lower bound for both starters and applies to every positive integer parameter. [View the construction / 查看构造](demo/d10.html) |

Run the P9, D8 and D9 calculations in the [reproduction guide](REPRODUCE.md). Read the general D9 and D10 proofs through the [evidence map](EVIDENCE_MAP.md).
