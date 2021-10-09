# Spyder Editor
# Created on Wed Oct  6 20:19:25 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 012 - Number Gussing

import os
from art012 import logo
import random

def set_hardness():
    '''
    Returns
    -------
    int
        hardness of the game based on the user's choice, 5 for hard and 10 for easy
    '''
    hardness_is_ok = False
    while not hardness_is_ok:
        hardness = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if hardness == "easy":
            hardness_is_ok = True
            return 10
        elif hardness == "hard":
            hardness_is_ok = True
            return 5
        else:
            print("Not a correct input.")

def choose_number():
    '''
    Returns
    -------
    int
        a random number between 1 and 100 (including both)
    '''
    print("I'm thinking of a number between 1 and 100.")
    return random.randint(1, 100)

def ask_numbers(chosen_number, number_of_tries):
    '''
    Parameters
    ----------
    chosen_number : int
        the number that should be guessed
    number_of_tries : int
        number of tries that user is allowed

    Returns
    -------
    ask the user to guess a number, if it is correct prints a message otherwise makes a hint till the number of tries finishes.

    '''
    is_guessed = False
    
    while number_of_tries > 0 and not is_guessed:
        print(f"You have {number_of_tries} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess == chosen_number:
            is_guessed = True
            print(f"You got it! The answer was {chosen_number}")
        elif user_guess < chosen_number:
            print("Too low.")
        else:
            print("Too high.")
        number_of_tries -= 1
    
    if not is_guessed:
        print("You've run out of guesses, you Lose!")

def game():
    '''
    main game function
    '''
    chosen_number = choose_number()
    number_of_tries = set_hardness()
    ask_numbers(chosen_number, number_of_tries)
    

os.system('clear')
print(logo)
print("Welcome to the Number Gussing Game!")

to_stop = False

while not to_stop:
    game()
    if input("Do you want to play again? 'y' or 'n': ") != "y":
        to_stop = True
    os.system("clear")


