# ======= Normal Method ============
# with open("weather_data.csv") as file:
#     data = file.readlines()
#     print(data)
#
#  ------------- CSV Method -------------
# import csv
#
# with open("weather_data.csv") as file_data:
#     data = csv.reader(file_data)
#     tempratures = []
#
#     for row in data:
#         if row[1] != "temp":
#             tempratures.append(int(row[1]))
#     print(tempratures)

# /////////////  PANDAS Method //////////////////

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # # print(data["temp"])
# temp_list = data["temp"].to_list()
# max_no = max(temp_list)
# average = sum(temp_list) / len(temp_list)
# print(average)
# print(max)
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# temp = data.temp * 9/5 + 32
# print(temp)

import pandas

data = pandas.read_csv("Squirrel_Data .csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
Cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(grey_squirrel_count)
print(black_squirrel_count)
print(Cinnamon_squirrel_count)

data_dict = {
    "Fur colors": ["Gray", "Black", "Cinnamon"],
    "Count": [grey_squirrel_count, black_squirrel_count, Cinnamon_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
