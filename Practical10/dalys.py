import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


os.chdir('/Users/Zhuanz/CODE/IBI1_2025-26/Practical10')
DALYS_all = pd.read_csv("dalys-rate-from-all-causes.csv")

africa_last_decade = DALYS_all.iloc[0:11,2:4]
print(africa_last_decade)
# 1998 reported the maximum DALYs across the first 10 years



zimbabwe_all_years = DALYS_all.loc[DALYS_all.Entity == 'Zimbabwe', 'Year']
print(zimbabwe_all_years)
#the first year is 1990 and the last year is 2019 for which Zimbabwe data were recorded


DALYS_2019 = DALYS_all.loc[DALYS_all.Year == 2019, ["Entity", "DALYs"]].set_index('Entity')['DALYs'].to_dict()
max_2019 = max(DALYS_2019, key=DALYS_2019.get)
min_2019 = min(DALYS_2019, key=DALYS_2019.get)
# The country with the highest DALYs in 2019 is Lesotho, and the country with the lowest DALYs in 2019 is Singapore.


lesotho_data = DALYS_all.loc[DALYS_all.Entity == max_2019, ["Year", "DALYs"]].set_index('Year')['DALYs'].to_dict()
singapore_data = DALYS_all.loc[DALYS_all.Entity == min_2019, ["Year", "DALYs"]].set_index('Year')['DALYs'].to_dict()
plt.plot(lesotho_data.keys(), lesotho_data.values(), label= 'Lesotho', color='red')
plt.plot(singapore_data.keys(), singapore_data.values(), label= 'Singapore', color='blue')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs over Time')
plt.legend()
plt.show()

#Start to answer the question here
SD_all = DALYS_all.groupby("Entity")["DALYs"].std().sort_values(ascending=True)
most_stable_5 = SD_all.head(5)
print(most_stable_5.index)
#the answer is Monaco, Dominica, San Marino, Northern Mariana Islands and  Paraguay