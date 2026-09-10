from tkinter import *

class MovingCircle:
    def __init__(self):
        window = Tk()
        window.title("Moving Circle")

        self.canvas = Canvas(window, width=250, height=140, bg="white")
        self.canvas.pack()

        
        self.x = 125
        self.y = 70
        self.radius = 20
        self.canvas.create_oval(self.x - self.radius, self.y - self.radius, 
                                self.x + self.radius, self.y + self.radius, tags="circle")

        self.canvas.bind("<Key>", self.move)
        self.canvas.focus_set()

        window.mainloop()

    def move(self, event):
        if event.keycode == 37:
            self.x -= 10
            self.canvas.delete("circle")
            self.canvas.create_oval(self.x - self.radius, self.y - self.radius, 
                                    self.x + self.radius, self.y + self.radius, tags="circle")
        elif event.keycode == 38:
            self.y -= 10
            self.canvas.delete("circle")
            self.canvas.create_oval(self.x - self.radius, self.y - self.radius, 
                                    self.x + self.radius, self.y + self.radius, tags="circle")
        elif event.keycode == 39:
            self.x += 10
            self.canvas.delete("circle")
            self.canvas.create_oval(self.x - self.radius, self.y - self.radius, 
                                    self.x + self.radius, self.y + self.radius, tags="circle")
        elif event.keycode == 40:
            self.y += 10
            self.canvas.delete("circle")
            self.canvas.create_oval(self.x - self.radius, self.y - self.radius, 
                                    self.x + self.radius, self.y + self.radius, tags="circle")

MovingCircle()