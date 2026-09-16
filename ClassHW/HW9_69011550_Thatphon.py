# Q1

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

# Q2

from tkinter import *
from tkinter import messagebox

class HabitTracker():
    def __init__(self):
        window = Tk()
        window.title("Habit Tracker")

        Label(window, text="Habit Tracker", width = 35,height=3, font=("Arial", 15), bg="#C9C9C9").grid(row=1,column=1, columnspan=3)
        Label(window, text="Habit", font=("Arial", 12), height=2).grid(row=2, column=1)


        self.entry = StringVar()
        Entry(window, textvariable=self.entry, justify=RIGHT, width=40).grid(row=2, column=2)

        Button(window, text="Add", command=self.addHabit).grid(row=2, column=3)
        self.habitList = []
        self.habitFrame = Frame(window)
        self.habitFrame.grid(row=3, column=1, columnspan=3)

        Button(window, text="Complete", width= 9, command=self.complete).grid(row=4, column=1)
        Button(window, text="Uncomplete", width= 9, command=self.uncomplete).grid(row=4, column=2)
        Button(window, text="Delete",  width= 9, command=self.delete).grid(row=4, column=3)

        Label(window, text="Today's Progress: ").grid(row=5, column=1,columnspan=3)
        window.mainloop()

    def complete(self):
        pass

    def uncomplete(self):
        pass

    def delete(self):
        pass

    def addHabit(self):
        self.habitList.append(self.entry.get())
        self.update()

    def update(self):
        Checkbutton(self.habitFrame, text=self.habitList[len(self.habitList) - 1]).pack(padx=5)


HabitTracker()


# Q3

from tkinter import *

class CircleDisplay():
    def __init__(self):
        window = Tk()
        window.title("tk")
        self.canvas = Canvas(window, width=400, height=270, bg="white")
        self.canvas.pack()
        self.id = 0
        self.radius = 17

        self.canvas.bind("<Button-1>", self.drawCircle)
        self.canvas.bind("<Button-3>", self.deleteCircle)
        window.mainloop()

    def deleteCircle(self, event):
        items = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
        for id in items:
            self.canvas.delete(id)

    def drawCircle(self, event):
        self.canvas.create_oval(event.x - self.radius, event.y - self.radius, event.x + self.radius, event.y + self.radius, fill="white", tags=f"{self.id}")
        self.id += 1

CircleDisplay()
