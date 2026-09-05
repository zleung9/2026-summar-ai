# Section 5 Answer Key

(For teacher use only — do not share with students)

## What This Section Tests

This assignment tests whether the student can treat a latent space as a model-dependent representation rather than a decorative scatter plot. A successful student should be able to:

1. match each input range, decoder output, target, and reconstruction loss;
2. preserve the train/validation/test boundary in an unsupervised experiment;
3. separate reconstruction, neighborhood structure, robustness, downstream usefulness, and sampleability;
4. explain how a bottleneck, corruption objective, and KL regularizer impose different constraints;
5. inspect latent geometry with several complementary tests and avoid causal or semantic overclaims;
6. implement and diagnose a small VAE, including reparameterization and correct KL calculation.

Exact scores are not fixed. They depend on stochastic training and reasonable architecture choices. Grade the experiment contract, evidence, and interpretation before visual appeal or score.

## Dataset Roles and Label Boundary

| Dataset | Inputs used to train the autoencoder | Permitted label use | Prohibited label use |
|---|---|---|---|
| Wine | 13 standardized measurements | Supplied stratification, post-training coloring, fixed frozen-representation probe | Autoencoder input, reconstruction target, loss, early stopping, architecture choice |
| Digits | Clean or corrupted 8-by-8 pixels | Supplied stratification, post-training interpretation | Denoising loss, checkpoint choice, corruption choice based on class results |
| Fashion-MNIST | 28-by-28 pixel tensor | Fixed subset/split construction and post-training coloring | VAE input beyond pixels, loss, beta choice, early stopping, sample selection |

Using labels to create the assignment's fixed stratified indices is not leakage into model fitting. Repeatedly changing a split or beta after viewing class separation is model selection with labels and should be corrected.

## Reference Experiment Contracts

| Lab | Input | Target | Output | Suggested loss | Essential constraint |
|---|---|---|---|---|---|
| Wine AE | Standardized float tensor `(N, 13)`, unbounded | Same tensor | Unbounded `(N, 13)` | Per-element MSE | Two-dimensional bottleneck |
| Digits plain AE | Clean float tensor `(N, 1, 8, 8)` in `[0, 1]` | Clean tensor | Sigmoid output with same shape | Per-pixel MSE | Small convolutional bottleneck |
| Digits denoising AE | Corrupted, clipped tensor in `[0, 1]` | Original clean tensor | Sigmoid output with same shape | Per-pixel MSE | Corruption plus bottleneck |
| Fashion-MNIST VAE | Float tensor `(N, 1, 28, 28)` in `[0, 1]` | Same clean tensor | Sigmoid output with same shape | BCE reconstruction plus beta-weighted KL | Two-dimensional distributional code and prior |

A student may use MSE rather than BCE for Fashion-MNIST if the likelihood interpretation and normalization are stated and both beta runs use the same contract. Do not accept a sigmoid Wine decoder: standardized values can lie below zero or above one.

## Split and Reproducibility Reference

The starter notebook uses:

```text
GLOBAL_SEED = 42
SPLIT_SEED = 42
NOISE_SEED = 31415
```

Expected approximate split sizes from two stratified `train_test_split` calls are:

| Dataset | Train | Validation | Test |
|---|---:|---:|---:|
| Wine, 178 rows | 106 | 36 | 36 |
| Digits, 1,797 images | 1,077 | 360 | 360 |

Fashion-MNIST uses a fixed 12,000-example subset of the official training set, split into 10,000 training and 2,000 validation items, plus 2,000 fixed items from the official test set. Small count differences are acceptable if the student's saved indices remain fixed, disjoint, class-reasonable, and documented.

Require direct intersection checks on integer indices. A statement that `train_test_split` was called is not sufficient evidence. Wine scaling and PCA must fit the training split only. Image scaling by a known constant such as `16` or `255` is not a learned transform and may be applied to all splits.

## Lab A Reference — Undercomplete Wine Autoencoder

### Acceptable model

One intentionally small architecture is:

```text
Encoder: Linear(13, 8) -> ReLU -> Linear(8, 2)
Decoder: Linear(2, 8) -> ReLU -> Linear(8, 13)
```

Other small symmetric or asymmetric dense networks are acceptable. The code must be exactly two-dimensional for the required direct plot and traversal. The final decoder layer must be unrestricted. Excessive width on 106 training examples should prompt an overfitting check.

### PCA comparison

The correct PCA reconstruction workflow is:

```python
pca.fit(X_train_scaled)
z_test = pca.transform(X_test_scaled)
X_test_pca_hat = pca.inverse_transform(z_test)
```

