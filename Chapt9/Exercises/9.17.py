from tkinter import *

class RacingCar:
    def __init__(self):
        window = Tk()
        window.title("Racing Car")

        self.canvas = Canvas(window, width=250, height=100, bg="white")
        self.canvas.pack()

        self.refX = 0
        self.refY = 100

        self.dx = 5

        self.drawCar()
        self.animate()
        

        window.mainloop()


    def setSpeed(self, event):
        if event.keycode == 37:
            self.dx -= 1
        elif event.keycode == 39:
            self.dx += 1
    def animate(self):
        while True:
            self.canvas.bind("<Key>", self.setSpeed)
            self.canvas.focus_set()

            self.refX += self.dx
            self.canvas.move("car", self.dx, 0)
            self.canvas.after(5)
            self.canvas.update()
            if self.refX > 270:
                self.canvas.delete("car")
                self.refX = -40
                self.drawCar()

    

    def drawCar(self):
        self.canvas.create_oval(self.refX + 10, self.refY - 10, self.refX + 20, self.refY, tags="car", fill="black")
        self.canvas.create_oval(self.refX + 30, self.refY - 10, self.refX + 40, self.refY, tags="car", fill="black")
        self.canvas.create_rectangle(self.refX, self.refY - 20, self.refX + 50, self.refY - 10, fill="red", tags="car")
        self.canvas.create_polygon(self.refX + 10, self.refY - 20, self.refX + 20, self.refY - 30,
                                    self.refX + 30, self.refY - 30, self.refX + 40, self.refY - 20, tags="car")
                    
                    
RacingCar()