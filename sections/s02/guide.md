# Section 2: Data Exploration

> Dates: August 1 — August 3

## What This Section Is About

Before choosing or training a model, learn to describe what a dataset contains, notice what may be wrong with it, and distinguish evidence from speculation.

You will complete one integrated exploratory analysis of a real polymer dataset. The work combines data auditing, descriptive statistics, visualization, correlation, standardization, and Principal Component Analysis (PCA). There is no separate day-by-day task list: use the questions and acceptance criteria in [homework.md](homework.md) to organize your work across the section.

Begin with [the notebook template](homework/s02_data_exploration_template.ipynb). It contains the full assignment as Markdown guidance and leaves the code and answer cells for you to complete.

## Topics

- Dataset structure, variable roles, data types, and data-quality checks
- Descriptive statistics: count, mean, median, variance, standard deviation, and quantiles
- Histograms, density plots, and box plots
- Outliers, suspicious values, and the effect of scale
- Pearson and Spearman correlation
- Feature standardization
- PCA, explained variance, loadings, and low-dimensional visualization
- **Bonus:** Singular Value Decomposition (SVD) and its connection to PCA

## Recommended Resources

Use the resources to answer a question or unblock the homework; you do not need to read every page.

- [pandas: Essential basic functionality](https://pandas.pydata.org/docs/user_guide/basics.html) — focus on descriptive statistics, `value_counts`, and function application.
- [pandas: Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html) — focus on detecting missing values; then ask whether non-null values can still be suspicious.
- [seaborn: Visualizing distributions of data](https://seaborn.pydata.org/tutorial/distributions.html) — focus on histograms and density estimates.
- [seaborn `boxplot`](https://seaborn.pydata.org/generated/seaborn.boxplot.html) — use the API example, then interpret the quartiles and whiskers yourself.
- [pandas `DataFrame.corr`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html) — compare the definitions of Pearson and Spearman correlation.
- [scikit-learn `StandardScaler`](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) — focus on why centering and scaling matter.
- [scikit-learn: PCA example](https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html) and [PCA API](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) — focus on scores, components, loadings, and `explained_variance_ratio_`.
- **Bonus:** [The Elements of Statistical Learning, §14.5.1](https://hastie.su.domains/ElemStatLearn/) — connect the SVD of a centered data matrix to PCA.

## The Example Dataset

Use:

```text
sections/s02/homework/openpoly_calculated_properties.csv
```

It contains 1,000 calculated polymers from OpenPoly, with identity and structure fields plus 13 numeric quantum-chemical properties. This is large enough to reveal redundant directions and useful low-dimensional structure through PCA.

Read [homework/DATASET.md](homework/DATASET.md) before analysis. Do not include `id` in the PCA merely because pandas recognizes it as numeric: decide whether a column is an analytical variable from its meaning, not only its data type.

## A Useful Analysis Loop

For every table or plot:

1. **Observe:** state what is directly visible or calculated.
2. **Interpret:** explain one plausible meaning.
3. **Question:** identify an alternative explanation or limitation.
4. **Check:** use another calculation, plot, or source to test the interpretation.

For example, a box plot may show a long upper tail and points beyond its whisker. It does not establish that those points are mistakes. Inspect the corresponding rows and the scientific meaning of the variable before deciding what to do.

## Purpose and Critical-Thinking Questions

The purpose of this section is not to produce many plots. It is to make defensible claims about data. By the end, you must be able to answer each question below with evidence from the example dataset.

| Topic | Critical question |
|---|---|
| Dataset structure | Which columns are identifiers, structures, categories, or numeric analytical variables, and why does that distinction matter? |
| Descriptive statistics | When do the mean and median describe different “typical” values, and what does that reveal about distribution shape? |
| Data quality | Does “zero missing values” prove that the dataset is complete? Which zero or extreme values deserve investigation? |
| Histograms and density plots | Is a variable symmetric, skewed, multimodal, bounded, or concentrated at a special value? What evidence supports the description? |
| Box plots and outliers | What do the median, box, whiskers, and points beyond the whiskers reveal? Why is a box-plot outlier not automatically an error? |
| Scale | How do units and numerical ranges affect comparisons among variables? |
| Correlation | What relationship does Pearson detect, what relationship does Spearman detect, and why can their values differ? |
| Standardization | What changes after z-score standardization, what stays the same, and why should it happen before PCA here? |
| PCA | How many components retain a useful amount of variance? Which original properties shape PC1 and PC2? |
| PCA limitations | Does high explained variance imply prediction, causation, or scientific importance? What information can a two-dimensional projection hide? |

## Self-Check

- [ ] I can classify columns by meaning rather than only by pandas dtype.
- [ ] I can explain mean, median, variance, standard deviation, and quartiles using concrete values.
- [ ] I can interpret a histogram and box plot without declaring every unusual point an error.
- [ ] I can compare Pearson and Spearman correlations.
- [ ] I can explain why PCA on these variables requires standardization.
- [ ] I can read an explained-variance plot and a component-loading table.
- [ ] I can support every critical-question answer with a result from my notebook.

**You know enough when:** you can look at an unfamiliar table, ask what its summaries and plots justify, and explain both your conclusions and their limits.
