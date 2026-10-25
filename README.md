# Anonymous Review Artifact

Download all ZIP files into one directory and run `python setup_review.py` to extract them into `review/`. Then follow `review/README.md`. Source and data archives contain only the curated release manifest.

# Rank-Based Competition: Anonymous Review Artifact

Code and sanitized recorded decisions supporting *Collective Behavior in Rank-Based Competition among LLM Agents*.

## Offline reproduction

Python 3.10 or later is required. From this directory:

```sh
python -m venv .venv
# Activate the virtual environment using your platform's command.
python -m pip install -r requirements.txt
python unpack_artifacts.py
python verify_release.py
```

The verification independently reconstructs scoring for 16 LLM configurations and their 16 paired Bayesian runs (320,000 agent-round records), and checks investment, selection quality and prize-normalized dissipation against the supplied tables. No LLM API calls are made.

## Contents and paper mapping

| Paper component | Entry point | Inputs / outputs |
|---|---|---|
| Competition environment and adaptive agents | `involution/src/`, `involution/baseline/purebayes_baseline.py` | Executable scoring, prompts, rolling memory and benchmark |
| Aggregate investment and collective outcomes | `prepare_global_std1.py` | Reconstructs all 16 configurations into `output/global_std1_story/metrics_all_std1.csv` |
| Shared rationale clustering and PCA | `strategy_pca.py`, `strategy_group.py` | Twelve main configurations; output in `pic/` |
| Ability, rank, investment and wealth | `ability-rank.py` | Main-grid recorded decisions; output in `pic/` |
| Rationale coding | `label_reasons.py` | Codebook and matching rules in `reason_analysis/labeled_v1/`; archived labels are bundled |
| Matched reasoning comparisons | `analyze_reasoning_section43.py` | Bundled labels, focus table and shared PCA snapshot; output in `output/reasoning43_reanalysis_20261022/` |
| Reasoning figures | `prepare_reasoning43_paper_figures.py`, `compact_reasoning43_matching.py` | Matched-analysis tables |
| Collective-outcome figures | `plot_collective_outcomes_v2.py`, `plot_quadrant_single_column.py` | Audited grid and budget comparison tables |
| Budget-controlled figure | `plot_fixed_budget_llm_only.py` | `output/fixed_P250000_complete/all_current_metrics.csv` |

For example, after unpacking:

```sh
python prepare_global_std1.py
python plot_collective_outcomes_v2.py
python plot_fixed_budget_llm_only.py
python analyze_reasoning_section43.py
python prepare_reasoning43_paper_figures.py
```

The included `pic/pca_global_coordinates.npz` preserves the original fitted snapshot assignments. Re-running `strategy_pca.py` recomputes clustering and overwrites this file; preserve it separately if comparing recomputed assignments with the archived reasoning analysis. Font availability and library versions may change figure appearance. Plot scripts reproduce scientific content; they do not promise identical final manuscript layout.

## Run new simulations

```sh
cd involution
python main.py --experiment 1b --config config/experiment_config.yaml
```

This runs the Bayesian main grid. The default command selects the benchmark, rather than paid LLM execution. To run new LLM experiments, explicitly set `LLM_API_KEY`, `LLM_MODEL` and optionally `LLM_BASE_URL` in your environment, then use `--experiment 1l`. The model ID placeholder must be replaced by an available model. Credentials are never distributed. New outputs use the runner's working-directory-relative layout; they do not replace the archived review data automatically.

The release configuration describes the paper's main grid (N=200, T=50, q=0.1/0.4/0.7, R=2500/5000/10000/20000). It is a reproduction template, not proof of the backend model identity used in historical runs. Historical runtime configurations are bundled with their runs where available, with credentials removed. Model/API changes prevent a claim of bitwise reproduction of LLM generations. The four additional budget configurations are documented in `artifacts/run_inventory.json` and their bundled configurations.

## Interpretation and scope

- Main results contain 12 reward-grid configurations plus four additional budget configurations, with one LLM run per configuration and benchmark seed 0.
- The q=0.06, R=20000 configuration has P=240000; the other three budget-path configurations have P=250000.
- Investment totals are reconstructed from saved rounds. Saved final ranks and reconstructed ranks can differ in resumed runs; both outcomes and ledger diagnostics are reported by the audit.
- The Bayesian system is an adaptive approximation, not an equilibrium or optimality bound. It receives an initial private rank signal while LLM agents initially do not.
- Reason codes are rule-based descriptive labels, not validated psychological states or causal effects. There is no inference based on treating agent-rounds as independent replications.
- Archived Claude / alternative-scoring and ability-dispersion supplementary experiments are not included in this main-result artifact. The included appendix source describes their limitations; this release does not claim to reproduce those supplementary plots.

Redundant figures, manuscript builds, screenshots, temporary revisions, virtual environments, caches, credentials and Git history are excluded. Data are compressed per run to keep individual repository files small. Run `unpack_artifacts.py` before analysis. The supplied code and records are provided for review; no new open-source license is asserted on behalf of the authors.
