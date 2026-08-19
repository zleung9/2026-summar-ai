# Section 4: Deep Neural Networks

> Dates: August 7 — August 9

## What This Section Is About

Learn how a neural network turns inputs into predictions, how a loss sends an error signal backward through the network, and how an optimizer uses that signal to update parameters.

You will first trace one tiny network by hand and verify the result with PyTorch. You will then train two small models on one task from Section 3: a multilayer perceptron (MLP) on tabular features and a one-dimensional convolutional neural network (1D CNN) on a sequence representation. The goal is not to make the deepest model. It is to build a correct, reproducible experiment and explain what the comparison does and does not show.

## Topics

- Neurons, layers, weights, biases, and tensor shapes
- Sigmoid and ReLU activations, including saturation and gradient behavior
- Forward propagation, loss, the chain rule, and backpropagation
- Gradient-based optimization, learning rate, batch size, and epochs
- Logits, probabilities, and numerical stability
- Class-index and one-hot target representations
- Regression, binary classification, multiclass classification, and multi-label classification
- Matching output width, target representation, activation, and loss
- MLPs for tabular features
- 1D CNNs for local patterns in sequence representations
- Learning curves, regularization, early stopping, and overfitting
- Reproducible comparison with the Section 3 baselines

## Three-Day Map

| Day | Focus | Output |
|---|---|---|
| 1 | Trace a tiny network; verify gradients; test regression, binary, and multiclass output/loss contracts | A forward/backward trace and three passing contract checks |
| 2 | Train and tune an MLP on one Section 3 task | Reproducible runs, learning curves, and a selected checkpoint |
| 3 | Train a 1D CNN on a sequence representation and compare all models | CNN results, comparison table, and evidence-based conclusions |

## Recommended Resources

Use a resource when it answers a question or unblocks the experiment. Do not try to finish every playlist.

### Intuition

