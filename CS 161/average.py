import math
num_grades = int(input(" How many grades would you like to input: "))


def grade_input(total_grades,):
    grades = []
    i = 0
    while i < total_grades:
        grade_score = float(input("Enter Grade: "))
        grades.append(grade_score)
        i += 1
    avg = sum(grades)/i
    print(f"The average of the test score is: {round(avg,2)} ")


grade_input(num_grades)