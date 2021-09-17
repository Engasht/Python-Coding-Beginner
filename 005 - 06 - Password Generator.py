# Spyder Editor
# Created on Thu Sep 16 22:41:01 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 005 - 06 - Password Generator

# print("Welcome to the PyPassword Generator!")
# input("How many letters would you like in your password?\n")
# input("How many symbols would you like?\n")
# input("How many numbers would you like?\n")

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
for n in range(0, nr_letters):
    password += random.choice(letters)  
for n in range(0, nr_symbols):
    password += random.choice(symbols)
for n in range(0, nr_numbers):
    password += random.choice(numbers)
    
print(f"Here is your password (ordered): {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password = "".join(random.sample(password, len(password)))
print(f"Here is your password: {hard_password}")

# another algorithm
# password_list = []
# for n in range(0, nr_letters):
#     password_list.append(random.choice(letters))
# for n in range(0, nr_symbols):
#     password_list.append(random.choice(symbols))
# for n in range(0, nr_numbers):
#     password_list.append(random.choice(numbers))
# random.shuffle(password_list)
# hard_password = ""
# for char in password_list:
#     hard_password += char    
# print(f"Here is your password: {hard_password}")