def m(i):
    if i == 1:
        return 1
    else:
        return (1 / i) + m(i - 1)

print(m(1999))
