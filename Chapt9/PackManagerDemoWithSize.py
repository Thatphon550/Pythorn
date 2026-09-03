from tkinter import *

class PackManagerDemoWithSize: 
    window = Tk()
    window.title("Pack Manager Demo 2")

    Label(window, text = "Blue", bg = "blue").pack(side = LEFT)
    Label(window, text = 'Red', bg = "red").pack(side = LEFT, fill=BOTH, expand=1)
    Label(window, text = 'Green', bg = "green").pack(side = LEFT, fill=BOTH)

    window.mainloop()

PackManagerDemoWithSize()