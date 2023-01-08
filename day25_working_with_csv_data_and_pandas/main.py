# <!======================================!>
# with open("weather_data.csv") as file:
#     data = file.read().split("\n")
#     temperatures = []
#     for row in data:
#         if row.split(",")[1] != "temp":
#             temperatures.append(int(row.split(",")[1]))
#     print(temperatures)

# <!================CSV======================!>

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# <!================PANDAS======================!>
import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
# print()
#
# temp_list = data["temp"].tolist()
# print(temp_list)
# print()
#
# average = sum(temp_list) / len(temp_list)
# print(f"Average Temperature: {average}")
# print()

# print(data["temp"].mean())

# max = data["temp"].max()
# print(f"Max Temperature: {max}")
# print()

# Get Data in Columns
# print(data["condition"])
# print(data.condition)


# Get data in rows
# print(data[data.day == "Monday"])


# Get max temp day
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = int(monday.temp)
# monday_temp_F = (monday_temp * 9 / 5) + 32
# print(monday_temp_F)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")