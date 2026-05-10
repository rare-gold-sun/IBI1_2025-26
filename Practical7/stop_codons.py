import re
raw = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r").read()

Tctn = re.sub(r'\n' , '' , raw)        
ctns = re.split('>', Tctn)


gene_blocks = []
for block in ctns:
    if block:
        gene_name = block.split('_')[0]
        sequence = block[len(gene_name)+5:]
        gene_blocks.append((gene_name, sequence))

import itertools
out = open("stop_genes.fa", "w")

for gene_name, seq in gene_blocks:
    orfs = re.findall(r'ATG(?:...)*?(?:TAA|TAG|TGA)', seq)
    for orf in orfs:
        stop_codon = orf[-3:]
        out.write(f">{gene_name} {stop_codon}\n")
        out.write(f"{orf}\n")
        
out.close()
