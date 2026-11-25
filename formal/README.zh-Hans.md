# Lean 源码与复现

[English](README.md) · [完整论文](../manuscript/Isolation_Game_Research_Report.pdf) · [复算指南](../REPRODUCE.zh-Hans.md)

四个目标均使用 **Lean 4.19.0**。D9 和 D10 的完整非核心构建输入分别包含 1,566 和 1,006 个模块；D6 和 D7 使用锁定依赖的 Lake 工程。官方预编译 Lean 核心需另行安装。下述构建结果来自 2026 年 11 月 25 日对这些源码字节的有记录复现。

| 目标 | 公开源码 | 核验定理 |
|---|---|---|
| D6 | [Lake 工程 ZIP](D6-L3.zip) · [审计源码](D6/MainAudit.lean) | `IsolationGame.tree_diameter_six_bound` |
| D7 | [Lake 工程 ZIP](D7-L3.zip) · [审计源码](D7/MainAudit.lean) | `IsolationGame.DiameterSeven.tree_diameter_seven_bound` |
| D9 | [主源码](D9/FourteenDiameterNineClosure.lean) · [模块对照表](D9/build-crosswalk.csv) · [D9/D10 源码包](D9-D10-lean-sources.tar.xz) | `IsolationGame.FourteenDiameterNineClosure.diameter_nine_ordinary_ceil_formula` |
| D10 | [主源码](D10/FinalDiameterCounterexample.lean) · [模块对照表](D10/build-crosswalk.csv) · [D9/D10 源码包](D9-D10-lean-sources.tar.xz) | `CounterexampleConcreteFinal.model_complete_counterexample` |

D9 和 D10 的主文件可用于定位定理；完整源码包含传递依赖、逐模块哈希清单、主定理与公理检查脚本，以及上游许可声明。D9 入口保留了一条早期候选阶段的注释，其源码哈希与公开对照表中历史成功构建的源码一致。D9 适用于普通 Dominator 先手博弈，D10 给出两种先手各自的下界。[论文定理范围](../manuscript/SOURCES.zh-Hans.md)

## 构建 D9 和 D10

使用 Python 3.12 和 [Lean 4.19.0 官方发行版](https://github.com/leanprover/lean4/releases/tag/v4.19.0)。在新的工作目录中执行下列 PowerShell 命令。先将 `D9-D10-lean-sources.tar.xz` 与 [rebuild_closure.py](rebuild_closure.py) 复制到该目录，再将 `$lean` 设为 Lean 4.19.0 的 `bin/lean.exe` 路径。

```powershell
python -m tarfile -e D9-D10-lean-sources.tar.xz .
& $lean --version
python -I rebuild_closure.py D9 --verify-only
python -I rebuild_closure.py D10 --verify-only
$env:LEAN_BUILD_WORKERS = '2'
python -I -u rebuild_closure.py D9 $lean
if ($LASTEXITCODE -ne 0) { throw 'D9 compilation failed' }
python -I -u rebuild_closure.py D10 $lean
if ($LASTEXITCODE -ne 0) { throw 'D10 compilation failed' }
```

构建器在编译前检查每个源码文件的哈希，并在新的运行目录中记录进度。D9 成功运行时报告完成 1,566 个非核心模块，D10 报告 1,006 个。内存不足时请减少工作进程数。

要重新运行定理检查，将 `$target` 设为 `D9` 或 `D10`，将 `$run` 设为对应成功运行目录的绝对路径。

```powershell
$env:LEAN_PATH = Join-Path $run 'lib'
$env:LEAN_SRC_PATH = (Resolve-Path "source_d9_d10/$target/src").Path
$checks = (Resolve-Path "source_d9_d10/$target/checks").Path
Push-Location $env:LEAN_SRC_PATH
try {
  foreach ($check in 'MainAudit', 'MainFullTypes') {
    & $lean -j1 -R $env:LEAN_SRC_PATH (Join-Path $checks "DOTS_$check.lean")
    if ($LASTEXITCODE -ne 0) { throw "$target $check failed" }
  }
} finally { Pop-Location }
```

构建对照表将源码哈希与历史成功构建中的对象文件对应起来。对象文件字节可能因平台或编译环境而异；所检查的定理类型和公理是语义核验结果。两项主审计均将 `propext`、`Classical.choice` 和 `Quot.sound` 列为递归依赖的公理。

## 构建 D6 和 D7

安装 Elan 和 Git，将两个 ZIP 分别解压到各自的工作目录。从包含 `lakefile.toml` 的内层 `D6` 或 `D7` 目录运行以下命令，将 `$audit` 设为上表中相应 `MainAudit.lean` 文件的绝对路径。

```powershell
lake build
if ($LASTEXITCODE -ne 0) { throw 'Lake build failed' }
lake env lean $audit
if ($LASTEXITCODE -ne 0) { throw 'Lean theorem audit failed' }
```

Lake 使用随包提供的 `lean-toolchain` 和 `lake-manifest.json`。构建依赖可能需要访问固定版本的上游仓库，并需要 Node.js/npm 来构建 ProofWidgets。[依赖源码清单](dependency-lock.json)记录上游来源；[逐材料许可说明](../LICENSE_SCOPE.md)说明项目文件及保留的声明。
