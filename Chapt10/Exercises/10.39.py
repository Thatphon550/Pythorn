from tkinter import *
import tkinter.messagebox
import random

class PointGame:
    def __init__(self):
        window = Tk()
        window.title("24-Point Game")

        self.imageList = []
        for i in range(1, 53):
            self.imageList.append(PhotoImage(file="Exercises/card/" + str(i) + ".gif"))
        Button(window, text="Refresh", command=self.refresh).pack()

        frame = Frame(window)
        frame.pack()

        self.labelList = []
        for i in range(4):
            self.labelList.append(Label(frame, image=self.imageList[i]))
            self.labelList[i].pack(side=LEFT)

        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, text="Enter an expression: ").pack(side=LEFT)

        self.expression = StringVar()
        Entry(frame1, textvariable=self.expression, justify=LEFT).pack(side=LEFT)

        Button(frame1, text="Verify", command=self.verify).pack(side=LEFT)

        window.mainloop()

    def verify(self):
        num = []
        for i in range(len(self.labelList)):
            n = int(self.labelList[i]["image"][7:])
            num.append(n % 13 if n % 13 else 13)
        if eval(self.expression.get()) == 24:
            tkinter.messagebox.showinfo("Correct", "You got it")
        else:
            tkinter.messagebox.showerror("Incorrect", f"{self.expression.get()} is not 24")


    def refresh(self):
        random.shuffle(self.imageList)
        for i in range(4):
            self.labelList[i]["image"] = self.imageList[i]

PointGame()
