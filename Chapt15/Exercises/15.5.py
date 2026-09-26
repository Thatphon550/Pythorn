def m(i):
    if i == 1:
        return 1 / 3
    else:
        return i / (2 * i + 1) + m(i - 1)

for i in range(1, 11):
    print(f"m({i}) is {m(i)}")
