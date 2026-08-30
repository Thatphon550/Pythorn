isbn = str(input("Enter the first 12 digits of an ISBN-13 as a string: "))

subtract = 0
for i in range(1, 13):
    if i % 2 == 1:
        subtract += int(isbn[i - 1])
    else:
        subtract += int(isbn[i - 1]) * 3

checkSum = 10 - (subtract % 10)
if checkSum == 10:
    isbn += "0"
else:
    isbn += str(checkSum)
    
print(isbn)
    