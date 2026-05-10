# Pseudocode:
# Set initial values: starting cases, spread factor, total people, start days
# Show the initial infection state
# Use a loop: keep computing daily cases while cases < total people
# Inside the loop: increase the day count by 1
# Inside the loop: update current cases (previous * (1 + spread factor))
# Inside the loop: display the number of cases for the day
# After the loop: output the total number of days needed


ini = 5
days = 0
#set the initial value and days



rate = 0.4
tostu = 91
infected = ini
#use a loop to calculate the days until the value reaches 91
while infected < tostu:
	days += 1
	infected = infected * (1 + rate)
	print(f"Day {days}: Infected count = {infected:.1f}")

print("----------------------")
print(f"All {tostu} students infected. Total days taken: {days}")