isbn = str(input("Enter the first 9 digits of an ISBN-10 as a string: "))

checkSum = 0
for i in range(1, 10):
    checkSum += int(isbn[i - 1]) * i
    
checkSum %= 11
if checkSum == 10:
    isbn += "X"
else:
    isbn += str(checkSum)

print(isbn)