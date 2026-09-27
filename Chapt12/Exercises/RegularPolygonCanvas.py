from tkinter import *
import math

class RegularPolygonCanvas(Canvas):
    def __init__(self, container, width, height, n):
        super().__init__(container, width=width, height=height)
        center_x = width / 2
        center_y = height / 2
        radius = 0.42 * width
        self.draw(n, center_x, center_y, radius)


    def draw(self, n, center_x, center_y, radius):
        points = []
        for i in range(n):
            angle = ((2 * math.pi * i) / n) - math.radians(90)
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            points.extend([x, y])
        self.create_polygon(points)

class display:
    def __init__(self):
        window = Tk()
        window.title("g")

        for n in range(3, 9):
            RegularPolygonCanvas(window, width=150, height=150, n=n).pack(side=LEFT)

        window.mainloop()
