from Circle2D import Circle2D
from tkinter import *

class Display(Canvas):
    def __init__(self, container, width, height):
        super().__init__(container, width=width, height=height)

    def displayCircle(self, c1: Circle2D, c2: Circle2D):
        self.create_oval(c1.getX() - c1.getRadius(), c1.getY() - c1.getRadius(),
                         c1.getX() + c1.getRadius(), c1.getY() + c1.getRadius())
        self.create_text(c1.getX(), c1.getY(), text="c1")
        self.create_oval(c2.getX() - c2.getRadius(), c2.getY() - c2.getRadius(),
                         c2.getX() + c2.getRadius(), c2.getY() + c2.getRadius())
        self.create_text(c2.getX(), c2.getY(), text="c2")

        self.create_text(150, 20, text="Two circles intersect" if c1.overlaps(c2) else "Two circles don't intersect")

class TwoCircles:
    def __init__(self):
        window = Tk()
        window.title("Two Circles")

        self.canvas = Display(window, width=300, height=200)
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        self.x1, self.y1, self.r1 = DoubleVar(), DoubleVar(), DoubleVar()
        self.x2, self.y2, self.r2 = DoubleVar(), DoubleVar(), DoubleVar()

        Label(frame, text="C1 Center x: ").grid(row=1, column=1)
        Entry(frame, textvariable=self.x1, justify=RIGHT, width=5).grid(row=1, column=2)
        Label(frame, text="  C2 Center x: ").grid(row=1, column=3)
        Entry(frame, textvariable=self.x2, justify=RIGHT, width=5).grid(row=1, column=4)

        Label(frame, text="C1 Center Y: ").grid(row=2, column=1)
        Entry(frame, textvariable=self.y1,justify=RIGHT, width=5).grid(row=2, column=2)
        Label(frame, text="  C2 Center Y: ").grid(row=2, column=3)
        Entry(frame, textvariable=self.y2,justify=RIGHT, width=5).grid(row=2, column=4)

        Label(frame, text="C1 Radius: ").grid(row=3, column=1)
        Entry(frame, textvariable=self.r1,justify=RIGHT, width=5).grid(row=3, column=2)
        Label(frame, text="  C2 Radius: ").grid(row=3, column=3)
        Entry(frame, textvariable=self.r2,justify=RIGHT, width=5).grid(row=3, column=4)

        Button(frame, text="Redraw Circles", command=self.draw).grid(row=4, column=2, columnspan=2)

        window.mainloop()

    def draw(self):
        self.canvas.delete("all")
        self.c1 = Circle2D(self.x1.get(), self.y1.get(), self.r1.get())
        self.c2 = Circle2D(self.x2.get(), self.y2.get(), self.r2.get())
        self.canvas.displayCircle(self.c1, self.c2)

TwoCircles()
