from tkinter import *
import tkinter.messagebox
import random

class SelectionSortAnimation:
    def __init__(self):
        window = Tk()
        window.title("Selection Sort Animation")

        self.index = 0
        self.lst = [i for i in range(1, 20)]
        random.shuffle(self.lst)

        self.canvas = Canvas(window, width=420, height=200)
        self.canvas.pack()
        self.draw()
        frame = Frame(window)
        frame.pack()

        Button(frame, text="Step", command=self.iterate).pack(side=LEFT)
        Button(frame, text="Reset", command=self.reset).pack(side=LEFT)

        window.mainloop()

    def draw(self):
        self.canvas.delete("all")
        div = 400 / len(self.lst)
        for i in range(len(self.lst)):
            self.canvas.create_rectangle(10 + i * div, 190 - self.lst[i] * 8, 10 + (i  + 1) * div, 190,
                                         fill = "#9E9E9E" if i == self.index - 1 else None)

            self.canvas.create_text(10 + (i + 0.5) * div, 182 - self.lst[i] * 8,
                                    text=self.lst[i], font=("Geist Mono", 10))

    def iterate(self):
        if self.index >= len(self.lst) - 1:
            tkinter.messagebox.showinfo("Finished", "The list is now sorted")
            return
        currentMin = self.lst[self.index]
        currentMinIndex = self.index
        for j in range(self.index + 1, len(self.lst)):
            if currentMin > self.lst[j]:
                currentMin = self.lst[j]
                currentMinIndex = j
        if currentMinIndex != self.index:
            self.lst[currentMinIndex] = self.lst[self.index]
            self.lst[self.index] = currentMin
        self.index += 1
        self.draw()

    def reset(self):
        self.canvas.delete("all")
        self.index = 0
        random.shuffle(self.lst)
        self.draw()

SelectionSortAnimation()
