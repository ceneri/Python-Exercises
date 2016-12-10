#Cesar Neri
#December 10, 2016

#Excercise 2-3 from Murach's Python Programming Book

#Area and Perimeter 

#!/usr/bin/env python3

#Print Greeting
print("The Area and Perimeter Program\n")

#Prompt for length and width
length = int(input("Please enter the length:\t"))
width = int(input("Please enter the width:\t\t"))

#calculate
area = length * width
perimeter = (length*2) + (width*2)

#output
print("\nArea:\t\t" + str(area))
print("Perimeter:\t" + str(perimeter))
print("\nGood bye!")
