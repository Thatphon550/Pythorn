count = {}

line = input("Enter a line: ").strip()
for ch in line.split():
    try:
        num = eval(ch)
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    except:
        continue

most_occurrences =[]
max = 0

for num in count:
    if count[num]:
        if count[num] > max:
            max = count[num]
            most_occurrences.clear()
            most_occurrences.append(num)
        elif count[num] == max:
            most_occurrences.append(num)

for n in most_occurrences:
    print(n, end = " ")
