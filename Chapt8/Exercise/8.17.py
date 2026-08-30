import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
        
    def __str__(self):
        return f"({self.__x}, {self.__y})"
    
    def distance(self, p):
        return math.sqrt(((p.__x - self.__x) ** 2) + ((p.__y - self.__y) ** 2))
    
    def isNearby(self, p):
        if self.distance(p) < 5:
            return True
        else:
            False
            
def main():
    x1, y1, x2, y2 = eval(input("Enter two points x1, y1, x2, y2: "))
    point1 = Point(x1, y1)
    point2 = Point(x2, y2)
    print(f"The distance between two points is {point1.distance(point2):.2f}")
    if point1.isNearby(point2):
        print("The two points are near each other")
    else:
        print("The two points are not near each other")
    
main()