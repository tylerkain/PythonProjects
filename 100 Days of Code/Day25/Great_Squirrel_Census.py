import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(grey_squirrels, black_squirrels, cinnamon_squirrels)

data_dict ={
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels,cinnamon_squirrels,black_squirrels]
}

df = pandas.DataFrame(data_dict)

df.to_csv("Squirrel_Count")