#Cesar Neri
#December 13, 2016

#Excercise 6-1 from Murach's Python Programming Book
#Movie List uses a 3D list now to keep movie information, and display it.



#!/usr/bin/env python3

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

#Removes a movie from the parameter list  
def del_movie(movie_list):
    movie_number = int(input("Number:\t"))
    if movie_number > 0 and movie_number <= len(movie_list):
        movie_del = movie_list.pop(movie_number-1)
        print(movie_del[0] + " was deleted.\n")
    else:
        print("Invalid movie number, please try again")
        
#Main
def main():
    movies = [ ["Monty Python and the Holy Grail", 1975, 9.95], ["On the Waterfront", 1954, 5.59], ["Cat on a Hot Tin Roof", 1958, 7.95] ]

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


    print("\nGood Bye!")

#If movie list is the main module, call main
if __name__ == "__main__":
    main()

    
