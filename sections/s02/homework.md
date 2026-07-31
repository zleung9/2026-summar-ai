# Section 2 Homework

> Due: August 3, before the section-end review

## Goal

Produce one reproducible exploratory data analysis of a high-dimensional polymer dataset and use evidence from the analysis to answer the section's critical-thinking questions.

This is one integrated assignment, not three separate daily tasks. Organize the work in whatever order helps you build a coherent analysis.

## Dataset

Analyze:

```text
sections/s02/homework/openpoly_calculated_properties.csv
```

Read [homework/DATASET.md](homework/DATASET.md) for provenance, license, column roles, and important cautions.

Use the 13 calculated numeric properties for the main multivariate analysis. Exclude `id`: it is an identifier, not a measured or calculated polymer property. Keep the raw CSV unchanged; perform any cleaning in notebook code and explain each decision.

## Required Work

### 1. Audit the dataset

- Load the CSV using a repository-relative path.
- Report its shape, column names, data types, missing-value counts, exact duplicates, and number of unique values per column.
- Create a compact data dictionary that classifies columns as identifiers, chemical structures, categorical metadata, or numeric analytical variables.
- Inspect zeros, extreme values, and constant columns. Identify at least two values or patterns that need investigation, even if pandas reports no missing values.

### 2. Describe and visualize distributions

- For all 13 numeric properties, report count, mean, median, variance, standard deviation, minimum, quartiles, and maximum.
- For at least six properties covering different units and scales, create distribution plots and box plots.
- Investigate at least three observations that a box plot or distribution plot makes look unusual.
- For at least three properties, write an observation, an interpretation, and a limitation. Include one case where the mean and median lead to different impressions.

### 3. Examine relationships

- Produce labeled Pearson and Spearman correlation heatmaps for the 13 numeric properties.
- Identify at least two strong relationships and inspect each with an appropriate scatter plot.
- Find at least one pair for which Pearson and Spearman differ meaningfully. Explain what the difference suggests and what it does not prove.
- Check whether any properties are exact or near-exact mathematical combinations of others.

### 4. Standardize and run PCA

- Standardize the 13 numeric properties with `StandardScaler`.
- Verify numerically that standardization worked.
- Run PCA on the standardized values.
- Create:
  - a scree or explained-variance plot;
  - a cumulative explained-variance plot;
  - a PC1-versus-PC2 scores plot;
  - a loading table or loading plot for PC1 and PC2.
- State how many components you would retain and justify the choice using both explained variance and the purpose of the analysis.
- Interpret the strongest loadings on PC1 and PC2, inspect unusual points in the scores plot, and state at least two limitations of the projection.

### 5. Answer the critical questions

Answer every question in the “Purpose and Critical-Thinking Questions” table in [guide.md](guide.md). Each answer must cite a specific number, table, row, or plot from your notebook.

### 6. Review your work

Ask Codex to review the notebook for calculation errors, unsupported interpretations, and reproducibility. Record:

- one suggestion you accepted;
- one suggestion you changed or rejected;
- the evidence you used to make each decision.

You remain responsible for the final analysis.

## Bonus: Connect SVD to PCA

Starting with the standardized data matrix:

1. Write its SVD as \(X = U\Sigma V^\top\).
2. Explain which matrix contains the principal directions.
3. Show how the singular values determine explained variance.
4. Compare the result with scikit-learn's PCA output.

## Deliverables

Submit one pull-request link containing:

1. `sections/s02/submissions/<github-username>/s02_data_exploration.ipynb`
2. A pull-request description that names:
   - the dataset;
   - your main data-quality concern;
   - the number of PCA components you retained and why;
   - one Codex suggestion you accepted and one you changed or rejected;
   - links to any GitHub Issues you opened, or “None.”

Put the critical-question answers inside the notebook as Markdown so the code, evidence, and reasoning stay together.

## Acceptance Criteria

- [ ] The work is on a branch named `s02/<github-username>`
- [ ] The notebook loads the supplied CSV through a relative path and does not modify it
- [ ] Restarting the kernel and running all cells completes without errors
- [ ] The audit covers shape, roles, dtypes, missing values, uniqueness, duplicates, constants, zeros, and suspicious values
- [ ] The descriptive-statistics table includes all 13 numeric properties
- [ ] At least six properties have readable distribution and box-plot analysis
- [ ] At least three unusual observations are inspected rather than automatically deleted
- [ ] Both labeled Pearson and Spearman correlation analyses are present
- [ ] At least two strong relationships and one Pearson–Spearman difference are interpreted
- [ ] PCA uses the 13 standardized properties and excludes `id`
- [ ] Explained variance, cumulative variance, PC1–PC2 scores, and PC1/PC2 loadings are shown and interpreted
- [ ] Every critical question from the guide has an evidence-based answer
- [ ] Observation, interpretation, and limitation are clearly distinguished
- [ ] The AI-review reflection shows that the student evaluated rather than automatically accepted advice
- [ ] The pull request is ready for review

## Scope Guidance

Aim for a focused notebook that can be rerun and discussed, not a gallery of every possible chart. Clear labels, units, short interpretations, and well-chosen evidence matter more than decoration.
