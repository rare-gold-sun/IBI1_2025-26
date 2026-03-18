import pandas as pd

poda = pd.DataFrame ({ 'country' :     [ 'UK'  ,  'China' , 'Italy' , 'Brazil' , 'USA' ] ,  
                '20population' : [ 66.7 , 1426 , 59.4 , 208.6 , 331.6 ] ,
                '24population' : [ 69.2 , 1410 , 58.9 , 212.0 , 340.1 ]      })

pocha = poda['24population'] - poda['20population']
percha = pocha / poda['20population'] * 100
print(percha)



pcido = reversed(sorted(pocha))
print(pcido)
pochadic = dict(zip(poda['country'], pocha))
print(max(pochadic, key=pochadic.get) + " has the largest increase")
print(min(pochadic, key=pochadic.get) + " has the largest decrease")



import matplotlib.pyplot as plt
plt.bar(poda['country'], pocha,color = ['lightcoral', 'lightskyblue', 'lightgreen', 'lightyellow', 'lightpink'])
plt.xlabel('Country')
plt.ylabel('Population Change (millions)')
plt.title('Population Change from 2020 to 2024')
plt.show()




