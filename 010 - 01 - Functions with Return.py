# Spyder Editor
# Created on Sun Oct  3 10:33:58 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 010 - 01 - Functions with Return

def format_name(f_name, l_name):
    return (f_name + " " + l_name).title()

print(format_name("mohammad", "mehrabi"))

def format_name_2(f_name, l_name):
    if f_name == "" or l_name =="":
        return "You didn't provide correct input."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"

print(format_name_2(input("What is your first name? "), input("What is your last name? ")))