# Q1

def time24hourTo12hour(string):
    hours = int(string[0:2])
    minutes = int(string[3:5])
    
    if hours >= 12:
        hours %= 12
        time = "PM"
    else:
        time = "AM"
        
    return f"{hours}:{minutes} {time}"

def main():
    print(time24hourTo12hour("23:24"))
    print(time24hourTo12hour("05:25"))
    print(time24hourTo12hour("11:59"))
        
main()

# Q2

import turtle as t

def calendar_of_2026(month):
    
    startDate = 4
    
    
    sumDays = 0
    
    for i in range(1, month + 1):
        if i == 1:
            totalDays = 31
        elif i == 2:
            totalDays = 28
            sumDays += 31
        elif i == 3: 
            totalDays = 31
            sumDays += 28
        elif i == 4:
            totalDays = 30
            sumDays += 31
        elif i == 5:
            totalDays = 31
            sumDays += 30
        elif i == 6:
            totalDays = 30
            sumDays += 31
        elif i == 7:
            totalDays = 31
            sumDays += 30
        elif i == 8:
            totalDays = 31
            sumDays += 31
        elif i == 9:
            totalDays = 30
            sumDays += 31
        elif i == 10:
            totalDays = 31
            sumDays += 30
        elif i == 11:
            totalDays = 30
            sumDays += 31
        elif i == 12:
            totalDays = 31
            sumDays += 30
        
    startMonth = (sumDays + startDate) % 7
    
    drawCalendar(startMonth, month, totalDays)

        
def drawCalendar(startMonth, month, totalDays):
    drawHeader(month)
    drawBody(startMonth, totalDays, month)

def drawHeader(month):
    t.teleport(-175, 180)
    t.forward(105)
    t.right(90)
    t.penup()
    t.forward(28)
    if month == 1:
        t.write("January 2026", font=("Verdana", 14, "normal"))
    elif month == 2:
        t.write("February 2026", font=("Verdana", 14, "normal"))
    elif month == 3:
        t.write("March 2026", font=("Verdana", 14, "normal"))
    elif month == 4:
        t.write("April 2026", font=("Verdana", 14, "normal"))
    elif month == 5:
        t.write("May 2026", font=("Verdana", 14, "normal"))
    elif month == 6:
        t.write("June 2026", font=("Verdana", 14, "normal"))
    elif month == 7:
        t.write("July 2026", font=("Verdana", 14, "normal"))
    elif month == 8:
        t.write("August 2026", font=("Verdana", 14, "normal"))
    elif month == 9:
        t.write("September 2026", font=("Verdana", 14, "normal"))
    elif month == 10:
        t.write("October 2026", font=("Verdana", 14, "normal"))
    elif month == 11:
        t.write("November 2026", font=("Verdana", 14, "normal"))
    elif month == 12:
        t.write("December 2026", font=("Verdana", 14, "normal"))
    t.right(180)
    t.forward(28)
    t.right(90)
    t.pendown()
    t.forward(245)
    t.right(90)
    t.forward(35)
    t.right(90)
    t.forward(350)
    t.right(90)
    t.forward(35)
    t.right(180)
    t.forward(35)

def getRow(month):
    if month == 1 or month == 2 or month == 4 or month == 5 or month == 6 or month == 7 or month == 9 or month == 10 or month == 12:
        return 6
    elif month == 3 or month == 8 or month == 11:
        return 7

