# Spyder Editor
# Created on Wed Sep  1 15:56:00 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 002 - 05 - bmi calculator

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

BMI = float(weight) / float(height) ** 2

print("Your BMI is: " + str(int(BMI)))