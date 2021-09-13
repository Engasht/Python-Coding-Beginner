# Spyder Editor
# Created on Mon Sep 13 21:17:50 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 004 - 06 - treasure map

row1 = ["◻️", "◻️", "◻️"]
row2 = ["◻️", "◻️", "◻️"]
row3 = ["◻️", "◻️", "◻️"]

treasure_map = [row1, row2, row3]

print("   1    2    3")
print(f"1{row1}\n2{row2}\n3{row3}")

position = input("Where do you want to put the treasure? ")

chosen_row = int(position) % 10
# print(chosen_row)
chosen_column = (int(position) - chosen_row) // 10
# print(chosen_column)

# chosen_row = int(position[1])
# chosen_column = int(position[0])

treasure_map[chosen_row - 1][chosen_column - 1] = "X"

print("   1    2    3")
print(f"1{row1}\n2{row2}\n3{row3}")