class ConnectFour:
    def __init__(self):
        self.board = [[None for _ in range(7)] for _ in range(6)]
        self.player = 1
        self.red_win = False
        self.yellow_win = False

    def place(self, col):
        if self.red_win or self.yellow_win:
            return 
        if self.board[0][col]:
            return False
        for row in range(len(self.board) - 1):
            if not self.board[len(self.board) - 1][col]:
                self.board[len(self.board) - 1][col] = self.player
                return True
            if self.board[row + 1][col]:
                self.board[row][col] = self.player
                return True

    def check(self):
        return self.check_col() or self.check_row() \
            or self.check_leftdown_rightup() or self.check_rightdown_leftup()

    def check_row(self):
        for row in range(len(self.board)):
            consecutive = 1
            for col in range(len(self.board[row]) - 1):
                if (self.board[row][col] == self.board[row][col + 1]) and self.board[row][col]:
                    consecutive += 1
                    if consecutive >= 4:
                        return True
                else:
                    consecutive = 1
        return False

    def check_col(self):
        for col in range(len(self.board[0])):
            consecutive = 1
            for row in range(len(self.board) - 1):
                if (self.board[row][col] == self.board[row + 1][col]) and self.board[row][col]:
                    consecutive += 1
                    if consecutive >= 4:
                        return True
                else:
                    consecutive = 1
        return False

    def check_rightdown_leftup(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                r, c = row, col
                consecutive = 1
                while r >= 1 and c >= 1:
                    if self.board[r][c] == self.board[r - 1][c - 1] and self.board[r][c]:
                        consecutive += 1
                        if consecutive >= 4:
                            return True
                    else:
                        consecutive = 1
                    r, c = r - 1, c - 1
        return False

    def check_leftdown_rightup(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                r, c = row, col
                consecutive = 1
                while c <= len(self.board) - 1 and r >= 1:
                    if self.board[r][c] == self.board[r - 1][c + 1] and self.board[r][c]:
                        consecutive += 1
                        if consecutive >= 4:
                            return True
                    else:
                        consecutive = 1
                    r, c = r - 1, c + 1
        return False
