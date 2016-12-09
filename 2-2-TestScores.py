#Cesar Neri
#December 9, 2016

#Excercise 2-2 from Murach's Python Programming Book

#Get 3 scores, prin them, the total and the average

#!/usr/bin/env python3

#Greeting
print("Test Scores Program")

#Get user data
print("\nEnter 3 test scores")
print("========================================")
score1  = int(input("Enter Test Score:\t\t"))
score2  = int(input("Enter Test Score:\t\t"))
score3  = int(input("Enter Test Score:\t\t"))
print("========================================")

#Calculate Output
totalScore = score1 + score2 + score3
averageScore = totalScore/3

#Print output
print ("Your Scores:\t" + str(score1), str(score2), str(score3) )
print ("Total Score: \t" + str(totalScore) )
print ("Average Score: \t" + str(averageScore) )

print("\nGoodbye!")
