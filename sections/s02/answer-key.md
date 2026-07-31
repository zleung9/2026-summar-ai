# Section 2 Answer Key

(For teacher use only — do not share with students)

## What This Section Tests

The assignment tests whether the student can move from mechanical plotting to evidence-based data reasoning. A successful student should be able to:

1. assign column roles from meaning rather than dtype;
2. detect suspicious values that are not encoded as `NaN`;
3. interpret distributions and box plots without automatically deleting outliers;
4. distinguish Pearson's linear association from Spearman's rank association;
5. explain why scaling changes PCA;
6. interpret explained variance and loadings without claiming causation or predictive importance.

Different plots and defensible cleaning choices are acceptable. Require the student to show how each decision changes the evidence.

## Dataset Reference Checks

Using `pandas.read_csv` on `homework/openpoly_calculated_properties.csv` should produce:

| Check | Reference result |
|---|---:|
| Rows | 1,000 |
| Columns | 23 |
| Numeric columns including `id` | 14 |
| Numeric analytical properties excluding `id` | 13 |
| Explicit missing values | 0 |
| Exact duplicate rows | 0 |
| Unique `id` values | 1,000 |
| Unique `Name` values | 1,000 |

`reaction_type`, `Software`, `Theory_Level`, and `Source` are constant in this extract. They provide context but no variation for correlation or PCA. `id` varies but is still an identifier and must not enter the PCA.

### Suspicious zeros

The absence of `NaN` does not prove completeness. A reference audit finds:

| Pattern | Count |
|---|---:|
| Zero values in `Energy_Hatree`, `Isotropic_Polarizability_au`, `HOMO_eV`, `LUMO_eV`, and `HOMO_LUMO_Gap_eV` | 74 each |
| Zero values in each correction/entropy/dipole/free-energy/enthalpy field | 36 each |

Some zero values are physically implausible for these quantities and may mark unavailable or failed calculations. A strong submission identifies the pattern, inspects the affected rows jointly, and avoids silently treating every zero as an ordinary observation. It is acceptable to retain the raw values for a reference analysis or to run a documented sensitivity analysis after treating implausible zeros as missing. It is not acceptable to delete rows solely because a box plot marks them as outliers.

`Isotropic_Polarizability_au` also contains a slightly negative minimum, approximately `-0.03647`, which deserves investigation.

## Descriptive-Statistics Landmarks

These values help detect implementation mistakes; small rounding differences are fine.

| Property | Mean | Median | Standard deviation | Minimum | Maximum |
|---|---:|---:|---:|---:|---:|
| `Energy_Hatree` | -2121.316 | -1692.087 | 1338.864 | -9263.852 | 0.000 |
| `Isotropic_Polarizability_au` | 255.060 | 263.661 | 92.647 | -0.036 | 674.733 |
| `HOMO_eV` | -7.865 | -8.450 | 2.254 | -10.192 | 0.000 |
| `LUMO_eV` | -0.172 | -0.048 | 0.362 | -3.676 | 0.354 |
| `Dipole_Debye` | 4.868 | 4.714 | 2.458 | 0.000 | 24.802 |
| `HOMO_LUMO_Gap_eV` | 7.693 | 8.298 | 2.225 | 0.000 | 10.001 |

The large mean–median difference for `Energy_Hatree`, long tails, point masses at zero, and the extreme upper tail of `Dipole_Debye` provide good material for distribution and box-plot discussion.

## Correlation Reference

On the 13 raw numeric properties:

- Pearson correlations among `Energy_Hatree`, `Gibbs_Free_Energy_Hatree`, and `Enthalpy_Hatree` round to `1.000`; these quantities differ by correction terms and should not be described as three independent signals.
- Pearson correlation between `HOMO_eV` and `HOMO_LUMO_Gap_eV` is approximately `-0.987`.
- Pearson correlation between `Isotropic_Polarizability_au` and `HOMO_eV` is approximately `-0.749`.
- Pearson correlation between `Thermal_correction_to_Enthalpy_Hatree` and `Entropy_Hatree` is approximately `0.851`.

Useful Pearson–Spearman contrasts include:

| Pair | Pearson | Spearman |
|---|---:|---:|
| `HOMO_eV` and `HOMO_LUMO_Gap_eV` | -0.987 | -0.686 |
| `Inner_energy_correction_Hatree` and `Thermal_correction_to_Gibbs_Free_Energy_Hatree` | 0.440 | 0.878 |

