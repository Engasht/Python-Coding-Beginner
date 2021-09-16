# Spyder Editor
# Created on Thu Sep 16 13:36:07 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 005 - 02 - height average

student_heights = input("Input a list of students heights ").split()
# print(student_heights)
# print(len(student_heights))
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_heights = 0
# for n in range(0, len(student_heights)):
#     total_heights += student_heights[n]
# print(total_heights)
# average = total_heights / len(student_heights)

# without For loop
# average = sum(student_heights) / len(student_heights)

# without len() and sum()
number_of_students = 0
for height in student_heights:
    total_heights += height
    number_of_students += 1
average = total_heights / number_of_students

print(average)