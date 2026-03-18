ini = 5
days = 0
#set the initial value and days

#use a loop to calculate the days until the value reaches 91
while ini < 91:
	ini += 0.4 * ini
	days += 1
print(days,"days")
