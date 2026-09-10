from tkinter import *

class Position:
    def __init__(self):
        window = Tk()
        window.title("Mouse Point")

        self.canvas = Canvas(window, width= 500, height=250, bg="white")
        self.canvas.pack()
        self.canvas.bind("<ButtonRelease-1>", self.showPos)

        window.mainloop()

    def showPos(self, event):
        self.canvas.delete("text")
        self.canvas.create_text(event.x, event.y, text=f"({event.x}, {event.y})", tags="text")

Position()