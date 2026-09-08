from tkinter import *

class Pyramid:
    def __init__(self):
        window = Tk()
        window.title("Pyramid")

        text = Text(window, wrap="word")
        text.pack()
        for i in range(1, 12):
            text.insert(END, " " * int(12-i))
            for j in range(1, i + 1):
                text.insert(END, f"{j} ")

            text.insert(END,"\n")


        window.mainloop()
        
Pyramid()