def drawBody(startDate, totalDays, month):
    rows = getRow(month)
    columns = 7
    day = 1
    started = False
    
    for row in range(1, rows + 1):
        for column in range(1, columns + 1):
            if row == 1:  
                t.forward(35)
                if column == 1:
                    x = t.xcor()
                    y = t.ycor()
                t.left(90)
                t.forward(15)
                t.penup()
                t.left(90)
                t.forward(5)
                if column == 1:
                    t.write("Mo", font=("Verdana", 13, "normal"))
                elif column == 2:
                    t.write("Tu", font=("Verdana", 13, "normal"))
                elif column == 3:
                    t.write("We", font=("Verdana", 13, "normal"))
                elif column == 4:
                    t.write("Th", font=("Verdana", 13, "normal"))
                elif column == 5:
                    t.write("Fr", font=("Verdana", 13, "normal"))
                elif column == 6:
                    t.write("Sa", font=("Verdana", 13, "normal"))
                elif column == 7:
                    t.write("Su", font=("Verdana", 13, "normal"))
                t.right(180)
                t.forward(5)
                t.pendown()
                t.left(90)
                t.forward(35)
                t.left(90)
                t.forward(35)
                t.right(180)
            elif row == 2:

                if column == startDate or (column == 7 and startDate == 0):
                    started = True
                if not started:
                    t.forward(35)
                    if column == 1:
                        x = t.xcor()
                        y = t.ycor()
                    t.left(90)
                    t.forward(15)
                    t.penup()
                    t.left(90)
                    t.forward(5)
                    
                    t.right(180)
                    t.forward(5)
                    t.pendown()
                    t.left(90)
                    t.forward(35)
                    t.left(90)
                    t.forward(35)
                    t.right(180)
                elif started: #started
                    t.forward(35)
                    if column == 1:
                        x = t.xcor()
                        y = t.ycor()
                    t.left(90)
                    t.forward(15)
                    t.penup()
                    t.left(90)
                    t.forward(5)
                    t.write(f"{day}", font=("Verdana", 13, "normal"))  
                    t.right(180)
                    t.forward(5)
                    t.pendown()
                    t.left(90)
                    t.forward(35)
                    t.left(90)
                    t.forward(35)
                    t.right(180)
                    day += 1
            else: # not row 2
                t.forward(35)
                if column == 1:
                    x = t.xcor()
                    y = t.ycor()
                t.left(90)
                t.forward(15)
                t.penup()
                t.left(90)
                t.forward(5)
                if day <= totalDays:
                    t.write(f"{day}", font=("Verdana", 13, "normal"))  
                t.right(180)
                t.forward(5)
                t.pendown()
                t.left(90)
                t.forward(35)
                t.left(90)
                t.forward(35)
                t.right(180)
                day += 1
        t.teleport(x, y)
        t.setheading(270)
            
def main():
    t.speed(0)
    calendar_of_2026(12)
    t.done()
    
main()

# Q4

def getText(num):
    if num < 0 or num > 999:
        return "I don't know"
    
    if len(str(num)) >= 1:
        if num % 10 == 0 and num != 10:
            digit1 = "zero"
        elif num % 10 == 1:
            digit1 = "one"
        elif num % 10 == 2:
            digit1 = "two"
        elif num % 10 == 3:
            digit1 = "three"
        elif num % 10 == 4:
            digit1 = "four"
        elif num % 10 == 5:
            digit1 = "five"
        elif num % 10 == 6:
            digit1 = "six"
        elif num % 10 == 7:
            digit1 = "seven"
        elif num % 10 == 8:
            digit1 = "eight"
        elif num % 10 == 9:
            digit1 = "nine"
        elif num == 10:
            return "ten"

        if len(str(num)) >= 2:
            num2 = num // 10

                
            if num2 % 10 == 1 and num < 100:
                if num == 11:
                    return "eleven"
                elif num == 12:
                    return "twelve"
                elif num == 13:
                    return "thirteen"
                elif num ==  15:
                    return "fifteen"
                elif num == 18:
                    return "eighteen"
                
                return digit1 + "teen"
                
            elif num2 % 10 == 2:
                digit2 = "twenty"
            elif num2 % 10 == 3:
                digit2 = "thirty"
            elif num2 % 10 == 4:
                digit2 = "forty"
            elif num2 % 10 == 5:
                digit2 = "fifty"
            elif num2 % 10 == 6:
                digit2 = "sixty"
            elif num2 % 10 == 7:
                digit2 = "seventy"
            elif num2 % 10 == 8:
                digit2 = "eighty"
            elif num2 % 10 == 9:
                digit2 = "ninety"
            
            
            if len(str(num)) >= 3:
                if num == 100:
                    return "one hundred"
                num3 = num // 100
                if num3 % 100  == 1:
                    digit3 = "one hundred"
                elif num3 == 2:
                    digit3 = "two hundred"
                elif num3 == 3:
                    digit3 = "three hundred"
                elif num3 == 4:
                    digit3 = "four hundred"
                elif num3 == 5:
                    digit3 = "five hundred"
                elif num3 == 6:
                    digit3 = "six hundred"
                elif num3 == 7:
                    digit3 = "seven hundred"
                elif num3 == 8:
                    digit3 = "eight hundred"
                elif num3 == 9:
                    digit3 = "nine hundred"
                    
                if num2 % 10 == 1:
                    if num % 10 == 1:
                        digit2 = "eleven"
                    elif num % 10 == 2:
                        digit2 = "twelve"
                    elif num % 10 == 3:
                        digit2 = "thirteen"
                    elif num % 10 ==  5:
                        digit2 = "fifteen"
                    elif num % 10 == 8:
                        digit2 = "eighteen"
                    elif num % 10 == 0:
                        digit2 = "ten"
                    else:
                        digit2 = digit1 + "teen"
                    return f"{digit3} and {digit2}"
                
                if num % 100 == 0:
                    return f"{digit3}"
                
                if 1 <= num % 100 <= 9:
                    return f"{digit3} and {digit1}"
                
                if num % 10 == 0:
                    return f"{digit3} and {digit2}"
                
                return f"{digit3} and {digit2} {digit1}"
               
            
            if num % 10 == 0 and num < 100:
                return f"{digit2}"
            return f"{digit2} {digit1}"
             
        return f"{digit1}"
        
    
    

