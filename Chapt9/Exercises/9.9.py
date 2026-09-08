from tkinter import *
from random import randint

def getRandomColor():
    color = "#"
    for j in range(6):
        color += toHexChar(randint(0, 15))
    return color

def toHexChar(hexValue):
    if 0 <= hexValue <= 9:
        return chr(hexValue + ord('0'))
    else:
        return chr(hexValue - 10 + ord('A'))

class Score:
    def __init__(self, name, percent):
        self.name = name
        self.percent = percent

class BarChart:
    def __init__(self):
        window = Tk()
        window.title("Bar Chart")

        self.canvas = Canvas(window, width=350, height=160)
        self.canvas.pack()

        
        self.canvas.create_line(0, 145, 350, 145, tags="line")
        self.barWidth = 70

        project = Score("Project", 20)
        quiz = Score("Quiz", 10)
        midterm = Score("Midterm", 30)
        final = Score("Final", 40)
        scoreLst = [project, quiz, midterm, final]

        self.x = 20
        
        for score in scoreLst:
            
            self.y = (score.percent / 100) * 140
            scoreColor = getRandomColor()
            self.canvas.create_text(self.x + self.barWidth / 2, 130 - self.y, text=f"{score.name} -- {score.percent}%")
            self.canvas.create_rectangle(self.x, 140 - self.y, self.x + self.barWidth, 145, fill=scoreColor)
            self.x += 80

        window.mainloop()
        
BarChart()