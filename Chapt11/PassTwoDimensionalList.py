def getMatrix():
    matrix = []

    numberOfRows = eval(input("Enter the number of rows: "))
    numberOfColumns = eval(input("Enter the number of columns: "))
    for row in range(numberOfRows):
        matrix.append([])
        for column in range(numberOfColumns):
            value = eval(input("Enter a value and press Enter: "))
            matrix[row].append(value)

    return matrix

def f(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] += 1

def printM(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end = "")
        print()

def accumulate(m):
    total = 0
    for row in m:
        total += sum(row)

    return total

def main():
    m = getMatrix()
    print(m)

    print("\nSum of all elements is", accumulate(m))

m = [[0, 0], [0, 1]]

printM(m)
f(m)
printM(m)

