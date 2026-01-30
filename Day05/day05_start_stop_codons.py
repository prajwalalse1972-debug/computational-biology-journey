rna = input("Enter RNA sequence: ").upper()

print("\n" + "-" * 60)

start_codon = "AUG"

if start_codon in rna:
    print("Start codon found")
else:
    print("No start codon found")

stop_codons = ["UAA", "UAG", "UGA"]

for codon in stop_codons:
    if codon in rna:
        print(f"Stop codon {codon}found")
    else: 
        print(f"Stop codon {codon} not found")

print("RNA Sequence Analysis Complete")

print("\n" + "-" * 60)
