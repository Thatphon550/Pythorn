from ConnectFour import ConnectFour
import tkinter.messagebox
from tkinter import *

class connect_four_gui(ConnectFour):
    def __init__(self):
        super().__init__()
        window = Tk()
        window.title("Connect Four")

        self.canvas = Canvas(window, width=350, height=300)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.process_mouse_input)
        Button(window, text="Start Over", command=self.reset).pack()
        self.draw()

        window.mainloop()

    def draw_grid(self):
        for row in range(6):
            for col in range(7):
                self.canvas.create_rectangle(
                    50 * col + 3, 50 * row + 3,
                    50 * (col + 1) - 3, 50 * (row + 1) - 3,
                    fill="#A3A3A3"
                )

    def process_mouse_input(self, event):
        if self.yellow_win or self.red_win:
            tkinter.messagebox.showerror("Error", "The Game has been completed!")
            return
        on_grid, exceed_row = False, False
        if 3 <= event.x <= 47:
            if not self.place(0):
                exceed_row = True
            else:
                on_grid = True
        elif 53 <= event.x <= 97:
            if not self.place(1):
                exceed_row = True
            else:
                on_grid = True
        elif 103 <= event.x <= 147:
            if not self.place(2):
                exceed_row = True
            else:
                on_grid = True
        elif 153 <= event.x <= 197:
            if not self.place(3):
                exceed_row = True
            else:
                on_grid = True
        elif 203 <= event.x <= 247:
            if not self.place(4):
                exceed_row = True
            else:
                on_grid = True
        elif 253 <= event.x <= 297:
            if not self.place(5):
                exceed_row = True
            else:
                on_grid = True
        elif 303 <= event.x <= 347:
            if not self.place(6):
                exceed_row = True
            else:
                on_grid = True
        if exceed_row:
            tkinter.messagebox.showwarning("Warning", "Row is already full!")
            return
        if on_grid:
            self.draw()
            if self.check():
                self.red_win = True if self.player == 1 else False
                self.yellow_win = True if self.player == -1 else False
                tkinter.messagebox.showinfo(
                    "Game Over!",
                    f"{"Red" if self.player == 1 else "Yellow"} Player Won!"
                    )
            self.player = -self.player

    def draw(self):
        self.canvas.delete("all")
        self.draw_grid()
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col]:
                    self.canvas.create_oval(
                        50 * col + 8, 50 * row + 8,
                        50 * (col + 1) - 4, 50 * (row + 1) - 4,
                        fill="#E3AFAF" if self.board[row][col] == 1 else "#F5EFC1",
                        outline=None
                    )
                    self.canvas.create_oval(
                        50 * col + 6, 50 * row + 6,
                        50 * (col + 1) - 6, 50 * (row + 1) - 6,
                        fill="#D11B1B" if self.board[row][col] == 1 else "#EDD939",
                        outline=None
                    )

    def reset(self):
        self.board = [[None for _ in range(7)] for _ in range(6)]
        self.player = 1
        self.red_win = False
        self.yellow_win = False
        self.canvas.delete("all")
        self.draw()

connect_four_gui()
