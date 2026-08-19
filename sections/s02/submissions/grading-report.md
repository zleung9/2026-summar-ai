# Section 2 Homework Completion Report

> Reviewed: August 6, 2026  
> Scope: notebooks in `sections/s02/submissions/`, their saved execution state, and locally available pull-request history

## Grading Method

Each submission was evaluated against `sections/s02/homework.md` and the instructor reference in `sections/s02/answer-key.md`.

| Area | Points |
|---|---:|
| Submission and reproducibility | 10 |
| Dataset audit and data-quality reasoning | 15 |
| Descriptive statistics, distributions, and outlier investigation | 20 |
| Pearson/Spearman relationships and mathematical dependencies | 15 |
| Standardization and PCA | 20 |
| Critical-question answers and use of evidence | 15 |
| AI-review reflection | 5 |
| **Total** | **100** |

Status meanings:

- **Complete:** meets the core learning goal; small corrections may remain.
- **Revision required:** substantial work exists, but one or more required skills are not yet demonstrated reliably.

The review did not alter or execute the submitted notebooks. Saved outputs, execution counts, source code, and Markdown reasoning were inspected. All three notebooks passed static Python syntax checks.

## Overall Results

| Student/folder | Score | Status | Main conclusion |
|---|---:|---|---|
| `Yuanjie-Tan` | **88/100** | **Complete** | Strong, reproducible analysis with a few unmet acceptance details and one PCA-loading interpretation error |
| `student0019425` (git author: Evan Lin) | **76/100** | **Revision required** | Good technical coverage, but a central Pearson/Spearman result remains reversed and several required explanations are incomplete |
| `陈梓末` (Zimo Chen) | **69/100** | **Revision required** | Ambitious analysis, but no saved execution evidence and several conclusions go beyond what the data supports |

## Yuanjie-Tan — 88/100

Submission: `Yuanjie-Tan/s02_data_exploration.ipynb`

| Area | Score | Evidence |
|---|---:|---|
| Submission and reproducibility | 8/10 | All 11 code cells have saved execution counts and no saved errors. The notebook finds the repository root robustly. PR #7 used `submission-s01` rather than the required `s02/<username>` branch and did not target `main` directly. |
| Audit and data quality | 15/15 | Correct 1,000 × 23 audit, column roles, constants, zero patterns, duplicates, and explicit distinction between non-null and valid data. |
| Distributions and outliers | 16/20 | Statistics and plots cover all 13 properties, with strong observation/interpretation/limitation writing. The requirement to inspect at least three specific unusual rows is not fully demonstrated; the claim that the maximum dipole is “genuine” is stronger than the evidence shown. |
| Relationships | 12/15 | Both heatmaps and the exact gap identity are correct. Only one strong relationship is inspected with a scatter plot, while the assignment requires at least two. |
| Standardization and PCA | 17/20 | Scaling, explained variance, score plot, and component table are correct. The written PC2 interpretation misses the largest absolute weight: `Thermal_correction_to_Gibbs_Free_Energy_Hatree` (~0.447), ahead of Energy/Gibbs/Enthalpy (~0.387). Unusual score-plot rows are not investigated explicitly. |
| Critical answers | 15/15 | All ten questions are answered with generally strong evidence and appropriate limitations. |
| AI-review reflection | 5/5 | Clearly records accepted and rejected suggestions and the evidence used. |

### Strongest Work

- Reproducible end-to-end notebook with no saved execution errors.
- Excellent handling of suspicious zeros without silently changing the raw CSV.
- Correct verification that `HOMO_LUMO_Gap_eV = LUMO_eV - HOMO_eV` to floating-point tolerance.
- Clear distinction among observation, interpretation, and limitation.
- Bonus SVD comparison agrees with scikit-learn PCA.

### Required Corrections

1. Add and interpret a second scatter plot for another strong relationship.
2. Inspect at least three named rows/IDs behind unusual plotted points.
3. Correct the PC2 loading description so the thermal Gibbs correction is identified first.
4. Avoid calling an extreme dipole value genuine unless a structural or source check supports that conclusion.
5. Use the required `s02/<github-username>` branch for future submissions.

## student0019425 — 76/100

Submission: `student0019425/s02_data_exploration.ipynb`  
Git author: Evan Lin; the notebook's student name, username, and date fields are blank.

| Area | Score | Evidence |
|---|---:|---|
| Submission and reproducibility | 8/10 | PR #9 correctly used `s02/student0019425` and included the requested description. Forty-two of 43 code cells have execution counts and there are no saved error outputs. The Pearson heatmap cell has output but no execution count and contains duplicated plotting statements, so the submitted state does not prove a clean restart-and-run-all. |
| Audit and data quality | 13/15 | Correct shape, roles, dtypes, uniqueness, zero counts, and constants. Some interpretations are too tentative or unclear, and identity fields are incomplete. |
| Distributions and outliers | 14/20 | Statistics and plots cover eight properties. Three specific unusual rows are not inspected. The claim that polarizability and HOMO–LUMO gap have the same distribution is unsupported. |
| Relationships | 8/15 | Three scatter plots and both heatmaps are present, but the central HOMO/gap result is reversed in the written findings: the reference values are Pearson ≈ **−0.987** and Spearman ≈ **−0.686**, not the reverse. The Codex reflection says this was corrected, but the notebook text still contains the error. |
| Standardization and PCA | 18/20 | Correct 13-column scaling, PCA, cumulative variance, scores, and loading tables. The scaling cell displays only the standard deviations because the mean expression is not displayed. |
| Critical answers | 11/15 | All ten prompts have responses, but several are too brief or incomplete. The structure answer does not list the roles, the scale answer says variables “cannot be compared” rather than explaining raw versus standardized comparison, and the 2D-loss explanation is vague. |
| AI-review reflection | 4/5 | Includes accepted and changed suggestions, but the accepted correlation correction was not propagated consistently into the final findings. |

