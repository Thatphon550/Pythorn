from tkinter import *
import tkinter.messagebox

class Phone:
    def __init__(self):
        window = Tk()
        window.title("KMITL Phone")

        self.number = StringVar()
        Label(window, height=1, textvariable=self.number, font = ("Arial", 17)).grid(row=1,column=1,columnspan=3, sticky=E)

        Button(window, width=5, height=1, text="1", command=self.one, font = ("Arial", 17)).grid(column=1, row=2)
        Button(window, width=5, height=1, text="2", command=self.two, font = ("Arial", 17)).grid(column=2, row=2)
        Button(window, width=5, height=1, text="3", command=self.three, font = ("Arial", 17)).grid(column=3, row=2)
        Button(window, width=5, height=1, text="4", command=self.four, font = ("Arial", 17)).grid(column=1, row=3)
        Button(window, width=5, height=1, text="5", command=self.five, font = ("Arial", 17)).grid(column=2, row=3)
        Button(window, width=5, height=1, text="6", command=self.six, font = ("Arial", 17)).grid(column=3, row=3)
        Button(window, width=5, height=1, text="7", command=self.seven, font = ("Arial", 17)).grid(column=1, row=4)
        Button(window, width=5, height=1, text="8", command=self.eight, font = ("Arial", 17)).grid(column=2, row=4)
        Button(window, width=5, height=1, text="9", command=self.nine, font = ("Arial", 17)).grid(column=3, row=4)
        Button(window, width=5, height=1, text="*", command=self.asterisk, font = ("Arial", 17)).grid(column=1, row=5)
        Button(window, width=5, height=1, text="0", command=self.zero, font = ("Arial", 17)).grid(column=2, row=5)
        Button(window, width=5, height=1, text="#", command=self.hashtag, font = ("Arial", 17)).grid(column=3, row=5)
        frame = Frame(window)
        frame.grid(column=1, row=6, columnspan=3)
        Button(frame, width=8, height=1, text="Talk", command=self.talk, font = ("Arial", 17)).grid(column=1, row=1)
        Button(frame, width=8, height=1, text="<", command=self.delete, font = ("Arial", 17)).grid(column=2, row=1)



        window.mainloop()

    def one(self):
        string = self.number.get() + "1"
        self.number.set(string)

    def two(self):
        string = self.number.get() + "2"
        self.number.set(string)

    def three(self):
        string = self.number.get() + "3"
        self.number.set(string)

    def four(self):
        string = self.number.get() + "4"
        self.number.set(string)

    def five(self):
        string = self.number.get() + "5"
        self.number.set(string)

    def six(self):
        string = self.number.get() + "6"
        self.number.set(string)

    def seven(self):
        string = self.number.get() + "7"
        self.number.set(string)

    def eight(self):
        string = self.number.get() + "8"
        self.number.set(string)

    def nine(self):
        string = self.number.get() + "9"
        self.number.set(string)

    def asterisk(self):
        string = self.number.get() + "*"
        self.number.set(string)

    def zero(self):
        string = self.number.get() + "0"
        self.number.set(string)

    def hashtag(self):
        string = self.number.get() + "#"
        self.number.set(string)

    def talk(self):
        tkinter.messagebox.showinfo("Making a call", f"Dialing {self.number.get()}")

    def delete(self):
        string = self.number.get()
        self.number.set(string[:len(string) - 1])
Phone()
