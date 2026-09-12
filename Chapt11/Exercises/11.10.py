import random

matrix = [[random.randint(0, 1) for _ in range(4)] for _ in range(4)]

largestRowIndex = []
largestRowAmount = 0

for row in range(len(matrix)):
    sumRow = sum(matrix[row])
    
    if sumRow > largestRowAmount:
        largestRowIndex.clear()
        largestRowIndex.append(row)
        largestRowAmount = sumRow
    elif sumRow == largestRowAmount:
        largestRowIndex.append(row)

largestColumnIndex = []
largestColumnAmount = 0

for col in range(len(matrix)):
    sumColumn = 0
    for row in range(4):
        sumColumn += matrix[row][col]

    if sumColumn > largestColumnAmount:
        largestColumnIndex.clear()
        largestColumnIndex.append(col)
        largestColumnAmount = sumColumn
    elif sumColumn == largestColumnAmount:
        largestColumnIndex.append(col)

for row in matrix:
    for col in row:
        print(col, end= "")
    print()

print("The largest row index:", *largestRowIndex, sep=" ")
print("The largest column index:", *largestColumnIndex, sep=" ")