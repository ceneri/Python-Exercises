#Cesar Neri
#December 10, 2016

#Excercise 3-3 from Murach's Python Programming Book

#Future value calculator

#!/usr/bin/env python3

#Greeting
print("Welcome to the Future Value Calculator\n")

#Initial response
response = "y"

#Allow multiple runs of the program
while response.lower() == "y":

    print()

    #Get Monthly investment
    while True:
        monthlyInvestment = round(float(input("Enter monthly investment:\t")), 2)
        if monthlyInvestment > 0:
            break
        else:
            print ("Entry must be greater than 0. Please try again.")
        
    #Get yearlly interest rate
    while True:
        yearlyRate = int(input("Enter yearly interest rate:\t"))
        if yearlyRate > 0 and yearlyRate <= 15:
            break
        else:
            print ("Entry must be greater than 0 and less than or equal to 15. Please try again.")
    
    #Get yearly interest rate
    while True:
        years = int(input("Enter number of years:\t\t"))
        if years > 0 and years <= 50:
            break
        else:
            print ("Entry must be greater than 0 and less than or equal to 50. Please try again.")


    #Calculate
    total = 0.0
    monthlyRate = yearlyRate/12/100
    print()
                   
    #Print result
    for i in range(1, years+1):
        #calculte each month
        for j in range (12):
            total += monthlyInvestment
            total += round(total*monthlyRate, 3)
        
        print("Year = " + str(i) +  "\tFuture Value = " + str( round(total,2) ) )
                   

    #Get new response
    response = input("\nContinue (y/n)?\t")

print("\nGoodbye!")
