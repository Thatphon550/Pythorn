from tkinter import *

class GeometricFigure:
    def __init__(self):
        window = Tk()
        window.title("Radiobuttons and Checkbuttons")

        self.canvas = Canvas(window, width=300, height=75, bg="white")
        self.canvas.pack()

        frame = Frame(window)
        frame.pack()

        self.shape = IntVar()
        Radiobutton(frame, text="Rectangle", variable=self.shape, value=1, command=self.drawShape).grid(column=1, row=1)
        Radiobutton(frame, text="Oval", variable=self.shape, value=2, command=self.drawShape).grid(column=2, row=1)
        self.filled_var = IntVar()
        Checkbutton(frame, text="Filled", variable=self.filled_var, command=self.toggle_fill).grid(column=3, row=1)

        window.mainloop()

    def drawShape(self):
        self.canvas.delete("all")

        fill_color = "red" if self.filled_var.get() == 1 else ""

        if self.shape.get() == 1:
            self.canvas.create_rectangle(30, 15, 270, 60, tags="current_shape", fill=fill_color)
        elif self.shape.get() == 2:
            self.canvas.create_oval(30, 15, 270, 60, tags="current_shape", fill=fill_color)

    def toggle_fill(self):
        if self.filled_var.get() == 1:
            self.canvas.itemconfig("current_shape", fill = "red")
        else:
            self.canvas.itemconfig("current_shape", fill = "")


GeometricFigure()

