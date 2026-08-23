import math

class RegularPolygon:
    
    def __init__(self, n=3, side=1, x=0, y=0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y
    
    def getN(self):
        return self.__n
    
    def setN(self, n):
        self.__n = n
        
    def getSide(self):
        return self.__side
    
    def setSide(self, side):
        self.__side = side
        
    def getX(self):
        return self.__x
    
    def setX(self, x):
        self.__x = x
        
    def getY(self):
        return self.__y
    
    def setY(self, y):
        self.__y = y
        
    def getPerimiter(self):
        return self.__side * self.__n
    
    def getArea(self):
        return (self.__n * self.__side ** 2) / (4 * math.tan(math.pi / self.__n))
    
def main():
    polygon1 = RegularPolygon(6, 4)
    polygon2 = RegularPolygon(10, 4, 5.6, 7.8)
    
    print(f"Polygon 1 Area: {polygon1.getArea():.2f} Perimeter: {polygon1.getPerimiter():.2f}")
    print(f"Polygon 2 Area: {polygon2.getArea():.2f} Perimeter: {polygon2.getPerimiter():.2f}")
    
main()