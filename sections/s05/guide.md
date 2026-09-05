# Section 5: Autoencoders and Latent-Space Thinking

> Dates: August 10 — August 12

## What This Section Is About

An autoencoder learns two functions:

```text
input x --encoder--> latent code z --decoder--> reconstruction x_hat
```

The encoder places each example at coordinates in a **latent space**. The decoder turns coordinates back into data. Training rewards coordinates that preserve information needed for reconstruction, but it does not automatically make every coordinate meaningful, every nearby pair similar, or every empty region decodable.

This section uses three established teaching datasets rather than the course polymer data. Each dataset isolates one question:

| Lab | Autoencoder variation | Dataset | Question about the latent space |
|---|---|---|---|
| A | Dense undercomplete autoencoder | UCI Wine, through `sklearn.datasets.load_wine` | What is preserved when 13 standardized measurements are compressed to two coordinates? |
| B | Convolutional denoising autoencoder | scikit-learn Digits | Does training noisy input to reconstruct clean input make the representation robust? |
| C | Variational autoencoder (VAE) | Fashion-MNIST | What changes when codes are regularized into a distribution that can be sampled? |

Except for constructing the fixed stratified splits, class labels are **not** model inputs, reconstruction targets, or selection signals. Keep them hidden during model fitting; reveal them afterward to color plots and run a frozen-representation probe. This makes the distinction between unsupervised representation learning and supervised evaluation concrete.

## Learning Goals

By the end of the section, you should be able to:

- identify the encoder, decoder, bottleneck, latent code, reconstruction, and reconstruction loss;
- explain how a bottleneck and other regularizers change what an autoencoder can copy;
- distinguish compression quality, neighborhood structure, downstream usefulness, and sample quality;
- compare a nonlinear autoencoder with PCA without claiming that either discovers the one true representation;
- explain why a denoising autoencoder maps corrupted inputs toward clean data;
- explain why a VAE encodes a distribution using `mu` and `log_var`, why reparameterization is needed, and what the KL term changes;
- inspect a latent space with reconstructions, nearest neighbors, interpolations, traversals, probes, and held-out metrics;
- state what a latent visualization supports and what it does not support.

## Topics

- Encoder, decoder, bottleneck, latent code, and latent dimension
- Reconstruction loss and input/output range contracts
- Undercomplete and overcomplete autoencoders
- Linear autoencoders and their relationship to PCA
- Denoising autoencoders and corruption processes
- Convolutional encoders and decoders for images
- Variational autoencoders, `mu`, `log_var`, sampling, and reparameterization
- Reconstruction–regularization trade-off and the role of beta
- Latent-space projection, neighborhoods, interpolation, traversal, and sampling
- Frozen-representation probes
- Data leakage, train/validation/test boundaries, and reproducibility

## Three-Day Map

| Day | Focus | Required output |
|---|---|---|
| 1 | Build a two-dimensional dense autoencoder on standardized Wine data and compare it with two-dimensional PCA | Reconstructions, test reconstruction error, PCA/AE plots, interpolations, and a fixed probe comparison |
| 2 | Train a convolutional denoising autoencoder on Digits | Clean/noisy/reconstructed panels, robustness curves, and a plain-AE versus denoising-AE comparison |
| 3 | Train a small VAE on a fixed Fashion-MNIST subset and compare two beta values | Separate reconstruction/KL curves, latent map, decoder grid, interpolation, samples, and a trade-off conclusion |

## Recommended Resources

Use a resource to answer a question in the lab. Do not try to finish a long playlist.

### Build intuition first

