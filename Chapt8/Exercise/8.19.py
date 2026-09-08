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
    
def main():
    x1, y1, width1, height1 = eval(input("Enter x1, y1, width1, height1: "))
    x2, y2, width2, height2 = eval(input("Enter x2, y2, width2, height2: "))
    r1 = Rectangle2D(x1, y1, width1, height1)
    r2 = Rectangle2D(x2, y2, width2, height2)

    print(f"The area for r1 is {r1.getArea()}")
    print(f"The perimeter for r1 is {r1.getPerimeter()}")
    print(f"The area for r2 is {r2.getArea()}")
    print(f"The perimeter for r2 is {r2.getPerimeter()}")
    print(f"r1 contains the center of r2? {r1.containsPoint(r2.x, r2.y)}")
    print(f"r1 contains r2? {r2 in r1}")
    print(f"r1 overlaps r2 {r1.overlapse(r2)}")

main()