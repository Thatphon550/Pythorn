def multiplyMatrix(a, b):
    result = []
    for row in range(3):
        result.append([])
        for col in range(3):
            result[row].append(a[row][0] * b[0][col] + a[row][1] * b[1][col] + a[row][2] * b [2][col])

    return result

def main():
    # line1 = str(input("Enter matrix1: "))
    # line2 = str(input("Enter matrix2: "))

    line1 = "1 2 3 4 5 6 7 8 9"
    line2 = "0 2 4 1 4.5 2.2 1.1 4.3 5.2"
    matrix1 = []
    line1 = line1.split()  
    for row in range(3):
        matrix1.append([eval(x) for x in line1[row * 3:row * 3 + 3]])

    matrix2 = []
    line2 = line2.split()
    for row in range(3):
        matrix2.append([eval(x) for x in line2[row * 3: row * 3 + 3]])

    resultMatrix = multiplyMatrix(matrix1, matrix2)
    print("The multiplication of the")
    for i in range(3):
        print(format(matrix1[0][i], "5.1f"), end = "")
    print("\t   ", end = " ")
    for i in range(3):
        print(format(matrix2[0][i], "5.1f"), end = "")
    print("   ", end = "  ")
    for i in range(3):
        print(format(resultMatrix[0][i], "5.1f"), end = "")
    
    
    print()
    for i in range(3):
        print(format(matrix1[1][i], "5.1f"), end = "")
    print("\t  *", end = " ")
    for i in range(3):
        print(format(matrix2[1][i], "5.1f"), end = "")
    print("   =", end = "  ")
    for i in range(3):
        print(format(resultMatrix[1][i], "5.1f"), end = "")
    
    print()
    for i in range(3):
        print(format(matrix1[2][i], "5.1f"), end = "")
    print("\t   ", end = " ")
    for i in range(3):
        print(format(matrix2[2][i], "5.1f"), end = "")
    print("\t ", end = "")
    for i in range(3):
        print(format(resultMatrix[2][i], "5.1f"), end = "")

main()