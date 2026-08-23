import math

class Circle:
    def __init__(self, radius = 1):
        self.radius = radius
        
    def getPerimeter(self):
        return 2 * self.radius * math.pi
        
    def getArea(self):
        return self.radius * self.radius * math.pi
        
    def setRadius(self, radius):
        self.radius = radius
            
c1 = Circle()

print(c1.radius)
print(c1.getPerimeter())
print(c1.getArea())

print(f'Area is {Circle(5).getArea()}')