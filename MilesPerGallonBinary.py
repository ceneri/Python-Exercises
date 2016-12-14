#Cesar Neri
#December 13, 2016

#Excercise 7-3 from Murach's Python Programming Book

#BINARY: Program now stores the all data entered inside a list, and reads/writes to a binary file



#!/usr/bin/env python3

import pickle

#Global file variable
FILENAME = "mpg.bin"

#writes data to a bin file
def write_trips(trips):
    with open(FILENAME, "wb") as file:
        writer = pickle.dump(trips, file)

#reads data from bin file
def read_trips():
    trips = []
    with open(FILENAME, "rb") as file:
        trips = pickle.load(file)
            
    return trips        

#Gets a valid float using the parameter message
def get_valid_input(msg):
    while True:
        var = round( float(input(msg)), 2)
        if var < 0:
            print("Input entered must be greater than zero, please try again.")
        else:
            break
        
    return var

#Displays data in format
def display_data(trips):
    print("Distance\tGallons\t\tMPG")

    for trip in trips:
        print( str(trip[0]), "\t\t", str(trip[1]), "\t\t", str(trip[2]), "\t\t")


#MAIN
def main():

    #Greeting
    print("Miles Per Gallon Program\n");

    #create list to store data
    trips = read_trips()

    #call to display trips
    display_data(trips)

    #check response
    while True:

        #Get user data
        print()
        miles  = get_valid_input("Enter Miles Driven:\t\t")
        gallons  = get_valid_input("Enter Gallons of Gas Used:\t")
        # gallonCost = get_valid_input("Enter Cost per Gallon:\t\t")
        print()

        #Calculate Output
        mpg = round(miles / gallons, 2)
        # total = round(gallons * gallonCost, 2)
        # mileCost = round (gallonCost / round(miles / mpg, 2), 2)

        #create list out of output
        trip = [miles, gallons, mpg]

        #add list to 2D list
        trips.append(trip)

        #Print output
        print ("Miles Per Gallon: \t" + str(mpg) + "\n")
        # print ("Total Gas Cost: \t" + str(total) )
        # print ("Cost Per Mile: \t\t" + str(mileCost) )

        #display all data again
        display_data(trips)
        
        #get new response 
        response = input("\nGet Entries for another trip(y/n)\t")

        if response.lower() == "n":
            #call to write_trips() to bin file
            write_trips(trips)
            break
    

    print("\nGoodbye!")

if __name__ == "__main__":
    main()
