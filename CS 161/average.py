import matplotlib.pyplot as plt
import pandas as pd

num_grades = int(input(" How many grades would you like to input: "))


def grade_input(total_grades, ):
    grades = []
    i = 0
    while i < total_grades:
        grade_score = float(input("Enter Grade: "))
        grades.append(grade_score)
        i += 1
    avg = sum(grades) / len(grades)
    plt.plot(grades)
    print(f"The average of the test score is: {round(avg, 2)} ")


grade_input(num_grades)
grades_df = pd.DataFrame(grade_input(num_grades), columns=['Grades'])
axes = grades_df.plot(x='Grades', y='Number', style='.-')
y_label = axes.set_ylabel('Number')

plt.show()