# Spyder Editor
# Created on Sat Sep  4 17:43:17 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 003 - 04 - BMI calculator and weight interpretation

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2, 1)

if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are underwight.")
elif bmi < 25:
    print(f"Your BMI is {bmi} and you have normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi} and you are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi} and you are obese.")
else:
    print(f"Your BMI is {bmi} and you are clinically obese.")