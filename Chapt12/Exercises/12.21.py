from RegularPolygonCanvas import RegularPolygonCanvas
from tkinter import *

class n_sided_polygons(Canvas):
    def __init__(self):
        window = Tk()
        window.title("n-sided Polygons")
        self.n = 5
        self.poly = RegularPolygonCanvas(window, width=250, height=250, n = self.n)
        self.poly.pack()

        Button(window, text="-1", command=self.decrease).pack(side=LEFT)
        Button(window, text="1", command=self.increase).pack(side=LEFT)
        window.mainloop()

    def decrease(self):
        if self.n == 3:
            return
        self.n -= 1
        self.poly.delete("all")
        self.poly.draw(self.n, 125, 125, 0.42 * 250)

    def increase(self):
        self.n += 1
        self.poly.delete("all")
        self.poly.draw(self.n, 125, 125, 0.42 * 250)

n_sided_polygons()
