protein = input("Enter protein sequence: ").upper()

aa_counts = {}

for aa in protein:
    if aa in aa_counts:
        aa_counts[aa] += 1
    else:
        aa_counts[aa] = 1

print("Amino acid counts:")
for aa, count in aa_counts.items():
    print(aa, ":", count)

print("\nPercentage composition:")
length = len(protein)

for aa, count in aa_counts.items():
    percentage = (count / length) * 100
    print(aa, ":", round(percentage, 2), "%")

most_common = max(aa_counts, key=aa_counts.get)

print("\nMost abundant amino acid:", most_common)
print("Count:", aa_counts[most_common])

# Example usage: MAAAMFAGAM
