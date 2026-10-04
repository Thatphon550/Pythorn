def binary_to_decimal(binstr):
    return bin_to_dec_helper(binstr, 0)

def bin_to_dec_helper(binstr, index):
    if index == len(binstr) - 1:
        if int(binstr[index]) % 2 == 1:
            return 1
        else:
            return 0
    else:
        if int(binstr[index]) % 2 == 1:
            return bin_to_dec_helper(binstr, index + 1) + 2 ** (len(binstr) - index - 1)
        else:
            return bin_to_dec_helper(binstr, index + 1)

print(binary_to_decimal("1010101101010110101011111011010011"))
