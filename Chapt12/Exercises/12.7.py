from tkinter import *

class Rectangle2D:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * self.width + 2 * self.height

    def containsPoint(self, x, y):
        if self.x - (self.width / 2) <= x <= self.x + (self.width / 2) and \
            self.y - (self.height / 2) <= y <= self.y + (self.height / 2):
            return True

        return False

    def contains(self, otherRect):
        if self.x - (self.width / 2) <= otherRect.x - (otherRect.width / 2) and \
            self.x + (self.width / 2) >= otherRect.x + (otherRect.width / 2) and \
            self.y - (self.height / 2) <= otherRect.y - (otherRect.height / 2) and \
            self.y + (self.height / 2) >= otherRect.y + (otherRect.height / 2):
                return True

        return False

    def overlapse(self, otherRect):
        if abs(self.x - otherRect.x) < (self.width + otherRect.width) / 2 and \
           abs(self.y - otherRect.y) < (self.height + otherRect.height) / 2:
                return True

        return False

    def __contains__(self, otherRect):
        if self.contains(otherRect):
            return True

        return False

    def __cmp__(self, otherRect):
        if self.getArea() > otherRect.getArea():
            return 1
        elif self.getArea() == otherRect.getArea():
            return 0
        else:
            return -1

    def __lt__(self, otherRect):
        if self.__cmp__(otherRect) < 0:
            return True
        else:
            return False

    def __le__(self, otherRect):
        if self.__cmp__(otherRect) <= 0:
            return True
        else:
            return False

    def __eq__(self, otherRect):
        if self.__cmp__(otherRect) == 0:
            return True
        else:
            return False

    def __ne__(self, otherRect):
        if self.__cmp__(otherRect) != 0:
            return True
        else:
            return False

    def __gt__(self, otherRect):
        if self.__cmp__(otherRect) > 0:
            return True
        else:
            return False

    def __gt__(self, otherRect):
        if self.__cmp__(otherRect) >= 0:
            return True
        else:
            return False

class Display(Canvas):
    def __init__(self, container, width, height):
        super().__init__(container, width=width,height=height)
        self.r1 = Rectangle2D(100, 200, 75, 75)
        self.r2 = Rectangle2D(300, 150, 55, 100)
        self.draw(1)
        self.draw(2)
        self.bind("<B1-Motion>", self.move)

    def move(self, event):
        if self.r1.containsPoint(event.x, event.y):
            self.delete("all")
            self.r1.x, self.r1.y = event.x, event.y
            self.draw(1)
            self.draw(2)
        elif self.r2.containsPoint(event.x, event.y):
            self.delete("all")
            self.r2.x , self.r2.y = event.x, event.y
            self.draw(1)
            self.draw(2)


    def draw(self, r):
        self.create_text(250, 30, text="Two rectangles intersect" if self.r1.overlapse(self.r2)
                         else "Two rectangles don't intersect", font=12)
        if r == 1:
            self.create_rectangle(self.r1.x - self.r1.width / 2, self.r1.y - self.r1.height / 2,
                                  self.r1.x + self.r1.width / 2, self.r1.y + self.r1.height / 2, fill = "")
            self.create_text(self.r1.x, self.r1.y, text="r1")
        elif r == 2:
            self.create_rectangle(self.r2.x - self.r2.width / 2, self.r2.y - self.r2.height / 2,
                                self.r2.x + self.r2.width / 2, self.r2.y + self.r2.height / 2, fill = "")
            self.create_text(self.r2.x, self.r2.y, text="r2")

class TwoRectangles:
    def __init__(self):
        window = Tk()
        window.title("Two Rectangles")

        a = Display(window, width=500, height=300)
        a.pack()

        window.mainloop()

TwoRectangles()
