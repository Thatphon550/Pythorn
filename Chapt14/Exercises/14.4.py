from tkinter import *
from tkinter.filedialog import askopenfilename

class OccurenceOfLetters:
    def __init__(self):
        window = Tk()
        window.title("Occurence of Letters")

        frame1 = Frame(window)
        frame1.pack()
        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text = Text(frame1, width=40, height=10,
                         wrap=WORD, yscrollcommand=scrollbar.set)
        self.text.pack()
        scrollbar.config(command=self.text.yview)
        Label(window, text="Enter a filename: ").pack(side=LEFT)
        self.filename = StringVar()
        Entry(window, textvariable=self.filename).pack(side=LEFT)
        Button(window, text="Browse", command=self.open_file).pack(side=LEFT)
        Button(window, text="Show Result", command=self.show_result).pack(side=LEFT)

        window.mainloop()

    def show_result(self):
        self.text.delete("1.0", END)
        char_count = [0 for _ in range(26)]
        infile = open(self.filename.get(), "r")
        for ch in infile.read():
            try:
                char_count[ord(ch.lower()) - ord('a')] += 1
            except:
                continue
        for i in range(len(char_count)):
            self.text.insert(
                END, f"{chr(i + ord('a'))} appears {char_count[i]} times\n"
                )

    def open_file(self):
        self.filename.set(askopenfilename())

OccurenceOfLetters()
