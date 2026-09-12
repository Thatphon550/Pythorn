from tkinter import *

class Fan:
    def __init__(self):
        window = Tk()
        window.title("Fan")

        self.canvas = Canvas(window, width=500, height=500, bg="white")
        self.canvas.pack()
        self.radius = 220

        self.start = 0
        self.time = 1
        while True:
            for _ in range(4):
                self.canvas.create_arc(250 - self.radius, 250 - self.radius, 250 + self.radius,
                                    250 + self.radius, start=self.start,extent=55, outline = "white",
                                    tags = "arc")
                self.start += 55
                self.canvas.create_arc(250 - self.radius, 250 - self.radius, 250 + self.radius,
                                    250 + self.radius, start=self.start,extent=35, fill="black",
                                    tags = "arc")

                self.start += 35 

            self.start += 5
            self.canvas.after(self.time)
            
            
            
            self.canvas.update()
            self.canvas.delete("arc")
        

        window.mainloop()

Fan()