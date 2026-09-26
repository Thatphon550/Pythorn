def reverseDisplay(value):
    if len(str(value)) == 1:
        return str(value)
    return str(value)[-1] + reverseDisplay(str(value)[:-1])

print(reverseDisplay(1234))
