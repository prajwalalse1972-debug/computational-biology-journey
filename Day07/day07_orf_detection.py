rna = input("Enter RNA sequence: ").upper()

start = rna.find("AUG")

if start == -1:
    print("No ORF found")
    exit()

print("Start codon at position:", start)


stop = len(rna)

for i in range(start, len(rna), 3):
    codon = rna[i:i+3]
    if codon in ["UAA", "UAG", "UGA"]:
        stop = i
        break
orf = rna[start:stop+3]
print("ORF sequence:", orf)

#rna sequence :- CGGCACUCGUCGCCCAUGCGACCCUG 
