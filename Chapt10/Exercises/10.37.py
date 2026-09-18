from tkinter import *
import tkinter.messagebox

def binarySearch(lst, key):
    high = len(lst) - 1
    low = 0

    while high >= low:
        mid = (high + low) // 2
        if lst[mid] > key:
            low = mid + 1
        elif lst[mid] == key:
            return mid
        else:
            high = mid - 1

    return -low - 1

class BinarySearch:
    def __init__(self):
        window = Tk()
        window.title("Binary Search Animation")

        self.canvas = Canvas(window, width=420, height=200)
        self.canvas.pack()

        self.lst = [x for x in range(1, 20)]
        frame = Frame(window)
        frame.pack()
        self.key = IntVar()
        self.high = len(self.lst) - 1
        self.low = 0
        self.draw()

        Label(frame, text="Enter a key (in float):").pack(side=LEFT)
        Entry(frame, textvariable=self.key, width=3, justify=RIGHT).pack(side=LEFT)

        Button(frame, text="Step", command=self.iterate).pack(side=LEFT)
        Button(frame, text="Reset", command=self.reset).pack(side=LEFT)


        window.mainloop()

    def draw(self):
        self.canvas.delete("all")
        div = 400 / len(self.lst)
        for i in range(len(self.lst)):
            fill = None
            if self.low <= self.lst[i] <= self.high + 1:
                fill = "#F0FA9B"
            if self.lst[i] == self.key.get():
                fill = "#56CC45"
            self.canvas.create_rectangle(10 + i * div, 190 - self.lst[i] * 8,
                                         10 + (i + 1) * div, 190, fill=fill)
            self.canvas.create_text(10 + (i + 0.5) * div, 190 - self.lst[i] * 8 - 8,
                                    text=self.lst[i], font=("JetBrains Mono", 10))

    def iterate(self):
        if self.high < self.low:
            return
        mid = (self.high + self.low) // 2
        if self.lst[mid] > self.key.get():
            self.high = mid - 1
        elif self.lst[mid] == self.key.get():
            tkinter.messagebox.showinfo("Found", f"Found {self.key.get()} at index {mid}")
        else:
            self.low = mid + 1
        self.draw()

    def reset(self):
        self.canvas.delete("all")
        self.high = len(self.lst) - 1
        self.low = 0
        self.key.set(0)
        self.draw()

BinarySearch()
