import pandas as pd
import matplotlib.pyplot as plt

poda = pd.DataFrame ({ 'country' :     [ 'UK'  ,  'China' , 'Italy' , 'Brazil' , 'USA' ] ,  
                '20population' : [ 66.7 , 1426 , 59.4 , 208.6 , 331.6 ] ,
                '24population' : [ 69.2 , 1410 , 58.9 , 212.0 , 340.1 ]      })

pocha = poda['24population'] - poda['20population']
percha = pocha / poda['20population'] * 100
print( [round(x,2) for x in percha] )

for _, row in poda.iterrows():
    print(f"{row['country']}: {row['pct_change']:.2f}%")


poda_sorted = poda.sort_values('pct_change', ascending=False)

print("\nSorted by percentage change (descending):")
for _, row in poda_sorted.iterrows():
    print(f"- {row['country']}: {row['pct_change']:.2f}%")


max_inc = poda.loc[poda['pct_change'].idxmax(), 'country']
min_inc = poda.loc[poda['pct_change'].idxmin(), 'country']
print(f"\nLargest increase: {max_inc}")
print(f"Largest decrease: {min_inc}")



plt.bar(
    poda_sorted['country'],
    poda_sorted['pct_change'],
    color=['lightgreen' if x > 0 else 'lightcoral' for x in poda_sorted['pct_change']]
)
plt.axhline(0, color='black', linewidth=0.8)
plt.xlabel('Country')
plt.ylabel('Percentage Change (%)')
plt.title('Population % Change (2020–2024)')
plt.show()




