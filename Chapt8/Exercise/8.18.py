import math

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

def main():
    while True:
        x1, y1, radius1 = eval(input("Enter x1, y2, radius: "))
        x2, y2, radius2 = eval(input("Enter x2, y2, radius: "))
        circ1 = Circle2D(x1, y1, radius1)
        circ2 = Circle2D(x2, y2, radius2)
        
        print(f"The area for c1 is {circ1.getArea()}")
        print(f"The perimeter for c1 is {circ1.getPerimeter()}")
        print(f"The area for c2 is {circ2.getArea()}")
        print(f"The perimeter for c21 is {circ2.getPerimeter()}")
        print(f"c1 contains the ceneter of c2?: {circ1.containsPoint(circ2.getX(), circ2.getY())}")
        print(f"c1 contains c2: {circ2 in circ1}")
        print(f"c1 overlaps c2?: {circ1.overlaps(circ2)}")
    
main()
    