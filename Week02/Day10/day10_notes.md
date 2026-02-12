# Day 10 – Amino Acid Composition Analysis

## Why analyze amino acid composition?

Analyzing amino acid composition is a fundamental step in protein characterization. It helps to:

- Identify an unknown protein by comparing its composition "fingerprint" to known database sequences  
- Determine the purity and concentration of a protein sample  
- Verify the correctness of a translated DNA sequence or synthetic peptide  
- Understand general biochemical properties of the protein  

---

## How can composition help predict protein function?

The relative frequency of specific amino acids provides clues about physical and biological properties:

- **Hydrophobicity**  
  A high proportion of non-polar amino acids often suggests a membrane-associated protein.

- **Charge properties**  
  Excess acidic (D, E) or basic (K, R, H) residues may indicate DNA-binding proteins or specific solubility behavior.

- **Structural stability**  
  High cysteine content may suggest disulfide bond formation, which stabilizes extracellular proteins.

---

## Why is normalization important?

Normalization is critical because proteins vary greatly in length.

- **Comparative analysis**  
  Converting raw counts into percentages (relative frequencies) allows accurate comparison between small and large proteins.

- **Error reduction**  
  It ensures results reflect intrinsic protein composition rather than total sequence length or sample amount.

---

## What was implemented in code?

- Count frequency of each amino acid using a dictionary
- Convert raw counts into percentage composition
- Identify the most abundant amino acid
- Output both absolute counts and normalized percentages

---

## Key Takeaway

Protein composition analysis transforms a raw amino acid sequence into meaningful biochemical insight.  
Normalization enables fair comparison and prepares the data for downstream computational modeling.
