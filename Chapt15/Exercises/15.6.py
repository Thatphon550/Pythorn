def m(i):
    if i == 1:
        return 1 / 2
    else:
        return i / (i + 1) + m(i - 1)

print(f"{m(int(input("Enter: an integer for i: ")))}")
