#Cesar Neri
#December 17, 2016

#Excercise 14-1 from Murach's Python Programming Book


#!/usr/bin/env python3

import random
from Dice import Dice, Die

def main():
    print("The Dice Roller program")

    #print an image of every possible roll
    die = Die()
    for i in range(1,7):
        die.value = i
        
        print(die.image)

    print()

    # get number of dice from user
    count = int(input("Enter the number of dice to roll: "))

    # create Die objects and add to Dice object
    dice = Dice()
    for i in range(count):
        die = Die()
        dice.addDie(die)

    while True:        
        # roll the dice
        dice.rollAll()
        print("YOUR ROLL: ")
        for die in dice.list:
            print(die.image)
        print("\nTotal:\t" + str(dice.getTotal()))
        print("\n")

        choice = input("Roll again? (y/n): ")
        if choice != "y":
            print("Bye!")
            break

if __name__ == "__main__":
    main()
