# Section 4 Answer Key

(For teacher use only — do not share with students)

## What This Section Tests

The assignment tests whether the student can connect neural-network concepts to a trustworthy experiment. A successful student should be able to:

1. trace a forward pass and use the chain rule to obtain parameter gradients;
2. match outputs, targets, activations, and losses without relying on trial and error;
3. preserve the Section 3 evaluation boundary while moving to PyTorch;
4. build an MLP for tabular data and a CNN only where local order is meaningful;
5. use learning curves and validation evidence to choose a checkpoint;
6. compare complete pipelines without claiming that a score difference proves one architecture is universally better.

Exact neural-network scores are not fixed because they depend on the Section 3 task, split, preprocessing, and stochastic training. Grade the validity and reproducibility of the experiment before the score.

## Part 1 Reference: Manual Forward Pass

The hidden pre-activation is:

```text
z1 = W1 x + b1 = [1.0, 1.0]
```

Both entries are positive, so ReLU leaves them unchanged:

```text
h = [1.0, 1.0]
```

The output and binary loss are approximately:

| Quantity | Reference value |
|---|---:|
| Logit | `0.500000` |
| Sigmoid probability | `0.622459` |
| Binary cross-entropy | `0.474077` |

For one binary example, the derivative of binary cross-entropy with logits with respect to the logit is:

```text
dL/dlogit = sigmoid(logit) - y = -0.377541
```

The parameter gradients are approximately:

```text
dL/dW2 = [-0.377541, -0.377541]
dL/db2 = -0.377541

dL/dW1 = [[-0.302033, -0.604065],
           [ 0.151016,  0.302033]]

dL/db1 = [-0.302033, 0.151016]
```

After one gradient-descent step with learning rate `0.1`:

```text
W1 = [[ 0.530203, 0.310407],
      [-0.515102, 0.969797]]
b1 = [0.030203, -0.515102]

W2 = [0.837754, -0.362246]
b2 = 0.137754
```

The updated logit is approximately `0.797903`, the probability is `0.689526`, and the loss falls to `0.371751`.

Small floating-point differences are acceptable. The autograd comparison should be near machine precision for `float64` and usually within about `1e-6` for `float32`. A large difference commonly indicates a missing bias gradient, an incorrect ReLU derivative, transposed outer product, or an average/sum mismatch.

### Activation interpretation

- Sigmoid approaches `0` or `1` for large-magnitude inputs, so its derivative approaches zero and early layers may receive a weak signal.
- ReLU has derivative `1` for positive inputs and `0` for negative inputs, aside from the convention chosen at zero.
- ReLU avoids positive-side saturation and is inexpensive, but a unit that remains on the negative side can stop receiving a gradient.

## Output–Target–Loss Reference

| Task | Correct training output | Correct target | Correct loss | Common wrong implementation |
|---|---|---|---|---|
| Regression | Shape `(N, 1)` or consistently `(N,)`; unrestricted float | Same shape and floating dtype | `MSELoss` | Applying sigmoid and restricting the prediction to `0–1` without transforming the target |
| Binary | One logit per sample | Floating `0/1`, same shape | `BCEWithLogitsLoss` | Model applies sigmoid and the loss applies it again; target has `long` dtype or shape `(N,)` against `(N, 1)` |
| Multiclass | Shape `(N, C)` logits | Shape `(N,)`, `torch.long`, class indices | `CrossEntropyLoss` | Applying softmax before the loss; passing a one-hot integer matrix to the class-index interface |
| Multi-label | Shape `(N, C)` independent logits | Shape `(N, C)` floating multi-hot values | `BCEWithLogitsLoss` | Using one softmax even though several labels can be true |

For inference, sigmoid turns binary or multi-label logits into independent probabilities. Softmax turns mutually exclusive class logits into probabilities that sum to one. `argmax` is sufficient to obtain the multiclass prediction; softmax is needed when probability scores are reported.

PyTorch `CrossEntropyLoss` can accept floating class-probability targets with the same shape as the logits. This is appropriate for soft labels, not a reason to one-hot encode ordinary hard labels. The student should know both representations but can use class indices for the project.

## Data and Split Review

Require explicit row-identifier checks, not only a statement that a split function was called. The following must be learned from training data only:

- numerical imputation and scaling values;
- sequence vocabulary;
- a data-dependent padding or truncation length;
- class weights or resampling rules;
- probability threshold;
- early-stopping epoch and all hyperparameters.

The test set must not choose any of these. If the student inspected test performance repeatedly while tuning, the final number is no longer an unbiased test estimate. Ask for a fresh held-out set only if a defensible one exists; otherwise require the limitation to be reported.

### Leakage checks

The student should reuse the Section 3 feature audit. In particular:

- identifiers must not become numeric predictors simply because they have numeric dtype;
- the target itself and deterministic target-derived columns must be excluded;
- scaling before splitting is leakage;
- fitting a vocabulary on all sequences leaks distribution information, even without labels;
- duplicate or near-duplicate chemical structures across splits may make performance optimistic and deserve inspection.

If the task predicts a calculated property from other calculated properties, correlated or algebraically related columns need special scrutiny. A high score may reflect the known formula rather than learning a transferable chemical relationship.

## MLP Reference Checks

A reasonable small MLP may contain one to three hidden linear layers, ReLU activations, and optional dropout. There is no required width. Look for:

