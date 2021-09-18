# Spyder Editor
# Created on Sat Sep 18 18:55:45 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 006 - 02 - While Loop

import random

number_of_hellos = random.randint(1, 20)
print(f"Number of Hellos are: {number_of_hellos}")

def print_hello(x):
    print(f"It's Hello number {x}")

counter = number_of_hellos
while counter > 0:
    print_hello(number_of_hellos - counter + 1)
    counter -= 1