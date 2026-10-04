from tkinter import *
from tkinter import messagebox
import math

class KochSnowflake:
    def __init__(self):
        window = Tk()
        window.title("Koch snowflake")

        self.width = 200
        self.height = 250

        self.canvas = Canvas(window, width=self.width, height=self.height)
        self.canvas.pack()


        frame1 = Frame(window)
        frame1.pack()
        self.order = StringVar()
        Label(frame1, text="Enter an order ").pack(side=LEFT)
        Entry(frame1, width=15, textvariable=self.order).pack(side=LEFT)
        Button(frame1, text="Display", command=self.display).pack(side=LEFT)


        window.mainloop()

    def display(self):
        try:
            order = int(self.order.get())
        except ValueError:
            messagebox.showerror("Invalid order", "Please enter a whole number.")
            return

        # A negative order never reaches the base case -> RecursionError.
        # Above ~7 the line count (3 * 4^n) makes Tkinter freeze.
        if order < 0 or order > 7:
            messagebox.showerror("Invalid order", "Order must be between 0 and 7.")
            return

        self.canvas.delete("line")

        side = self.width - 20
        p2 = [10, 190]
        p3 = [self.width - 10, 190]
        # Place the top vertex so the triangle is equilateral.
        p1 = [self.width / 2, 190 - side * math.sqrt(3) / 2]

        self.displaySnowFlake(order, p1, p2, p3)

    def displaySnowFlake(self, order, p1, p2, p3):
        self.drawKochLine(order, p1, p2)
        self.drawKochLine(order, p2, p3)
        self.drawKochLine(order, p3, p1)

    def drawKochLine(self, order, p1, p2):
        if order == 0:
            self.drawLine(p1, p2)
            return

        a, b = self.segment(p1, p2)
        dx = b[0] - a[0]
        dy = b[1] - a[1]

        sin60 = math.sqrt(3) / 2
        peak = [a[0] + dx * 0.5 - dy * sin60,
                a[1] + dx * sin60 + dy * 0.5]

        self.drawKochLine(order - 1, p1, a)
        self.drawKochLine(order - 1, a, peak)
        self.drawKochLine(order - 1, peak, b)
        self.drawKochLine(order - 1, b, p2)

    def segment(self, p1, p2):
        p3 = 2 * [0]
        p4 = 2 * [0]
        p3[0] = (2 * p1[0] + p2[0]) / 3
        p3[1] = (2 * p1[1] + p2[1]) / 3

        p4[0] = (p1[0] + 2 * p2[0]) / 3
        p4[1] = (p1[1] + 2 * p2[1]) / 3

        return p3, p4

    def drawLine(self, p1, p2):
        self.canvas.create_line(
            p1[0], p1[1], p2[0], p2[1], tags="line"
        )

KochSnowflake()
