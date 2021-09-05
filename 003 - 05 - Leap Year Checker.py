# Spyder Editor
# Created on Sun Sep  5 14:06:24 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 003 - 05 - leap year checker

year = int(input("Which year do you want to check? "))

# on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"The year {year} is a leap year!")
        else:
            print(f"The year {year} is not a leap year!")
    else:
        print(f"The year {year} is a leap year!")
else:
   print(f"The year {year} is not a leap year!")         