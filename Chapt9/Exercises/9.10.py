from tkinter import *
import math

class Score:
    def __init__(self, name, percent, fill):
        self.name = name
        self.percent = percent
        self.fill = fill

class PieChart:
    def __init__(self):
        window = Tk()
        window.title("Pie Chart")

        self.canvas = Canvas(window, bg="white", width = 500, height=500)
        self.canvas.pack()
        self.x = 250
        self.y = 250
        self.radius = 220

        project = Score("Project", 20, "red")
        quiz = Score("Quiz", 10, "blue")
        midterm = Score("Midterm", 30, "green")
        final = Score("Final", 40, "orange")
        self.scoreLst = [project, quiz, midterm, final]

        self.start = 0
        for score in self.scoreLst:
            self.extent = ((score.percent / 100) * 360)

            self.canvas.create_arc(self.x - self.radius, self.y - self.radius, self.x + self.radius, 
                self.y + self.radius, start = self.start, extent = self.extent if self.extent != 360 else 5, fill = score.fill)

            self.middleAngle = self.start + (self.extent / 2)
            self.radians = math.radians(self.middleAngle)
            self.labelRadius = 0.6 * self.radius
            self.labelX = self.x + self.labelRadius * math.cos(self.radians)
            self.labelY = self.y - self.labelRadius * math.sin(self.radians)

            self.canvas.create_text(self.labelX, self.labelY, text=f"{score.name} -- {score.percent}%", fill = "white", font=("Arial", 11, "bold"))
            

            self.start += self.extent

        window.mainloop()

PieChart()