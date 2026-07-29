# 20_OpenPoly - OpenPoly: Multi-property Polymer Database

## Source

- Database: https://cleanenergymaterials.cn/polymer/polymer_database/experiment_polymer_database
- Benchmark code: https://github.com/WangGroupFDU/Openpoly_benchmark
- Paper: Wang, J. F.; Sun, Y. B.; Chen, Q. T.; Ji, F. F.; Song, Y. Y.; Ruan, M. Y.; Wang, Y. *OpenPoly: A Polymer Database Empowering Benchmarking and Multi-property Predictions*. Chinese Journal of Polymer Science 43, 1749–1760 (2025).
- License: CC BY 4.0 (as stated in the paper)

## What's Included

- `experiment_polymer_data.xlsx` — 13,140 polymer records (756 unique names) × 54 columns. Includes PSMILES, 50 experimental property columns, and source references.
- `calculated_monomer_data.xlsx` — 10,519 monomers × 45 columns. Includes SMILES, monomer type, redox/electronic/thermochemical properties, solvent free energies, software, and theory level.
- `calculated_polymer_data.xlsx` — 1,000 polymers × 23 columns. Includes reactants, PSMILES/SMILES, reaction type, electronic and thermochemical properties, software, and theory level.
- `ml_polymer_data.csv` — 213,581 generated polymers × 10 columns. Includes two reactants, polymer SMILES, reaction type, and five predicted properties.

## Property Coverage

- Thermal: Tg, Tm, Td, crystallization temperature, lower/upper critical solution temperatures, and thermal conductivity.
- Mechanical: tensile, compressive, flexural and impact strength; Young's modulus; hardness; elongation at break.
- Dielectric/electronic/optical: band gaps, dielectric constants, HOMO/LUMO, electron affinity, ionization energy, refractive index, dipole and polarizability.
- Transport and interfacial: CH4, CO2, H2, He, N2, O2, and methanol permeability; gas diffusivity and solubility; water uptake, swelling, and contact angle.
- Quantum chemistry: total and Gibbs energies, enthalpy, entropy, redox potentials, conceptual-DFT descriptors, and solvation free energies.
- ML predictions: Tg, Tm, tensile strength, Young's modulus, and total dielectric constant for 213,581 generated polymers.

## Notes

- The accompanying paper describes the manually curated benchmark as 3,985 unique polymer-property pairs across 26 experimental properties. The archived spreadsheet is a broader 13,140-row export with 50 property columns; both figures are retained here because they describe different representations/releases.
- Experimental coverage is sparse: each row generally contains only a subset of the available property columns.
- Polymer structures use PSMILES with wildcard attachment points.
- The paper is intentionally excluded from the course repository. It can be distributed after the exercise for comparison with the students' independent results.
