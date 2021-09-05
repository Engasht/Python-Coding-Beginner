# Spyder Editor
# Created on Sun Sep  5 14:47:26 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 003 - 07 - pizza order challenge

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L. ")
add_pepperoni = input("Do you want pepperoni? Y or N. ")
extra_cheese = input("Do you want extra cheese? Y or N. ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
        
if add_pepperoni == "Y":
    if size =="S":
        bill += 2
    else:
        bill += 3
    
if extra_cheese == "Y":
    bill += 1
    
print(f"Your bill is ${bill}!")