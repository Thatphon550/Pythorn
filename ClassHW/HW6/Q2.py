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
