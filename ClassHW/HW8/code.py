# Q1



def decimalToBinary(integer):
    if integer < 0:
        return "The number is negative"

    binaryStr = ""
    
    while integer > 0:
        if integer % 2 == 1:
            binaryStr = "1" + binaryStr
        else:
            binaryStr = "0" + binaryStr

        integer //= 2

    return binaryStr

def binaryToDecimal(binaryStr):
    sum = 0
    for i in range(0, len(binaryStr)):
        sum += int(binaryStr[i]) * (2 ** (len(binaryStr) - i - 1))

    return str(sum)


for num in range(1, 101):
    binary = decimalToBinary(num)
    print(f"\nThe binary for {num} is {binary}")
    integer = binaryToDecimal(binary)
    print(f"The decimal for {binary} is {integer}")