- input width equals the number of transformed tabular features;
- output width matches the task contract;
- the model returns unrestricted outputs or logits;
- parameter count is reported and plausible;
- `model.train()` and `model.eval()` are used in the correct phases;
- gradients are cleared once per optimization step;
- validation uses `torch.no_grad()` or `torch.inference_mode()`;
- the saved checkpoint corresponds to a validation rule chosen in advance.

The controlled comparison should change one main factor. If the student changes width, learning rate, dropout, and epoch count at once, they cannot attribute the observed difference to one choice.

## CNN Reference Checks

For character one-hot input, the expected shape before `Conv1d` is:

```text
(batch_size, vocabulary_size, sequence_length)
```

An acceptable small pipeline is conceptually:

```text
one-hot sequence
  -> Conv1d
  -> ReLU
  -> pooling over sequence positions
  -> optional dropout or hidden layer
  -> task output
```

Alternative correct designs are acceptable. Require the student to print the major shapes and explain which axis is batch, channels, and sequence length.

A convolution kernel may respond to local character patterns that recur at different sequence positions. This is only an introductory representation: character tokens do not perfectly match chemical tokens, padding and truncation can distort the sequence, and `psmiles` syntax does not make every learned filter chemically interpretable.

Do not accept an architecture-only conclusion from the required MLP–CNN score comparison. The MLP uses tabular features and the CNN uses a string representation. The result compares two complete pipelines in this dataset and split. A cleaner architecture comparison would hold the representation and other conditions fixed.

## Evaluation Reference

### Regression

Require R2, MAE, MSE, and RMSE in the original target units. The predicted-versus-observed and residual plots should be based on the held-out test predictions. If the target was standardized, inverse-transform predictions and targets before reporting scientific units.

### Binary classification

Require a confusion matrix, precision, recall, F1, and ROC-AUC. F1 and the confusion matrix depend on a threshold; ROC-AUC uses continuous scores. The threshold must be fixed from training/validation evidence or a stated default, not selected on test labels. ROC-AUC is undefined when the evaluation labels contain only one class.

### Multiclass classification

Require an explicit class mapping, confusion matrix, per-class results, and macro F1. Multiclass ROC-AUC requires a score for every class and a declared averaging and multiclass convention, such as one-vs-rest macro averaging. It may be omitted with a correct explanation when the split or task does not support a valid calculation.

### Interpreting learning curves

| Pattern | Plausible interpretation | Next check |
|---|---|---|
| Training and validation losses both high and flat | Underfitting, weak features, or optimization failure | Compare with a trivial baseline; inspect gradients and learning rate |
| Training loss falls while validation loss rises | Overfitting | Check the best epoch; consider a smaller model, regularization, or more data |
| Both losses fluctuate or diverge | Learning rate may be too large or data may be unstable | Inspect batch losses, scaling, and finite values |
| Both losses improve and remain close | No clear overfitting in the observed range | Confirm metrics and repeat with another seed |

These are diagnoses to investigate, not proofs from plot shape alone.

## What a Strong Comparison Says

A strong conclusion resembles:

> “On the fixed test split, the CNN pipeline had lower RMSE than the tabular MLP but not the linear baseline. Because the models used different input representations and only one split and seed were tested, this does not establish that CNNs are inferior or superior. The result supports retaining the simpler baseline for this dataset while testing whether sequence representation and sample size limit the CNN.”

A weak conclusion resembles:

> “CNNs are best because the CNN score was highest.”

Require practical magnitude, not only rank. A tiny metric improvement may not justify higher training cost, instability, or complexity.

## Common Failure Modes

| Symptom | Likely cause | Useful diagnostic |
|---|---|---|
| Binary loss behaves strangely | Sigmoid applied before `BCEWithLogitsLoss`, wrong target shape, or wrong dtype | Print raw logits, target shape/dtype, and loss call |
| Multiclass loss does not improve | Softmax before `CrossEntropyLoss`, wrong class mapping, or label leakage/error | Inspect logits, unique class indices, and a tiny overfit test |
| Validation results change during evaluation | Dropout remains active because `model.eval()` is missing | Run the same batch twice in evaluation mode |
| Gradients grow every batch | `zero_grad()` is missing or misplaced | Print a gradient norm before and after clearing |
| Excellent validation result but weak test result | Overfitting or repeated validation tuning | Review the experiment log and number of decisions based on validation |
| Implausibly excellent results everywhere | Leakage, duplicates, or target-derived features | Audit feature formulas and row/structure overlap |
| CNN shape error | Channels and sequence axes reversed | Confirm `(N, C, L)` immediately before `Conv1d` |
| CNN learns padding | Padding dominates or pooling ignores valid length | Inspect padding rate and activation locations |

## What to Probe During Review

1. Ask the student to derive `dL/dlogit = sigmoid(logit) - y` for the manual example.
2. Give a binary output of shape `(32, 1)` and a target of shape `(32,)`; ask why broadcasting or a runtime error is not an acceptable contract.
3. Ask where softmax appears in the multiclass training pipeline and why.
4. Ask the student to show proof that the scaler and vocabulary saw training data only.
5. Ask what one CNN filter slides over and what “nearby” means in that representation.
6. Ask which single result changed a model-selection decision.
7. Ask for one conclusion that the experiment supports and one it cannot support.
8. Ask the student to explain a Codex suggestion they did not accept.

The section is complete when the student can diagnose a shape/loss mismatch, defend the evaluation boundary, and explain the model comparison without overclaiming.
