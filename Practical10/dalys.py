import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


os.chdir('/Users/Zhuanz/CODE/IBI1_2025-26/Practical10')
dada = pd.read_csv("dalys-rate-from-all-causes.csv")

Afirdec = dada.iloc[0:11,2:4]
print(Afirdec)
# 1998 reported the maximum DALYs across the first 10 years



Zrecda = dada.loc[dada.Entity == 'Zimbabwe', 'Year']
print(Zrecda)
#the first year is 1990 and the last year is 2019 for which Zimbabwe data were recorded


recda = dada.loc[dada.Year == 2019, ["Entity", "DALYs"]].set_index('Entity')['DALYs'].to_dict()
ma19 = max(recda, key=recda.get)
mi19 = min(recda, key=recda.get)
# The country with the highest DALYs in 2019 is Lesotho, and the country with the lowest DALYs in 2019 is Singapore.


Lda = dada.loc[dada.Entity == ma19, ["Year", "DALYs"]].set_index('Year')['DALYs'].to_dict()
Sda = dada.loc[dada.Entity == mi19, ["Year", "DALYs"]].set_index('Year')['DALYs'].to_dict()
plt.plot(Lda.keys(), Lda.values(), label= 'Lesotho', color='red')
plt.plot(Sda.keys(), Sda.values(), label= 'Singapore', color='blue')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs over Time')
plt.legend()
plt.show()

#Start to answer the question here
alsd = dada.groupby("Entity")["DALYs"].std().sort_values(ascending=True)
mosta5 = alsd.head(5)
print(mosta5.index)
#the answer is Monaco, Dominica, San Marino, Northern Mariana Islands and  Paraguay