### Strongest Work

- Correct branch naming and complete pull-request description.
- Good breadth of plotting and a complete PCA implementation.
- Correct five-component retention choice for approximately 85.6% of the raw-data variance.
- Correct loading table and SVD calculation.

### Required Corrections

1. Correct the Pearson/Spearman labels and interpretations everywhere in the notebook.
2. Restart and run all cells, remove duplicated plot commands, and save the final outputs.
3. Inspect at least three specific unusual records rather than only describing plot shapes.
4. Replace the “same distribution” claim with separate evidence for polarizability and the HOMO–LUMO gap.
5. Expand Questions 5.1, 5.6, and 5.10 with concrete evidence and limitations.
6. Fill in the student identity fields.

## 陈梓末 / Zimo Chen — 69/100

Submission: `陈梓末/s02_data_exploration.ipynb`

| Area | Score | Evidence |
|---|---:|---|
| Submission and reproducibility | 2/10 | All 17 code cells have `execution_count: null` and no saved outputs, so the required restart-and-run-all evidence is absent. PR #10 used `main`, had an empty description, and was titled as an S01 submission rather than using `s02/<username>`. |
| Audit and data quality | 12/15 | The code performs a thoughtful audit and identifies coordinated zero patterns. However, it states “failed DFT convergence” and specific pipeline behavior as fact without calculation logs or source documentation. Those should be labeled hypotheses. |
| Distributions and outliers | 12/20 | Code covers six variables and inspects named extreme rows. The table omits required variance. Several written claims are incorrect after the 74-row removal: gap skew is about **−0.53** rather than right-skewed, only one row equals 10.001 eV so a hard ceiling is not established, and polarizability is right-skewed (about **+1.40**) rather than roughly symmetric. |
| Relationships | 13/15 | Strong code for dual heatmaps, two scatter plots, coefficient differences, and mathematical identities. Conclusions still depend on an unvalidated cleaning decision. |
| Standardization and PCA | 16/20 | The source code is comprehensive and should calculate a valid clean-subset PCA, but no outputs are saved. The written answer leaves the retained component count as “exact N shown in output”; it should state five components and approximately 85.9%. Claims about molecular size and backbone flexibility require more evidence. |
| Critical answers | 10/15 | Answers are detailed and often thoughtful, but several repeat unsupported claims such as confirmed pipeline failures, a hard gap ceiling, no batch effects, and incorrect distribution shapes. |
| AI-review reflection | 4/5 | Both decisions and evidence are documented. A raw-versus-clean sensitivity analysis would have been a stronger response than accepting deletion as definitively correct. |

### Strongest Work

- Clear code organization and useful row-level investigations.
- Correct mathematical-dependency checks and strong visualization design.
- Good explanation of PCA limitations and the SVD relationship.
- Thoughtful attempt to distinguish invalid calculations from valid observations.

### Required Corrections

1. Restart and run every cell, resolve any errors, and save all outputs.
2. Add variance to the descriptive-statistics table.
3. Treat “failed DFT convergence,” pipeline order, and a 10.001 eV cap as hypotheses unless documentation supports them.
4. Correct the clean-subset distribution descriptions using computed skewness and counts.
5. Compare raw-data PCA with cleaned-data PCA before deciding that removal is harmless; the first two raw components explain about 59.8%, while the first two cleaned components explain about 51.0%.
6. State the exact retained component count and variance in the written findings.
7. Use a correctly named S02 branch and complete the pull-request description.

## Class-Level Completion Findings

### Skills demonstrated by most students

- Correctly excluded `id` from the 13 analytical properties.
- Produced descriptive plots, correlation matrices, standardized data, and PCA.
- Recognized that zero explicit missing values do not guarantee valid data.
- Understood that PCA variance is not causation or predictive importance.
- Included an AI-review reflection and attempted the optional SVD connection.

### Skills requiring reinforcement

1. **Pearson versus Spearman:** coefficients must be read from the correct matrix and interpreted using the scatter plot.
2. **Observation versus hypothesis:** “failed calculation,” “hard cap,” “real outlier,” and “no batch effect” require supporting evidence.
3. **Sensitivity analysis:** cleaning decisions should be tested by comparing conclusions before and after cleaning.
4. **PCA interpretation:** distinguish row scores from property weights and rank weights by absolute magnitude.
5. **Reproducibility:** a finished notebook must be restarted, run top-to-bottom, and saved with outputs.
6. **Acceptance details:** branch names and pull-request descriptions are part of the assignment.

## Recommended Follow-Up

- Yuanjie-Tan: make the five listed corrections; no full resubmission is necessary if the quiz confirms understanding.
- student0019425: revise the relationship findings and critical answers, then rerun and resave the notebook.
- Zimo Chen: complete a full executed resubmission and add a raw-versus-clean sensitivity comparison.
- Administer `critical-thinking-quiz.md`. Each student should answer the shared core and only their named follow-up section.
