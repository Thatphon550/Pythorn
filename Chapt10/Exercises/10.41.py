from tkinter import *

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def containsPoint(self, x, y):
        if ((x - self.x) ** 2) + ((y - self.y) ** 2) <= (self.radius ** 2):
            return True
        else:
            return False

class Olympic:
    def __init__(self):
        window = Tk()
        window.title("Olympic Symbol")

        self.canvas = Canvas(window, width=420, height= 200, bg="white")
        self.canvas.pack()

        self.circle_list = []
        self.canvas.create_line(420 / 2, 0, 420 / 2, 200)
        self.fill = ["blue", "black", "red", "yellow", "green"]
        for i in range(3):
            self.circle_list.append(Circle(110 + 100 * i, 80, radius=40))
        for i in range(2):
            self.circle_list.append(Circle(160 + 100 * i, 115, radius=40))


        self.draw()
        self.canvas.bind("<B1-Motion>", self.move)
        window.mainloop()

    def move(self, event):
        for i in range(len(self.circle_list)):
            if self.circle_list[i].containsPoint(event.x, event.y):
                self.circle_list[i].x, self.circle_list[i].y = event.x, event.y
                self.draw()
                for j in range(len(self.circle_list)):
                    if i == j:
                        pass
                    elif self.circle_list[j].containsPoint(event.x, event.y):
                        return

    def draw(self):
        self.canvas.delete("all")
        for i, circle in enumerate(self.circle_list):
            self.canvas.create_oval(circle.x - circle.radius, circle.y - circle.radius,
                                    circle.x + circle.radius, circle.y + circle.radius,
                                    outline=self.fill[i], width=4)
Olympic()
