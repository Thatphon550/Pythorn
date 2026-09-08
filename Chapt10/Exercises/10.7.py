import random

lst = []
for i in range(1000):
    lst.append(random.randint(0, 9))

countLst = 10 * [0]

for num in lst:
    countLst[num] += 1

print(countLst)