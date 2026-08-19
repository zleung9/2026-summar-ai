# Section 4 Homework

> Due: August 9, before the section-end review

## Goal

Build and evaluate a correct neural-network pipeline for one Section 3 prediction task. Use a manual gradient trace and small contract tests to show that you understand what the framework is doing, then compare an MLP, a 1D CNN, and the relevant Section 3 baseline.

This is one integrated assignment. Aim for roughly three hours per part and prefer a few controlled experiments over a large hyperparameter search.

## Start from the Notebook Template

Copy:

```text
sections/s04/homework/s04_deep_neural_networks_template.ipynb
```

to:

```text
sections/s04/submissions/<github-username>/s04_deep_neural_networks.ipynb
```

Keep the template headings. Complete its code and answer cells, and add cells only when the experiment needs them.

## Experiment Contract

Before training, state:

- the primary task and target;
- whether it is regression, binary classification, or multiclass classification;
- the row identifiers in each train, validation, and test split;
- the Section 3 baseline and metrics you will compare against;
- the MLP input columns and the CNN sequence column;
- the output width, target shape and dtype, loss, and probability conversion for the primary task.

Reuse the target definition and split from Section 3. If Section 3 did not preserve a validation split, derive it from the training portion without touching the test set, then record and reuse its row identifiers throughout this assignment.

## Required Work

### Part 1: Trace and test the learning mechanism

Use this one-sample binary network:

```text
x = [1.0, 2.0]                         y = 1

W1 = [[ 0.5, 0.25],                    b1 = [0.0, -0.5]
      [-0.5, 1.00]]

h = ReLU(W1 x + b1)

W2 = [0.8, -0.4]                       b2 = 0.1
logit = W2 h + b2
loss = binary cross-entropy with logits
```

1. Calculate and show the hidden pre-activations, hidden activations, output logit, sigmoid probability, and loss.
2. Use the chain rule to calculate the gradient of the loss with respect to `W2`, `b2`, `W1`, and `b1`.
3. Apply one gradient-descent update with learning rate `0.1` and confirm that the loss decreases.
4. Recreate the same calculation in PyTorch and compare every manual gradient with autograd. Report the maximum absolute difference.
5. Plot sigmoid and ReLU and annotate where each has a small or zero gradient. Explain saturation and one advantage and one risk of ReLU.

Then implement three small, untrained contract checks using toy tensors:

| Check | Required evidence |
|---|---|
| Regression | Output and floating-point target have the same shape; `MSELoss` returns a scalar |
| Binary classification | One logit per sample; floating-point `0/1` target has the same shape; `BCEWithLogitsLoss` receives logits; sigmoid is used only to report probabilities |
| Multiclass classification | `C` logits per sample; target is a one-dimensional `torch.long` tensor of class indices; `CrossEntropyLoss` receives logits; softmax rows sum to approximately one for reporting |

For each check, print the output shape, target shape, target dtype, scalar loss, and reported predictions. Explain how a one-hot target differs from a class-index target and when independent sigmoids describe multi-label rather than multiclass classification.

### Part 2: Prepare the real experiment

For the exact data used by the models:

1. report split sizes and verify that row identifiers do not overlap;
2. update the target distribution or class balance;
3. update descriptive statistics, distributions, box plots, correlations, and PCA for the MLP inputs;
4. identify missing, suspicious, target-derived, or leakage-prone values and document each decision;
5. fit numerical preprocessing on training data only and verify the transformed shapes;
6. for the CNN sequence input, report length and character-frequency distributions, vocabulary size, unknown-token counts, maximum length, padding rate, and truncation rate.

Use `psmiles` unless Section 3 established another ordered sequence field. Build the character vocabulary on the training split only and include explicit padding and unknown tokens. Explain why the CNN input has local order while the MLP's tabular columns do not.

### Part 3: Train and tune an MLP

Build a small MLP for the standardized tabular features.

- Use at least one hidden layer and a nonlinear activation.
- Return raw regression values or logits that match the experiment contract.
- Record the architecture, parameter count, optimizer, learning rate, batch size, regularization, maximum epochs, and stopping rule.
- Plot training and validation loss for every epoch.
- Run at least two controlled configurations that change one important choice, such as learning rate, hidden width, weight decay, or dropout.
- Select the checkpoint using validation evidence only.
- Explain whether the curves show underfitting, overfitting, unstable optimization, or no clear problem.

