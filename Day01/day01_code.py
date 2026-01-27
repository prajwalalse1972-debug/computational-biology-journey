print("Computational Biology Journey Started")

gene = "INS"
genes = ["HBB", "EGFR", "BRCA1", "GAPDH"]

gene_info = {
    "name": "BRCA1",
    "function": "DNA repair",
    "location": "Chromosome 17"
}
gene_info2 = {
    "name" : "INS",
    "funciton": "Regulation of glucose metabolism",
    "location": "Chromosome 11"
}
gene_info3={
    "name" : "GAPDH",
    "function": "Glycolysis",
    "location": "Chromosome 12"
}
print(f"Analyzing gene: {gene} and its details:{gene_info2}") 

#CompB Madlibs Gene description

print("=== Gene Description Generator ===\n")

# Get gene information
gene_name = input("Gene name: ")
organism = input("Organism: ")
function = input("Main function: ")
disease = input("Associated disease: ")
tissue = input("Primary tissue/organ: ")

# To Generate description
description = f"""
The {gene_name} gene in {organism} is responsible for {function}. 
Mutations in {gene_name} have been linked to {disease}. This gene 
shows significant expression in {tissue}, highlighting its importance 
in maintaining normal physiological function.
"""
print("\n--- GENE DESCRIPTION ---")
print(description) 
