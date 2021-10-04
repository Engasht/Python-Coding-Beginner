# Spyder Editor
# Created on Sun Oct  3 13:03:25 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 010 - 04 - Calculator

# Add
def add(n1, n2):
    '''returns the sum of n1 and n2 (n1 + n2)'''
    return n1 + n2

# Subtract
def subtract(n1, n2):
    '''returns subtract of n1 and n2 (n1 - n2)'''
    return n1 - n2

# Multiply
def multiply(n1, n2):
    '''returns multiply of n1 and n2 (n1 * n2)'''
    return n1 * n2

# Divide
def divide(n1, n2):
    '''returns the division of n1 and n2 (n1 / n2)'''
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}

from art01004 import logo

def calculator():
    print(logo)

    num1 = float(input("What's the first number? "))
        
    for symbol in operations:
        print(symbol)
        
    continue_calculation = True
    while continue_calculation:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        to_continue = input(f"type 'y' to continue calculating with {answer}, or type 'r' to start a new calculation, or 'n' to exit.: ")
        if to_continue == "y":
            num1 = answer
        elif to_continue == "r":
            continue_calculation = False
            calculator()
        else:
            continue_calculation = False
            
calculator()