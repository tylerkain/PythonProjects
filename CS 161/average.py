num_grades = int(input(" How many grades would you like to input: "))


def grade_input(total_grades,):
    grades = []
    i = 0
    while i < total_grades:
        grade_score = float(input("Enter Grade: "))
        grades.append(grade_score)
        i += 1
    print(grades)

def get_grade_avg():


grade_input(num_grades)

