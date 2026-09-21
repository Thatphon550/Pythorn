def main():
    matrix = []
    for i in range(6):
        matrix.append([int(input(f"Enter row: {i} column: {j}: ")) for j in range(6)])

    odd = check_even(matrix)
    if odd:
        print(f"({odd[0]}, {odd[1]})")

def check_even(matrix):
    for row in range(len(matrix)):
        count_1 = 0
        for col in range(len(matrix[row])):
            if matrix[row][col]:
                last = col
                count_1 += 1

        if count_1 % 2:
            return [row, last]

main()
