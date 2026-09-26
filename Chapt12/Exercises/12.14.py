from tkinter import *

class BarChart(Canvas):
    def __init__(self, parent, data, width = 400, height = 300):
        super().__init__(parent, width=width, height=height)
        div = (width - 40) / len(data)
        for i in range(len(data)):
            info = data[i]
            self.create_rectangle(
                20 + (i * div), height - 20 - info[0] * 4,
                20 + (i + 1) * div, height - 20,
                fill=info[2]
            )
            self.create_text(
                20 + (i + 0.5) * div, height - 10,
                text=info[1]
            )


class Display:
    def __init__(self):
        window = Tk()
        window.title("BarChart Reusable Class")
        data = [
            [40, "CS", "red"], [30, "IS", "blue"], [50, "IT", "yellow"]
        ]
        self.chart = BarChart(window, data)
        self.chart.pack()

        window.mainloop()

Display()
