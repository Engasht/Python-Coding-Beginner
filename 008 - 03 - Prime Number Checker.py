# Spyder Editor
# Created on Sat Sep 25 09:24:54 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 008 - 03 - Prime Number Checker

#Write your code below this line 👇
import math
def prime_checker(number):
    not_found = True
    numerator = 1
    square_root = math.sqrt(number)
    while not_found:
        numerator += 1
        if numerator <= square_root:
            if number % numerator == 0:
                print(f"{number} is not a prime number.")
                not_found = False
        else:
            print(f"{number} is a prime number.")
            not_found = False




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
