def sortRows(m):
    for row in range(len(m)):
        m[row].sort()

def main():
    matrix = [
        [0.15, 0.875, 0.375],
        [0.55, 0.005, 0.225],
        [0.30, 0.12, 0.4]
    ]

    sortRows(matrix)
    print(matrix)

main()
