#Cesar Neri
#December 9, 2016

#Excercise 2-1 from Murach's Python Programming Book

#!/usr/bin/env python3

#Greeting
print("Miles per Gallon Program");

#Get user data
miles  = round(float(input("\nEnter Miles Driven:\t\t")), 2)
gallons  = round(float(input("Enter Gallons of Gas Used:\t")), 2)
gallonCost = round(float(input("Enter Cost per Gallon:\t\t")), 3)
print()

#Calculate Output
mpg = round(miles / gallons, 2)
total = round(gallons * gallonCost, 2)
mileCost = round (gallonCost / round(miles / mpg, 2), 2)

#Print output
print ("Miles Per Gallon: \t" + str(mpg) )
print ("Total Gas Cost: \t" + str(total) )
print ("Cost Per Mile: \t\t" + str(mileCost) )

print("\nGoodbye!")
