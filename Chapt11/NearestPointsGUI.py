import NearestPoints
from tkinter import *

RADIUS = 2

class NearestPointsGUI:
    def __init__(self):
        self.points = []
        window = Tk()
        window.title("Find Nearest Points")

        self.canvas = Canvas(window, width=400, height=200)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.addPoint)

        window.mainloop()

    def addPoint(self, event):
        if not self.isTooCloseToOtherPoints(event.x, event.y):
            self.addThisPoint(event.x, event.y)

    def addThisPoint(self, x, y):
        self.canvas.create_oval(x - RADIUS, y - RADIUS, x + RADIUS, y + RADIUS)
        self.points.append([x, y])

        if len(self.points) > 2:
            self.canvas.delete("line")
            p1, p2 = NearestPoints.nearestPoints(self.points)
            self.canvas.create_line(self.points[p1][0], self.points[p1][1],
                                    self.points[p2][0], self.points[p2][1], tags="line")

    def isTooCloseToOtherPoints(self, x, y):  
        for i in range(len(self.points)):
            if NearestPoints.distance(self.points[i][0], self.points[i][1], x, y) <= RADIUS + 2:
                return True

        return False
        
NearestPointsGUI()