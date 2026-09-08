from tkinter import *

class Grid:
    def __init__(self):
        window = Tk()
        window.title("8 x 8 Grid")

        self.canvas = Canvas(window, width= 275, height=275, bg="white")
        self.canvas.pack()
        self.xpos = 35
        self.ypos = 10

        for i in range(8):
            self.canvas.create_line(self.xpos, self.ypos, self.xpos, self.ypos + 265, tags="line")
            self.xpos += 30

        self.xpos = 10
        self.ypos = 35

        for i in range(8):
            self.canvas.create_line(self.xpos, self.ypos, self.xpos + 265, self.ypos, tags="line")
            self.ypos += 30

        window.mainloop()

Grid()
        