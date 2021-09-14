# Spyder Editor
# Created on Tue Sep 14 09:45:32 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 004 - 07 - rock paper scissors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

elements = [rock, paper, scissors]
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if user_choice != "2" and user_choice != "1" and user_choice != "0":
    print("You entered an invalid input. You lose!")
else:
    user_choice = int(user_choice)
    print(elements[user_choice])
    print("\nComputer chose:\n")
    computer_choice = random.randint(0, 2)
    print(elements[computer_choice])
    result = user_choice * 10 + computer_choice
    # print(result)
    
    
    if user_choice == computer_choice:
    # if result == 0 or result == 11 or result == 22:
        print("It's a draw.")
    elif user_choice == computer_choice - 2 or user_choice == computer_choice + 1:
    # elif result == 2 or result == 10 or result == 21:
        print("You Win!")
    else:
        print("You Lose!")