The comparison is between two-dimensional representations on the same standardized held-out features. Report MSE with the same reduction for both. It is not enough to compare PCA explained variance with AE training loss.

PCA is a linear projection with orthogonal directions ordered by explained variance. A nonlinear AE can bend its representation and may reconstruct better, but has no guaranteed ordering, orthogonality, sign, scale, or run-to-run orientation. A one-hidden-layer **linear** AE trained with squared error spans the same principal subspace under standard conditions, but its coordinates need not equal PCA coordinates.

### Fixed probe

The probe should use identical logistic-regression settings and the same train/test rows for:

1. 13 standardized features;
2. two training-fitted PCA coordinates;
3. two frozen AE coordinates.

The encoder and PCA remain frozen. The probe is supervised evaluation of a representation, not part of representation learning. Because the test set is small, minor accuracy differences are unstable; the student should report counts or confusion matrices and avoid universal ranking claims.

### Neighbors and interpolation

Neighbors must be selected in the declared latent metric, normally Euclidean distance, and should come from training codes for a held-out query. Comparing original measurements is essential: a list of row indices does not show what “nearby” preserved.

For interpolation,

```python
t = torch.linspace(0, 1, 11).unsqueeze(1)
z_path = (1 - t) * z_a + t * z_b
X_path_scaled = decoder(z_path)
X_path = scaler.inverse_transform(X_path_scaled.detach().cpu().numpy())
```

Smooth curves show decoder behavior along this path. They do not show that an intermediate wine exists, is physically realizable, or results from mixing the endpoint wines.

### Strong answers to the critical questions

- Reconstruction MSE evaluates retained input information; neighbors inspect local geometry; the frozen probe evaluates cultivar information accessible to a simple classifier.
- Cultivar separation can emerge because reconstruction retains measurements correlated with cultivar. The labels were not the objective.
- Better reconstruction and worse probe accuracy are compatible because reconstruction weights all input variation, while the probe asks about one external label.
- Interpolation tests continuity of this decoder on one segment. It does not establish causality, a chemical process, or data density along the path.

## Lab B Reference — Denoising Digits Autoencoder

### Acceptable model and shapes

One compact architecture is:

```text
(N, 1, 8, 8)
 -> Conv2d(1, 8, kernel=3, stride=2, padding=1) -> (N, 8, 4, 4)
 -> Conv2d(8, 16, kernel=3, stride=2, padding=1) -> (N, 16, 2, 2)
 -> flatten -> (N, 64)
 -> Linear(64, 8) -> (N, 8) latent
 -> Linear(8, 64) -> reshape (N, 16, 2, 2)
 -> ConvTranspose2d(16, 8, kernel=4, stride=2, padding=1) -> (N, 8, 4, 4)
 -> ConvTranspose2d(8, 1, kernel=4, stride=2, padding=1) -> (N, 1, 8, 8)
 -> sigmoid
```

Other working convolutional shapes are acceptable. The student must print actual shapes rather than copying the reference. A fully connected denoiser does not satisfy the required convolutional practice.

### Corruption contract

A correct seeded corruption resembles:

```python
noise = torch.randn(x.shape, generator=generator, device=x.device) * sigma
noisy = torch.clamp(x + noise, 0.0, 1.0)
```

Depending on the PyTorch version and device, generate the noise on CPU and transfer it if a device-specific generator is awkward. The important points are fixed randomness, clipping, and a clean target.

Training `noisy -> noisy` teaches reconstruction of the corrupted observation, not denoising. Generating one fixed noisy copy for the entire training run is acceptable if stated, but new seeded corruption per epoch offers more corruption examples. Validation and test corruption must be fixed for paired comparisons.

### Robustness comparison

At sigma `0`, the identity baseline has exactly zero error and should outperform a non-perfect reconstruction model. This is expected and is a useful check. The denoising AE may be slightly worse than the plain AE on clean inputs while better near the trained noise level. At sigma `0.5`, either network may fail; extrapolation is not guaranteed.

For each sigma, the plain AE and denoising AE must receive the exact same corrupted test tensors. Otherwise, their error difference contains corruption-sample noise. Report mean per-pixel MSE consistently.

### Latent-distance evidence

A robust code should often place a clean image closer to its own corrupted version than to unrelated images. Compare distributions over many held-out items; a single attractive example is weak evidence. Raw distance magnitude depends on latent scale, so same-model paired comparisons are more meaningful than comparing raw distances across models.

