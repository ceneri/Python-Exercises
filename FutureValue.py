#Cesar Neri
#December 14, 2016

#Excercise 8-1 from Murach's Python Programming Book (Future value calculator)

#Function main(), get_float(), and get_int() defined.
#main() called only if it is the main module

#UPODATED: Exception handling added to helper functions



#!/usr/bin/env python3

#MAIN DEFINITION-------------------------------------------------------------

def main():
    
    #Greeting
    print("Welcome to the Future Value Calculator\n")

    #Initial response
    response = "y"

    #Allow multiple runs of the program
    while response.lower() == "y":

        print()

        #Get Monthly investment
        monthlyInvestment = get_float("Enter monthly investment:\t", 0, 1000)
        
        #Get yearlly interest rate
        yearlyRate = get_float("Enter yearly interest rate:\t", 0, 15)
               
        #Get yearly interest rate
        years = get_int("Enter number of years:\t\t", 0, 50)

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
    

#HELPER FUNCTIONS-------------------------------------------------------------


#Takes a prompt argument to get input from user, it is then transformed to float and returned
def get_float(prompt, low_val, high_val):
    while True:
        try:
            fNumber = float(input(prompt));
            if fNumber > low_val and fNumber <= high_val:
                break
            else:
                print("Entry must be greater than " + str(low_val) + " and less than or equal to " + str(high_val) + ". Please try again.")
                
        except ValueError:
            print("Invalid float number entered. Please try again.")
            continue

    return fNumber

#Takes a prompt argument to get input from user, it is then transformed to int and returned
def get_int(prompt, low_val, high_val):
    while True:
        try:
            fNumber = int(input(prompt));
            if fNumber > low_val and fNumber <= high_val:
                break
            else:
                print("Entry must be greater than " + str(low_val) + " and less than or equal to " + str(high_val) + ". Please try again.")
        except ValueError:
            print("Invalid integer number entered. Please try again.")
            continue

    return fNumber
    

#CALL TO MAIN-------------------------------------------------------------------------

#If started as the main module, call the main() function
if __name__ == "__main__":
    main()
