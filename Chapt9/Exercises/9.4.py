from tkinter import *

class DisplayRectangle:
    def __init__(self):
        window = Tk()
        window.title("Display Rectangles")

        self.canvas = Canvas(window, width=500, height=330, bg="white")
        self.canvas.pack()

        
        self.width = 200
        self.height = 40


        for i in range(0, 160, 8):
            self.canvas.create_rectangle(170 - i, 155 - i, 330 + i, 165 + i, tags="rect")
        window.mainloop()

DisplayRectangle()