### Strong answers to the critical questions

- The objective maps a corrupted observation back toward the clean-data manifold; using noisy targets would preserve noise.
- Improvement must be stated by method and tested sigma. It should not be generalized beyond the curve.
- Gaussian-pixel robustness does not establish robustness to structured corruptions, transformations, or real measurement processes.
- Better decoded MSE indicates improved output recovery. Large clean/noisy code distances show that invariance in the representation has not clearly improved.

## Lab C Reference — Fashion-MNIST VAE

### Acceptable model

A CPU-friendly MLP VAE is sufficient:

```text
Encoder: flatten 784 -> Linear(784, 256) -> ReLU
Heads: Linear(256, 2) for mu; Linear(256, 2) for log_var
Sample: z = mu + exp(0.5 * log_var) * epsilon
Decoder: Linear(2, 256) -> ReLU -> Linear(256, 784) -> sigmoid -> reshape
```

A small convolutional VAE is also acceptable if all shapes and loss reductions are correct. Two latent dimensions are required for the direct decoder grid.

### Reparameterization and gradients

Reference implementation:

```python
def reparameterize(mu, log_var):
    std = torch.exp(0.5 * log_var)
    epsilon = torch.randn_like(std)
    return mu + std * epsilon
```

Writing `Normal(mu, std).sample()` creates a sample operation that ordinarily blocks the desired pathwise gradient. `rsample()` is a valid alternative because it implements reparameterized sampling.

After one backward pass, gradients for both the `mu` and `log_var` head weights should exist and be finite. A zero gradient in one tiny batch is possible but unlikely; inspect the implementation before accepting it.

### Loss reference

One consistent per-sample loss is:

```python
reconstruction_sum = F.binary_cross_entropy(x_hat, x, reduction="sum")
kl_sum = -0.5 * torch.sum(1 + log_var - mu.pow(2) - log_var.exp())

reconstruction = reconstruction_sum / x.shape[0]
kl = kl_sum / x.shape[0]
total = reconstruction + beta * kl
```

The reconstruction term is then summed over pixels and averaged over examples; KL is summed over latent dimensions and averaged over examples. Averaging both over all elements without adjusting their relative scale changes the effective beta. This is not automatically wrong, but it must be intentional, identical across runs, and explained.

Common KL errors include the wrong sign, using `std` where `log_var` is expected, omitting `exp(log_var)`, or averaging one term per pixel and the other per sample.

### Interpreting beta

Relative to beta `1`:

- beta `0.25` often favors reconstruction, allows more irregular or dispersed codes, and can make prior samples less reliable;
- beta `4` often lowers KL, pushes codes toward the prior, worsens detail, and can cause posterior collapse if the decoder ignores `z`.

These are hypotheses, not guaranteed outcomes. The student's curves and outputs decide what happened. A nearly zero KL combined with very similar reconstructions across inputs is evidence to investigate for posterior collapse.

### Latent map, grid, interpolation, and sampling

The direct two-dimensional map should normally use `mu` rather than one stochastic sample so repeated plotting is stable. The student should state this choice.

For the decoder grid, a range such as `[-3, 3]` on each axis is reasonable for a standard-normal prior, but the student must compare it with actual test-code occupancy. Corners near `(±3, ±3)` have low prior density; a rectangular grid visually overrepresents them.

Reconstructions use `z ~ q(z|x)` or `mu` for observed `x`. Prior samples use `z ~ Normal(0, I)` without an input. Good reconstructions do not prove prior samples are good because an irregular aggregate posterior may occupy only selected regions.

All 64 fixed-seed samples must be shown. Selecting the best-looking samples invalidates the visual evidence. Visual quality remains partly subjective; reconstruction and KL terms are numerical, but realism/diversity need an explicitly defined metric for a stronger claim.

### Strong answers to the critical questions

- `mu` and `log_var` parameterize an input-dependent approximate posterior, expressing location and uncertainty rather than one deterministic coordinate.
- Reparameterization moves randomness into `epsilon`, leaving a differentiable transformation of `mu` and `std`.
- KL encourages each approximate posterior toward the standard-normal prior. Too much pressure can discard input information and damage reconstruction.
- Reconstructions start from codes produced for real images, while generation starts from arbitrary prior draws. The latter requires prior/posterior alignment.
- Reconstruction and KL are numeric. Continuity, recognizability, diversity, and whether samples look “good” remain visual judgments unless operational metrics are added.

## What a Strong Synthesis Says

A strong synthesis resembles:

