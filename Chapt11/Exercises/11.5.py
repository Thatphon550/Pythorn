def addMatrix(a, b):
    sumMatrix = []

    for row in range(len(a)):
        sumMatrix.append([])
        for column in range(len(a)):
            sumMatrix[row].append([])
            sumMatrix[row][column] = a[row][column] + b[row][column]

    return sumMatrix

def main():
    line1 = str(input("Enter matrix1: "))
    line2 = str(input("Enter matrix2: "))

    matrix1 = []
    line1 = line1.split()  
    for row in range(3):
        matrix1.append([eval(x) for x in line1[row * 3:row * 3 + 3]])

    matrix2 = []
    line2 = line2.split()
    for row in range(3):
        matrix2.append([eval(x) for x in line2[row * 3: row * 3 + 3]])

    resultMatrix = addMatrix(matrix1, matrix2)

 
    print("The matrices are added as follows: ")
    for i in range(3):
        print(format(matrix1[0][i], "5.1f"), end = "")
    print("\t   ", end = " ")
    for i in range(3):
        print(format(matrix2[0][i], "5.1f"), end = "")
    print("\t  ", end = " ")
    for i in range(3):
        print(format(resultMatrix[0][i], "5.1f"), end = "")


    print()
    for i in range(3):
        print(format(matrix1[1][i], "5.1f"), end = "")
    print("\t  +", end = " ")
    for i in range(3):
        print(format(matrix2[1][i], "5.1f"), end = "")
    print("\t=", end = "  ")
    for i in range(3):
        print(format(resultMatrix[1][i], "5.1f"), end = "")

    print()
    for i in range(3):
        print(format(matrix1[2][i], "5.1f"), end = "")
    print("\t   ", end = " ")
    for i in range(3):
        print(format(matrix2[2][i], "5.1f"), end = "")
    print("\t  ", end = " ")
    for i in range(3):
        print(format(resultMatrix[2][i], "5.1f"), end = "")
main()