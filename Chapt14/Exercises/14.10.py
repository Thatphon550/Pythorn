from tkinter import *
import random

class HangMan:
    def __init__(self):
        window = Tk()
        window.title("Hangman")

        self.words_list = ["programming", "python", "computer", "software"]
        self.canvas = Canvas(window, width=400, height=350)
        self.canvas.pack()
        self.word = self.words_list[random.randint(0, len(self.words_list) - 1)]
        self.answer = [None for _ in range(len(self.word))]
        self.missed_letters = []
        self.lost = False
        self.win = False

        self.draw_post()
        self.draw_word()
        self.canvas.bind("<Key>", self.process_key)
        self.canvas.focus_set()

        window.mainloop()

    def process_key(self, event):
        if self.lost or self.win:
            if event.keycode == 13:
                self.reset()
            return
        if not len(str(event.char)):
            return
        if not ord('a') <= ord(event.char.lower()) <= ord('z'):
            return

        ch = event.char.lower()
        if ch in self.word:
            if self.answer.count(ch) < self.word.count(ch):
                for i in range(len(self.word)):
                    if self.word[i] == ch and self.answer[i]:
                        continue
                    elif self.word[i] == ch:
                        self.answer[i] = ch
                        self.check_win()
                        break
            else:
                if self.missed(ch):
                    return
        else:
            if self.missed(ch):
                return

        if not self.win:
            self.draw_word()

    def draw_hangman(self):
        count = len(self.missed_letters)
        if count == 1:
            self.canvas.create_oval(
                175, 51, 225, 100
            )
        elif count == 2:
            self.canvas.create_line(
                180, 90, 140, 130
            )
    def check_win(self):
        for ch in self.answer:
            if not ch:
                self.win = False
                return
        self.win = True
        self.finished_screen()


    def reset(self):
        self.word = self.words_list[random.randint(0, len(self.words_list) - 1)]
        self.answer = [None for _ in range(len(self.word))]
        self.missed_letters.clear()
        self.lost = False
        self.win = False

        self.canvas.delete("all")
        self.draw_post()
        self.draw_word()

    def missed(self, ch):
        self.missed_letters.append(ch)
        self.draw_hangman()
        if len(self.missed_letters) >= 7:
            self.lost = True
            self.finished_screen()
            return True

    def finished_screen(self):
        string = ""
        for ch in self.word:
            string += ch
        self.canvas.delete("text")
        self.canvas.create_text(
            255, 310,
            text=f"The word is: {string}",
            font=14, tags = "text"
            )
        self.canvas.create_text(
            255, 330,
            text= "To continue the game, press ENTER",
            font = 14,
            tags = "text"
        )

    def draw_post(self):
        self.canvas.create_arc(
            30, 320, 120, 380,
            start=0, extent=180,
            tags="post"
            )
        self.canvas.create_line(75, 320, 75, 25, tags="post")
        self.canvas.create_line(75, 25, 200, 25, tags="post")
        self.canvas.create_line(200, 25, 200, 50, tags="post")

    def draw_word(self):
        self.canvas.delete("text")
        self.canvas.create_text(
            255, 310,
            text=f"Guess a word: {self.get_text_display()}",
            font=14, tags = "text"
            )
        if self.missed_letters:
            string = "Missed letters: "
            for ch in self.missed_letters:
                string += ch
            self.canvas.create_text(
                255, 330,
                text=string,
                font = 14,
                tags = "text"
            )

    def get_text_display(self):
        string = ""
        for ch in self.answer:
            if ch:
                string += ch
            else:
                string += "*"
        return string


HangMan()
