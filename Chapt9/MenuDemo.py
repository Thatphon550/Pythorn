from tkinter import *

class MenuDemo:
    def __init__(self):
        window = Tk()
        window.title("Menu Demo")

        menubar = Menu(window)
        window.config(menu = menubar)

        operationMenu = Menu(menubar)

        mainloop()