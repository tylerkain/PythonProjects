temp_celsius ={

    'Monday': 53.6,
    'Tuesday': 57.2,
    'Wednesday': 59.0,
    'Thursday': 57.2,
    'Friday': 69.8,
    'Saturday': 71.6,
    'Sunday': 75.2

}

temp_f = {day: temp_c * 9/5 + 32 for (day, temp_c) in temp_celsius.items()}
print(temp_f)