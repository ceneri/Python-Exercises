#Cesar Neri
#December 13, 2016

#Excercise 6-1 from Murach's Python Programming Book
#Movie List uses a 3D list now to keep movie information, and display it.

#UPDATED: Program now uses file I/O to write and read data from BINARY file



#!/usr/bin/env python3

import pickle

#Global variable with the name of text file to read/write from
FILENAME = "movies.bin"

#Reads every line from file, and stores them as movies in a 2D list
def read_movies():
    movies = []
    with open(FILENAME, "rb") as file:
        movies = pickle.load(file)

    return movies

#Writes every movies from 2D list, into the text file as a line each
def write_movies(movies):
    with open(FILENAME, "wb") as file:
        pickle.dump(movies, file)
    

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
    movie_year = input("Year:\t")
    movie_price = round( float(input("Price:\t")), 2)
    
    #Create new movie obj (list)
    new_movie = [movie_title, movie_year, movie_price]

    #Add ne movie to list of movies
    movie_list.append(new_movie)
    print(movie_title + " was added.\n")

    #Call to write_movies() to save/update data
    write_movies(movie_list)

#Removes a movie from the parameter list  
def del_movie(movie_list):
    movie_number = int(input("Number:\t"))
    if movie_number > 0 and movie_number <= len(movie_list):
        movie_del = movie_list.pop(movie_number-1)
        print(movie_del[0] + " was deleted.\n")

        #Call to write_movies() to save/update data
        write_movies(movie_list)
    else:
        print("Invalid movie number, please try again")
        
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

    