A difference can indicate nonlinear monotonic structure, ties, clusters, or influential extreme values. It does not identify a cause. The student should inspect a scatter plot and the suspicious-zero groups before deciding which explanation is plausible.

The identity

```text
HOMO_LUMO_Gap_eV = LUMO_eV - HOMO_eV
```

should be found numerically, apart from floating-point tolerance. The three total-energy columns are also near-exact combinations of shared energy and correction terms. Recognizing these relationships is more important than merely reporting a large coefficient.

## PCA Reference

Reference procedure:

1. exclude `id` and all nonnumeric metadata;
2. keep the 13 raw numeric properties;
3. standardize each column with `StandardScaler`;
4. fit scikit-learn `PCA`.

The explained-variance ratios are approximately:

| Component | Individual | Cumulative |
|---|---:|---:|
| PC1 | 40.41% | 40.41% |
| PC2 | 19.40% | 59.82% |
| PC3 | 10.67% | 70.49% |
| PC4 | 8.36% | 78.85% |
| PC5 | 6.70% | 85.55% |
| PC6 | 6.20% | 91.75% |
| PC8 | 3.24% | 99.08% |

The final three components carry essentially zero variance because the dataset contains exact or near-exact linear relationships. This is an important result, not a software failure.

With scikit-learn's sign convention in the reference run, the largest absolute PC1 loadings are approximately:

| Property | PC1 loading |
|---|---:|
| `Isotropic_Polarizability_au` | 0.363 |
| `HOMO_eV` | -0.362 |
| `HOMO_LUMO_Gap_eV` | 0.357 |
| `Thermal_correction_to_Enthalpy_Hatree` | 0.343 |
| `Entropy_Hatree` | 0.337 |
| each major total-energy column | -0.314 |

PC2 is led by `Thermal_correction_to_Gibbs_Free_Energy_Hatree` at approximately `0.447`, followed by the three total-energy columns at approximately `0.387` each.

PCA component signs may all be reversed without changing the solution. Grade interpretation using absolute magnitude and relative direction, not sign matching.

A reasonable retention choice could be:

- two components for a deliberately simple visualization, while admitting that they retain only about 60% of variance;
- six components for a roughly 90% threshold;
- eight components for roughly 99%.

There is no single required cutoff. The student must connect the choice to the analysis purpose and acknowledge lost information.

## Reference Answers to the Critical Questions

1. **Dataset structure:** `id` and `Name` identify rows; reactants and SMILES-like strings encode chemical structure; four metadata columns are constant; 13 columns are calculated numeric properties. Numeric dtype alone does not make `id` a feature.
2. **Descriptive statistics:** mean is sensitive to tails and unusual values; median is rank-based and more robust. Their disagreement for total energy and several electronic properties flags skew, mixtures, or suspicious zero groups.
3. **Data quality:** explicit missingness is zero, but coordinated zeros and the negative polarizability show that validity requires domain and pattern checks.
4. **Distributions:** conclusions should name visible evidence such as skew, tails, modes, bounds, or point masses. A density curve is an estimate and may hide discrete piles or boundary effects.
5. **Box plots:** the box spans the interquartile range, the line marks the median, and conventional whiskers extend to observations within 1.5 IQR. Points outside are unusual under that rule, not proven mistakes.
6. **Scale:** Hartree, eV, Debye, and atomic units have very different numerical spreads. Unscaled PCA would give variables with large variance disproportionate influence.
7. **Correlation:** Pearson summarizes linear association; Spearman summarizes monotonic rank association. Neither establishes causation, and both can be distorted by data-quality groups.
8. **Standardization:** z-scoring changes location and scale to roughly zero mean and unit population variance. It preserves ordering and the shape up to a linear transformation; it does not repair invalid values.
9. **PCA:** the first two components retain about 59.8%; loadings show how variables combine into each direction. Six components exceed 90% in the raw reference analysis.
10. **PCA limitations:** variance is not the same as scientific importance, causality, or predictive usefulness. Projection can overlap distinct groups and hide structure in later components.

## What to Probe During Review

- Ask the student to point to one sentence that is an observation and one that is an interpretation.
- Ask what would change if suspicious zeros were treated as missing.
- Ask why `id` must be excluded despite being numeric.
- Ask why a perfectly correlated derived property can make PCA appear more compressible.
- Ask the student to explain one Codex suggestion they did not accept.

The section is complete when the student can defend conclusions with evidence and state what the analysis cannot establish.
