def decimal_to_bin(decimal):
    if decimal == 0:
        return 0
    if decimal == 1:
        return "1"
    if decimal % 2 == 1:
        return decimal_to_bin(decimal // 2) + "1"
    else:
        return decimal_to_bin(decimal // 2) + "0"

for n in range(100):
    print(decimal_to_bin(n))
