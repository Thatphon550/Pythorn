def isConsecutiveFour(matrix):
    for row in range(len(matrix)):
        consecutive = 0
        for col in range(len(matrix[row]) - 1):
            if matrix[row][col] == matrix[row][col + 1]:
                consecutive += 1
                if consecutive == 3:
                    return True
            else:
                consecutive = 0

    for col in range(len(matrix)):
        consecutive = 0
        for row in range(len(matrix) - 1):
            if matrix[row][col] == matrix[row + 1][col]:
                consecutive += 1
                if consecutive == 3:
                    return True
            else:
                consecutive = 0

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            r, c = row, col
            consecutive = 1
            while r >= 1 and c >= 1:
                if matrix[r][c] == matrix[r - 1][c - 1]:
                    consecutive += 1
                    if consecutive >= 4:
                        return True
                else:
                    consecutive = 0
                r, c = r - 1, c - 1

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            r, c = row, col
            consecutive = 1
            while r >= 1 and c < len(matrix[row]) - 1:
                if matrix[r][c] == matrix[r - 1][c + 1]:
                    consecutive += 1
                    if consecutive >= 4:
                        return True
                else:
                    consecutive = 0
                r, c = r - 1, c + 1
def main():
    m1 = [
        [0, 1, 0, 3, 1, 6, 1],
        [0, 1, 6, 8, 6, 0, 1],
        [5, 6, 2, 1, 8, 2, 9],
        [6, 5, 6, 1, 1, 9, 1],
        [1, 3, 6, 1, 4, 0, 7],
        [3, 3, 3, 3, 4, 0, 7]
    ]
    m2 = [
        [0, 1, 0, 3, 1, 6, 1],
        [0, 1, 6, 8, 6, 0, 1],
        [5, 5, 2, 1, 8, 2, 9],
        [6, 5, 6, 1, 1, 9, 1],
        [1, 5, 6, 1, 4, 0, 7],
        [3, 5, 3, 3, 4, 0, 7]
    ]
    m3 = [
        [0, 1, 0, 3, 1, 6, 1],
        [0, 1, 6, 8, 6, 0, 1],
        [5, 5, 2, 1, 6, 2, 9],
        [6, 5, 6, 6, 1, 9, 1],
        [1, 5, 6, 1, 4, 0, 7],
        [3, 6, 3, 3, 4, 0, 7]
    ]
    m4 = [
        [0, 1, 0, 3, 1, 6, 1],
        [0, 1, 6, 8, 6, 0, 1],
        [9, 5, 2, 1, 6, 2, 9],
        [6, 9, 6, 6, 1, 9, 1],
        [1, 5, 9, 1, 4, 0, 7],
        [3, 6, 3, 9, 4, 0, 7]
    ]



    print(isConsecutiveFour(m1))
    print(isConsecutiveFour(m2))
    print(isConsecutiveFour(m3))
    print(isConsecutiveFour(m4))

if __name__ == "__main__":
    main()
