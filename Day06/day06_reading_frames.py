rna = input("Enter RNA sequence: ").upper()

print("\n"+ '-' *18)

frame1_codons = len(rna)//3
frame2_codons = len(rna[1:])//3
frame3_codons = len(rna[2:])//3

print("Frame 1 codons:", frame1_codons)
print("Frame 2 codons:", frame2_codons)
print("Frame 3 codons:", frame3_codons)

print("\n"+ '-' *18)
