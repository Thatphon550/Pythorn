lst = eval(input("Enter a list of integers separated by commas: "))

for i, elem in enumerate(lst[::-1]):
    if i != len(lst) - 1:
        print(elem, end=", ")
    else:
        print(elem)