# Initializing Lists with Input Values

# matrix = []

# numberOfRows = eval(input("Enter the number of rows: "))
# numberOfColumns = eval(input("Enter the number of columns: "))
# for row in range(numberOfRows):
#     matrix.append([])
#     for column in range(numberOfColumns):
#         value = eval(input(f"Enter an element for [{row}, {column}] and press enter: "))
#         matrix[row].append(value)

# print(matrix)

# Initializing Lists with Input Values

# import random
# import time

# matrix = []

# numberOfRows = eval(input("Enter the number of rows: "))
# numberOfColumns = eval(input("Enter the number of columns: "))
# for row in range(numberOfRows):
#     matrix.append([])
#     for column in range(numberOfColumns):
#         matrix[row].append(random.randint(0, 99))

# for row in matrix:
#     time.sleep(0.090)
#     print("[", end ="")
#     for i, column in enumerate(row):
#         if i == numberOfColumns - 1:
#             print(format(column, "3d"), end = " ]")
#         else:
#             print(format(column, "3d"), end = ",")
#     print()

# Printing Lists

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for row in range(len(matrix)):
#     for column in range(len(matrix[row])):
#         print(matrix[row][column], end = " ")
#     print()

# for row in matrix:
#     for value in row:
#         print(value, end = " ")
#     print()

# Summing All Elements

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# total = 0
# for row in matrix:
#     for value in row:
#         total += value

# print("Total is", total)

# Summing Elements by Column

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for column in range(len(matrix[0])):
#     total = 0
#     for row in range(len(matrix)):
#         total += matrix[row][column]
#     print("Sum for column", column, "is", total)

# Finding the Row with the Largest Sum

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# maxRow = sum(matrix[0])
# IndexOfMaxRow = 0

# for row in range(1, len(matrix)):
#     if sum(matrix[row]) > maxRow:
#         maxRow = sum(matrix[row])
#         IndexOfMaxRow = row

# print(f"Row {IndexOfMaxRow} has the maximum sum of {maxRow}")

# Random Shuffling

# import random

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for row in range(len(matrix)):
#     for column in range(len(matrix[row])):
#         i = random.randint(0, len(matrix) - 1)
#         j = random.randint(0, len(matrix[row]) - 1)

#         matrix[row][column], matrix[i][j] = matrix[i][j], matrix[row][column]

# print(matrix)

# Sorting

points = [[4, 2], [1, 7], [4, 5], [1, 2], [1, 1], [4, 1]]
points.sort()
print(points)