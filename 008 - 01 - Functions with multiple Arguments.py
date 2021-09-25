# Spyder Editor
# Created on Sat Sep 25 08:35:25 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 008 - 01 - Functions with multiple Arguments

def greeting(name, location, age):
    print(f"Hello {name}")
    print(f"How's the weather in {location}?\nHope you are enjoying your day!")
    if age <= 40:
        posture = "young"
    elif age <= 60:
        posture = "still young"
    else:
        posture = "healthy"
    print(f"It seems you are {posture}.")
    
greeting(location = "Tehran", age = 42, name = "Mani")