hr = [72,60,126,85,90,59,76,131,88,121,64]



mhr = sum(hr) / len(hr)
print("there are " + str(len(hr)) + " patients in the dataset and the mean heart rate is " + str(mhr))


low = [r for r in hr if r < 60]
normal = [r for r in hr if 60 <= r <= 120]
high = [r for r in hr if r > 120]
ctg = {'low': len(low), 'normal': len(normal), 'high': len(high)}
print("there are " + str(ctg['low']) + " patients with low heart rate, " + str(ctg['normal']) + " patients with normal heart rate and "
       + str(ctg['high']) + " patients with high heart rate")
print(str(max(ctg.keys())) + " contains the largest number of patients, which is " + str(max(ctg.values())))




import matplotlib.pyplot as plt
plt.pie(ctg.values(), labels=ctg.keys(), autopct='%1.1f%%',colors = [ 'lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Heart Rate Analysis')
plt.show()




