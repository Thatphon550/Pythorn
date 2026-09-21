import random

def main():
    matrix = [[random.randint(0, 1) for _ in range(6)] for _ in range(6)]
    while not check_even(matrix):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                matrix[row][col] = random.randint(0, 1)

    for i in matrix:
        print(i)

def check_even(matrix):
    for row in range(len(matrix)):
        count_0 = 0
        count_1 = 0
        for col in range(len(matrix[row])):
            if matrix[row][col]:
                count_1 += 1
            else:
                count_0 += 1
        if count_0 % 2 or count_1 % 2:
            return False

    for col in range(len(matrix[0])):
        count_0 = 0
        count_1 = 0
        for row in range(len(matrix)):
            if matrix[row][col]:
                count_1 += 1
            else:
                count_0 += 1
        if count_0 % 2 or count_1 % 2:
            return False
    return True

main()
