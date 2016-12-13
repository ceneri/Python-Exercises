#Cesar Neri
#December 13, 2016

#Excercise 6-1 from Murach's Python Programming Book

#Get a set of scores from the user and prints the processed data
#It now uses functions that return lists, and take lists as arguments



#!/usr/bin/env python3

#Get every score from the user
def get_scores():
    scores = []
    
    while True:
        score = input("Enter the test score:\t")
        if score == "x":
            break
        elif int(score) < 0 or int(score) > 100 :
            print ("Please enter a valid score between 1 and 100")
        else:
            scores.append(int(score))

    return scores

#Calculates the outut values and prints them
def process_scores(scores):
    total = 0
    count = len(scores)
    low = min(scores)
    high = max(scores)
    median = scores [count//2]

    for item in scores:
        total += item
 
    average = round(total/count, 2)

    print("\nTotal\t\t\t", total)
    print("Number of Scores:\t", count)
    print("Average Score:\t\t", average)
    print("Low Score\t\t", low)
    print("High Score\t\t", high)
    print("Median Sccore\t\t", median)    

#Calls the get_scores and process_scores functions from the user
def main():
    print("Test Scores Program\nEnter 'x' to exit.\n")

    scores = get_scores()

    process_scores(scores)

    print("\nGoodbye!")

#If TestScores is the main module, call main()
if __name__ == "__main__":
    main()
