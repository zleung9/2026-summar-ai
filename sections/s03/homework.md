# Section 3 Homework

> Due: August 6, before the section-end review

## Goal

Build reproducible linear- and logistic-regression baselines for the OpenPoly calculated-properties data, then decide whether their evaluation supports a trustworthy claim.

This is one integrated assignment. Keep the data audit, code, results, error inspection, and critical-question answers together in one notebook.

## Create the Notebook

Create:

```text
sections/s03/submissions/<github-username>/s03_ml_baselines.ipynb
```

Run the notebook from the repository root and load:

```text
sections/s02/homework/openpoly_calculated_properties.csv
```

Use repository-relative paths, keep the raw CSV unchanged, set every random seed explicitly, and make sure **Restart Kernel and Run All** completes without errors.

## Fixed Experiment Contract

Use these definitions so that results can be discussed and compared.

### Rows and target

- One row is one calculated polymer record.
- Use `HOMO_LUMO_Gap_eV` as the continuous regression target.
- Treat rows with `Energy_Hatree == 0` as apparent failed calculations for this baseline. Exclude them with notebook code, report how many rows are removed and retained, and connect the choice to Section 2 evidence.
- Do not silently remove any additional row. If you believe another rule is necessary, report results both with the fixed rule and with your alternative.

### Honest predictors

Start from the numeric analytical-property columns used in Section 2, then exclude:

- `id`, because it is an identifier;
- `HOMO_LUMO_Gap_eV`, because it is the target;
- `HOMO_eV` and `LUMO_eV`, because together they calculate the target exactly.

The remaining ten numeric properties are the **honest feature set** for this exercise. Do not encode `Name`, SMILES strings, or constant metadata as numeric features in Section 3.

“Honest” here means that the direct formula leakage is removed. It does not mean the model is ready for scientific deployment: the remaining inputs are also calculated properties.

### Split and classification label

1. Make one 80/20 train/test split of the valid row indices with `random_state=42`.
2. Do not inspect or use test results while developing the workflow.
3. Compute the median regression target using **training rows only**.
4. Define `high_gap = 1` when a row's gap is greater than or equal to that training median, and `high_gap = 0` otherwise.
5. Use the same training and test row indices for regression and classification. Report the threshold and class counts in both sets.

This threshold creates a practice classification task; it is not a scientifically validated boundary. Your interpretation must preserve that distinction.

## Required Work

The sections below describe the required evidence, not the order in which you should reveal results. Define the split, pipelines, models, metrics, and cross-validation analysis first. Keep all final-test metric calls together near the end of the notebook, after those choices are fixed; do not revise the workflow in response to test performance.

### 1. Define and audit the modeling table

- State the prediction target, its unit, the unit of observation, and the intended meaning of each task.
- Show the raw and valid row counts and verify that training and test indices do not overlap.
- List the honest predictors and explain every excluded numeric column.
- For the valid modeling rows, show:
  - target count, mean, median, standard deviation, minimum, quartiles, and maximum;
  - a labeled target histogram and box plot;
  - a compact table of predictor data types, missing counts, and ranges;
  - predictor-to-target Pearson and Spearman correlations.
- After final evaluation, compare the target distribution in the training and test sets. Describe any difference that may affect evaluation, but do not revise the model in response.

Keep this update focused on the data that enters the models; do not repeat every Section 2 plot.

### 2. Establish dummy baselines

- Fit `DummyRegressor(strategy="mean")` on the regression training data.
- Fit `DummyClassifier(strategy="prior")` on the classification training data.
- Evaluate both on the held-out test rows with the same metrics used for the corresponding real models.
- Explain what “beating the dummy” establishes and what it does not.

### 3. Fit the honest linear-regression baseline

- Create a pipeline containing `StandardScaler` and `LinearRegression`.
- On training rows only, run five-fold shuffled `KFold` cross-validation with `random_state=42`.
- Report the fold values, mean, and standard deviation for \(R^2\) and RMSE.
- Fit the pipeline on all training rows.
- Report training and test \(R^2\), MAE, MSE, and RMSE in a single table.
- Create:
  - an actual-versus-predicted plot with a reference line;
  - a residual-versus-predicted plot;
  - a table of the five largest absolute test errors, including the row identifier, actual value, prediction, and residual.
- Explain whether MAE and RMSE tell different stories and identify at least one pattern or limitation in the residuals.

Do not interpret standardized linear coefficients as causal effects.

### 4. Run and diagnose the deliberate leakage experiment

- Add `HOMO_eV` and `LUMO_eV` to the honest feature set and repeat the linear-regression test evaluation using the same row split.
- Numerically verify the relationship:

  \[
  \text{HOMO\_LUMO\_Gap\_eV}=\text{LUMO\_eV}-\text{HOMO\_eV}.
  \]

- Compare the honest and leaky results in one table.
- Explain why the leaky result is invalid as evidence of useful prediction even though test rows were held out correctly.
- Remove the two columns again for every final baseline claim.

