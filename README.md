# BAXMAXX_analysis

Analysis, affinity-model training data preparation, and figure generation for
the MSc thesis *Affinity-Guided Generative Design of BAX-Targeting Peptides*.

The design pipeline itself lives in
[BaxMaxxCraft](https://github.com/GyulaMaloveczky/BaxMaxxCraft-BAX-Molecular-Affinity-eXtended-eXploration),
a fork of [BindCraft](https://github.com/martinpacesa/BindCraft) that adds a
learned affinity score to the discrete design search. This repository covers
everything downstream: turning MD trajectories into MM/PBSA labels, preparing
those labels for model training, and producing the thesis figures.

University of Amsterdam and Vrije Universiteit Amsterdam, computational
chemistry group. Supervisor: Dr. ir. I. M. Ilie.

---

## Scope

BindCraft selects binders on AlphaFold2 confidence. On the BAX canonical groove,
those metrics track physics-based binding energy weakly: interface pTM explains
6% of the variance in MM/PBSA and, at fixed binder length, the composite
BindCraft objective does not correlate with it. Buried interface area explains
72%. To supply the missing signal, a BALM-PPI model fine-tuned on our own
MM/PBSA labels was added to the discrete search stage, and the
design-simulation-refitting loop was run three times. The third iteration
improved mean MM/PBSA over an unguided control by 6.4 kcal/mol and occupied a
shifted region of sequence space. The second iteration, guided by a weaker
model, did neither.

![MM/PBSA against the design-time metrics. Buried interface area correlates at
r = -0.85 in the variable-length campaign; at fixed binder length interface pTM
reaches r = -0.03 and the reconstructed BindCraft objective r =
0.09.](figures/fig_correlates.png)

*The result the repository exists to support: the metrics BindCraft selects on
do not rank simulated binding energy. Produced by `dSASA.ipynb` and
`metric_corr_delta_total.ipynb`.*

---

## Setup

The notebooks read BindCraft campaign outputs and MM/PBSA results from a single
root directory, set in `paths.py`. Override it without editing the file:

```bash
export BAXMAXX_DATA=/path/to/DATA
export BAXMAXX_MODELS=/path/to/finetune_results
```

`DATA` is expected to hold one subdirectory per campaign, each containing
BindCraft's `mpnn_design_stats*.csv`, `trajectory_stats.csv`, an `Accepted/`
directory of PDBs, and the MM/PBSA results for those designs.

The data are not included in this repository, being several hundred gigabytes
of trajectories and per-design energies. They are available on request, and can
be regenerated with BaxMaxxCraft and the GROMACS protocol given in the thesis
Methods.

Some notebooks still contain absolute `/FastHome/gyula/...` paths from the
cluster on which they were run. `paths.py` is the replacement; notebooks are
being migrated to it incrementally.

---

## Notebooks by stage

### 1. Label generation and quality

| Notebook | What it does |
|---|---|
| `MMPBSA_MD_analysis.ipynb` | Main MM/PBSA processing from gmx_MMPBSA output. |
| `All_mmpbsas.ipynb` | Pools MM/PBSA across campaigns into one table. |
| `Umbrella-MMPBSA.ipynb` | Calibrates the interior dielectric against the umbrella-sampling reference free energies, giving ε = 1.5. |
| `Fidelity_check.ipynb` | Replicate agreement and the resulting reliability ceiling (r₁ = 0.815, r_kk = 0.957). |
| `RMSD_adder.ipynb` | Binder-vs-target Cα RMSD as a pose-stability diagnostic. |
| `MMPBSA_new_binders.ipynb` | MM/PBSA for later campaigns. |

### 2. What predicts MM/PBSA

| Notebook | What it does |
|---|---|
| `dSASA.ipynb` | Buried interface area against MM/PBSA. |
| `metric_corr_delta_total.ipynb` | Correlation of each design-time metric with MM/PBSA. |
| `Length_ipTM.ipynb` | Binder length against interface pTM. |
| `Rejected_accepted_analysis.ipynb` | Filter-passing vs rejected designs; includes the ipTM nonlinearity check. |
| `length_18_compare.ipynb` | Cross-campaign comparison at matched binder length. |

### 3. Affinity model

| Notebook | What it does |
|---|---|
| `PPB-Affinity_peptides.ipynb` | Prepares PPB-Affinity for pretraining; enforces the longer-chain-first ordering. |
| `PPB-Affinity Augment.ipynb` | Augmented pretraining set. |
| `Clear_BCL2_from_train.ipynb` | Removes BCL-2 family entries from the pretraining set to test memorisation. |
| `Prepare_training data.ipynb` | Builds the fine-tuning set from MM/PBSA labels. |
| `inspect_training.ipynb` | Inspects a training run from its pickled state. |
| `PPLM_analysis.ipynb` | Protein language model comparison. |

### 4. Sequence and structure analysis

![UMAP of the designs by binding orientation, with the seven natural ligands
marked, and a permutation test of between-set distance for every pair of design
sets.](figures/fig_seqspace.png)

*Designs separate by binding orientation rather than by campaign, and the
natural ligands fall inside the designed territory. Produced by
`extract_n_to_c_orientation.ipynb` and `sequence_analysis.ipynb`.*

| Notebook | What it does |
|---|---|
| `extract_n_to_c_orientation.ipynb` | Assigns each design one of the two antiparallel binding orientations from its PDB. Subsequent sequence-level analyses are computed within an orientation. |
| `sequence_analysis.ipynb` | BLOSUM80 distances, UMAP projection, sequence logos, between-set permutation test. |
| `new_seq.ipynb` | Sequence logos and PSSM analysis for later campaigns. |

### 5. Campaign comparison

![Split violin plot of MM/PBSA across the unguided control and the second and
third iterations, each violin split by binding orientation, with significance
brackets.](figures/fig_iterations.png)

*Only the third iteration improves on its predecessors. Produced by
`Test_vs_control.ipynb` and `third_iter_analysis.ipynb`.*

| Notebook | What it does |
|---|---|
| `Test_vs_control.ipynb` | Guided campaigns against the unguided control. |
| `third_iter_analysis.ipynb` | Third-iteration results. |

### Helper scripts

| Script | What it does |
|---|---|
| `paths.py` | Central path configuration. |
| `delta_G_calc.py` | Converts a dissociation constant in nM to ΔG in kcal/mol. |
| `atom_counter.py` | Counts atom types in chain B of a PDB. |
| `atom_summer.py` | Sums N, O, S, C counts across PDBs. |
| `pyrosetta_free_energy.ipynb` | PyRosetta scoring scratch. |

---

## Where the reported numbers come from

| Reported value | Notebook |
|---|---|
| dSASA explains 72% of MM/PBSA variance; interface pTM 6%, pLDDT 3% | `dSASA.ipynb`, `metric_corr_delta_total.ipynb` |
| Composite BindCraft objective, r = −0.04 at fixed length | `metric_corr_delta_total.ipynb` |
| Replicate reliability r₁ = 0.815, ceiling 0.978 | `Fidelity_check.ipynb` |
| ε_in = 1.5 from umbrella calibration | `Umbrella-MMPBSA.ipynb` |
| Two binding orientations, 291 N-proximal / 712 C-proximal | `extract_n_to_c_orientation.ipynb` |
| Third iteration displaced in sequence space, p = 0.001 | `sequence_analysis.ipynb` |
| Third iteration beats control, Holm p = 1.5 × 10⁻³ | `Test_vs_control.ipynb`, `third_iter_analysis.ipynb` |

---

## Notes

Notebook outputs are committed deliberately, so that results can be inspected
without access to the data or a GPU. This makes some notebooks large: the
largest are `MMPBSA_MD_analysis.ipynb` (7 MB) and `sequence_analysis.ipynb`
(3.6 MB).

## Citation

See `CITATION.cff`. If you use the design pipeline, please also cite
[BindCraft](https://www.nature.com/articles/s41586-025-09429-6).
