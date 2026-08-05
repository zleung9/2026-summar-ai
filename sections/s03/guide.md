# Section 3: Trustworthy Machine-Learning Baselines

> Dates: August 4 — August 6

## What This Section Is About

Turn the Section 2 exploration into two supervised-learning baselines:

- a **linear-regression** model that predicts a continuous polymer property;
- a **logistic-regression** model that predicts a binary class derived from that property.

The main goal is not to obtain a high score. It is to decide whether a score is trustworthy. You will define the task, protect a final test set, use cross-validation on the training data, compare with simple dummy models, detect a deliberate leakage trap, and interpret errors in the context of the dataset.

Complete one integrated notebook using the instructions and critical questions in [homework.md](homework.md).

## Topics

- Supervised learning: features, targets, regression, and classification
- Linear regression and mean-squared-error minimization
- Logistic regression, probabilities, decision thresholds, and log loss
- Training, validation, and test data
- Five-fold cross-validation
- Bias, variance, underfitting, and overfitting
- Data leakage and preprocessing pipelines
- Regression metrics: \(R^2\), MAE, MSE, and RMSE
- Classification metrics: confusion matrix, accuracy, precision, recall, F1, and ROC-AUC
- Dummy baselines and error inspection

## Three-Day Map

| Day | Focus | Notebook evidence |
|---|---|---|
| 1 | Define the two tasks, update the data audit, make one train/test split, and fit dummy and linear models | Target and feature definitions, split checks, and regression results |
| 2 | Investigate leakage and generalization; place preprocessing inside pipelines and run cross-validation | Leaky-versus-honest comparison and fold-level results |
| 3 | Fit and evaluate logistic regression, inspect errors, and answer the critical questions | Classification metrics, error analysis, and final claims |

## Recommended Resources

Use these to answer a question or unblock the notebook; do not try to watch or read everything.

- [机器学习模型入门讲解](https://www.bilibili.com/video/BV1NWTjz4Efg/) — watch the short linear-regression and logistic-regression episodes; focus on the difference between a numeric prediction and a class probability.
- [人工智能机器学习入门：Data leakage](https://www.bilibili.com/video/BV1YT4y1f7H2/) — connect the examples to scaling before a split, using the test set repeatedly, and including a target-derived feature.
- [scikit-learn: Linear models](https://scikit-learn.org/stable/modules/linear_model.html) — use the linear- and logistic-regression sections as a reference, especially the stated optimization objective.
- [scikit-learn: Cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html) — focus on held-out tests, five-fold cross-validation, stratification, and transformations inside a `Pipeline`.
- [scikit-learn: Metrics and scoring](https://scikit-learn.org/stable/modules/model_evaluation.html) — use the regression and binary-classification metric definitions when interpreting results.
- [scikit-learn: Common pitfalls](https://scikit-learn.org/stable/common_pitfalls.html) — focus on inconsistent preprocessing and data leakage.

## The Modeling Dataset

Continue with:

```text
sections/s02/homework/openpoly_calculated_properties.csv
```

Read [the dataset notes](../s02/homework/DATASET.md) and reuse evidence from your Section 2 analysis. Do not copy the old notebook unchanged: report the rows, target, predictors, and distributions **after** applying the exact validity rule used for modeling.

For this section, use `HOMO_LUMO_Gap_eV` as the continuous target. The supplied data contains an important trap:

\[
\text{HOMO\_LUMO\_Gap\_eV}=\text{LUMO\_eV}-\text{HOMO\_eV}.
\]

A model given both `HOMO_eV` and `LUMO_eV` can therefore reconstruct the answer instead of learning a useful relationship. You will demonstrate this once, label the result as leaky, and exclude those two columns from the honest baseline.

The remaining calculated properties are acceptable for this learning exercise, but they raise a second question: would all of them be available when a real prediction is needed? This baseline predicts one calculation from other calculations; it does not yet predict directly from a new polymer structure. State that limitation.

## A Trustworthy Experiment Loop

Use this order throughout the homework:

1. **Define:** state the target, candidate predictors, unit of observation, validity rule, and intended use.
2. **Split:** reserve 20% of valid rows as the final test set and record the random seed.
3. **Learn from training data:** derive the classification threshold, fit preprocessing, and run cross-validation without using the test set.
4. **Compare:** evaluate a meaningful model against a dummy baseline and against variation across folds.
5. **Test once:** use the held-out test set only after the workflow is fixed.
6. **Inspect:** examine residuals and classification errors, not only aggregate scores.
7. **Limit the claim:** say what the evidence supports and what it does not.

Use a scikit-learn `Pipeline` when a transformation such as `StandardScaler` is part of a model. During cross-validation, each fold must learn its scaler from that fold's training portion.

## Purpose and Critical Questions

Organize the notebook around these three questions. Each final answer must cite concrete notebook evidence.

### 1. Are we solving a meaningful prediction problem?

- What exactly is the target, and what does one row represent?
- Which inputs would be available at the moment a prediction is requested?
- Does the high/low classification threshold have scientific meaning, or does it only create a balanced practice task?
- Is this a structure-to-property model, or a calculation-to-calculation model?

### 2. Does the evaluation measure generalization rather than leakage or memory?

- Why must the final test set remain unused during preprocessing, model choice, and interpretation?
- Why does scaling belong inside a cross-validation pipeline?
- Why do `HOMO_eV` and `LUMO_eV` make this target leaky even if the test rows were never used for training?
- What population does a random row split represent, and would it estimate performance on genuinely new chemical families?
- Do the model results beat a dummy baseline, and are they stable across folds?
- What do the training, cross-validation, and test differences suggest about underfitting, overfitting, bias, and variance? What can they not prove?

### 3. What do the scores say—and what do they hide?

- Why can MAE and RMSE give different impressions of the same residuals? What units do they use?
- What does a negative \(R^2\) mean relative to predicting the training mean?
- Which classification error is more important here: a false positive or a false negative? What assumption is required to answer?
- Why can accuracy, F1, and ROC-AUC disagree?
- Is the model trained to optimize the same quantity that you report as the main scientific metric?

## Metric Interpretation Reminders

- **MAE** is the average absolute error in eV. It weights errors linearly.
- **MSE** is in squared eV and emphasizes large residuals.
- **RMSE** returns to eV but still emphasizes large residuals through squaring.
- **\(R^2\)** compares squared error with a mean-prediction reference; it is not a percentage of predictions that are correct.
- A **confusion matrix** contains counts at one decision threshold.
- **Precision** asks how many predicted positives are positive; **recall** asks how many actual positives were found.
- **F1** combines precision and recall at one threshold.
- **ROC-AUC** evaluates ranking across thresholds; it does not select a useful operating threshold or describe probability calibration.

## Self-Check

- [ ] I can distinguish a feature, a continuous target, and a binary label.
- [ ] I can explain what linear and logistic regression optimize.
- [ ] I can protect a test set while using cross-validation on the training set.
- [ ] I can explain why preprocessing must be fitted without validation or test rows.
- [ ] I can identify both formula leakage and deployment-time feature leakage.
- [ ] I can compare a model with a dummy baseline and variation across folds.
- [ ] I can calculate and interpret all required regression and classification metrics.
- [ ] I can use residuals and confusion-matrix cases to qualify an aggregate score.
- [ ] I can answer the three critical questions with evidence rather than definitions alone.

**You know enough when:** a surprisingly good metric makes you ask how the task, features, split, preprocessing, and baseline were defined before you trust the model.
