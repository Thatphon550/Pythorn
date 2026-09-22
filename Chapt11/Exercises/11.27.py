def sortColumns(m):
    for col in range(len(m)):
        for row in range(len(m) - 1):
            if m[row][col] > m[row + 1][col]:
                m[row][col], m[row + 1][col] = m[row + 1][col], m[row][col]

def main():
    matrix = [
        [0.15, 0.875, 0.375],
        [0.55, 0.005, 0.225],
        [0.30, 0.12, 0.4]
    ]

    sortColumns(matrix)

    for r in matrix:
        for c in r:
            print(c, end = " ")
        print()

main()
