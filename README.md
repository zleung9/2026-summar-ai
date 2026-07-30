# AI Native Machine Learning Engineer — Summer Course Plan

> This is a living plan. It will be updated as each section's guide, homework, and schedule evolve.

## Overall Goal

24 study days centered on a polymer materials mini-project:

> **Predicting Polymer Material Properties with Machine Learning**

The target property (glass transition temperature, melting point, etc.) will be chosen based on data availability.

The course follows two parallel threads:

1. **Top-down:** Use Codex for data analysis, model development, debugging, testing, and project presentation.
2. **Bottom-up:** Progress from data exploration and classical machine learning to deep learning, latent-variable models, Transformers, and modern generative models.

Final deliverables:

- A working machine learning project for polymer material properties
- A complete GitHub repository
- A project description and experiment report
- A 10–15 minute project demo

---

## Q&A Schedule

### Daily Check-in

Every morning **8:00–8:30**, a 30-minute session for:

- Reviewing the previous day's homework
- Answering questions from learning and coding
- Checking whether the student understands AI-generated code
- Clarifying the day's learning tasks

### Section-end Review

After each Section, schedule a **1-hour review session** as needed for:

- Resolving leftover issues from the section
- Checking three days of homework
- Discussing project design and model selection
- Adjusting the next section's learning plan

---

## Section 1: AI-Native Development & Environment Setup

**Dates: July 29 — July 31**

### Topics

- GitHub forks, clones, branches, issues, pull requests, and code review
- Running Python scripts and notebooks in VS Code
- Virtual environments and dependency management with `uv`
- Debugging with breakpoints and variable inspection
- Using Codex while critically reviewing its suggestions

### Three-Day Tasks

- Day 1: Fork and clone the course repository; set up Python, `uv`, and VS Code
- Day 2: Create and run a simple polymer-temperature script and notebook; practise debugging
- Day 3: Review the work with Codex and submit it through a GitHub pull request

### Homework

- Submit one pull request containing `polymer_demo.py` and `polymer_demo.ipynb`
- Include a short debugger observation and reflection on one Codex suggestion
- Ask questions through GitHub Issues when needed

---

## Section 2: Data Exploration

**Dates: August 1 — August 3**

### Purpose

Develop an intuition for the dataset before building models. The student should be able to describe the typical values, variability, distributions, outliers, relationships, and dominant directions in the data.

### Topics

- Descriptive statistics: count, mean, median, variance, standard deviation, quantiles, and missing values
- Data distributions, histograms, density plots, and box plots
- Outliers and the effect of scale
- Pearson correlation for linear relationships
- Spearman correlation for monotonic relationships
- Feature standardization
- Principal Component Analysis (PCA), explained variance, and low-dimensional visualization
- **Bonus:** Singular Value Decomposition (SVD), its derivation, and its connection to PCA

### Three-Day Tasks

- Day 1: Load and audit the polymer dataset; calculate descriptive statistics and inspect missing values
- Day 2: Visualize distributions and outliers; compare Pearson and Spearman correlation matrices
- Day 3: Standardize the features, run PCA, and interpret the principal components and explained variance

### Homework

- Submit a reproducible exploratory data analysis notebook
- Include a descriptive-statistics table and a missing-data summary
- Include distribution plots and box plots for important variables
- Compare Pearson and Spearman correlations and explain at least one meaningful difference
- Include a PCA projection and explained-variance analysis
- **Bonus:** Derive the main SVD steps and explain how SVD is used to compute PCA

---

## Section 3: Machine Learning

**Dates: August 4 — August 6**

### Purpose

Build trustworthy regression and classification baselines, understand how training choices affect generalization, and evaluate models with metrics appropriate to the task.

### Topics

#### Models

- Linear regression for continuous targets
- Logistic regression for classification

#### Training and Generalization

- Bias and variance
- Train/test splits and the role of a validation set
- Loss functions and optimization objectives
- Underfitting and overfitting
- Cross-validation
- Data leakage

#### Evaluation

- **Regression:** R2 as the primary metric, plus MAE, MSE, and RMSE
- **Classification:** confusion matrix, precision, recall, F1 score, and ROC-AUC
- Comparing training, validation, and test performance
- Choosing metrics based on the scientific question and class balance

### Three-Day Tasks

- Day 1: Define regression and classification tasks and train linear and logistic regression baselines
- Day 2: Study bias, variance, loss, data splits, leakage, and overfitting; apply cross-validation
- Day 3: Evaluate both tasks, interpret errors, and document what the metrics do and do not show

