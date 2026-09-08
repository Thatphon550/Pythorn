numString = str(input("Enter integers between 1 and 100: "))
lst = numString.split(" ")
countLst = 100 * [0]

for num in lst:
    countLst[int(num) - 1] += 1

for i, count in enumerate(countLst):
    if count:
        print(f"{i + 1} occurs {count} ", end ="")
        print("time" if count == 1 else "times")
  
