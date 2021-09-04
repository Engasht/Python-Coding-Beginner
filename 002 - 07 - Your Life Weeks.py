# Spyder Editor
# Created on Wed Sep  1 16:26:11 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 002 - 07 - weeks of your life

age = input("What is your current age? ")
left_years = 90 - int(age)
left_months = left_years * 12
left_weeks = left_years * 52
left_days = left_years * 365

print(f"You have {left_days} days, {left_weeks} weeks, and {left_months} months left!")