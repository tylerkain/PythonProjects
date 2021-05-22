# with open("weather_data.csv") as weather_data:
#   data = weather_data.readlines()
#   print(data)

# import csv

# with open("weather_data.csv") as data_file:
#   temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print(temperatures)

import pandas

data = pandas.read_csv("Day25/weather_data.csv")
data_dict = data.to_dict()
print(data_dict)

temperature_list = data["temp"].tolist()
# print(temperature_list)
# average_temperature = sum(temperature_list)/len(temperature_list)
# avg = data["temp"].max()
# print(average_temperature, avg)

# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * (9/5) + 32
# print(monday_temp_F)

