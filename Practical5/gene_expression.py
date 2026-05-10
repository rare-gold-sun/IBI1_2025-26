exlev = { 'TP53': 12.4 , 'EGFR': 15.1 , 'BRCA1': 8.2 , 'PTEN' : 5.3 , 'ESR1' : 10.7 }
print(exlev)

exlev['MYC'] = 11.6



import matplotlib.pyplot as plt   
import numpy as np              
plt.bar(exlev.keys(), exlev.values()) 
plt.xlabel('Gene')  
plt.ylabel('Expression Level')  
plt.title('Gene Expression Levels')  
plt.show()



goit = 'EGFR'
if goit in exlev:
    print("expression level:" + str(exlev[goit]))
else:
    print("inform: gene of interest not found")


AGEL = sum(exlev.values()) / len(exlev)
print("Average Gene Expression Level:" + str(round(AGEL,3)) )