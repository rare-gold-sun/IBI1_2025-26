import re
raw = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r").read()

Tctn = re.sub(r'\n' , '' , raw)        
ctns = re.split('>', Tctn)


import itertools
ORF = list(itertools.chain.from_iterable([re.findall(r'ATG(?:...)*?(?:TAA|TAG|TGA)',   genes  ) for genes in ctns  ]))
genam = re.findall(r'>[A-Z0-9]+_mRNA', Tctn  )
stoco = list(itertools.chain.from_iterable([re.findall(r'...$' ,  orfs) for orfs in ORF  ]  ))

choco = input('choose from three possible stop codons')
count = stoco.count(choco)

import matplotlib.pyplot as plt
plt.pie([count, len(stoco)-count], labels = ['stop codon ' + choco, 'other stop codons'], autopct='%1.1f%%')
charna = 'Distribution of ' + choco + ' in ORFs'
plt.title(charna)
plt.savefig(charna + '.png')


