# Section 2 Critical-Thinking Quiz

> Based on the submitted OpenPoly exploratory analyses  
> Suggested time: 45 minutes  
> Format: open notebook, written or oral defense  
> Total: 30 points

## Instructions

Answer all eight shared questions, then answer only the three questions under your own submission folder. Short calculations or small code snippets are welcome. Every empirical claim must point to a number, plot, row, or calculation.

The goal is not to repeat definitions. Explain what the evidence permits you to conclude and what remains uncertain.

## Part A — Shared Core Questions (24 points)

### 1. Column roles (3 points)

`id` is numeric, but the assignment excludes it from PCA.

1. Classify `id`, `Name`, `SMILES`, `reaction_type`, and `Energy_Hatree` by role.
2. Explain why pandas dtype alone cannot decide whether a column belongs in PCA.
3. Predict one misleading pattern that could appear if `id` were included.

### 2. Missingness versus validity (3 points)

Pandas reports zero `NaN` values, yet several properties contain coordinated zeros.

1. Give two possible explanations for these zeros.
2. What evidence would distinguish a failed calculation from a legitimate physical zero?
3. State one conclusion you must not make without additional documentation.

### 3. Distribution and box-plot reasoning (3 points)

For raw `Energy_Hatree`, the mean is approximately −2121.3, the median is approximately −1692.1, and the minimum is approximately −9263.9.

1. Describe the skew direction and explain the mean–median difference.
2. Explain what a point beyond a box-plot whisker means.
3. Explain why that point is not automatically an error.

### 4. Read Pearson and Spearman correctly (3 points)

For raw `HOMO_eV` versus `HOMO_LUMO_Gap_eV`, Pearson is approximately −0.987 and Spearman is approximately −0.686.

1. Which coefficient describes linear association and which describes monotonic rank association?
2. Explain why their magnitudes may differ here.
3. Name one plot or calculation you would use before interpreting the difference.

### 5. Mathematical dependency (3 points)

The data satisfy `HOMO_LUMO_Gap_eV = LUMO_eV - HOMO_eV` to floating-point tolerance.

1. Why does this matter when interpreting correlations?
2. Why can including all three columns make PCA appear more compressible?
3. Give another near-dependent property family in this dataset and describe the relationship.

### 6. Standardization (3 points)

1. What should each column's mean and population standard deviation be after `StandardScaler`?
2. Which distribution properties remain unchanged after this linear transformation?
3. Why would unscaled PCA overemphasize the total-energy columns?

### 7. Choosing PCA components (3 points)

On the raw 13-property analysis:

- PC1 explains about 40.4%;
- PC1–PC2 explain about 59.8%;
- PC1–PC5 explain about 85.6%;
- PC1–PC6 explain about 91.8%.

Choose a component count for each purpose and justify it:

1. a two-dimensional classroom visualization;
2. a compressed representation intended to retain at least 90% of variance; and
3. a scientific analysis where a low-variance property may still be important.

### 8. PCA scores versus component weights (3 points)

1. What does one row in the PCA score matrix represent?
2. What does one value in `pca.components_` represent?
3. In the raw analysis, the largest absolute PC2 weight is the thermal correction to Gibbs free energy (~0.447), followed by Energy/Gibbs/Enthalpy (~0.387). Write a defensible one-sentence interpretation and a one-sentence limitation.

## Part B — Individual Follow-Up (6 points)

Answer only the section matching your submission folder. Each question is worth 2 points.

### Yuanjie-Tan

1. Your notebook plots one strongest correlation pair. Choose a different strong pair, state its Pearson and Spearman coefficients, and explain what a second scatter plot would test.
2. Your notebook calls the maximum `Dipole_Debye` value genuine. What row-level or chemical evidence would be needed to support that word? Rewrite the claim so it stays within the current evidence.
3. Your PC2 description names Energy, Gibbs, and Enthalpy first. Re-rank the PC2 properties by absolute weight and explain how that changes the component interpretation.

### student0019425

1. Your relationship findings reverse the Pearson and Spearman values for HOMO versus gap. Write the corrected values and rewrite the interpretation in two sentences.
2. Identify three specific row IDs that deserve investigation, state why each was selected, and separate observation from hypothesis for each.
3. Explain why a code cell with saved plot output but `execution_count: null` weakens reproducibility evidence. Describe the exact final notebook workflow that fixes this.

### 陈梓末 / Zimo Chen

1. Separate evidence from hypothesis for the 74 coordinated-zero rows. Which findings are directly calculated, and which claims require DFT logs or source documentation?
2. After removing those 74 rows, the gap skewness is about −0.53 and polarizability skewness is about +1.40; only one row has gap 10.001 eV. Correct your three corresponding distribution claims.
3. The raw first two PCs explain about 59.8%, while the cleaned first two explain about 51.0%. Explain why deleting a structured group can rotate PCA and design a sensitivity comparison that would justify retaining or rejecting the cleaning choice.

## Completion Standard

- **24–30:** Ready to proceed; explanations use evidence and acknowledge uncertainty.
- **18–23:** Proceed after correcting the missed concepts.
- **Below 18:** Revisit Section 2 and revise the notebook before beginning dependent work.

Answers that state a correct number without explaining its meaning receive at most half credit. Answers that present an unsupported hypothesis as fact receive at most half credit.
