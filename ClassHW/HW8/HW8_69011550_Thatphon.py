# Q1

def decimalToBinary(integer):
    if integer < 0:
        return "The number is negative"

    binaryStr = ""
    
    while integer > 0:
        if integer % 2 == 1:
            binaryStr = "1" + binaryStr
        else:
            binaryStr = "0" + binaryStr

        integer //= 2

    return binaryStr

def binaryToDecimal(binaryStr):
    sum = 0
    for i in range(0, len(binaryStr)):
        sum += int(binaryStr[i]) * (2 ** (len(binaryStr) - i - 1))

    return str(sum)


def main():
    num = int(input("Enter an integer input: "))
    binary = decimalToBinary(num)
    print(f"The binary is {binary}")
    print(f"Binary converted back to decimal is {binaryToDecimal(binary)}")

# main()

# Q2

text = str(input("Enter some text: "))
text = list(text)

textCount = 26 * [0]
for char in text:
    textCount[ord(char) - ord('a')] += 1

print("-- Character Frequency Table --")
for i, count in enumerate(textCount):
    if count:
        print(f"{chr(i + ord('a'))}:    {(count / len(text)) * 100:.2f}%")


# Q3

import turtle
import math

class Info:
    def __init__(self, char, percent):
        self.char = char
        self.percent = percent


def drawGraph(lst):
    width = 600
    scale = (width - 50) / len(lst)
    drawAxis(width)
    drawData(lst, scale)

def drawData(lst, scale):
    amplify = 1 if len(lst) == 1 else math.log10(len(lst) + 2) * 3
    turtle.teleport(-300, -200)
    for i in lst:
        turtle.forward(scale / 4)

        turtle.left(90)
        turtle.pendown()
        turtle.forward(i.percent * 4 * amplify)
        turtle.right(90)
        turtle.forward(scale / 2)
        turtle.right(90)
        turtle.forward(i.percent * 4 * amplify)
   
        turtle.left(90)
        turtle.penup() 
        turtle.left(180)
        turtle.forward(scale / 4)
        turtle.left(90)
        turtle.forward(30)
        turtle.write(i.char, font=("Arial", 12, "bold"))
        turtle.right(180)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(scale / 4)


        turtle.forward(scale / 4)


def drawAxis(width):
    turtle.teleport(-300, -200)
    turtle.forward(width)
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.right(150)
    turtle.forward(15)
    turtle.right(120)
    turtle.forward(15)
    turtle.right(120)
    turtle.forward(15)
    turtle.end_fill()

    turtle.teleport(-300, -200)
    turtle.setheading(90)
    turtle.forward(400)
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.right(150)
    turtle.forward(15)
    turtle.right(120)
    turtle.forward(15)
    turtle.right(120)
    turtle.forward(15)
    turtle.end_fill()
    turtle.teleport(0, 0)
    turtle.setheading(0)

def main():
    infoLst = []

    text = str(input("Enter some text: "))
    text = list(text)
    
    textCount = 26 * [0]
    for char in text:
        textCount[ord(char) - ord('a')] += 1

    for i in range(len(textCount)):
        if textCount[i]:
            infoLst.append(Info(chr(i + ord('a')), (textCount[i] / len(text) * 100)))


    turtle.speed(0)
    drawGraph(infoLst)
    turtle.done()

main()

# Q4

isbn = str(input("Enter the first 9 digits of an ISBN-10 as a string: "))

sumOfDigits = 0

for i in range(len(isbn)):
    sumOfDigits += int(isbn[i]) * (i + 1)

checkSum = sumOfDigits % 11
if checkSum == 10:
    checkSum = "X"

print(f"Your ISBN-10 number is {isbn}{checkSum}")