Do not maximize the number of runs. The purpose is to predict what one change should do, observe what happened, and explain the difference.

### Part 4: Train a 1D CNN

Build a small 1D CNN for the character-level sequence representation.

- Present the input as `(batch, channels, sequence_length)`.
- Use at least one `Conv1d`, a nonlinear activation, a pooling operation, and a final prediction layer.
- Print and explain the tensor shape after each major stage for one batch.
- Use the same primary target and row split as the MLP.
- Record the same experiment metadata and plot training and validation loss.
- Make one controlled CNN change, such as kernel size, channel count, dropout, or learning rate, and explain the result.
- Select the checkpoint using validation evidence only.

Explain what a convolution kernel can detect in a character sequence and why applying the same kernel to an arbitrary ordering of tabular columns would not have the same meaning.

### Part 5: Evaluate once and compare

After all choices are fixed, evaluate each selected checkpoint on the untouched test set.

For a regression task, report:

- R2, MAE, MSE, and RMSE;
- a predicted-versus-observed plot and residual plot.

For a binary classification task, report:

- confusion matrix, precision, recall, F1, and ROC-AUC;
- the probability threshold and how it was chosen without using the test set.

For a multiclass classification task, report:

- confusion matrix, per-class results, macro F1, and ROC-AUC when it is valid and clearly defined;
- the class mapping and `argmax` prediction rule.

Create one comparison table containing the Section 3 baseline, MLP, and CNN. Include input representation, parameter count, best validation result, test metrics, approximate training time, and random seed. Then answer:

1. Did either neural network outperform the baseline by a practically meaningful amount?
2. What evidence of overfitting or underfitting appears in the curves?
3. Because the MLP and CNN use different inputs, what can and cannot be concluded from their score difference?
4. What are the two most important threats to validity in this experiment?
5. Which model would you carry into Section 5, and why?

### Part 6: Review the work

Ask Codex to review the notebook for tensor-shape mistakes, double activation, leakage, test-set tuning, missing evaluation mode, and unsupported claims. Record:

- one suggestion you accepted;
- one suggestion you changed or rejected;
- the evidence used for each decision.

You remain responsible for the final experiment.

## Deliverables

Submit one pull-request link containing:

1. `sections/s04/submissions/<github-username>/s04_deep_neural_networks.ipynb`
2. any small helper module written specifically for the notebook;
3. a pull-request description that states:
   - the task, target, and fixed split;
   - the MLP and CNN input representations;
   - the selected model and primary test result;
   - whether either network beat the Section 3 baseline;
   - one Codex suggestion accepted and one changed or rejected;
   - links to any GitHub Issues opened, or “None.”

Do not commit model checkpoints, cached datasets, or generated training artifacts unless the instructor requests them.

## Acceptance Criteria

- [ ] The work is on a branch named `s04/<github-username>`
- [ ] Restarting the kernel and running all cells completes without errors
- [ ] The primary task, target, split, features, output, target representation, loss, and metrics form a consistent contract
- [ ] Train, validation, and test row identifiers do not overlap, and learned preprocessing uses training data only
- [ ] The manual forward pass, gradients, update, and autograd comparison are complete and numerically consistent
- [ ] Regression, binary, and multiclass toy contract checks show correct shapes, dtypes, logits, losses, and probability conversion
- [ ] The exact MLP inputs have updated statistics, plots, correlations, PCA, and leakage checks
- [ ] The sequence analysis covers lengths, characters, vocabulary, unknown tokens, padding, and truncation
- [ ] The MLP and CNN architectures are explained and their major tensor shapes are verified
- [ ] Each model has at least one controlled comparison and reproducible experiment metadata
- [ ] Training and validation curves support the discussion of optimization and overfitting
- [ ] Model selection uses validation evidence; the test set is evaluated only after choices are fixed
- [ ] The required task metrics and diagnostic plots are correct
- [ ] The comparison table includes the Section 3 baseline, MLP, and CNN
- [ ] Conclusions distinguish a complete-pipeline comparison from an architecture-only comparison
- [ ] The AI-review reflection shows that advice was evaluated rather than automatically accepted
- [ ] The pull request is ready for review

## Scope Guidance

Keep both networks small enough to train on CPU in minutes, not hours. Two deliberate configurations per model are enough. If a neural network performs worse than the baseline, report the result and diagnose it; do not keep tuning against the test set until it looks better.