### Homework

- Repeat and update the Section 2 data exploration for the exact data used in training
- Submit reproducible train/test splitting and cross-validation code
- Report R2, MAE, MSE, and RMSE for the regression model
- Report a confusion matrix, F1 score, and ROC-AUC for the classification model
- Compare training and test results and explain whether there is evidence of bias, variance, or overfitting
- Record both baselines so later sections can compare against them

---

## Section 4: Deep Neural Networks

**Dates: August 7 — August 9**

### Purpose

Understand how neural networks learn and apply that understanding through a multilayer perceptron (MLP) and a convolutional neural network (CNN).

### Topics

- Neurons, layers, weights, biases, and activation functions
- Forward propagation
- Loss functions for regression and classification
- Backpropagation and the chain rule
- Gradient-based optimization
- Batch size, learning rate, epochs, and regularization
- MLPs for tabular representations
- CNNs for local patterns in grid or sequence representations

### Three-Day Tasks

- Day 1: Implement a small neural network and trace forward propagation, loss, and backpropagation
- Day 2: Train and tune an MLP while monitoring learning curves and overfitting
- Day 3: Build a CNN experiment and compare it with the MLP and Section 3 baselines

### Homework

- Include updated data statistics, distributions, box plots, correlations, and PCA for the model inputs
- Submit training code and learning curves for an MLP and a CNN
- Explain the chosen architecture, activation functions, loss function, and optimizer
- Evaluate regression with R2, MAE, MSE, and RMSE where applicable
- Evaluate classification with a confusion matrix, F1 score, and ROC-AUC where applicable
- Compare both neural networks with the Section 3 baselines and discuss overfitting

---

## Section 5: Autoencoders

**Dates: August 10 — August 12**

### Purpose

Learn representation learning by compressing data into a latent space and reconstructing it with an encoder-decoder model.

### Topics

- Encoder, decoder, bottleneck, and latent space
- Reconstruction objectives and reconstruction loss
- The effect of latent-space dimensionality
- Visualizing and interpreting latent representations
- Denoising and regularized autoencoders
- **Bonus:** Variational autoencoder intuition

### Three-Day Tasks

- Day 1: Build and train a basic autoencoder and inspect reconstruction quality
- Day 2: Explore the latent space and compare it with PCA
- Day 3: Use latent features in a downstream prediction task and test different bottleneck sizes

### Homework

- Repeat the core data exploration and compare raw-feature and latent-feature distributions
- Submit the encoder, decoder, training loop, and reconstruction analysis
- Visualize the latent space and compare it with the Section 2 PCA projection
- Evaluate reconstruction error and the downstream prediction task
- Report the appropriate regression or classification metrics from Section 3
- Compare raw features, PCA features, and autoencoder features

**August 13–14: Makeup days, code cleanup, homework revision, and review session.**

---

## Section 6: Transformer Part I — Foundations

**Dates: September 15 — September 17**

### Purpose

Understand the components of the original Transformer and implement a small attention-based model for molecular or material sequences.

### Topics

- Tokens and tokenization for molecular strings or material sequences
- Embedding vectors and learned representations
- Positional encoding and why order must be represented
- Queries, keys, and values
- Scaled dot-product attention
- Self-attention, cross-attention, and attention masks
- Multi-head attention
- Feed-forward networks
- Residual connections and layer normalization
- Encoder and decoder blocks
- Training objectives and sequence-level prediction

### Three-Day Tasks

- Day 1: Tokenize sample molecular sequences and inspect embeddings and positional encodings
- Day 2: Calculate self-attention by hand and in code, then extend it to multiple heads
- Day 3: Assemble a small Transformer encoder and train it on a prediction task

### Homework

- Explore token counts, sequence lengths, target distributions, outliers, correlations, and PCA of learned embeddings
- Submit a working scaled dot-product attention implementation with shape checks
- Visualize and interpret at least one attention map
- Train a small Transformer and document its loss curve
- Evaluate it with the Section 3 metrics appropriate to the task
- Compare it with the strongest earlier baseline

---

## Section 7: Transformer Part II — Modern Architectures and Mixture of Experts

**Dates: September 18 — September 20**

### Purpose

Connect the foundational Transformer to modern large-model design and understand how Mixture-of-Experts (MoE) increases model capacity without activating every parameter for every token.

### Topics

