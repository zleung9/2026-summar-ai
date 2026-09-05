# Section 5 Homework — A Latent-Space Field Guide

> Due: August 12
> Expected effort: about 9 hours across three days

## Goal

Build and compare three small autoencoder variations on three established teaching datasets. Use evidence to explain what each latent space preserves, how it behaves between observations, and which claims it does not support.

Do **not** use the polymer dataset in this section. Begin with [`homework/s05_autoencoders_template.ipynb`](homework/s05_autoencoders_template.ipynb).

## Rules Shared by All Three Labs

1. Use the supplied split seeds and keep train, validation, and test indices disjoint.
2. Learn preprocessing and model parameters from the training split only.
3. Use validation evidence for architecture, epoch, and configuration choices.
4. Write the selection rule before evaluating the test set.
5. Apart from creating the required fixed stratified splits, do not use dataset labels in an autoencoder input, loss, or model selection. Labels may be revealed afterward for a plot or frozen-representation probe.
6. Record architecture, tensor shapes, parameter count, optimizer, learning rate, batch size, epochs, checkpoint rule, seed, and approximate training time.
7. Report how each loss is normalized. Never compare raw loss values across different datasets.

## Task 1 — State the Latent-Space Contract

Before training, complete the contract table in the notebook for all three labs. For each model, identify:

- input shape and numerical range;
- reconstruction target shape and range;
- latent representation and dimension;
- decoder output activation;
- loss and normalization;
- regularizer or corruption process;
- validation selection rule;
- what makes the model undercomplete or otherwise prevents a trivial copy.

Draw one encoder–latent–decoder diagram with tensor shapes for each lab.

## Task 2 — Lab A: Undercomplete Autoencoder on UCI Wine

Use `sklearn.datasets.load_wine`. The 13 measurements are inputs; the cultivar label is hidden during autoencoder and PCA fitting.

### Required work

1. Create the supplied stratified train/validation/test split and prove the indices are disjoint.
2. Fit `StandardScaler` and two-dimensional PCA on the training features only.
3. Train a dense autoencoder with a two-dimensional bottleneck and an unrestricted output layer.
4. Select the checkpoint using validation reconstruction MSE.
5. After locking the model, report test feature-reconstruction MSE for PCA inverse reconstruction and the autoencoder.
6. Show original versus reconstructed values for at least five held-out rows and report per-feature MSE in original feature units.
7. Plot the two PCA coordinates and two AE coordinates. Use split markers and reveal cultivar colors only after fitting.
8. Fit the same fixed logistic-regression probe on:
   - all 13 standardized features;
   - two PCA coordinates;
   - two frozen AE coordinates.
   Report held-out accuracy and the three confusion matrices.
9. For two test examples chosen by index before inspection, show their three nearest training neighbors in AE space and compare named measurements.
10. Decode 11 evenly spaced points between two fixed test codes. Inverse-transform and plot at least four named measurements along the path.

### Critical questions

1. Which evidence evaluates reconstruction, which evaluates neighborhood structure, and which evaluates downstream usefulness?
2. If cultivar colors form clusters, why does that not mean the model was trained to classify cultivar?
3. If the AE has lower reconstruction MSE than PCA but lower probe accuracy, is either result contradictory? Explain.
4. What does the decoded interpolation show, and what scientific claim would go too far?

## Task 3 — Lab B: Denoising Autoencoder on Digits

Use `sklearn.datasets.load_digits`. Scale the 8-by-8 pixels to `[0, 1]`. Train two models with the same convolutional architecture:

- **Plain AE:** clean image to clean image
- **Denoising AE:** Gaussian-corrupted image to clean image, using training noise standard deviation `0.35` and clipping to `[0, 1]`

### Required work

1. Create the supplied stratified split and prove that it is disjoint.
2. Print and explain every major encoder and decoder tensor shape for one batch.
3. Train both models with the same split, architecture, optimizer family, maximum epochs, and checkpoint rule.
4. Select each checkpoint using its validation objective only.
5. Choose 12 test indices before inspecting the outputs. Show clean input, noisy input, plain-AE reconstruction, and denoising-AE reconstruction for every index.
6. With fixed test corruptions, report per-pixel test MSE at noise standard deviations `0.0`, `0.2`, `0.35`, and `0.5` for:
   - the noisy identity baseline;
   - the plain AE;
   - the denoising AE.
7. Plot error against noise level for all three methods.
8. For at least 50 held-out images, calculate the latent distance between each clean image and its corrupted version. Compare that distribution with distances between unrelated test images.

### Critical questions

1. Why is the noisy image the input but not the target?
2. At which noise levels does the denoising model improve over the plain model and the identity baseline?
3. Does success with clipped Gaussian noise support robustness to blur, rotation, missing strokes, or real sensor noise? Why or why not?
4. If denoising improves output MSE but clean/noisy codes remain far apart, what property improved and what property did not clearly improve?

## Task 4 — Lab C: Variational Autoencoder on Fashion-MNIST

Use `torchvision.datasets.FashionMNIST` and the fixed CPU-sized subset in the starter notebook. Train the same two-dimensional VAE with:

