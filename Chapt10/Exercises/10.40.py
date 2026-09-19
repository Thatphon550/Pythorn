from tkinter import *
import tkinter.messagebox
import random
import time

class InsertionSort:
    def __init__(self):
        window = Tk()
        window.title("Insertion Sort Animation")

        self.lst = [i for i in range(1, 2000)]
        random.shuffle(self.lst)
        self.index = 0
        self.width = 1920
        self.canvas = Canvas(window, width=self.width, height=190, bg="white")
        self.canvas.pack()
        self.draw()
        frame = Frame(window)
        frame.pack()
        Button(frame, text="Step", command=self.iterate).pack(side=LEFT)
        Button(frame, text="Reset", command=self.reset).pack(side=LEFT)



        window.mainloop()

    def draw(self):
        div = self.width / len(self.lst)
        self.canvas.delete("all")
        for i in range(len(self.lst)):
            self.canvas.create_rectangle(10 + i * div, 190 - self.lst[i] * 0.08, 10 + (i + 1) * div, 190,
                                         fill = "#8C8C8C" if i == self.index - 1 else None, outline="#CDDB91")
            # self.canvas.create_text(10 + (i + 0.5) * div, 182 - self.lst[i],
            #                         text=self.lst[i], font=("Geist Mono", 10))
    def iterate(self):
        self.stop = False
        if self.index >= len(self.lst):
            tkinter.messagebox.showinfo("Finished", "The list has been sorted")
            return
        while self.index < len(self.lst) and not self.stop:
            currentElement = self.lst[self.index]
            k = self.index - 1
            while k >= 0 and self.lst[k] > currentElement:
                self.lst[k + 1] = self.lst[k]
                k -= 1
            self.lst[k + 1] = currentElement
            self.index += 1
            self.draw()
            self.canvas.after(1)
            self.canvas.update()

    def reset(self):
        self.stop = True
        self.canvas.delete("all")
        random.shuffle(self.lst)
        self.index = 0
        self.draw()

InsertionSort()
