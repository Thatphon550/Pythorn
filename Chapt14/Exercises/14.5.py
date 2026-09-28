from tkinter import *
import tkinter.filedialog
import os.path

class Histogram:
    def __init__(self):
        window = Tk()
        window.title("Occurence of Letters")

        self.canvas = Canvas(window, width=400, height=190, bg="white")
        self.canvas.pack()

        frame1 = Frame(window)
        frame1.pack()

        self.file_name_var = StringVar()
        Label(frame1, text="Enter a filename: ").pack(side=LEFT)
        Entry(frame1, textvariable=self.file_name_var, width=30).pack(side=LEFT)
        Button(frame1, text="Browse", command=self.browse_file).pack(side=LEFT)
        Button(frame1, text="Show Result", command=self.show_result).pack(side=LEFT)
        window.mainloop()

    def browse_file(self):
        self.file_name_var.set(tkinter.filedialog.askopenfilename())

    def show_result(self):
        if os.path.isfile(self.file_name_var.get()):
            infile = open(self.file_name_var.get(), "r")
            count = count_alphabet(infile)
            self.draw_graph(count)
            infile.close()

    def draw_graph(self, count):
        div = 380 / len(count)
        for i in range(len(count)):
            percent = (count[i] / sum(count)) * 100
            self.canvas.create_rectangle(
                10 + (i * div), 180 - percent * 12,
                10 + (i + 1) * div, 180
            )
            self.canvas.create_text(
                10 + (i + 0.5) * div, 185,
                text=chr(ord('a') + i), font=("Geist Mono", 9)
            )

def count_alphabet(infile):
    count = [0 for _ in range(26)]
    for ch in infile.read():
        try:
            count[ord(ch.lower()) - ord('a')] += 1
        except IndexError:
            continue
    return count


Histogram()
