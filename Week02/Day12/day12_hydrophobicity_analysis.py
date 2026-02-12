# Get protein sequence
sequence = input("Enter protein sequence: ").upper()

# Define amino acids
hydrophobic = 'AVILMFWY'
hydrophilic = 'RKDENQSTCHG'

# Count residues
hydrophobic_count = sum(1 for aa in sequence if aa in hydrophobic)
hydrophilic_count = sum(1 for aa in sequence if aa in hydrophilic)
total = hydrophobic_count + hydrophilic_count

# Calculate percentages
hydrophobic_percent = (hydrophobic_count / total) * 100
hydrophilic_percent = (hydrophilic_count / total) * 100

# Print results
print(f"Hydrophobic: {hydrophobic_percent:.0f}%")
print(f"Hydrophilic: {hydrophilic_percent:.0f}%")

# Interpretation
if hydrophobic_percent > 50:
    print("Interpretation: Likely membrane protein")
else:
    print("Interpretation: Protein likely soluble")

#Example usage: MAAAVVVLLL
