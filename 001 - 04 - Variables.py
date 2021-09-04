# Spyder Editor
# Created on Sun Aug 29 13:24:44 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 001 - 04 - Variables

name = input("What is your name? ")
familyName = input("What is your family name? ")
nameLength = len(name)
familyNameLength = len(familyName)
print("***************\nYour name consists of " + str(nameLength) + 
      " characters\nand your family name consists of " + str(familyNameLength)
       + " characters\nand all together are " + str(nameLength + familyNameLength)
        + " characters.")

