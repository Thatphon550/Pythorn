def sumMajorDiagonal(m):
    row = len(m)

    sumDiagonal = 0
    for i in range(row):
        sumDiagonal += m[i][i]

    return sumDiagonal

def main():
    matrix = []
    for i in range(4):
        line = str(input(f"Enter a 4-by-4 matrix row for row {i + 1}: "))
        matrix.append([eval(x) for x in line.split()])

    print(f"Sum of elements in the major diagonal is {sumMajorDiagonal(matrix)}")

main()