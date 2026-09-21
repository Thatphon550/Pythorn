def main():
    matrix = []
    print("Enter a 3-by-3 matrix row by row: ")
    for i in range(3):
        matrix.append([eval(x) for x in input().strip().split()])

    if isMarkovMatrix(matrix):
        print("It is a Markov matrix")
    else:
        print("It is not a Markov matrix")

def isMarkovMatrix(matrix):
    if len(matrix) != len(matrix[0]):
        return False
    for col in range(len(matrix[0])):
        total = 0
        for row in range(len(matrix)):
            total += matrix[row][col]
        if total != 1:
            return False

    return True

main()
