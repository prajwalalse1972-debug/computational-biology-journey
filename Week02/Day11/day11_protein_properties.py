# Amino acid weights (average, in Daltons)
aa_weights = {
    'A': 89, 'R': 174, 'N': 132, 'D': 133, 'C': 121,
    'Q': 146, 'E': 147, 'G': 75, 'H': 155, 'I': 131,
    'L': 131, 'K': 146, 'M': 149, 'F': 165, 'P': 115,
    'S': 105, 'T': 119, 'W': 204, 'Y': 181, 'V': 117
}

# Get protein sequence
sequence = input("Enter protein sequence: ")
sequence = sequence.upper()

# Calculate length
length = len(sequence)

# Calculate approximate molecular weight
weight = sum(aa_weights.get(aa, 110) for aa in sequence)

# Count acidic residues (D, E)
acidic = sequence.count('D') + sequence.count('E')

# Count basic residues (K, R, H)
basic = sequence.count('K') + sequence.count('R') + sequence.count('H')

# Determine interpretation
if acidic > basic:
    interpretation = "Likely acidic protein"
elif basic > acidic:
    interpretation = "Likely basic protein"
else:
    interpretation = "Likely neutral protein"

# Print output
print("\nOutput:")
print(sequence)
print()
print(f"Length: {length}")
print(f"Approx. Molecular Weight: {weight} Da")
print(f"Acidic residues (D, E): {acidic}")
print(f"Basic residues (K, R, H): {basic}")
print(f"Interpretation: {interpretation}")

#Reference DNA input : MAAAMFAGAM
