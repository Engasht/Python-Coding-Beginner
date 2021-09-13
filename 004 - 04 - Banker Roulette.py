# Spyder Editor
# Created on Mon Sep 13 20:00:52 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 004 - 04 - banker roulette

import random

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

# print(names)
# print(len(names) - 1)

chosen = random.randint(0, len(names) - 1)
print(f"{names[chosen]} is going to by the meal today!")

# chosen = random.choice(names)
# print(f"{chosen} is going to by the meal today!")


