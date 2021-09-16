# Spyder Editor
# Created on Thu Sep 16 22:31:31 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 005 - 05 - fizz buzz

for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

