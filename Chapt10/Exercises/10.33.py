from tkinter import *
import random

class DisplayHistogram:
    def __init__(self):
        window = Tk()
        window.title("Count of Each Letter")

        self.canvas = Canvas(window, width= 400, height=300)
        self.canvas.pack()

        Button(window, text="Display Histogram", command=self.display).pack()
        window.mainloop()

    def display(self):
        self.canvas.delete("all")
        randomChars = [random.randint(0, 25) for _ in range(1000)]
        count = [0 for _ in range(26)]
        for char in randomChars:
            count[char] += 1

        print(count)
        self.canvas.create_line(20, 280, 380, 280)
        div = 360 / 26
        for i, char in enumerate(count):
            height = 45 * (char / 1000 * 100)
            self.canvas.create_rectangle(20 + i * div, 280 - height, 20 + (i + 1) * div, 280)
            self.canvas.create_text(20 + i * div + (div / 2), 290, text = f"{chr(i + ord('a'))}", font=("JetBrains Mono", 9))
        

DisplayHistogram()