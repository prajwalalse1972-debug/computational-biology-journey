# Day 09 – RNA Translation & Codon Table Implementation

## What is Translation?

Translation is the biological process where the genetic information in mRNA is decoded to synthesize a protein (polypeptide chain).

- Occurs on ribosomes
- mRNA is read in the 5' → 3' direction
- Converts nucleotide sequence into amino acid sequence
- Second major step of gene expression (after transcription)

---

## What is a Codon Table?

A codon table is a standardized mapping of:

mRNA codon (3 nucleotides) → Amino acid

Since RNA has 4 bases (A, U, G, C):

4³ = 64 possible codons

These encode:
- 20 amino acids
- 3 stop codons (UAA, UAG, UGA)

---

## Why is the Genetic Code Degenerate?

The genetic code is degenerate because:

- Multiple codon triplets encode the same amino acid
- This redundancy increases mutation tolerance
- Example: Some amino acids are encoded by 4–6 different codons

However:
- Methionine (AUG) has only one codon
- Stop codons do not encode amino acids

---

## Why Do Stop Codons Terminate Translation?

Stop codons terminate translation because:

- They do not have corresponding tRNA molecules
- Release factors bind instead of tRNA
- The ribosome adds water (hydrolysis)
- The completed polypeptide is released

---

## Why Must Translation Start at AUG?

Translation begins at AUG because:

- AUG is the universal start codon
- It codes for Methionine
- It establishes the correct reading frame
- Starting at the wrong position causes a frameshift

---

## Computational Implementation (Day 09 Task)

In this task:

- A simplified codon table was implemented using a Python dictionary
- The program:
  - Finds the first AUG
  - Reads RNA in triplets
  - Stops at STOP codon
  - Builds the protein sequence
  - Outputs protein sequence and length

This models biological translation using algorithmic logic.

---

## Key Takeaway

Biological translation can be simulated computationally by:

- Using dictionaries for codon mapping
- Applying start/stop logic
- Iterating through sequences in triplets

This connects molecular biology principles with algorithmic modeling.
