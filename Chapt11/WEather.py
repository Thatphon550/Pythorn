def main():
    NUMBER_OF_DAYS = 10
    NUMBER_OF_HOURS = 24

    data = []
    for i in range(NUMBER_OF_DAYS):
        data.append([])
        for j in range(NUMBER_OF_HOURS):
            data[i].append([])
            data[i][j].append(0)
            data[i][j].append(0)

    for k in range(NUMBER_OF_DAYS * NUMBER_OF_HOURS):
        line = input().strip().split()
        day = eval(line[0])
        hour = eval(line[1])
        temperature = eval(line[2])
        humidity = eval(line[3])

        data[day - 1][hour - 1][0] = temperature
        data[day - 1][hour - 1][1] = humidity

    for i in range(NUMBER_OF_DAYS):
        dailyTemperatureTotal = 0
        dailyHumidityTotal = 0
        for j in range(NUMBER_OF_HOURS):
            dailyTemperatureTotal += data[i][j][0]
            dailyHumidityTotal += data[i][j][1]

        print(f"Day {i}'s average temperature is {dailyTemperatureTotal / NUMBER_OF_HOURS:.2f}")
        print(f"Day {i}'s average temperature is {dailyHumidityTotal / NUMBER_OF_HOURS:.2f}")

main()