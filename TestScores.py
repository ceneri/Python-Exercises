#Cesar Neri
#December 10, 2016

#Excercise 3-2 from Murach's Python Programming Book

#Get sets a set of scores, as many as the user wants, print the total and their average

#!/usr/bin/env python3

#Greeting
print("Test Scores Program")

#Initial response
response = "y"

#Check user response (run program more than once)
while response.lower() == "y":

    #Clear score and count
    totalScore = 0
    count = 0

    #Get user data
    print("\nEnter a set of scores, enter 'end' to end input\n========================================")
    
    #Get more than one test score
    while True:
        score  = input("Enter Test Score:\t\t")
        
        #validate score
        if score.lower() == "end":
            break
        elif int(score) > 0 and int(score) <= 100:  #validate score range
            totalScore += int(score)
            count += 1
        else:
            print("Test score must be within 0 and 100, please try again.")
        
        
    print("========================================")

    #Calculate Output
    averageScore = round(totalScore/count, 2)

    #Print output
    print ("Total Score: \t" + str(totalScore) )
    print ("Average Score: \t" + str(averageScore) )

    #Get new response
    response = input("Enter another set of scores (y/n)?\t")

print("\nGoodbye!")
