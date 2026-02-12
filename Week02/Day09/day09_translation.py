codon_table = {
    "AUG": "M",   # Methionine (start)
    "UUU": "F", "UUC": "F",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
}

rna = input("Enter RNA sequence: ").upper()

start = rna.find("AUG")

if start == -1:
    print("No start codon found")
    exit()

protein = ""

for i in range(start, len(rna), 3):
    codon = rna[i:i+3]

    if codon not in codon_table:
        break

    amino_acid = codon_table[codon]

    if amino_acid == "STOP":
        break

    protein += amino_acid
print("Protein sequence:", protein)
print("Protein length:", len(protein))

#RNA SEQUENCE :- CCCAUGGCCGCUUAAUGGG
