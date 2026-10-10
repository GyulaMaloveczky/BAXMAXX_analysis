# Jupyter notebook cleanup plan

This repository has a large set of notebooks, many of which were originally created as one-off exploratory analyses. To make the project easier to maintain, the canonical workflow is now organized by analysis stage.

## Stage map

- `01_label_generation/` — MM/PBSA processing, aggregate labels, and quality checks
- `02_metric_analysis/` — design metrics and physical-energy correlation studies
- `03_affinity_model/` — training data and model selection logic
- `04_sequence_structure/` — orientation classification and sequence-space analysis
- `05_campaign_comparison/` — final comparison against controls and iterations
- `legacy/` — notebooks retained for historical context but not part of the primary workflow

## Guidance

- Prefer the canonical stage folders when rerunning the analysis.
- Keep exploratory analyses in `legacy/` rather than cluttering the root directory.
- Use `paths.py` to avoid hardcoded cluster paths.
- Treat notebooks as analytical steps, not as ad hoc scripts.
