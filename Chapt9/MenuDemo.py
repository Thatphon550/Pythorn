from tkinter import *

class MenuDemo:
    def __init__(self):
        window = Tk()
        window.title("Menu Demo")

        menubar = Menu(window)
        window.config(menu = menubar)

        operationMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label = "Operation", menu = operationMenu)
        operationMenu.add_command(label = "Add", command=self.add)
        operationMenu.add_command(label = "Subtract", command=self.subtract)
        operationMenu.add_separator()
        operationMenu.add_command(label="Multiply", command=self.multiply)
        operationMenu.add_command(label = "Divide", command=self.divide)

        exitmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label = "Exit", menu=exitmenu)
        exitmenu.add_command(label= "Quit", command=window.quit)

        frame0 = Frame
