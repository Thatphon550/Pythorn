from tkinter import *


class FlashingText:
    def __init__(self):
        window = Tk()
        window.title("Flashing Text")

        self.canvas = Canvas(window, width= 250, height= 140)
        self.canvas.pack()

        self.visible = False
        self.flash()
        window.mainloop()

    def flash(self):
        if self.visible:
            self.canvas.delete("text")
            self.visible = False
        else:
            self.canvas.create_text(125, 70, text="Welcome",tags="text")
            self.visible = True

        self.canvas.after(250, self.flash)

FlashingText()