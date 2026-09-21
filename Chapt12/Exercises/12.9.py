from Rectangle2D import Rectangle2D
from tkinter import *

class DisplayRectangle(Canvas):
    def __init__(self, container, width, height):
        super().__init__(container, width=width, height=height)

class TwoRectangles:
    def __init__(self):
        window = Tk()
        window.title("Two Rectangles")

        window.mainloop()
