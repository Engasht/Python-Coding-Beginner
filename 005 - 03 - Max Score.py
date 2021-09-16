# Spyder Editor
# Created on Thu Sep 16 15:00:20 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 005 - 03 - max score

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# without For loop
# print(max(student_scores))
# print(min(student_scores))

highest = 0
for score in student_scores:
    if highest < score:
        highest = score
print(f"The highest score in the class is : {highest}")