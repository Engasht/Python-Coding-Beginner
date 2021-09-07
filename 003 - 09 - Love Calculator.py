# Spyder Editor
# Created on Mon Sep  6 10:07:07 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 003 - 09 - love calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1.lower() + name2.lower()

true_score = names.count("t") + names.count("r") + names.count("u") + names.count("e")
love_score = names.count("l") + names.count("o") + names.count("v") + names.count("e")

score = int(str(true_score) + str(love_score))
# score = true_score * 10 + love_score

if score < 10 or score > 90:
    print(f"Your score is {score}, you go togrther like coke and mentos!")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright togrther.")
else:
    print(f"Your score is {score}.")