- Encoder-only, decoder-only, and encoder-decoder architectures
- Autoregressive and masked-token training objectives
- Pre-normalization, RMSNorm, and gated feed-forward layers
- Rotary positional embeddings (RoPE) and relative position methods
- Multi-query and grouped-query attention
- KV caching and efficient autoregressive inference
- FlashAttention as an algorithmic and systems concept
- Pretraining, fine-tuning, and parameter-efficient adaptation
- Scaling tradeoffs: parameters, context length, data, compute, and memory
- MoE experts, routers, top-k routing, and sparse activation
- Expert capacity, load balancing, auxiliary losses, and expert collapse
- Quality, efficiency, communication, and serving tradeoffs in MoE systems

### Three-Day Tasks

- Day 1: Compare modern Transformer architecture choices and modify the Section 6 model with selected improvements
- Day 2: Implement a small MoE feed-forward layer and inspect routing and expert utilization
- Day 3: Compare dense and MoE models at similar compute budgets and analyze quality-efficiency tradeoffs

### Homework

- Repeat the relevant data and representation exploration, including token and routing distributions
- Submit diagrams of a modern Transformer block and an MoE block
- Report router behavior, expert utilization, and load-balance statistics
- Evaluate dense and MoE models with the appropriate Section 3 metrics
- Compare parameter count, active parameters, training time, memory use, and predictive performance
- Explain when an MoE model is and is not a sensible choice

**September 21: Makeup day, project debugging, homework revision, and review session.**

---

## Section 8: Diffusion and Flow Matching

**Dates: September 22 — September 24**

### Purpose

Develop an introductory mental model of modern continuous generative modeling through diffusion and flow matching, then connect these methods to scientific and materials data.

### Topics

- Generative versus predictive modeling
- The diffusion forward process: gradually adding noise
- The reverse process: learned denoising
- Noise schedules, timestep conditioning, and sampling
- Predicting noise, data, or velocity
- Score-function intuition
- Conditional generation and classifier-free guidance
- Flow matching with probability paths and learned vector fields
- The ordinary differential equation (ODE) view of generation
- Similarities and differences between diffusion and flow matching
- Evaluation challenges for generative models
- Potential applications to molecular and material generation

### Three-Day Tasks

- Day 1: Visualize the forward and reverse diffusion processes on a simple two-dimensional dataset
- Day 2: Train a small conditional diffusion model and inspect its generated distribution
- Day 3: Implement a simple flow-matching experiment and compare its trajectories and samples with diffusion

### Homework

- Explore and compare the real and generated data distributions using summary statistics, box plots, correlations, and PCA
- Submit visualizations of diffusion timesteps, denoising, and flow trajectories
- Explain the training target and sampling process for both diffusion and flow matching
- Evaluate predictive components with the Section 3 metrics where applicable
- Evaluate generated samples with distributional comparisons and clearly state the limitations
- Write a short comparison of autoencoders, Transformers, diffusion, and flow matching

---

## Recurring Homework Requirements

The course is cumulative. Later sections must continue to demonstrate the habits established earlier.

### Data Exploration

Every homework submission from Section 2 onward must include an updated exploration of the exact data or representations used in that section. At minimum, the student should report relevant summary statistics, inspect distributions and outliers, and use appropriate visualizations. Pearson correlation, Spearman correlation, box plots, and PCA should be revisited whenever they help explain the inputs, learned representations, errors, or generated samples.

### Evaluation

Every homework submission after Section 3 must evaluate the new method against a meaningful earlier baseline:

- Regression tasks must prioritize **R2** and also report MAE, MSE, and RMSE.
- Classification tasks must include a confusion matrix, F1 score, and ROC-AUC when ROC-AUC is well-defined.
- Representation-learning tasks must report reconstruction or representation quality plus downstream-task performance.
- Generative tasks must compare real and generated distributions and explain the limitations of the selected measurements.
- Every submission must distinguish training, validation, and test results and discuss possible overfitting or data leakage.

---

# Suggested Daily Rhythm

Approximately 3 hours of study per day:

- 8:00–8:30: Teacher check-in and previous day's homework review
- 45 min: Complete theory study per the learning plan
- 90 min: Use Codex for programming and project tasks
- 30 min: Record prompts, questions, and experiment results
- 15 min: Commit code and write a learning log

At the end of each day, submit:

- Code completed that day
- Important prompts used
- Problems encountered and how they were resolved
- A daily learning summary
- Questions to address the next day

After completing each Section (every 3 days), schedule a 1-hour review session and evaluate that section's homework.
