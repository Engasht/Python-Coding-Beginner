# Spyder Editor
# Created on Thu Sep 16 15:18:35 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 005 - 04 - sum of even numbers

number = int(input("Enter the number to which you want the sum of even numbers: "))

# total = 0
# for n in range(2, number + 1, 2):
#     total += n
# print(total)

total_list = []
for n in range(2, number + 1, 2):
    total_list.append(n)
print(sum(total_list))

