from tkinter import *

class Circle:
    def __init__(self):
        window = Tk()
        window.title("Inside the rectangle?")

        self.canvas = Canvas(window, width=250, height=140, bg="white")
        self.canvas.pack()
        self.radius = 50
        self.canvas.create_rectangle(125 - self.radius, 70 - self.radius, 125 + self.radius, 70 + self.radius, tags="circle")
        self.exist = False
        self.canvas.bind("<B1-Motion>", self.inside)
        self.canvas.bind("<ButtonRelease-1>", self.delete)
        window.mainloop()

    def inside(self, event):
        if not 125 - self.radius <= event.x <= 125 + self.radius:
            self.printOut(event)
        if not 70 - self.radius <= event.y <= 70 + self.radius:
            self.printOut(event)

        if  125 - self.radius <= event.x <= 125 + self.radius:
            self.printIn(event)
        if  70 - self.radius <= event.y <= 70 + self.radius:
            self.printIn(event)

    def printOut(self, event):
        if not self.exist:
            self.canvas.create_text(event.x, event.y, text="Mouse pointer is not in the rectangle", tags="text")
            self.exist = True
        else:
            self.canvas.delete("text")
            self.canvas.create_text(event.x, event.y, text="Mouse pointer is not in the rectangle", tags="text")
        # self.canvas.after(1)
        # self.canvas.update()
        # self.canvas.delete("text")
        # self.exist = False
    def printIn(self, event):
        if not self.exist:
            self.canvas.create_text(event.x, event.y, text="Mouse pointer is in the rectangle", tags="text")
            self.exist = True
        else:
            if 125 - self.radius <= event.x <= 125 + self.radius and 70 - self.radius <= event.y <= 70 + self.radius:
                self.canvas.delete("text")
                self.canvas.create_text(event.x, event.y, text="Mouse pointer is in the rectangle", tags="text")

    def delete(self, event):
        self.canvas.delete("text")
    
Circle()    