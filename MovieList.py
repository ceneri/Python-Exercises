#Cesar Neri
#December 11, 2016

#!/usr/bin/env python3

#display available options
def display_menu():
    print ("COMMAND MENU")
    print("list - List all Movies\nadd - Add a movie\n" +
                    "del - Delete a movie\nexit - Exit program")
    print()

#List the movies in the parameter list    
def list_movies(movie_list):
    for i in range(0, len(movie_list)):
        print(str(i+1) + ". " + str(movie_list[i]))
    print()

#Adds a new movie to the parameter list        
def add_movie(movie_list):
    movie_title = input("Name:\t")
    movie_list.append(movie_title)

#removes a movie from the parameter list  
def del_movie(movie_list):
    movie_number = int(input("Number:\t"))
    if movie_number > 0 and movie_number <= len(movie_list):
        movie_list.pop(movie_number-1)
    else:
        print("Invalid movie number, please try again")
        
#MAIN
def main():
    movies = ["Monty Python and the Holy Grail", "On the Waterfront", "2012"]

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

    
