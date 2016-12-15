#Cesar Neri
#December 15, 2016

#Excercise 10-2 from Murach's Python Programming Book



#!/usr/bin/env python3


import WordList as wl

#calls get_random_word(), and returns it in uppercase
def get_word():
    word = wl.get_random_word()

    return word.upper()

#word passed, gets blank spaces in between each letter
def add_spaces(word):
    return " ".join(word)

#Draws game info screen using parameter passed
def draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word):
    print("=" * 79)
    print("Word:", add_spaces(displayed_word),
          "   Guesses Left:", num_guesses,
          "   Wrong:", num_wrong,
          "   Tried:", add_spaces(guessed_letters))

#Draws game info screen using parameter passed
def draw_hangman(num_wrong):
    if  num_wrong > 0:
        print("_" * 5)
    if  num_wrong > 1:
        print(" " * 4, "|")
    if  num_wrong > 2:
        print(" " * 4, "O")

    if  num_wrong > 3:
        if  num_wrong > 5:
            print(" " * 3, "\|/")
        elif num_wrong > 4:
            print(" " * 3, "\|")
        else :
            print(" " * 4, "|")

    if num_wrong > 6:
        print(" " * 4, "|")
    if num_wrong > 7:
        if num_wrong > 8:
            print(" " * 3, "/ \\")
        else:
            print(" " * 3, "/")

    print()
        

#gets a letter from the user and checks that it has not been used before
def get_letter(guessed_letters):
    while True:
        guess = input("Enter a letter:\t")
        guess = guess.upper()
        
        #check that it is a single letter
        if len(guess) > 1 or guess == "":
            print("Invalid Entry: You can only enter a single letter!")
            continue

        #check that letter hasnt been used before
        if guess in guessed_letters:
            print("Invalid Entry: You have already used that letter!")
            continue

        #if both checks are passed, letetr is turned to uppercase and returned
        return guess
            

def play_game():
    #get the word to guess 
    word = get_word()

    #initiate variables
    num_wrong = 0
    num_guesses = 9
    guessed_letters = ""
    displayed_word = "_" * len(word)
    remaining_letters = len(word)

    #draw initial screen
    draw_hangman(9)
    draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    #10 turns
    while num_guesses > 0 and remaining_letters > 0:

        #get a letter from user and add to list of guessed letters
        guess = get_letter(guessed_letters)
        guessed_letters += guess

        #chek that new letter is in word
        index = word.find(guess)
        if index >= 0:
            displayed_word = ""
            remaining_letters = len(word)
            for char in word:
                if char in guessed_letters:
                    displayed_word += char
                    remaining_letters -= 1
                else:
                    displayed_word += "_"
        else:
            num_wrong += 1        
            #increment
            num_guesses -= 1

        #print screen afterwards
        draw_hangman(num_wrong)
        draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)
    
    print("=" * 79)

    #check if user succeded
    if remaining_letters == 0:
        print ("Congrats, you did it in " + num_guesses + " guesses.")

    #otherwise he failed
    else:
        print ("Sorry, you do not have any more guesses left.")
        print ("The word was:\t" + word)
        
#MAIN
def main():
    #greeting
    print("welcome to the H A N G M A N game!")

    #multiple plays
    while True:
        play_game()
        response = input("Do you want to play again? (y/n)")

        if response.lower() != "y":
            break

#eExecute main() only if it is the main module
if __name__ == "__main__":
    main()
