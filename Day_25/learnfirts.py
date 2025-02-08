import pandas
# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

#com pandas
data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data)
# print()
# print(data["temp"])
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

temp_media = data["temp"].mean()
print(f"Temperatura media (com panda): {temp_media:.2f}")

temp_max = data["temp"].max()
print(f"Temperatura media (com panda): {temp_max:.2f}")

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)
