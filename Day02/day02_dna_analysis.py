# Get DNA sequence from user

DNA_SEQUENCE = input("Enter DNA sequence: ").upper()

print("\n" + "-" * 60)

# Purine analysis (A and G)
print(f"The purine A content of the DNA sequence has been repeated {DNA_SEQUENCE.count('A')}")
print(f"The purine G content of the DNA sequence has been repeated {DNA_SEQUENCE.count('G')}")
print(f"The purine content of the DNA sequence is: {DNA_SEQUENCE.count('A') + DNA_SEQUENCE.count('G')}")

print()  

# Pyrimidine analysis (C and T)
print(f"The pyrimidine C content of the DNA sequence has been repeated {DNA_SEQUENCE.count('C')}")
print(f"The pyrimidine T content of the DNA sequence has been repeated {DNA_SEQUENCE.count('T')}")
print(f"The pyrimidine content of the DNA sequence is: {DNA_SEQUENCE.count('C') + DNA_SEQUENCE.count('T')}")

print("-" * 60) 
