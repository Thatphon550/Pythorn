from tkinter import *
import tkinter.messagebox

class TicTacToe(Canvas):
    def __init__(self, container, width, height):
        super().__init__(container, width = width, height = height)

        self.over = False
        self.pos = [[None for _ in range(3)] for _ in range(3)]
        self.player = 1
        self.bind("<Button-1>", self.place)

    def place(self, event):
        if self.over:
            tkinter.messagebox.showerror("Error", "Error: The Game is Already Completed")
            return
        if 0 <= event.x <= 100:
            col = 0
        elif 100 <= event.x <= 200:
            col = 1
        elif 200 <= event.x <= 300:
            col = 2

        if 0 <= event.y <= 100:
            row = 0
        elif 100 <= event.y <= 200:
            row = 1
        elif 200 <= event.y <= 300:
            row = 2

        if self.pos[row][col]:
            tkinter.messagebox.showerror("Error", "Error: Grid already occupied")
            return

        self.create_rectangle(100 * col, 100 * row, 100 * (col + 1), 100 * (row + 1),
                              fill="red" if self.player else "blue")
        self.pos[row][col] = "X" if self.player else "O"

        if self.checkWin(row, col):
            string = "Player "
            string += "1 won" if self.player else "2 won"
            self.over = True
            tkinter.messagebox.showinfo("Game Over", string)

        if self.player:
            self.player = 0
        else:
            self.player = 1

    def checkWin(self, row, col):
        return self.checkHorizontal(row) or self.checkVertical(col) or self.checkDiagonal()

    def checkHorizontal(self, row):
        return self.pos[row][0] == self.pos[row][1] == self.pos[row][2]

    def checkVertical(self, col):
        return self.pos[0][col] == self.pos[1][col] == self.pos[2][col]

    def checkDiagonal(self):
        return (self.pos[0][0] == self.pos[1][1] == self.pos[2][2] or
             self.pos[0][2] == self.pos[1][1] == self.pos[2][0]) and self.pos[1][1] != None

class Game:
    def __init__(self):
        window = Tk()
        window.title("TicTacToe")
        a = TicTacToe(window, height=300, width=300)
        a.pack()
        window.mainloop()

Game()
