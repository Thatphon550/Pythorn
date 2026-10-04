def decimal_to_hex(value):
    if value < 16:
        if value >= 10:
            return chr(ord('A') + value - 10)
        else:
            return str(value)
    else:
        if value % 16 >= 10:
            return decimal_to_hex(value // 16) + chr(ord('A') + (value % 16) - 10)
        else:
            return decimal_to_hex(value // 16) + str(value % 16)

print(decimal_to_hex(415030))