- `beta = 1`; and
- one alternative selected **before training** from `beta = 0.25` or `beta = 4`.

Class labels must not affect the VAE loss, early stopping, beta choice, or sample selection.

### Required work

1. Implement `mu`, `log_var`, reparameterization, decoding, and the two-part VAE loss.
2. Verify tensor shapes and show that gradients reach both the `mu` and `log_var` encoder heads.
3. Train both beta configurations with the same split, subset, architecture, optimizer, epoch budget, and random seeds.
4. Plot training and validation total, reconstruction, and KL loss as separate quantities.
5. Use a written validation rule to lock one checkpoint per beta, then report test reconstruction and KL terms separately.
6. Plot test `mu` coordinates. Make one unlabeled version first, then a second version colored by the ten Fashion-MNIST labels.
7. Decode a fixed two-dimensional grid over a stated coordinate range. Show or summarize where encoded test points lie relative to the grid.
8. Interpolate between two fixed test images and decode at least 11 points.
9. Draw 64 codes from `Normal(0, I)` using a fixed seed and display every decoded sample.
10. Compare the two beta values using reconstruction detail, KL value, code occupancy, interpolation, and random samples.

### Critical questions

1. Why does the encoder produce `mu` and `log_var` rather than one code?
2. How does `z = mu + exp(0.5 * log_var) * epsilon` allow gradient-based training through sampling?
3. What behavior does the KL term encourage, and what can be lost when beta is too large?
4. Why are reconstructions not evidence that samples drawn from the prior will be good?
5. Which parts of the beta comparison are numerical, and which still require cautious visual judgment?

## Task 5 — Synthesize a Latent-Space Field Guide

Create one final table with one row per trained representation and these columns:

| Dataset | Model | Code dimension | Constraint | Reconstruction evidence | Neighborhood or robustness evidence | Sampling evidence | Main limitation |
|---|---|---:|---|---|---|---|---|

Then answer in 250–400 words:

1. How did the bottleneck, corruption objective, and KL regularization create different kinds of latent spaces?
2. Which model best supports interpolation? Which best supports sampling from a known prior? What evidence supports each answer?
3. Name three conclusions that the plots do not establish.
4. Give one example of a useful latent space that would not form clean class clusters.

## Task 6 — Critical AI Review

Ask Codex to review the completed notebook for:

- labels leaking into unsupervised training or selection;
- preprocessing fit outside the training split;
- mismatched input range, output activation, and loss;
- incorrect VAE loss normalization or KL sign;
- test-set tuning;
- cherry-picked reconstructions or samples;
- claims that exceed the evidence.

Record one suggestion you accepted and one you changed or rejected. For each, show the evidence used in your decision.

## Deliverables

Submit one pull-request link containing:

1. `sections/s05/submissions/<github-username>/s05_autoencoders.ipynb`;
2. any small helper module written specifically for the notebook;
3. a pull-request description that states:
   - the three dataset/model pairs;
   - the fixed seeds and split sizes;
   - the main result from each lab;
   - the selected VAE beta and why;
   - one supported latent-space claim and one claim you rejected;
   - one Codex suggestion accepted and one changed or rejected;
   - links to GitHub Issues opened, or “None.”

Do not commit Fashion-MNIST files, cached data, model checkpoints, or generated training artifacts.

## Acceptance Criteria

- [ ] The work is on a branch named `s05/<github-username>`
- [ ] Restarting the kernel and running all cells completes without errors
- [ ] Wine, Digits, and Fashion-MNIST are used; the polymer dataset is not used
- [ ] All train, validation, and test indices are disjoint and reproducible
- [ ] Learned preprocessing sees training data only
- [ ] Dataset labels do not enter autoencoder inputs, losses, checkpoint selection, beta choice, or sample selection
- [ ] Each model's input range, decoder output activation, target, loss, and tensor shapes form a correct contract
- [ ] Experiment metadata and loss normalization are recorded for every run
- [ ] Wine includes PCA and AE reconstruction, two-dimensional plots, fixed probes, neighbors, and interpolation
- [ ] Digits includes matched plain and denoising models, fixed corruption, reconstruction panels, a robustness curve, and latent-distance evidence
- [ ] Fashion-MNIST includes two beta values, correct reparameterization, separate reconstruction/KL curves, a latent map, decoder grid, interpolation, and all 64 random samples
- [ ] Test sets are evaluated only after the selection rules and checkpoints are locked
- [ ] The final field-guide table distinguishes reconstruction, robustness, downstream use, and sampling
- [ ] Critical answers separate observation, interpretation, and unsupported claims
- [ ] The AI-review reflection shows independent judgment
- [ ] The pull request is ready for review and contains no cached datasets or checkpoints

## Scope Guidance

The starter notebook deliberately limits Fashion-MNIST for CPU use. Do not expand the search. One dense AE, two matched convolutional AEs, and two matched VAE beta runs are enough. If a model performs poorly, diagnose its contract, curves, and outputs; do not repeatedly tune against the test set.
