# Spyder Editor
# Created on Sat Sep  4 12:01:19 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 002 - 08 - tip calculator

print("Welcome to the tip calculator.")
# total bill amount
bill = float(input("What was the total bill? $"))
# tip percentage
tip = int(input("What percentage tip whould you like to give? 10, 12, or 15? "))
# number of people
people = int(input("How many people to split the bill? "))

# calculations

int_people = int(people)
share = bill * (1 + tip / 100) / people
# output
print(f"Each person should pay: ${round(share, 2)}")
share_with_two_decimals = "{:.2f}".format(share)
print(f"Each person should pay: ${share_with_two_decimals}")
print("Each person should pay: ${:.2f}".format(share))