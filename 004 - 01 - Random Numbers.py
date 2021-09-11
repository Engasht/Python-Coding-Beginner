# Spyder Editor
# Created on Sat Sep 11 10:29:09 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 004 - 01 - random numbers

import random
import ConstantsModule

random_integer = random.randint(1, 10)
print(f"A random integer between 1 and 10 (inclusive): {random_integer}")

random_float = random.random()
print(f"A random float number between zero and one (including 0 but excluding 1): {random_float}")

random_between_zero_five = random.random() * 5
print(f"A random float number between zero and 5 (including 0 but excluding 5): {random_between_zero_five}")

love_score = random.randint(0, 100)
print(f"Your Love Score is: {love_score}")

print(f"PI = {ConstantsModule.pi}")