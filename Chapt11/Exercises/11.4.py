strings = [
    "2, 4, 3, 4, 5, 8, 8",
    "7, 3, 4, 3, 3, 4, 4",
    "3, 3, 4, 3, 3, 2, 2",
    "9, 3, 4, 7, 3, 4, 1",
    "3, 5, 4, 3, 6, 3, 8",
    "3, 4, 4, 6, 3, 4, 4",
    "3, 7, 4, 8, 3, 8, 4",
    "6, 3, 5, 9, 2, 7, 9"
]

hours = []
for line in strings:
    hours.append([eval(x) for x in line.split(",")])

data = []
for employee in range(len(hours)):
    total = 0
    for hour in hours[employee]:
        total += hour
    data.append([total, employee])

data.sort(reverse=True)
print("Total hours worked by each employee this week.")
for i in range(len(data)):
    print(f"{i + 1}. Employee {data[i][1]}, Total hours: {data[i][0]}")