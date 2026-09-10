from tkinter import *

class Fan:
    def __init__(self):
        window = Tk()
        window.title("Fan")

        self.canvas = Canvas(window, width=500, height=500, bg="white")
        self.canvas.pack()
        self.radius = 220

        self.start = 0
    
        for _ in range(4):
            self.canvas.create_arc(250 - self.radius, 250 - self.radius, 250 + self.radius,
                                250 + self.radius, start=self.start,extent=55, outline = "white")
            self.start += 55
            self.canvas.create_arc(250 - self.radius, 250 - self.radius, 250 + self.radius,
                                250 + self.radius, start=self.start,extent=35, fill="black")

            self.start += 35
        

        window.mainloop()

Fan()