board = 8 * [8 * [0]]


for row in range(len(board)):
    for column in range(len(board)):
        #check for column
        found = False
        for r in range(len(board)):
            if board[r][column]:
                found = True
                break #queen is found
        if not found:
            board[row][column] = "Q"

for row in range(len(board)):
    for column in range(len(board)):
        print(board[row][column], end = " ")
    print()

# row1 = 8 * [None]
# row2 = 8 * [None]
# row3 = 8 * [None]
# row4 = 8 * [None]
# row5 = 8 * [None]
# row6 = 8 * [None]
# row7 = 8 * [None]
# row8 = 8 * [None]

