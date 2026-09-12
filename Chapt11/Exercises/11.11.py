def constructMatrix(binaryCode):
    binaryCode = list(binaryCode)
    matrix = []
    for i in range(3):
        matrix.append(["T" if eval(j) else "H" for j in binaryCode[i * 3: i * 3 + 3]])

    for row in matrix:
        for col in row:
            print(col, end =" ")
        print()

def decimalToBinary(num):
    string = ""
    while num > 0:
        if num % 2:
            string = "1" + string
        else:
            string = "0" + string
        num //= 2
    
    return formatBinary(string)

def formatBinary(string):
    while len(string) < 9:
        string = "0" + string
    return string

def main():
    num = int(input("Enter a number between 0 and 511: "))
    if not 0 <= num <= 511:
        print("Number out of range")
    else:
        binaryCode = decimalToBinary(num)
        constructMatrix(binaryCode)

main()
