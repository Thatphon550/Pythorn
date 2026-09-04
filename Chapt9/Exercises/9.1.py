from tkinter import *
import tkinter.messagebox

class Panel:
    def __init__(self):
        window = Tk()
        window.title("Moving Ball")

        self.width = 200
        self.canvas = Canvas(window, bg="white", width=200, height=200)
        self.canvas.pack()
        self.x = 100
        self.y = 100
        self.dx = 10
        self.dy = 10

        self.canvas.create_oval(self.x - 10, self.y - 10, self.x + 10, self.y + 10, fill="red", tags="circle")

        frame = Frame(window)
        frame.pack()
        btnLeft = Button(frame, text="Left", command=self.left)
        btnLeft.pack(side=LEFT)
        btnUp = Button(frame, text="Up", command=self.up)
        btnUp.pack(side=LEFT)
        btnRight = Button(frame, text="Right", command=self.right)
        btnRight.pack(side=LEFT)
        btnDown = Button(frame, text="Down", command=self.down)
        btnDown.pack(side=LEFT)

        window.mainloop()

    def left(self):
        if 0 < self.x < 200 and 0 < self.y < 200:
            self.canvas.move("circle", -self.dx, 0)
            self.x -= self.dx
        else:
            self.y = 100
            self.x = 100
            self.canvas.delete("circle")
            self.canvas.create_oval(self.x - 10, self.y - 10, self.x + 10, self.y + 10, fill="red", tags="circle")
            tkinter.messagebox.showwarning("Limit exceeded", "You exceeded the boundaries")

    def up(self):
        if 0 < self.x < 200 and 0 < self.y < 200:
            self.canvas.move("circle", 0, -self.dy)
            self.y -= self.dy
        else:
            self.y = 100
            self.x = 100
            self.canvas.delete("circle")
            self.canvas.create_oval(self.x - 10, self.y - 10, self.x + 10, self.y + 10, fill="red", tags="circle")
            tkinter.messagebox.showwarning("Limit exceeded", "You exceeded the boundaries")

    def right(self):
        if 0 < self.x < 200 and 0 < self.y < 200:
            self.canvas.move("circle", self.dx, 0)
            self.x += self.dx
        else:
            self.y = 100
            self.x = 100
            self.canvas.delete("circle")
            self.canvas.create_oval(self.x - 10, self.y - 10, self.x + 10, self.y + 10, fill="red", tags="circle")
            tkinter.messagebox.showwarning("Limit exceeded", "You exceeded the boundaries")

    def down(self):
        if 0 < self.x < 200 and 0 < self.y < 200:
            self.canvas.move("circle", 0, self.dy)
            self.y += self.dy
        else:
            self.y = 100
            self.x = 100
            self.canvas.delete("circle")
            self.canvas.create_oval(self.x - 10, self.y - 10, self.x + 10, self.y + 10, fill="red", tags="circle")
            tkinter.messagebox.showwarning("Limit exceeded", "You exceeded the boundaries")

Panel()
        