# new_dict = {new_key:new_value for item in list}
names = ["Alex", "Beth","Caroline", "Dave", "Eleanor"]

import random
student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)
passed_students = {student:score for (student, score) in student_scores.items() if score >= 70}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow "

result = {word:len(word) for word in sentence.split()}
print(result)