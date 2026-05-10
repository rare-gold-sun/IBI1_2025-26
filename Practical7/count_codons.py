import re
import matplotlib.pyplot as plt
from collections import Counter

with open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r") as f:
    lines = f.readlines()

genes = []
name = ""
seq = ""
for line in lines:
    line = line.strip()
    if line.startswith(">"):
        if name and seq:
            genes.append((name, seq))
        name = line.split()[0][1:]
        seq = ""
    else:
        seq += line
if name and seq:
    genes.append((name, seq))


target_stop = input("Choose stop codon (TAA/TAG/TGA): ").strip().upper()

all_codons = []

PATTERN = r"ATG(?:...)*?" + target_stop

for name, seq in genes:
    orfs = re.findall(PATTERN, seq)
    if not orfs:
        continue

    longest_orf = max(orfs, key=len)
    coding_region = longest_orf[:-3]


    codons = [coding_region[i:i+3] for i in range(0, len(coding_region)-len(coding_region)%3, 3)]
    all_codons.extend(codons)


count = Counter(all_codons)
plt.figure(figsize=(10, 10))
plt.pie(count.values(), 
        labels=count.keys(), 
        autopct="%1.1f%%",
        textprops={'fontsize': 10},
        labeldistance=0.85,
        pctdistance=1.1)
plt.title(f"Codon Distribution upstream of {target_stop}")
plt.savefig(f"codon_pie_{target_stop}.png", bbox_inches="tight")
plt.close()

print(f"Done! Image saved as codon_pie_{target_stop}.png")