- [3Blue1Brown: What is a neural network? (Chinese dub)](https://www.bilibili.com/video/BV16ssYzrECx/) — focus on layers, weights, biases, sigmoid, and ReLU.
- [3Blue1Brown neural-network series](https://www.bilibili.com/video/BV1G51UBTELr/) — watch the gradient-descent and backpropagation chapters after attempting the manual trace.
- [PyTorch zero-to-practice course](https://www.bilibili.com/video/BV1fb4y1h7Cv/) — use the indexed chapters on tensors, autograd, training, loss functions, and evaluation; skip unrelated later material.

### Implementation References

- [PyTorch: Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/) — tensors, datasets, models, automatic differentiation, and optimization in one sequence.
- [Optimizing model parameters](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html) — the training and validation loop and the roles of epochs, batch size, and learning rate.
- [`BCEWithLogitsLoss`](https://docs.pytorch.org/docs/stable/generated/torch.nn.BCEWithLogitsLoss.html) and [`CrossEntropyLoss`](https://docs.pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html) — read the expected input, target, shape, and dtype carefully.
- [`Conv1d`](https://docs.pytorch.org/docs/stable/generated/torch.nn.Conv1d.html) — focus on the input shape `(batch, channels, length)`.
- [PyTorch reproducibility notes](https://docs.pytorch.org/docs/stable/notes/randomness.html) — understand what a seed can and cannot guarantee.

## Environment

Use the existing `uv` environment. Install only the packages that are not already present:

```bash
uv pip install torch numpy pandas matplotlib seaborn scikit-learn jupyter ipykernel
uv run python -c "import torch; print(torch.__version__)"
```

CPU training is sufficient for the small models in this assignment. Confirm that the notebook uses the repository's `.venv` kernel before starting.

## The Output–Target–Loss Contract

Treat these choices as one contract. A model can run while still implementing the wrong statistical task.

| Task | Model output during training | Typical target | PyTorch loss | Convert to predictions |
|---|---|---|---|---|
| Regression with one target | One unrestricted value per sample | Floating-point value, same output shape | `MSELoss` | Use the value directly |
| Binary classification | One unrestricted **logit** per sample | Floating-point `0` or `1`, same output shape | `BCEWithLogitsLoss` | Apply sigmoid, then choose a threshold |
| Mutually exclusive multiclass classification | `C` unrestricted logits per sample | Integer class index from `0` to `C-1` | `CrossEntropyLoss` | Apply softmax for probabilities; use `argmax` for the class |
| Multi-label classification | One logit per label | A floating-point multi-hot vector | `BCEWithLogitsLoss` | Apply sigmoid independently to each label |

For ordinary mutually exclusive classes, class indices are simpler than one-hot targets in PyTorch. `CrossEntropyLoss` can also accept valid class-probability targets, but the target must then have the same shape as the logits and represent a probability distribution. Do not one-hot encode labels merely because the term appeared in a tutorial.

Do not put sigmoid before `BCEWithLogitsLoss` or softmax before `CrossEntropyLoss`. These losses expect logits and combine the probability transformation with the loss calculation in a more numerically stable way. Apply sigmoid or softmax when you need probabilities for interpretation or metrics.

## A Trustworthy Experiment

### 1. Freeze the task and split

Choose one primary regression or classification task from Section 3. Reuse the same target definition and the same train, validation, and test row indices so the new results are comparable with the recorded baseline.

Keep the test set closed while choosing architectures, learning rates, epoch counts, thresholds, and regularization. Fit scalers, vocabularies, and other learned preprocessing on the training set only.

### 2. Audit the exact model inputs

Update the Section 2 analysis for the exact rows and features used here. At minimum, check split sizes, target balance or distribution, missing and suspicious values, feature distributions, box plots, correlations, and PCA for the MLP inputs. State which identifiers, target-derived columns, and leakage-prone features you excluded.

For the CNN, inspect sequence lengths, token frequencies, unknown-token counts, padding, and truncation. A character-level representation is sufficient for this section. Build the vocabulary and choose any data-dependent maximum length from the training split only.

### 3. Make the architecture match the representation

Use the MLP on standardized tabular features. Use the 1D CNN on an ordered sequence such as `psmiles`, represented as character channels with shape `(batch, vocabulary_size, sequence_length)`.

Do not apply a CNN to an arbitrary ordering of tabular columns and then describe adjacent columns as a local scientific pattern. Convolution assumes that nearby positions have a meaningful relationship.

### 4. Separate training from evaluation

During each training epoch:

1. switch to training mode;
2. run a forward pass on a batch;
3. calculate loss from logits or regression outputs;
4. clear old gradients, backpropagate, and update parameters;
5. switch to evaluation mode and calculate validation loss without gradient tracking.

Save the checkpoint with the best validation result. Record training and validation loss at every epoch, not only the final number.

### 5. Compare cautiously

The MLP and CNN use different representations, so their score difference cannot be attributed to architecture alone. Compare them as complete pipelines. Also report parameter count, training time, and variability across repeated runs when practical. A neural network that fails to beat a simple baseline can still be a successful experiment if the implementation is sound and the conclusion is honest.

## Framing Questions

1. **Where should probability conversion happen?** Why do `BCEWithLogitsLoss` and `CrossEntropyLoss` expect logits, and what error can result from applying sigmoid or softmax twice?

2. **What actually travels backward?** Starting from the loss, how does the chain rule assign a gradient to a weight in the first layer? What happens to that signal when a sigmoid saturates or a ReLU input is negative?

3. **What makes a comparison fair?** If the MLP uses calculated tabular properties and the CNN uses `psmiles`, which conclusions are supported by the result, and which architecture-only claim is not supported?

## Self-Check

- [ ] I can trace one forward pass and one gradient update with concrete numbers.
- [ ] I can explain the difference among a logit, a probability, a predicted class, and a target.
- [ ] I can choose the output width, target shape and dtype, and loss for regression, binary, multiclass, and multi-label tasks.
- [ ] I can explain why sigmoid can saturate and why ReLU can have a zero gradient.
- [ ] I can write a training loop that clears gradients and a validation loop that does not update parameters.
- [ ] I can identify overfitting from training and validation curves.
- [ ] I can explain why a CNN requires meaningful local order.
- [ ] I can compare neural networks with Section 3 baselines without using the test set for tuning.
- [ ] I can state at least two limitations of the comparison.

**You know enough when:** you can defend every tensor shape, activation, loss, data split, and evaluation choice in your experiment—and diagnose a mismatch instead of changing code at random.