This is a diagnosis exercise, not an invitation to optimize the leaky model.

### 5. Fit the honest logistic-regression baseline

- Use the honest feature set and the training-derived `high_gap` label.
- Create a pipeline containing `StandardScaler` and `LogisticRegression`. Set a sufficiently large `max_iter` and report whether fitting converged.
- On training rows only, run five-fold shuffled `StratifiedKFold` cross-validation with `random_state=42`.
- Report fold values, mean, and standard deviation for F1 and ROC-AUC.
- Fit on all training rows, then report training and test:
  - accuracy;
  - precision;
  - recall;
  - F1;
  - ROC-AUC.
- For ROC-AUC, use positive-class probabilities or decision scores, not hard class predictions.
- Show a labeled test confusion matrix whose rows and columns make the positive class unambiguous.
- Inspect at least two false positives and two false negatives. Include their identifiers, true gap values, predicted classes, and predicted probabilities.
- Explain how the classification conclusion would change if false positives and false negatives had different scientific costs.

### 6. Compare generalization evidence

Create one compact summary that includes:

- dummy, training, cross-validation, and test results;
- cross-validation spread, not only its mean;
- the honest and leaky regression results, clearly labeled;
- the classification threshold and class balance.

Using that evidence, discuss:

- whether either honest model appears to underfit;
- whether there is evidence of overfitting or high variance;
- whether one unusual split or a few large errors may dominate the conclusion;
- why these observations are evidence rather than proof of the model's behavior on future chemical space.

### 7. Answer the three critical questions

Answer all three numbered questions in the “Purpose and Critical Questions” section of [guide.md](guide.md):

1. Are we solving a meaningful prediction problem?
2. Does the evaluation measure generalization rather than leakage or memory?
3. What do the scores say—and what do they hide?

Write one concise answer section per question. Address its subquestions and cite specific notebook evidence: a value, fold range, table, plot, equation check, or inspected row. Do not answer with definitions alone.

### 8. Review the experiment with Codex

Ask Codex to review the notebook for:

- target or preprocessing leakage;
- misuse of the test set;
- metric calculation errors;
- unsupported bias, variance, or scientific claims;
- reproducibility problems.

Record:

- one suggestion you accepted;
- one suggestion you changed or rejected;
- the evidence used for each decision.

You remain responsible for the final experiment.

## Deliverables

Submit one pull-request link containing:

1. `sections/s03/submissions/<github-username>/s03_ml_baselines.ipynb`
2. A pull-request description that reports:
   - the valid row count and honest feature count;
   - regression test \(R^2\) and RMSE;
   - classification test F1 and ROC-AUC;
   - whether the models beat their dummy baselines;
   - why the leaky regression score must be rejected;
   - one Codex suggestion accepted and one changed or rejected;
   - links to any GitHub Issues opened, or “None.”

Put all reasoning and critical-question answers inside the notebook so the evidence and claims stay together.

## Acceptance Criteria

- [ ] The work is on a branch named `s03/<github-username>`
- [ ] The notebook uses the supplied CSV through a repository-relative path and does not modify it
- [ ] Restarting the kernel and running all cells completes without errors
- [ ] The validity rule is reproducible, and removed and retained row counts are reported
- [ ] The target, unit of observation, feature set, classification threshold, and intended tasks are explicit
- [ ] `id`, the target, `HOMO_eV`, and `LUMO_eV` are absent from the honest features
- [ ] Training and test indices are disjoint, reproducible, and shared by both tasks
- [ ] The classification threshold is derived from training targets only, and class counts are reported
- [ ] Target and predictor exploration describes the exact modeling rows
- [ ] Dummy regression and classification baselines are evaluated
- [ ] Scaling is inside each model pipeline and therefore fitted separately within cross-validation folds
- [ ] Five-fold training-only cross-validation reports individual folds, mean, and standard deviation
- [ ] Regression results include training and test \(R^2\), MAE, MSE, and RMSE
- [ ] Regression plots and the five largest absolute test errors are interpreted
- [ ] The deliberate formula-leakage relationship is verified and its score is rejected
- [ ] Classification results include accuracy, precision, recall, F1, ROC-AUC, and a labeled confusion matrix
- [ ] ROC-AUC is calculated from probabilities or decision scores
- [ ] At least two false positives and two false negatives are inspected
- [ ] Bias, variance, underfitting, and overfitting claims are tied to training, fold, and test evidence
- [ ] All three critical questions and their subquestions receive evidence-based answers
- [ ] The AI-review reflection demonstrates independent judgment
- [ ] The pull request is ready for review

## Scope Guidance

Aim for approximately nine hours across the section. Use only linear regression, logistic regression, and the two dummy models. Do not add complex models or broad hyperparameter searches: a carefully audited baseline is more valuable here than a leaderboard of unexamined scores.

If you are short on time, prioritize correct splitting, leakage prevention, required metrics, error inspection, and the critical-question answers over decorative plots.