> “The Wine bottleneck learned two coordinates that retained enough standardized measurement variation for reconstruction, but its cultivar probe result evaluated a separate property. The Digits corruption objective improved recovery near the trained Gaussian noise level; it did not establish robustness to other distortions. The Fashion-MNIST VAE traded reconstruction detail for a code distribution closer to the standard-normal prior. Its prior samples therefore address a question that deterministic AE reconstructions cannot. Across all three labs, distance and interpolation are properties of a learned encoder/decoder and objective, not direct measurements of real-world causality.”

Weak claims include:

- “The axes discovered the true factors.”
- “Clusters prove the labels were learned.”
- “Smooth interpolation proves the intermediate is real.”
- “The VAE generated new data” when only reconstructions are shown.
- “The denoising AE is robust to noise” without naming and varying the corruption.
- “A lower loss makes this dataset/model better” across incomparable loss scales.

## Common Failure Modes

| Symptom | Likely cause | Useful diagnostic |
|---|---|---|
| Wine reconstructions are restricted to `[0, 1]` | Sigmoid on standardized output | Print target min/max and final activation |
| Extremely optimistic PCA or AE result | Scaler/PCA fit before split or test used for selection | Show the exact rows passed to each `.fit()` |
| Latent plot changes every display | VAE stochastic samples used instead of `mu` | Plot `mu`; use a fixed seed when sampling |
| Denoiser reproduces noise | Noisy image used as both input and target | Display one training input/target pair |
| Denoiser comparison varies each run | Different test noise for each model | Cache one corrupted test tensor per sigma |
| VAE KL is negative | Sign or formula error | Evaluate the formula on `mu=0`, `log_var=0`; KL should be zero |
| VAE ignores the latent code | Excessive beta or powerful decoder; posterior collapse | Inspect KL per dimension and reconstructions across inputs |
| Good reconstructions, bad prior samples | Aggregate posterior does not match the prior | Overlay code occupancy and sample coordinates |
| Beautiful classes after t-SNE | Nonlinear projection used as proof of separation | Require direct 2D code or a quantitative fixed probe |
| Test score improves across notebook attempts | Test-set tuning | Review execution order and experiment log |
| Only attractive samples are displayed | Cherry-picking | Require fixed indices/seeds and the complete sample grid |

## Section-Specific Grading Guide

Apply the course-wide rubric and completion gates. The following evidence helps allocate the 100 points:

| Area | Points | Full-credit evidence |
|---|---:|---|
| Required deliverables and scope | 10 | All three labs, field guide, critical answers, AI review, and PR metadata are present; no polymer data or cached datasets are committed |
| Technical correctness and reproducibility | 25 | Correct splits, training-only preprocessing, range/loss contracts, shapes, seeded corruption, VAE reparameterization/KL, and clean restart/run-all |
| Core concepts and critical reasoning | 25 | Clear distinctions among reconstruction, geometry, robustness, probing, and sampling; accurate bottleneck/denoising/VAE explanations; no semantic or causal overclaims |
| Evidence and evaluation | 15 | Required curves, metrics, reconstructions, neighbors, traversals, probes, robustness tests, grids, and all samples support the conclusions |
| Communication and organization | 10 | Figures are labeled, reductions and units are explicit, tables are readable, and observations are separated from interpretations |
| AI-native workflow and judgment | 10 | One accepted and one changed/rejected review suggestion with evidence; student can defend generated code |
| Git and professional workflow | 5 | Correct branch, file location, commits, PR description, and issue links |

Completion requires all three working models, a valid VAE loss, held-out evaluation, and a defensible synthesis. Bonus polish cannot compensate for a missing lab or test-set misuse.

## What to Probe During Review

1. Ask the student to rotate or swap two latent axes mentally. Which reported quantities should stay the same?
2. Ask why Wine uses no sigmoid while Digits and Fashion-MNIST may use sigmoid.
3. Give a Wine point between two codes and ask what “between” means and does not mean.
4. Ask to show the exact tensor pair used for one denoising update.
5. Ask why the identity baseline must win at noise sigma zero.
6. Ask the student to derive why KL is zero at `mu=0`, `log_var=0`.
7. Ask whether `sample()` and `rsample()` have the same gradient behavior.
8. Ask for the difference between a reconstruction, interpolation, traversal, and prior sample.
9. Ask which single conclusion changed after viewing quantitative evidence.
10. Ask the student to identify one attractive plot that could still be misleading.

The section is complete when the student can inspect a latent-space claim, name the training objective and evaluation that produced it, and explain what additional evidence would be needed to make a stronger claim.
