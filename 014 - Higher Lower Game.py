# Spyder Editor
# Created on Sun Oct 10 10:28:53 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 014 - Higher Lower Game

# import logo and data and random and os
from random import randint
from art014 import logo, vs
from data014 import data
import os

# length of data
# list of comparing items (dictionaries)
# score
NUMBER_OF_ITEMS = len(data)
COMPARING_ITEMS = [
    {}, 
    {}
]
SCORE = 0

# function to choose from data and return dictionary
def choose_item(name_of_first_item):
    '''
    Choose an item from the list of data and return a dictionary. Check to not return the same item.
    '''
    chosen_item = data[randint(0, NUMBER_OF_ITEMS - 1)]
    while chosen_item["name"] == name_of_first_item:
        chosen_item = data[randint(0, NUMBER_OF_ITEMS - 1)]
    return chosen_item

# function to check the result and track the score, return (True/False), check input to be correct
def check_answer(answer):
    '''
    Ask the user to answer, then checks the answer and returns True/False
    Check if the user answer with 'A' or 'B' (not case-sensative)
    Argument should be 'A' or 'B' which is the correct answer
    '''
    answered = False
    while not answered:
        user_answer = input("Who has more followers? Type 'A' or 'B': ").capitalize()
        if user_answer == "A" or user_answer == "B":
            answered = True
            if user_answer == answer:
                global SCORE
                SCORE += 1
                return True
            else:
                return False
        else:
            print("Please provide a correct answer.")
            
# function to find the correct answer
def correct_answer() :
    '''
    Finds the correct answer and returns 'A' or 'B'
    '''
    a_count = COMPARING_ITEMS[0]['follower_count']
    b_count = COMPARING_ITEMS[1]['follower_count']
    if a_count > b_count:
        return "A"
    else:
        return "B"

# function of game over
# clear page
# show logo
# show game over message with score
def game_over_message():
    os.system("clear")
    print(logo)
    print(f"Sorry, That's wrong! Final score: {SCORE}")

# function of game
# choose the first item
# while with game token
# clear page
# show logo
# show the first item
# show vs
# choose and show the second item
# ask the user and check the result
# if correct then continue game and replace the first item with second
# else game over
def game():
    COMPARING_ITEMS[0] = choose_item("")
    game_over = False
    while not game_over:
        os.system("clear")
        print(logo)
        if SCORE != 0:
            print(f"You're right! Current score: {SCORE}.")
        print(f"Compare A: {COMPARING_ITEMS[0]['name']}, a {COMPARING_ITEMS[0]['description']}, from {COMPARING_ITEMS[0]['country']}.")
        print(vs)
        COMPARING_ITEMS[1] = choose_item(COMPARING_ITEMS[0]['name'])
        print(f"Against B: {COMPARING_ITEMS[1]['name']}, a {COMPARING_ITEMS[1]['description']}, from {COMPARING_ITEMS[1]['country']}.")
        if check_answer(correct_answer()):
            COMPARING_ITEMS[0] = COMPARING_ITEMS[1]
        else:
            game_over = True
            game_over_message()
    
game()