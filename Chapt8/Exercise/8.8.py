def binaryToDecimal(binaryString):
    decimal = 0
    power = len(binaryString) - 1
    for digit in binaryString:
        decimal = decimal + int(digit) * (2 ** power)
        power -= 1
        
    return decimal

def main():
    while True:
        binary = str(input("Enter binary number: "))
        print(f"The number for {binary} is {binaryToDecimal(binary)}")
    
main()