- [Animated explanation of autoencoders and their uses](https://www.bilibili.com/video/BV1kw4m1r783/) — watch before Lab A; focus on the bottleneck and reconstruction objective.
- [Latent-space visualization: PCA, t-SNE, and UMAP](https://www.bilibili.com/video/BV1oH4y1c7ZR/) — use it to ask what a two-dimensional plot preserves and distorts. PCA is required here; t-SNE and UMAP are not.
- [Visual explanation of variational autoencoders](https://www.bilibili.com/video/BV1D54reZE2g/) — watch before Lab C; focus on distributions, continuity, sampling, and the reconstruction trade-off.

### Dataset and implementation references

- [UCI Wine dataset](https://archive.ics.uci.edu/dataset/109/wine) and [`load_wine`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html) — 178 samples, 13 chemical measurements, and three cultivar labels.
- [`load_digits`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html) — 1,797 handwritten 8-by-8 images with pixel values from 0 to 16.
- [Fashion-MNIST dataset card](https://github.com/zalandoresearch/fashion-mnist) and [`torchvision.datasets.FashionMNIST`](https://docs.pytorch.org/vision/stable/generated/torchvision.datasets.FashionMNIST.html) — 60,000 training and 10,000 test 28-by-28 grayscale clothing images.
- [PyTorch `DataLoader` tutorial](https://docs.pytorch.org/tutorials/beginner/basics/data_tutorial.html), [`ConvTranspose2d`](https://docs.pytorch.org/docs/stable/generated/torch.nn.ConvTranspose2d.html), and [`binary_cross_entropy`](https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.binary_cross_entropy.html) — consult these when a dataset or decoder shape is unclear.
- [Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114) — optional original paper; read the abstract and model diagram before attempting the derivation.

## Environment and Data

From the repository root:

```bash
uv sync
uv run python -c "import torch, torchvision; print(torch.__version__, torchvision.__version__)"
uv run jupyter lab
```

Wine and Digits ship with scikit-learn and require no network download. Fashion-MNIST downloads on first use to `.course-data/`; the repository ignores that directory. If the download is interrupted, remove only the incomplete `FashionMNIST/raw` download and try again.

Use CPU unless you already have a working accelerator. The starter notebook uses a fixed subset of Fashion-MNIST so that the section remains practical on CPU. Do not silently reduce the subset after seeing poor results; record any resource-driven change.

## A Working Mental Model of Latent Space

### Coordinates are learned for an objective

For a deterministic autoencoder,

```text
z = encoder(x)
x_hat = decoder(z)
loss = reconstruction_loss(x_hat, x)
```

The code `z` is useful because the encoder and decoder learned to cooperate. Rotating, reflecting, or permuting the latent coordinates can leave reconstruction quality unchanged. Therefore, axis 1 is not automatically a named physical concept.

### Four different questions require four kinds of evidence

| Question | Useful evidence | Evidence that is insufficient by itself |
|---|---|---|
| Can the code preserve the input? | Held-out reconstruction loss and per-example reconstructions | Training loss |
| Are local neighborhoods sensible? | Nearest-neighbor examples and small interpolations | A colored scatter plot alone |
| Is the code useful for another task? | A frozen encoder with the same simple probe and split across representations | Visually separated training points |
| Can the model generate from arbitrary codes? | Samples or a decoder grid from the claimed prior | Reconstructions of encoded test examples |

A good reconstruction can coexist with a poor downstream representation. A visually clean cluster can be an artifact of labels, a projection, scale, or cherry-picking. A deterministic autoencoder can reconstruct encoded inputs well while decoding random points badly because its latent space contains gaps.

### Distance inherits assumptions

When you call two codes “nearby,” specify the distance metric, preprocessing, model, checkpoint, and dataset. Euclidean distance in a two-dimensional Wine code is not the same scientific statement as pixel similarity or class identity. Treat latent distance as a model-dependent hypothesis to test.

### Interpolation is a question, not proof

Choose two examples, encode them as `z_a` and `z_b`, and decode points along

```text
z(t) = (1 - t) * z_a + t * z_b,  for t from 0 to 1.
```

Smooth decoded changes show how this decoder behaves along that path. They do not prove that every intermediate is realistic, causal, or present in nature.

## Lab A — Undercomplete Autoencoder on Wine

### Why this dataset

Wine is small, well documented, and has 13 continuous measurements on different scales. Its two-dimensional bottleneck can be viewed directly. The known cultivar labels provide an external diagnostic and the fixed stratification, but the autoencoder must never see them during training.

### Experiment contract

1. Make one stratified train/validation/test split and save the indices.
2. Fit `StandardScaler` on the training features only.
3. Fit two-dimensional PCA on the standardized training features only.
4. Train a dense `13 -> hidden -> 2 -> hidden -> 13` autoencoder using feature reconstruction.
5. Select architecture and stopping epoch using validation reconstruction loss only.
6. Lock the checkpoint, then evaluate the test set once.

Because standardized Wine values are unbounded, the decoder output should also be unbounded. Do not put sigmoid on the final layer. Mean squared error is a reasonable reconstruction loss in standardized feature space.

### Required practice

- Report split sizes, feature names, scaling evidence, tensor shapes, parameter count, and learning curves.
- Compare held-out reconstruction MSE for PCA inverse reconstruction and the autoencoder.
- Plot PCA coordinates and AE coordinates with the same split markers; reveal cultivar colors only after fitting.
- Fit the same fixed logistic-regression probe on raw standardized features, two PCA coordinates, and two AE coordinates. This probe evaluates a frozen representation; it does not turn the AE training into supervised learning.
- Find nearest neighbors of two held-out examples in latent space and compare their original standardized measurements.
- Interpolate between two held-out codes, decode the path, inverse-transform it, and inspect how several named measurements change.
- Explain why lower reconstruction MSE would not by itself prove better cultivar separation.

## Lab B — Denoising Convolutional Autoencoder on Digits

### Why this dataset

Digits is small enough for fast CPU experiments and has a meaningful image grid. The denoising task makes the training contract visible: corrupted pixels are inputs, while clean pixels are targets.

### Experiment contract

1. Scale pixels from `[0, 16]` to `[0, 1]` and reshape them to `(N, 1, 8, 8)`.
2. Make one stratified train/validation/test split.
3. Define one seeded corruption function, such as clipped Gaussian noise with standard deviation `0.35`.
4. Train a plain convolutional autoencoder on `clean -> clean`.
5. Train the same architecture as a denoising autoencoder on `noisy -> clean`.
6. Select both checkpoints using validation loss. Use the same test corruptions for both models.

The decoder output may use sigmoid because the target pixels are scaled to `[0, 1]`. Keep the noise-generating seed separate from the split seed so the experiment can reproduce both.

### Required practice

- Print the shape after every convolution, latent layer, reshape, and transposed convolution.
- Show at least 12 columns of clean, noisy, plain-AE output, and denoising-AE output. Choose indices before inspecting the outputs.
- Report test MSE for clean inputs and for noise levels `0.0`, `0.2`, `0.35`, and `0.5`.
- Plot error against noise level for the identity baseline, plain AE, and denoising AE.
- Encode clean and corrupted versions of the same test image. Compare their latent distance with distances to unrelated images.
- Explain whether the evidence supports robustness only to the trained corruption or to noise in general.

## Lab C — Variational Autoencoder on Fashion-MNIST

### Why this dataset

Fashion-MNIST is a standard, documented image benchmark with more variation than handwritten digits. A two-dimensional VAE code makes sampling, occupancy, and the effect of regularization visible. Use the starter notebook's fixed subset for CPU training.

### From a point to a distribution

The encoder outputs two vectors for each input:

```text
mu, log_var = encoder(x)
std = exp(0.5 * log_var)
epsilon ~ Normal(0, I)
z = mu + std * epsilon
```

The random draw is isolated in `epsilon`, so gradients can flow through `mu` and `std`. The loss has two separately reported parts:

```text
loss = reconstruction_loss + beta * KL(q(z|x) || Normal(0, I))
```

The reconstruction term asks the decoder to preserve each image. The KL term asks each encoded distribution to stay near the chosen prior. Larger beta usually makes sampling from the prior more defensible but can remove reconstruction detail. This is a trade-off to measure, not a rule that one beta is always best.

### Required practice

- Train the same small VAE with `beta = 1` and one deliberate alternative from `{0.25, 4}`.
- State whether reconstruction loss is summed or averaged and keep the normalization identical across runs.
- Plot training and validation total, reconstruction, and KL loss separately.
- Select checkpoints using a rule written before looking at the test set.
- Plot test `mu` coordinates, then reveal the Fashion-MNIST labels only for interpretation.
- Decode a fixed grid spanning a stated latent range; mark or compare where encoded test points actually occur.
- Interpolate between two fixed test items and display the decoded path.
- Draw at least 64 samples from `Normal(0, I)` with a fixed seed and show all of them, not only favorites.
- Compare beta values using reconstruction, KL, latent occupancy, interpolation, and random samples. State what remains subjective.

Do not use class labels in the VAE loss, early stopping, beta choice, or sample selection.

## Evaluation Boundary

The three labs answer different questions and should not be ranked by raw loss. Wine uses standardized feature MSE, while Digits and Fashion-MNIST use image-pixel objectives with different shapes and ranges. A smaller number across datasets has no meaning.

Within each lab:

- learn preprocessing from training data only;
- use validation data for checkpoint and configuration choices;
- evaluate the test set only after choices are locked;
- report loss normalization and units;
- save the seed, split indices, model architecture, parameter count, optimizer, learning rate, batch size, epoch rule, and approximate training time;
- distinguish observed results from interpretations and hypotheses.

## Framing Questions

1. **What did the objective ask the code to preserve?** If a latent plot separates known labels, did the model learn those labels, or did reconstruction preserve features correlated with them? What experiment would distinguish the claims?

2. **Where is “between” meaningful?** If a decoded interpolation changes smoothly, what does that establish about the decoder, and why does it not establish a causal path in the real world?

3. **What price buys a sampleable space?** How does the VAE's KL term change where codes are allowed to live, and what reconstruction detail may be lost when the regularization is too strong?

## Self-Check

- [ ] I can draw the encoder–latent–decoder data flow and label every tensor shape.
- [ ] I can explain why scaling and the decoder's final activation must match the target range.
- [ ] I can compare PCA and an autoencoder without describing either as the true latent space.
- [ ] I can evaluate reconstruction, neighborhoods, and downstream usefulness as separate properties.
- [ ] I can state exactly which corruption a denoising autoencoder was trained to reverse.
- [ ] I can explain `mu`, `log_var`, reparameterization, KL divergence, and beta in plain language.
- [ ] I can distinguish reconstructing an encoded example from generating a sample from the prior.
- [ ] I can identify empty or weakly supported regions of a two-dimensional latent plot.
- [ ] I can explain why labels used only after training are probes rather than training targets.
- [ ] I can name at least three claims that a visually attractive latent plot does not prove.

**You know enough when:** you can point to a region, path, neighbor, or sample in a latent space and say what evidence created it, which objective shaped it, and which conclusion would go beyond the evidence.
