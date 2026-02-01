def find_orfs_in_frame(rna, frame):
    orfs = []
    start = None
    
    for i in range(frame, len(rna), 3):
        codon = rna[i:i+3]
        
        if codon == "AUG" and start is None:
            start = i
        
        elif codon in ["UAA", "UAG", "UGA"] and start is not None:
            orfs.append(rna[start:i+3])
            start = None
    
    return orfs

rna = input("Enter RNA sequence: ").upper()

all_orfs = []
for frame in range(3):
    all_orfs.extend(find_orfs_in_frame(rna, frame))

if not all_orfs:
    print("No ORFs found")
else:
    longest_orf = max(all_orfs, key=len)
    print("Total ORFs found:", len(all_orfs))
    print("Longest ORF:", longest_orf)
    print("Length:", len(longest_orf))

# Example usage:
#Input RNA sequence1: CCCAUGGCUACGACCUAAUUUGG
#Input RNA sequence2 : GGGAUGAAACCCUAGCCCAUGGCUUUGA
#Input RNA sequence3 : AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG
