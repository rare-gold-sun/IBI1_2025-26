#set the input of different parameters
#gender decides coefficient
#use the given formula to compute
#abandon the invalid conditions
#print the result ONLY when ALL inputs are valid



# This program calculates the creatinine clearance using the Cockcroft-Gault formula
age = int(input("Enter age: "))
weight = float(input("Enter weight in kg: "))
gender = input("Enter gender (M/F): ")
Cr = float(input("Enter creatinine concentration in µmol/l: "))
#to separate the situation into male or female
if gender == 'M':
    sexco = 1   
elif gender == 'F':  
    sexco = 0.85
else:print("Invalid gender") 
#and decide the coefficient according

CrCl = sexco*(140 - age)*weight/(72*Cr)  #just use the given equation

#to exclude the invalid input
if age > 100 or age < 0:
    print("Invalid age")
if  weight < 20  or weight > 80:
    print("Invalid weight")
if Cr < 0 or Cr > 100:
    print("Invalid creatinine concentration")

#to permit the valid input and print the result
if age >= 0 and age <= 100 and weight >= 20 and weight <= 80 and Cr >= 0 and Cr <= 100 and gender in ['M', 'F']:
    print("Creatinine clearance is: ", CrCl)