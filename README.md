# AI Native Machine Learning Engineer — Summer Course Plan

> This is a living plan. It will be updated as each section's guide, homework, and schedule evolve.

## Overall Goal

24 study days centered on a polymer materials mini-project:

> **Predicting Polymer Material Properties with Machine Learning**

The target property (glass transition temperature, melting point, etc.) will be chosen based on data availability.

The course follows two parallel threads:

1. **Top-down:** Use Codex for data analysis, model development, debugging, testing, and project presentation.
2. **Bottom-up:** Learn machine learning and neural network fundamentals, culminating in understanding Transformers.

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

## Section 2: Material Data & Supervised Learning Basics

**Dates: August 1 — August 3**

### Topics

- Concepts of data, features, and labels
- Regression vs. classification problems
- Basic structure of polymer material data
- pandas, NumPy, and data visualization basics

### Three-Day Tasks

- Day 1: Decide which material property to predict
- Day 2: Use Codex for data loading, cleaning, and visualization
- Day 3: Split train/test sets and build a linear regression baseline model

### Homework

- Submit a dataset description
- Submit a data cleaning and visualization notebook
- Submit train/test split code
- Submit the linear regression baseline model and results summary

---

## Section 3: Loss Functions, Gradient Descent & Classification

**Dates: August 4 — August 6**

### Topics

- Mean Squared Error and Mean Absolute Error
- Basic idea of gradient descent
- Logistic Regression
- Accuracy, Precision, Recall, and the confusion matrix

### Three-Day Tasks

- Day 1: Compare characteristics of different loss functions
- Day 2: Implement or observe the gradient descent process with a simple example
- Day 3: Bin material properties into high/low classes and complete a classification experiment

### Homework

- Submit a loss function comparison experiment
- Submit gradient descent visualization results
- Submit material classification model code
- Explain the basic principle of gradient descent in your own words

---

## Section 4: Model Evaluation, Overfitting & Optimization

**Dates: August 7 — August 9**

### Topics

- Training, validation, and test sets
- Cross-validation
- Overfitting and underfitting
- Regularization
- Data leakage
- Model evaluation metrics

### Three-Day Tasks

- Day 1: Redesign a proper data splitting pipeline
- Day 2: Compare linear models, decision trees, random forests, etc.
- Day 3: Analyze whether the model overfits and attempt hyperparameter tuning

### Homework

- Submit proper data splitting and cross-validation code
- Submit a performance comparison table across models
- Submit an overfitting analysis
- Explain why you chose a particular model for the project

---

## Section 5: Neural Networks & Project v1

**Dates: August 10 — August 12**

### Topics

- Neurons, weights, and activation functions
- Input, hidden, and output layers
- Forward and backward propagation basics
- Building a simple neural network with PyTorch

### Three-Day Tasks

- Day 1: Understand the structure of a multi-layer perceptron
- Day 2: Use Codex to write and train a simple neural network
- Day 3: Compare neural network results with traditional ML models

### Homework

- Submit a neural network that can train and predict
- Submit a comparison between the neural network and traditional models
- Submit polymer materials project v1
- Write a Phase 1 learning summary

**August 13–14: Makeup days, code cleanup, homework revision, and review session.**

---

## Section 6: AI-Native Software Engineering & Project Upgrade

**Dates: September 15 — September 17**

### Topics

- Using Codex to read, refactor, and debug existing code
- Modular project structure
- Configuration files, logging, and error handling
- Unit testing and result reproducibility
- Git branching, commits, and version management

### Three-Day Tasks

- Day 1: Refactor notebooks into a proper Python project
- Day 2: Add tests, configuration, and error handling
- Day 3: Build a CLI program or simple interactive interface

### Homework

- Submit the refactored project directory
- Submit training and prediction scripts
- Submit at least two unit tests
- Submit project v2 with run instructions

---

## Section 7: From Neural Networks to Transformers

**Dates: September 18 — September 20**

### Topics

- Tokens and Embeddings
- The basic idea of Attention
- Self-Attention
- Overall Transformer architecture
- Differences between Transformers and ordinary neural networks
- Basic concepts of molecular strings and material sequence representations

### Three-Day Tasks

- Day 1: Understand Tokens, Embeddings, and Attention
- Day 2: Use simple code to observe the Self-Attention computation process
- Day 3: Analyze how Transformers can be applied to molecular or material data and compare with the current project model

### Homework

- Submit a simple Attention experiment
- Submit "From ML to Transformers" study notes
- Draw a diagram of the basic Transformer architecture
- Prepare a 5-minute oral explanation of the connection between neural networks and Transformers

**September 21: Makeup day, project debugging, homework revision, and review session.**

---

## Section 8: Project Refinement, Evaluation & Final Presentation

**Dates: September 22 — September 24**

### Topics

- Model error analysis
- Interpreting project results
- Quality-checking AI-generated code
- Writing README and technical reports
- Project presentation and defense

### Three-Day Tasks

- Day 1: Check for data leakage, model errors, and anomalous predictions
- Day 2: Polish code, charts, README, and presentation materials
- Day 3: Deliver the final project demo and defense

### Homework

- Submit the complete polymer materials ML project
- Submit the cleaned-up GitHub repository
- Submit the data processing and model evaluation report
- Submit the Transformer learning summary
- Complete the 10–15 minute project demo and defense

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
