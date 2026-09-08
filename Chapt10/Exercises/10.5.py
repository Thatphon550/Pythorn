numString = str(input("Enter ten numbers: "))

lst1 = numString.split(' ')
lst2 = []

for elem in lst1:
    if elem not in lst2:
        lst2.append(elem)

print("The distinct numbers are ", end ="")
for elem in lst2:
    print(elem, end = " ")