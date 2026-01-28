dna = input("Enter DNA sequence: ").upper()

valid_bases = {'A', 'T', 'G', 'C'}

# validation
for base in dna:
     if base not in valid_bases:
        print("Invalid DNA sequence detected")
        exit()
  
# counts
A = dna.count('A')
T = dna.count('T')
G = dna.count('G')
C = dna.count('C')

gc_content = ((G+C)/len(dna))*100

print(f"GC Content: {gc_content:.2f}%") 

#The gene input given by the user is ATCGTTCGCTATTCAGGGATTGACCAACAC and the GC content turned out to be 46.67%
