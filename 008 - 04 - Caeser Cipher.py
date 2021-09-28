# Spyder Editor
# Created on Sat Sep 25 10:26:40 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 008 - 04 - Caeser Cipher

from art00804 import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser():
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    shift %= len(alphabet) // 2
    
    if direction != "encode" and direction != "decode":
        print("Wrong input!")
    else:
        if direction == "decode":
            shift *= -1
        output = ""
        
        for letter in text:
            if letter not in alphabet:
                output += letter
            else:
                letter_index = alphabet.index(letter)
                shifted_letter_index = letter_index + shift
                output += alphabet[shifted_letter_index]
        
        print(f"The {direction}d text is '{output}'.")
        
        again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if again == "yes":
            caeser()
        else:
            print("Goodbye!")
    
caeser()

# Non-repeatative
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# shift %= len(alphabet) // 2

# def caeser(direction, text, shift):
#     if direction != "encode" and direction != "decode":
#         print("Wrong input!")
#     else:
#         if direction == "decode":
#             shift *= -1
#         output = ""
        
#         for letter in text:
#             if letter not in alphabet:
#                 output += letter
#             else:
#                 letter_index = alphabet.index(letter)
#                 shifted_letter_index = letter_index + shift
#                 output += alphabet[shifted_letter_index]
        
#         print(f"The {direction}d text is '{output}'.") 
    
# caeser(direction.lower(), text, shift)

# Easy way
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# def encrypt(text, shift):
#     cipher_text = ""
#     list_length = len(alphabet)
    
#     for letter in text:
#         letter_index = alphabet.index(letter)
#         # print(letter_index)
#         shifted_letter_index = letter_index + shift - list_length
#         # if shifted_letter_index + 1 > list_length:
#         #     shifted_letter_index -= list_length
#         cipher_text += alphabet[shifted_letter_index]
    
#     print(f"The encoded text is {cipher_text}")

# def decrypt(text, shift):
#     plain_text = ""
    
#     for letter in text:
#         letter_index = alphabet.index(letter)
#         shifted_letter_index = letter_index - shift
#         plain_text += alphabet[shifted_letter_index]
        
#     print(f"The decoded text is {plain_text}.")

# if direction.lower() == "encode":
#     encrypt(text, shift)
# elif direction.lower() == "decode":
#     decrypt(text, shift)
# else:
#     print("Wrong input!")