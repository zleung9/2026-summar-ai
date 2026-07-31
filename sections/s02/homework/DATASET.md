# OpenPoly Calculated Polymer Properties — Homework Extract

## File

`openpoly_calculated_properties.csv` contains 1,000 polymer records and 23 columns:

- `id` and `Name`: identifiers
- `reactant_1`, `reactant_2`, `psmiles`, and `SMILES`: chemical-structure strings
- `reaction_type`, `Software`, `Theory_Level`, and `Source`: calculation metadata
- 13 numeric quantum-chemical properties, from `Energy_Hatree` through `HOMO_LUMO_Gap_eV`

The dataset does not designate a prediction target. In Section 2, treat the 13 calculated properties as variables for exploratory multivariate analysis. Do not treat `id` as an analytical feature.

## Source and Attribution

This CSV is derived from `data/OpenPoly/calculated_polymer_data.xlsx` in the course repository.

- Database: [OpenPoly polymer database](https://cleanenergymaterials.cn/polymer/polymer_database/experiment_polymer_database)
- Paper: J.-F. Wang et al., “OpenPoly: A Polymer Database Empowering Benchmarking and Multi-property Predictions,” *Chinese Journal of Polymer Science* 43, 1749–1760 (2025), [https://doi.org/10.1007/s10118-025-3402-y](https://doi.org/10.1007/s10118-025-3402-y)
- Benchmark code: [WangGroupFDU/Openpoly_benchmark](https://github.com/WangGroupFDU/Openpoly_benchmark)
- License: Creative Commons Attribution 4.0 (CC BY 4.0), as stated for the source data

Please retain this attribution when redistributing the CSV.

## Conversion Notes

- The 1,000 rows and 23 source columns were retained.
- Column names and numeric values were not changed.
- Embedded line breaks in text metadata were replaced with `; ` so that each polymer occupies one physical CSV line.
- SHA-256: `f8b4b7bb438a10230e1018e634616ef293ba7447aeb9c7cb7a0f0ece7ac6db6e`

## Important Caution

`pandas` reports no explicit missing values, but some calculated properties contain zeros or extreme values that may not be physically plausible. Treat this as a data-quality question to investigate, not as permission to silently delete observations. The raw CSV must remain unchanged so that every analysis is reproducible.
