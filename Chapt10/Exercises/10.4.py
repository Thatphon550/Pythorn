scoreString = str(input("Enter scores separated by a space: "))

scoreLst = scoreString.split(' ')


for i in range(len(scoreLst)):
    scoreLst[i] = int(scoreLst[i])

average = sum(scoreLst) / len(scoreLst)
aboveCount = 0
belowCount = 0
averageCount = 0

for score in scoreLst:
    if score > average:
        aboveCount += 1
    elif score < average:
        belowCount += 1
    else:
        averageCount += 1
print(f"Average = {average:.2f}")
print(f"Above: {aboveCount}")
print(f"At average: {averageCount}")
print(f"Below: {belowCount}")