from tkinter import *

class RotatingMessage:
    def __init__(self):
        window = Tk()
        window.title("Rotating Message")

        
        self.canvas = Canvas(window, width=300, height= 140)
        self.canvas.create_text(150, 70, text="Programming is fun", tags="text", font = 15)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.leftClick)
        self.canvas.bind("<Button-3>", self.rightClick)

        window.mainloop()

    def leftClick(self, event):
        self.canvas.delete("text")
        self.canvas.create_text(150, 70, text="Programming is fun", tags="text", font = 15)

    def rightClick(self, event):
        self.canvas.delete("text")
        self.canvas.create_text(150, 70, text="It is fun to program", tags="text", font = 15)
        
RotatingMessage()