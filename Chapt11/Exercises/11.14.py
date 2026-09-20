import random

def main():
    matrix = []
    size = int(input("Enter the size for the matrix: "))
    for i in range(size):
        matrix.append([random.randint(0, 1) for _ in range(size)])


    printMatrix(matrix)
    check(matrix)

def printMatrix(m):
    for row in m:
        for col in row:
            print(col, end="")
        print()

def check(matrix):
    row_check(matrix)
    col_check(matrix)
    check_major_diagonal(matrix)

def row_check(matrix):
    matrix = [[0, 1], [1, 0]]
    zero_row = []
    one_row = []
    for row in range(len(matrix)):
        all_zero = True
        all_one = True
        for col in range(len(matrix)):
            if matrix[row][col]:
                all_zero = False
            else:
                all_one = False
        if all_zero:
            zero_row.append(row)
        elif all_one:
            one_row.append(row)

    if zero_row or one_row:
        if zero_row:
            print(f"All 0s on row {[x for x in zero_row]}")
        else:
            print("No same 0s in a row")
        if one_row:
            print(f"All 1s on row {[x for x in one_row]}")
        else:
            print("No same 1s in a row")
    else:
        print("No same numbers in a row")

def col_check(matrix):
    zero_col = []
    one_col = []
    for col in range(len(matrix)):
        all_zero = True
        all_one = False
        for row in range(len(matrix)):
            if matrix[row][col]:
                all_zero = False
            else:
                all_one = False
        if all_zero:
            zero_col.append(col)
        elif all_one:
            one_col.append(col)

    if zero_col or one_col:
        if zero_col:
            print(f"All 0s on column {[x for x in zero_col]}")
        else:
            print("No same 0s in a column")
        if one_col:
            print(f"All 1s on column {[x for x in one_col]}")
        else:
            print("No same 1s in a column")
    else:
        print("No same numbers in a column")

def check_major_diagonal(matrix):
    n = matrix[0][0]
    all_diagonal = True 
    for i in range(len(matrix)):
        if matrix[i][i] != n:
            all_diagonal = False
    if all_diagonal:
        print(f"All {"1s" if matrix[0][0] else "0s"} in the major diagonal")
    else:
        print("No same numbers in the major diagonal")

main()
