#Cesar Neri
#December 14, 2016

#Excercise 8-2 from Murach's Python Programming Book
#Movie List uses a 3D list now to keep movie information, and display it.

#UPDATED: Program now uses file I/O to write and read data from CSV file

#UPDATED: Program now handles file and value exceptions, as well as data validation on year and price


#!/usr/bin/env python3

import csv
import sys

#Global variable with the name of text file to read/write from
FILENAME = "movies.csv"

#Reads every line from file, and stores them as movies in a 2D list
def read_movies():
    try:
        movies = []
        with open(FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)

        return movies
    
    except FileNotFoundError:
        #print("Could not find " + FILENAME + " file.")
        #exit_program
        return movies
    except Exception as e:
        print( type(e), e)
        exit_program()

#Writes every movies from 2D list, into the text file as a line each
def write_movies(movies):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(movies)

    except OSError as e:
        print( type(e))
        exit_program()
            
    except Exception as e:
        print( type(e), e)
        exit_program()


#function to cllose program witha message
def exit_program():
    print("terminating program.")
    sys.exit()

#Display available options
def display_menu():
    print ("COMMAND MENU")
    print("list - List all Movies\nadd - Add a movie\n" +
                    "del - Delete a movie\nexit - Exit program")
    print()

#List the movies in the parameter list    
def list_movies(movie_list):
    count = 1
    for item in movie_list:
        print(str(count) + ". " + item[0] + " (" + str(item[1]) + ") @ " + str(item[2]) )
        count += 1
    
    print()

#Adds a new movie to the parameter list        
def add_movie(movie_list):

    #Get user input
    movie_title = input("Name:\t")

    #validate year
    while True:
        try:
            movie_year = int(input("Year:\t"))
            if movie_year < 1896 or movie_year > 2017:
                print("Movie year must be between 1896 and 2017. Please try again.")
                continue
        except ValueError:
            print("Invalid year value. Please try again.")
            continue
        break

        #validate price
    while True:
        try:
            movie_price = round( float(input("Price:\t")), 2)
            if movie_price <= 0 or movie_price >= 100:
                print("Movie price must be greater than zero but less than 100. Please try again.")
                continue
        except ValueError:
            print("Invalid price value. Please try again.")
            continue

        break
    
    #Create new movie obj (list)
    new_movie = [movie_title, movie_year, movie_price]

    #Add thee movie to list of movies
    movie_list.append(new_movie)
    print(movie_title + " was added.\n")

    #Call to write_movies() to save/update data
    write_movies(movie_list)

#Removes a movie from the parameter list  
def del_movie(movie_list):
    while True:
        try:
            movie_number = int(input("Number:\t"))
        except ValueError:
            print("Invalid Integer. Please try again.")
            continue
            
        if movie_number > 0 and movie_number <= len(movie_list):
            movie_del = movie_list.pop(movie_number-1)
            print(movie_del[0] + " was deleted.\n")

            #Call to write_movies() to save/update data
            write_movies(movie_list)
            break
        else:
            print("Invalid movie number. Please try again.")
        
#Main
def main():
    #Load the movie list from text file
    movies = read_movies()

    display_menu()

    while True:
        command = input("Command:\t")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            del_movie(movies)
        elif command.lower() == "exit":
            break
        else:
            print("Please enter a valid command\n")
            display_menu()

    #Before closing, write to file (save data)
    write_movies(movies)
    
    print("\nGood Bye!")

#If movie list is the main module, call main
if __name__ == "__main__":
    main()

    
