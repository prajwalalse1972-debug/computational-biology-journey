def dna_to_rna_converter():
    """
    DNA to RNA Converter
    Takes DNA input, validates it, converts to RNA, counts bases, and displays results.
    """
    
    # 1. Take DNA input
    print("=== DNA to RNA Converter ===\n")
    dna_sequence = input("Enter DNA sequence: ").strip().upper()
    
    # 2. Validate DNA sequence (A, T, G, C)
    valid_bases = set('ATGC')
    if not dna_sequence:
        print("Error: Empty sequence entered.")
        return
    
    invalid_bases = set(dna_sequence) - valid_bases
    if invalid_bases:
        print(f"Error: Invalid bases found: {', '.join(sorted(invalid_bases))}")
        print("DNA sequences can only contain A, T, G, and C.")
        return
    
    print(f"\n✓ Valid DNA sequence: {dna_sequence}")
    
    # 3. Convert DNA to RNA (Replace T with U)
    rna_sequence = dna_sequence.replace('T', 'U')
    
    # 4. Count RNA bases (A, U, G, C)
    base_counts = {
        'A': rna_sequence.count('A'),
        'U': rna_sequence.count('U'),
        'G': rna_sequence.count('G'),
        'C': rna_sequence.count('C')
    }
    
    # 5. Print RNA sequence + counts
    print(f"\n{'='*50}")
    print("RESULTS:")
    print(f"{'='*50}")
    print(f"RNA Sequence: {rna_sequence}")
    print(f"\nBase Counts:")
    print(f"  A (Adenine):  {base_counts['A']}")
    print(f"  U (Uracil):   {base_counts['U']}")
    print(f"  G (Guanine):  {base_counts['G']}")
    print(f"  C (Cytosine): {base_counts['C']}")
    print(f"\nTotal bases: {len(rna_sequence)}")
    print(f"{'='*50}")


if __name__ == "__main__":
    dna_to_rna_converter()
