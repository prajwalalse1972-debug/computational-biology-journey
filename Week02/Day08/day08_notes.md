# Day 08 – Multiple ORFs & Longest ORF Selection

## Why can multiple ORFs exist?
Multiple ORFs can exist because:
- RNA can be read in three different reading frames on a single strand
- Start codons (AUG) can occur at multiple positions
- Each start codon can initiate an ORF until an in-frame stop codon is reached
- Different frames and positions can produce overlapping or distinct ORFs within the same sequence

---

## Why is the longest ORF often selected?
The longest ORF is typically selected because:
- Functional genes usually encode substantial proteins
- Short ORFs often arise randomly by chance
- Long uninterrupted ORFs are statistically unlikely to occur randomly
- Selecting the longest ORF is a practical heuristic in gene prediction when additional information is limited

---

## Key takeaway
ORF detection involves scanning all reading frames, collecting valid start-to-stop regions, and using biologically motivated heuristics to identify the most likely protein-coding sequence.
