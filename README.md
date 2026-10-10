# BAXMAXX_analysis

Analysis, affinity-model training data preparation, and figure generation for the MSc thesis project on affinity-guided peptide design.

## Scope

This repository contains the downstream workflow for the BAX design campaign:

- MM/PBSA label generation from simulation outputs
- data preparation for affinity-model training
- correlation analysis between design metrics and physical binding signal
- sequence/orientation analysis of accepted designs
- campaign-comparison analysis and figure generation

The design pipeline itself lives in a separate project; this repository focuses on analysis and downstream modeling.

## Project structure

The repository is organized by analysis stage to reduce clutter and make the workflow clearer.

- `notebooks/01_label_generation/` — MM/PBSA assembly and validation
- `notebooks/02_metric_analysis/` — correlation and design-metric analysis
- `notebooks/03_affinity_model/` — training-data prep and model inspection
- `notebooks/04_sequence_structure/` — orientation, sequence, and structural analysis
- `notebooks/05_campaign_comparison/` — final campaign-vs-control comparisons
- `notebooks/legacy/` — historical exploratory notebooks
- `scripts/` — reusable helper utilities
- `figures/` — final figure assets
- `docs/` — project discussion and layout notes

## Environment setup

The notebooks should not rely on machine-specific absolute paths. Use environment variables or the central `paths.py` config.

```bash
export BAXMAXX_DATA=/path/to/DATA
export BAXMAXX_MODELS=/path/to/finetune_results
```

## Quick start

1. Configure the environment.
2. Inspect the stage-by-stage notebook folders.
3. Run the label-generation notebooks first.
4. Then move through the analysis, model-training, and sequence-analysis sections.
5. Use the final comparison notebooks for reporting and figure creation.

## Reproducibility notes

Notebook outputs are intentionally retained so results can be inspected without rerunning the full analysis pipeline. Large notebooks remain in the repository for traceability, but the workflow should be read in the order described above.

## Notes

This cleanup is deliberately opinionated: it favors clarity, reproducible workflow ordering, and separation of canonical analysis from exploratory legacy work.
