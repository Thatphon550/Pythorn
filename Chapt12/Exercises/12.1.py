class TriangleError(RuntimeError):
    def __init__(self, side1, side2, side3):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def get_side1(self):
        return self.__side1

    def get_side2(self):
        return self.__side2

    def get_side3(self):
        return self.__side3

class GeometricObject:
    def __init__(self, color = "green", filled = True):
        self.__color = color
        self.__filled = filled

    def getColor(self):
        return self.__color

    def setColor(self, color):
        self.__color = color

    def isFilled(self):
        return self.__filled

    def setFilled(self, filled):
        self.__filled = filled

    def __str__(self):
        return "color:" + self.__color + " and filled: " + str(self.__filled)

class Triangle(GeometricObject):
    def __init__(self, side1=1.0, side2=1.0, side3=1.0):
        super().__init__()
        if side1 + side2 < side3 or side1 + side3 < side2 or side2 + side3 < side1:
            raise TriangleError(side1, side2, side3)
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def getSide1(self):
        return self.__side1

    def setSide1(self, side1):
        self.__side1 = side1

    def getSide2(self):
        return self.__side2

    def setSide2(self, side2):
        self.__side2 = side2

    def getSide3(self):
        return self.__side3

    def setSide3(self, side3):
        self.__side3 = side3

    def getArea(self):
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        return (s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3)) ** 0.5

    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def __str__(self):
        return f"Triangle: side1 = {self.__side1} side2 = {self.__side2} side3 = {self.__side3}"

try:
    Triangle(1, 2, 4)
except TriangleError as t:
    print(f"Cannot form triangle with {t.get_side1()}, {t.get_side2()}, {t.get_side3()}")
