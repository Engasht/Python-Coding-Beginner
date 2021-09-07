# Spyder Editor
# Created on Mon Sep  6 09:52:45 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 003 - 08 - logical operators

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill += 5
        print("Child tickets are $5.")
    elif age < 18:
        bill += 7
        print("Youth tickets are $7.")
    elif age < 45 or age > 55:
        bill += 12
        print("Adault tickets are $12.")
    else:
        print("We care about midlife crisis. You don't need to pay anything!")
        
    wants_photo = input("Do you want photos? Y or N. ")
    if wants_photo == "Y":
        bill += 3
        
        print(f"Your bill is ${bill}.")
        
else:
    print("Sorry, you have to grow taller to ride.")