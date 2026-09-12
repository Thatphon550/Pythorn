def exist(table, row, col):
    if table[row][col]:
        return True
    return False

def checkWin(table, row, col, target):
    if table[0][col] == target and table[1][col] == target and table[2][col] == target:
        return True
    if table[row][0] == target and table[row][1] == target and table[row][2] == target:
        return True
    if table[0][0] == target and table[1][1] == target and table[2][2] == target:
        return True
    if table[0][2] == target and table[1][1] == target and table[2][0] == target:
        return True
    return False

def printTable(table):
    print("-------------")
    for row in table:
        print("|", end = " ")
        for col in row:
            if col:
                print(col, end = " | ")
            else:
                print(" ", end = " | ")
        print("\n-------------")

def game():
    table = [[None for _ in range(3)] for _ in range(3)]
    p1win, p2win = False, False
    while not p1win and not p2win:
        row1 = int(input("Enter a row (0, 1, or 2) for player X: "))  
        col1 = int(input("Enter a column (0, 1, or 2) for player X: "))
        if not exist(table, row1, col1):
            table[row1][col1] = "X"
        else:
            print("\nERROR: Grid already occupied!")
            break

        printTable(table)
        p1win = checkWin(table, row1, col1, "X")
        if p1win:
            print("X player won")
            break

        row2 = int(input("Enter a row (0, 1, or 2) for player O: "))  
        col2 = int(input("Enter a column (0, 1, or 2) for player O: "))
        if not exist(table, row2, col2):
            table[row2][col2] = "O"
        else:
            print("\nERROR: Grid already occupied!")
            break
        printTable(table)
        p2win = checkWin(table, row2, col2, "O")
        if p2win:
            print("Y player won")
            break

def main():
    game()

main()