try:
    number = eval(input("Enter a number: "))
    print(f"The number is entered as {number}")
except NameError as ex:
    print(f"Exception: {ex}")
