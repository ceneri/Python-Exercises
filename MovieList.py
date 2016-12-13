#Cesar Neri
#December 11, 2016

#Movie List uses a 2D list to keep movie information, and display it.

#!/usr/bin/env python3

#display available options
def display_menu():
    print ("COMMAND MENU")
    print("list - List all Movies\nadd - Add a movie\n" +
                    "del - Delete a movie\nexit - Exit program")
    print()

#List the movies in the parameter list    
def list_movies(movie_list):
    count = 1
    for item in movie_list:
        print(str(count) + ". " + item[0] + " (" + str(item[1]) + ")" )
        count += 1
    
    print()

#Adds a new movie to the parameter list        
def add_movie(movie_list):
    movie_title = input("Name:\t")
    movie_year = input("Year:\t")
    new_movie = [movie_title, movie_year]
    movie_list.append(new_movie)
    print(movie_title + " was added.\n")

#removes a movie from the parameter list  
def del_movie(movie_list):
    movie_number = int(input("Number:\t"))
    if movie_number > 0 and movie_number <= len(movie_list):
        movie_del = movie_list.pop(movie_number-1)
        print(movie_del[0] + " was deleted.\n")
    else:
        print("Invalid movie number, please try again")
        
#MAIN
def main():
    movies = [ ["Monty Python and the Holy Grail", 1975], ["On the Waterfront", 1954], ["2012", 2012] ]

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


if __name__ == "__main__":
    main()

    
