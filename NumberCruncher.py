#Cesar Neri
#December 13, 2016

#Number Cruincher tests some list and tuple functionalities



#!/usr/bin/env python3

#Import random module
import random

#Crunch numbers calculates the average, median, max, min and calls get_duplicates() on a list or a tuple
def crunch_numbers(data):
    total = 0
    count = len(data)
    median = data[count//2]
    data_min = min(data)
    data_max = max(data)

    #add every value to the total
    for item in data:
        total += item

    average = round(total/count, 2)

    #call to get duplicates
    dups = get_duplicates(data)

    #output
    print ("Average = ", average,
           " Median = ", median,
           " Min = ", data_min,
           " Max = ", data_max,
           " Dups = ", dups)

#It check every value from 0 to 50 looking for duplicates ina  list or tuple
def get_duplicates(data):
    dups = []
    for i in range(51):
        if data.count(i) > 1:
            dups.append(i)

    #retuns a list containig the duplicates        
    return dups


#Main creates a tuple with 11 values in asending order increasing by 5
#Also a list with 11 random numbers, sorts them, then calls crunch_numbers on both
def main():
    tup = (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
    
    liss = []
    for i in range(11):
        liss.append( random.randint(0, 50) )
        
    liss.sort()

    print("TUPLE DATA", tup)
    crunch_numbers(tup)
    print()
    print("RANDOM DATA", liss)
    crunch_numbers(liss)

#If NumberCruncher is the main module, execute main
if __name__ == "__main__":
    main()

    
