from tkinter import *
import tkinter.messagebox
import random

class LinearAnimation():
    def __init__(self):
        window = Tk()
        window.title("Linear Search Animation")

        self.canvas = Canvas(window, width=500, height=270)
        self.canvas.pack()
        frame = Frame(window)
        frame.pack()
        self.i = 0
        self.lst = [x for x in range(1, 20)]
        random.shuffle(self.lst)
        
        Label(frame, text="Enter a key (in float)", font=("JetBrains Mono", 11)).pack(side=LEFT)
        self.key = IntVar()
        self.d = 5
        Entry(frame, textvariable=self.key, justify=RIGHT, width=3, font=("JetBrains Mono", 11)).pack(side=LEFT)
        Button(frame, text="Step", command=self.iterate).pack(side=LEFT)
        Button(frame, text="Reset", command=self.reset).pack(side=LEFT)

        self.found = False
        self.display()

        window.mainloop()

    def reset(self):
        random.shuffle(self.lst)
        self.i = 0
        self.canvas.delete("all")
        self.found = False
        self.display()
    

    def iterate(self):
        if not self.found:
            target = self.key.get()
            self.i += 1
            self.display()
            if self.lst[self.i] == target:
                self.found = True
                tkinter.messagebox.showinfo("Found", f"Found Target: {self.key.get()}")
        else:
            tkinter.messagebox.showerror("Error!", "Target Already Found!")

    def display(self):
        self.canvas.delete("all")
        self.canvas.create_line(20, 260, 480, 260, tags="line")
        div = 460 / 19
        for j in range(len(self.lst)):
            height = self.lst[j] * 10
            fill = "red" if self.i == j else None
            self.canvas.create_rectangle(20 + j * div, 260 - height, 20 + (j + 1) * div, 260, fill=fill )
            self.canvas.create_text(20 + j * div + div / 2, 260 - height - 8, 
                                    text=self.lst[j], font=("Spline Sans Mono", 11))

LinearAnimation()
