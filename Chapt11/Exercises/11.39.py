from tkinter import *

class ConsecutiveFour:
    def __init__(self):
        window = Tk()
        window.title("Consecutive Four")

        self.frame = Frame(window)
        self.frame.pack()

        self.cells = []
        for i in range(6):
            self.cells.append([])
            for j in range(9):
                self.cells[i].append(StringVar())

        for i in range(6):
            for j in range(7):
                Entry(self.frame, width=3, justify=LEFT, textvariable=self.cells[i][j], font=("Geist Mono", 10)).grid(
                    row = i, column=j)

        Button(window, text="Solve", command=self.solve).pack()
        window.mainloop()

    def solve(self):
        if self.check_row():
            return
        if self.check_column():
            return
        if self.check_leftup_rightdown():
            return
        if self.check_leftdown_rightup():
            return

    def check_row(self):
        for row in range(len(self.cells)):
            self.consec_cells = [[row, 0]]
            consecutive = 1
            for col in range(len(self.cells[row]) - 1):
                if eval(self.cells[row][col].get()) == eval(self.cells[row][col + 1].get()):
                    consecutive += 1
                    self.consec_cells.append([row, col + 1])
                    if consecutive >= 4:
                        self.highlight_btn()
                        return True
                else:
                    consecutive = 1
                    self.consec_cells = [[row, col + 1]]

    def check_column(self):
        for col in range(len(self.cells[0])):
            self.consec_cells = [[0, col]]
            consecutive = 1
            for row in range(len(self.cells) - 1):
                if eval(self.cells[row][col].get()) == eval(self.cells[row + 1][col].get()):
                    consecutive += 1
                    self.consec_cells.append([row + 1, col])
                    if consecutive >= 4:
                        self.highlight_btn()
                        return True
                else:
                    consecutive = 1
                    self.consec_cells = [[row + 1, col]]

    def check_leftup_rightdown(self):
        for row in range(len(self.cells)):
            for col in range(len(self.cells[row])):
                self.consec_cells = [[row, col]]
                consecutive = 1
                r, c = row, col
                while r < len(self.cells) - 1 and c < len(self.cells[0]) - 1:
                    if eval(self.cells[r][c].get()) == eval(self.cells[r + 1][c + 1].get()):
                        consecutive += 1
                        self.consec_cells.append([r + 1, c + 1])
                        if consecutive >= 4:
                            self.highlight_btn()
                            return True
                    else:
                        consecutive = 1
                        self.consec_cells = [[r + 1, c + 1]]
                    r, c = r + 1, c + 1

    def check_leftdown_rightup(self):
        for row in range(len(self.cells)):
            for col in range(7):
                self.consec_cells = [[row, col]]
                consecutive = 1
                r, c = row, col
                while r > 0 and c < 7 - 1:
                    if eval(self.cells[r][c].get()) == eval(self.cells[r - 1][c + 1].get()):
                        consecutive += 1
                        self.consec_cells.append([r - 1, c + 1])
                        if consecutive >= 4:
                            self.highlight_btn()
                            return True
                    else:
                        consecutive = 1
                        self.consec_cells = [[r - 1, c + 1]]
                    r, c = r - 1, c + 1

    def highlight_btn(self):
        print(self.consec_cells)
        for entry in self.frame.winfo_children():
            entry.destroy()
        for i in range(6):
            for j in range(7):
                if [i, j] in self.consec_cells:
                    print(i, j)
                Entry(self.frame, width=3, justify=LEFT, textvariable=self.cells[i][j],
                      bg = "yellow" if [i, j] in self.consec_cells else None, font=("Geist Mono", 10)).grid(
                          row=i, column=j)

ConsecutiveFour()
