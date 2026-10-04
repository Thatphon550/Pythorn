def hex_to_decimal(hexstr):
    return hex_to_decimal_helper(hexstr, 0)

def hex_to_decimal_helper(hexstr, index):
    decimal = 0
    if index == len(hexstr) - 1:
        if hexstr[index].isalpha():
            return ord(hexstr[index]) - ord('A') + 10
        else:
            return int(hexstr[index])
    else:
        if hexstr[index].isalpha():
            decimal += (ord(hexstr[index]) - ord('A') + 10) * 16 ** (len(hexstr) - index - 1) \
            + hex_to_decimal_helper(hexstr, index + 1)
        else:
            decimal += int(hexstr[index]) * 16 ** (len(hexstr) - index - 1) \
            + hex_to_decimal_helper(hexstr, index + 1)
        return decimal

print(hex_to_decimal("19"))
