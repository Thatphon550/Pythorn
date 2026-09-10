from tkinter import *
import tkinter.messagebox

class ArrowKeys:
    def __init__(self):
        window = Tk()
        window.title("Arrow Keys")

        self.width = 500
        self.height = 250
        self.canvas = Canvas(window, width=self.width, height=self.height, bg="white")
        self.canvas.pack()

        self.x = 250
        self.y = 125

        self.dx = 25
        self.dy = 25

        self.canvas.bind("<Key>", self.move)
        self.canvas.focus_set()

        window.mainloop()

    def move(self, event):
        if not  0 <= self.x <= 500:
            tkinter.messagebox.showerror("Limit Error", "Exceeded boundaries")

        if not 0 <= self.y <= 250:
            tkinter.messagebox.showerror("Limit Error", "Exceeded boundaries")

        if event.keycode == 37:
            self.canvas.create_line(self.x, self.y, self.x - self.dx, self.y, tags="line")
            self.x -= self.dx
        elif event.keycode == 38:
            self.canvas.create_line(self.x, self.y, self.x, self.y - self.dy, tags="line")
            self.y -= self.dy
        elif event.keycode == 39:
            self.canvas.create_line(self.x, self.y, self.x + self.dx, self.y, tags="line")
            self.x += self.dx
        elif event.keycode == 40:
            self.canvas.create_line(self.x, self.y, self.x, self.y + self.dy, tags="line")
            self.y += self.dy



ArrowKeys()