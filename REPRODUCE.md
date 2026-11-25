# Reproduce the exhibits / 复算指南

[English home](README.md) · [中文首页](README.zh-Hans.md) · [Evidence map / 证据导航](EVIDENCE_MAP.md)

Download the repository ZIP from GitHub or clone it, then open a terminal in the directory containing this file. The scripts use the Python 3 standard library. Run them without `-O`, since the verifiers use assertions. On Windows, `py -3` can replace `python3`.

下载、解压后在含本文件的目录中打开终端。两个网页可以直接打开，脚本只需 Python 3 标准库。请保留断言检查。

## Replay the examples / 复算案例

```sh
python3 -I ai-cases/check_ai_case_p9_d8.py
python3 -I ai-cases/check_ai_case_d9.py
```

The first script checks the P9 center opening and the two D8 trees. The D-start values are 3 versus 4 for the free and center-forced P9 openings, and 9 versus 10 for the two D8 trees. The second script checks a failed local-rule generalization on marked forests. Its D-start value changes from 9 to 13 and its S-start value from 10 to 13.

## Check the finite certificates / 核验有限证书

Extract [supplemental.zip](supplemental.zip) into a separate directory and run these commands from the extraction root.

```sh
python3 -I supplemental/finite_certificates/verify_certificates.py
python3 -I supplemental/verify_supplement.py
```

The first verifier checks 2,745 reachable local states and 5,340 classification candidates, with 14 retained classes. The second checks the 239-row supplement. The general proof and the scope of each certificate are in the [report](manuscript/Isolation_Game_Research_Report.pdf).

## Open the browser exhibits / 打开交互演示

Try the [online board](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/index.html) or the [interactive D10 diagram](https://prooflog553.github.io/isolation-game-on-trees-exhibit/demo/d10.html). After extracting the repository ZIP, both HTML files can also run locally. [Offline steps](demo/README.md)

## Rebuild Lean / 重建 Lean

Use the [public Lean companion](formal/README.md) for four source targets, the Lean 4.19.0 toolchain, full theorem checks and D9/D10 build crosswalks. The [sources table](manuscript/SOURCES.md) records the mathematical scope of each endpoint. The [SHA-256 manifest](SHA256SUMS.txt) lists the other files in the current repository release.
