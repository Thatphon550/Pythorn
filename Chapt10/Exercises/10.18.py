board = [[0 for _ in range(8)] for _ in range(8)]


def isSafe(row, column):

    # Check column
    for i in range(len(board)):
        if board[i][column] != 0:
            return False

    # Check row
    for i in range(len(board[row])):
        if board[row][i] != 0:
            return False

    # Check ↖
    r = row - 1
    c = column - 1

    while r >= 0 and c >= 0:
        if board[r][c] != 0:
            return False
        r -= 1
        c -= 1

    # Check ↘
    r = row + 1
    c = column + 1

    while r < len(board) and c < len(board):
        if board[r][c] != 0:
            return False
        r += 1
        c += 1

    # Check ↗
    r = row - 1
    c = column + 1

    while r >= 0 and c < len(board):
        if board[r][c] != 0:
            return False
        r -= 1
        c += 1

    # Check ↙
    r = row + 1
    c = column - 1

    while r < len(board) and c >= 0:
        if board[r][c] != 0:
            return False
        r += 1
        c -= 1

    return True


def solve(row):

    # All 8 queens have been placed
    if row == len(board):
        return True

    # Try every column in this row
    for column in range(len(board)):

        if isSafe(row, column):

            board[row][column] = "Q"

            # Try to solve the next row
            if solve(row + 1):
                return True

            # Didn't work -> undo the queen
            board[row][column] = 0

    return False


solve(0)


for row in range(len(board)):
    for column in range(len(board)):
        print("|", end="")

        if board[row][column]:
            print(board[row][column], end="")
        else:
            print(" ", end="")

    print("|")