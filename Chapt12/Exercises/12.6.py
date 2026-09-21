import math
from tkinter import *

class Circle2D:
    def __init__(self, x, y, radius):
        self.__x = x
        self.__y = y
        self.__radius = radius

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getRadius(self):
        return self.__radius

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def setRadius(self, radius):
        self.__radius = radius

    def getArea(self):
        return math.pi * self.__radius * self.__radius

    def getPerimeter(self):
        return 2 * math.pi * self.__radius

    def containsPoint(self, x, y):
        if ((x - self.__x) ** 2) + ((y - self.__y) ** 2) <= (self.__radius ** 2):
            return True
        else:
            return False

    def contains(self, otherCirc):
        if ((otherCirc.__x - self.__x) ** 2) + ((otherCirc.__y - self.__y) ** 2) <= (self.__radius - otherCirc.__radius) ** 2:
            return True
        else:
            return False

    def overlaps(self, otherCirc):
        d = math.sqrt(((otherCirc.__x - self.__x) ** 2) + ((otherCirc.__y - self.__y) ** 2))
        if abs(self.__radius - otherCirc.__radius) <= d <= self.__radius + otherCirc.__radius:
            return True
        else:
            return False

    def __contains__(self, otherCirc):
        if self.contains(otherCirc):
            return True
        else:
            False

    def __cmp__(self, otherCirc):
        if self.__radius > otherCirc.__radius:
            return 1
        elif self.__radius == otherCirc.__radius:
            return 0
        else:
            return -1

    def __lt__(self, otherCirc):
        return self.__cmp__(otherCirc) < 0

    def __le__(self, otherCirc):
        return self.__cmp__(otherCirc) <= 0

    def __eq__(self, otherCirc):
        return self.__cmp__(otherCirc) == 0

    def __ne__(self, otherCirc):
        return self.__cmp__(otherCirc) != 0

    def __gt__(self, otherCirc):
        return self.__cmp__(otherCirc) > 0

    def __ge__(self, otherCirc):
        return self.__cmp__(otherCirc) >= 0


class Display(Canvas):
    def __init__(self, container, width, height):
        super().__init__(container,width=width,height=height)

        self.c1 = Circle2D(x=150, y= 150, radius=50)
        self.c2 = Circle2D(x= 300, y=200, radius=40)
        self.draw(1)
        self.draw(2)
        self.bind("<B1-Motion>", self.move)

    def move(self, event):
        if self.c1.containsPoint(event.x, event.y):
            self.delete("all")
            self.c1.setX(event.x)
            self.c1.setY(event.y)
            self.draw(1)
            self.draw(2)
        elif self.c2.containsPoint(event.x, event.y):
            self.delete("all")
            self.c2.setX(event.x)
            self.c2.setY(event.y)
            self.draw(1)
            self.draw(2)

    def draw(self, circle):
        intersect = self.c1.overlaps(self.c2)
        if circle == 1:
            self.create_text(250, 20, text="Two circles don't intersect" if not intersect else "Two circles intersect", font=12)
            self.create_oval(self.c1.getX() - self.c1.getRadius(), self.c1.getY() - self.c1.getRadius(),
                            self.c1.getX() + self.c1.getRadius(), self.c1.getY() + self.c1.getRadius(), fill="")
            self.create_text(self.c1.getX(), self.c1.getY(), text="c1")
        elif circle == 2:
            self.create_text(250, 20, text="Two circles don't intersect"if not intersect else "Two circles intersect", font=12)
            self.create_oval(self.c2.getX() - self.c2.getRadius(), self.c2.getY() - self.c2.getRadius(),
                            self.c2.getX() + self.c2.getRadius(), self.c2.getY() + self.c2.getRadius(), fill="")
            self.create_text(self.c2.getX(), self.c2.getY(), text="c2")

class TwoCircles:
    def __init__(self):
        window = Tk()
        window.title("Two Circles")
        d = Display(window, width=500, height=300)
        d.pack()
        window.mainloop()

def main():
    TwoCircles()

if __name__ == "__main__":
    main()
