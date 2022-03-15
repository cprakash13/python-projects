# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     temperatures = []
#     data = csv.reader(data_file)
#     for row in data:
#         if row[1] == "temp":
#             continue
#         temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas as pd
#
# data = pd.read_csv("weather_data.csv")
# temperatures = data["temp"]
# print(temperatures.mean())
data = pd.read_csv("squirrel_data.csv")
color_count = data["Primary Fur Color"].value_counts()
color_count.to_csv("color_analysis.csv")
# print(data[data["Primary Fur Color"] == "Gray"]["Primary Fur Color"])