# 复算指南

[中文首页](README.zh-Hans.md) · [English](REPRODUCE.md) · [证据与证明导航](EVIDENCE_MAP.zh-Hans.md)

从 GitHub 下载并解压仓库 ZIP，或克隆仓库，然后在包含本文件的目录中打开终端。脚本只使用 Python 3 标准库。验证器依赖断言，请勿使用 `-O` 运行。在 Windows 上，可以用 `py -3` 代替 `python3`。

## 复算案例

```sh
python3 -I ai-cases/check_ai_case_p9_d8.py
python3 -I ai-cases/check_ai_case_d9.py
```

第一个脚本检查 P9 的中心首着和两棵 D8 树。P9 在 Dominator 自由选择首着和固定选择中心时的最优手数分别为 3 和 4；两棵 D8 树的 Dominator 先手值分别为 9 和 10。第二个脚本检查预标记森林中一条局部规则的失败推广：Dominator 先手值从 9 变为 13，Staller 先手值从 10 变为 13。

## 核验有限证书

将 [supplemental.zip](supplemental.zip) 解压到单独目录，在解压后的根目录运行：

```sh
python3 -I supplemental/finite_certificates/verify_certificates.py
python3 -I supplemental/verify_supplement.py
```

第一个验证器检查 2,745 个可达局部状态和 5,340 个分类候选项，保留其中 14 类。第二个验证器检查包含 239 行的补充材料。一般证明及各证书的适用范围见[研究报告](manuscript/Isolation_Game_Research_Report.pdf)。

## 打开交互演示

可以使用[在线棋盘](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html)或 [D10 交互构造图](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/d10.html)。解压仓库 ZIP 后，两个 HTML 文件也可在本地打开。[离线使用说明](demo/README.zh-Hans.md)

## 重建 Lean

[Lean 复现说明](formal/README.zh-Hans.md)提供四个目标的源码、Lean 4.19.0 工具链、完整定理检查和 D9/D10 构建对照表。[定理对照表](manuscript/SOURCES.zh-Hans.md)记录各结论的数学范围。[SHA-256 清单](SHA256SUMS.txt)列出当前仓库版本中其他文件的校验值。
