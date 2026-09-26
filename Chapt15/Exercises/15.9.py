def reverse_display(value):
    if len(value) == 1:
        return value
    else:
        return value[-1] + reverse_display(value[:-1])

print(reverse_display("abcd"))
