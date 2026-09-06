from tkinter import *

class CheckerBoard:
    def __init__(self):
        window = Tk()
        window.title("Displaying a Checkerboard")

        self.canvas = Canvas(window, width=400, height=400, bg="white")
        self.canvas.pack()

        self.width = 50
        self.height = 50

        self.rows = 8
        self.columns = 8

        for row in range(1, self.rows + 1):
            for column in range(1, self.columns + 1):
                if row % 2 == 1:
                    if column % 2 == 0:
                        self.fill = "black"
                    else:
                        self.fill = "white"
                else:
                    if column % 2 == 1:
                        self.fill = "black"
                    else:
                        self.fill = "white"

                self.canvas.create_rectangle(self.width * (row - 1), self.height * (column - 1), self.width * row, self.height * column, fill=self.fill, outline="white")

        window.mainloop()
CheckerBoard()
