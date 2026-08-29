def decimalToBinary(value):
    binary = ""
    exit = False
    
    while value >= 1 and not exit:
        binary += str(int(value % 2))
        value /= 2
        if value == 1:
            exit = True
        
    return binary[::-1]

print(decimalToBinary(25))