# lesson 3 assignment
user_score = int(input("Please enter your score (0-100) here: "))
if user_score < 60:
     grade= "F"
elif user_score < 70:
    grade = "D"
elif user_score < 80:
    grade = "C"
elif user_score < 90:
    grade = "B"
else :
    grade = "A"

"""
Grade Ranges
______________
90 - 100: A
80 - 89: B
70 - 79: C
60 - 69: D
0 - 59: F
"""
print(f"Your score was {user_score}, which means you earned a {grade}!" )
#___________________
#extra challenge 1
import random
rival_score = random.randint(1,100)
if rival_score < 60:
     rival_grade= "F"
elif rival_score < 70:
    rival_grade = "D"
elif rival_score < 80:
    rival_grade = "C"
elif rival_score < 90:
    rival_grade = "B"
else :
    rival_grade = "A"

if rival_score < user_score:
    print(f"Your rival got worse grade then you! They scored {rival_score} so they earned {rival_grade}!")
elif rival_score > user_score:
    print(f"Your rival got better grade then you! They scored {rival_score} so they earned {rival_grade}!")
else :
    print(f"Your rival revived the same score of {user_score} meaning you both earned the same grade of a {grade}!")









