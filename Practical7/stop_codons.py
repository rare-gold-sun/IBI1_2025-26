
import re
raw = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r").read()

Tctn = re.sub(r'\n' , '' , raw)        
ctns = re.split('>', Tctn)


import itertools
ORF = list(itertools.chain.from_iterable([re.findall(r'ATG(?:...)*?(?:TAA|TAG|TGA)',   genes  ) for genes in ctns  ]))
genam = re.findall(r'>[A-Z0-9]+_mRNA', Tctn  )
stoco = list(itertools.chain.from_iterable([re.findall(r'...$' ,  orfs) for orfs in ORF  ]  ))

out = open("stop_genes.fa", "w")

for name, stop, seq in zip(genam, stoco, ORF):
    out.write(f"{name} {stop}\n")  
    out.write(f"{seq}\n")  

out.close()
