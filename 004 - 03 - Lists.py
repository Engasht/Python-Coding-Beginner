# Spyder Editor
# Created on Sat Sep 11 12:10:33 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 004 - 03 - lists

fruits = ["aple", "orange", "banana", "pineapple"]

print(fruits[0])
print(fruits[3])
print(fruits[-1])
print(fruits[-4])

fruits[0] = "apple"
print(fruits[0])

fruits.append("cherry")
print(fruits)

print(len(fruits))

fruits.extend(["blackberry", "melon"])
print(fruits)