# Spyder Editor
# Created on Sat Sep  4 17:34:16 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 003 - 03 - nested if and elif

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller to ride.")
