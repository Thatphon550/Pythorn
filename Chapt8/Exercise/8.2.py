str_1 = str(input("Enter the first string: "))
str_2 = str(input("Enter the second string: "))

if str_1.find(str_2) != -1:
    print("found")
else:
    print("not found")