def main():
    number = eval(input("Enter a number: "))
    print(getText(number))
    
main()

# Q5

amount = eval(input("Enter an integer amount of money in Thai Baht: "))


remaining = amount
count1000 = 0
count500 = 0
count100 = 0
count50 = 0
count20 = 0
count10 = 0
count5 = 0
count2 = 0
count1 = 0

while remaining > 0:
    if remaining >=1:
        
        if remaining >= 2:
            
            if remaining >= 5:
                
                if remaining >= 10:
                    
                    if remaining >= 20:
                        
                        if remaining >= 50:
                            
                            if remaining >= 100:
                                
                                if remaining >= 500:
                                    
                                    if remaining >= 1000:
                                        remaining -= 1000
                                        count1000 += 1
                                        continue
                                
                                    remaining -= 500
                                    count500 += 1
                                    continue
                            
                                remaining -= 100
                                count100 += 1
                                continue
                            
                            remaining -= 50
                            count50 += 1
                            continue
                        
                        remaining -= 20
                        count20 += 1
                        continue
                    
                    remaining -= 10
                    count10 += 1
                    continue
                
                remaining -= 5
                count5 += 1
                continue
            
            remaining -= 2
            count2 += 1
            continue
        
        remaining -= 1
        count1 += 1
        continue
    
    

if count1 >= 1 or count2 >= 1 or count5 >= 1 or count10 >= 1 or count20 >= 1 or count50 >= 1 or count100 >= 1 or count500 >= 1 or count1000 >= 1:
        
    print("\nYou get:")    
    
    if count2 >= 1 or count5 >= 1 or count10 >= 1 or count20 >= 1 or count50 >= 1 or count100 >= 1 or count500 >= 1 or count1000 >= 1:
            
        if count5 >= 1 or count10 >= 1 or count20 >= 1 or count50 >= 1 or count100 >= 1 or count500 >= 1 or count1000 >= 1:
                
            if count10 >= 1 or count20 >= 1 or count50 >= 1 or count100 >= 1 or count500 >= 1 or count1000 >= 1:
                    
                if count20 >= 1 or count50 >= 1 or count100 >= 1 or count500 >= 1 or count1000 >= 1:
                        
                    if count50 >= 1 or count100 >= 1 or count500 >= 1 or count1000 >= 1:
                            
                        if count100 >= 1 or count500 >= 1 or count1000 >= 1:
                                
                            if count500 >= 1 or count1000 >= 1:
                                    
                                if count1000 >= 1:
                                    if count1000 == 1:
                                        print(f"    {count1000} 1000-Baht note")
                                    elif count1000 > 1:
                                        print(f"    {count1000} 1000-Baht notes")
                                            
                                if count500 == 1:
                                    print(f"    {count500} 500-Baht note")
                                elif count500 > 1:
                                    print(f"    {count500} 500-Baht notes")
                                        
                            if count100 == 1:
                                print(f"    {count100} 100-Baht note")
                            elif count100 > 1:
                                print(f"    {count100} 100-Baht notes")
                                    
                        if count50 == 1:
                            print(f"    {count50} 50-Baht note")
                        elif count50 > 1:
                            print(f"    {count50} 50-Baht notes")
                        
                    if count20 == 1:
                        print(f"    {count20} 20-Baht note")
                    elif count20 > 1:
                        print(f"    {count20} 20-Baht notes")
                            
                if count10 == 1:
                    print(f"    {count10} 10-Baht coin")
                elif count10 > 1:
                    print(f"    {count10} 10-Baht coins")
                        
            if count5 == 1:
                print(f"    {count5} 5-Baht coin")
            elif count5 > 1:
                print(f"    {count5} 5-Baht coins")
                    
        if count2 == 1:
            print(f"    {count2} 2-Baht coin")
        elif count2 > 1:
            print(f"    {count2} 2-Baht coins")
                
    if count1 == 1:
        print(f"    {count1} 1-Baht coin")
    elif count1 > 1:
        print(f"    {count1} 1-Baht coins")
                                
# Q6

def reverseDigit(n):
    return int(str(n)[::-1])


def main():
    print(reverseDigit(5831))
    
main()
