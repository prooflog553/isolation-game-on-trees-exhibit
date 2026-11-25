# Lean source and replay / Lean 源码与复现

[Full paper / 完整论文](../manuscript/Isolation_Game_Research_Report.pdf) · [Reproduction guide / 复现](../REPRODUCE.md) · [中文首页](../README.zh-Hans.md)

All four targets use **Lean 4.19.0**. The complete non-core build inputs for D9 and D10 comprise 1,566 and 1,006 modules respectively. D6 and D7 use locked Lake projects. The official precompiled Lean core is installed separately. The build results cited below are from the documented 25 November 2026 replay of these source bytes.

| Target | Public source | Statement to check |
|---|---|---|
| D6 | [Lake project ZIP](D6-L3.zip) · [audit source](D6/MainAudit.lean) | `IsolationGame.tree_diameter_six_bound` |
| D7 | [Lake project ZIP](D7-L3.zip) · [audit source](D7/MainAudit.lean) | `IsolationGame.DiameterSeven.tree_diameter_seven_bound` |
| D9 | [Main source](D9/FourteenDiameterNineClosure.lean) · [module crosswalk](D9/build-crosswalk.csv) · [D9/D10 source bundle](D9-D10-lean-sources.tar.xz) | `IsolationGame.FourteenDiameterNineClosure.diameter_nine_ordinary_ceil_formula` |
| D10 | [Main source](D10/FinalDiameterCounterexample.lean) · [module crosswalk](D10/build-crosswalk.csv) · [D9/D10 source bundle](D9-D10-lean-sources.tar.xz) | `CounterexampleConcreteFinal.model_complete_counterexample` |

中文读者可以直接下载四个结果的源码。从 D9 和 D10 的两个主文件可定位定理，完整源码包含传递依赖、逐模块哈希清单、主定理与公理检查脚本以及上游许可声明。

The D9 entry preserves an early candidate-stage comment. The file's source hash matches the successful historical build in the public crosswalk. D9 applies to ordinary Dominator-start play, while D10 gives lower bounds for both starters. [Manuscript theorem scopes](../manuscript/SOURCES.md)

## Build D9 and D10

Use Python 3.12 and the [official Lean 4.19.0 release](https://github.com/leanprover/lean4/releases/tag/v4.19.0). The following PowerShell commands run in a fresh working directory. Copy `D9-D10-lean-sources.tar.xz` and [rebuild_closure.py](rebuild_closure.py) into it, and set `$lean` to the path of Lean 4.19.0's `bin/lean.exe`.

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

The builder checks every source hash before compiling and records progress in a new run directory. A successful D9 run reports 1,566 completed non-core modules. D10 reports 1,006. Use fewer workers on a memory-constrained machine.

To rerun the theorem checks, set `$target` to `D9` or `D10` and `$run` to the absolute path of its successful run directory.

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

The crosswalk pairs source hashes with the objects from the accepted historical build. Object bytes may differ with platform or compiler environment. The checked theorem types and axioms are the semantic results. Both main audits identified `propext`, `Classical.choice` and `Quot.sound` as the recursive axioms.

## Build D6 and D7

Install Elan and Git, then extract each ZIP into its own working directory. Run the following from the inner `D6` or `D7` folder containing `lakefile.toml`. Set `$audit` to the absolute path of the corresponding `MainAudit.lean` linked above.

```powershell
lake build
if ($LASTEXITCODE -ne 0) { throw 'Lake build failed' }
lake env lean $audit
if ($LASTEXITCODE -ne 0) { throw 'Lean theorem audit failed' }
```

Lake uses the included `lean-toolchain` and `lake-manifest.json`. Building dependencies can require access to the pinned upstream repositories and Node.js/npm for ProofWidgets. The [dependency-source inventory](dependency-lock.json) supplies upstream provenance. The [material-specific terms](../LICENSE_SCOPE.md) describe the project files and retained notices.
