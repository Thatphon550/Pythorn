class Rectangle:
    def __init__(self, width=1, height=2):
        self.__width = width
        self.__height = height
        
    def getArea(self):
        return self.__width * self.__height
    
    def getPerimeter(self):
        return (self.__width * 2) + (self.__height * 2)
    
    
def main():
    rect1 = Rectangle(width=4, height=40)
    rect2 = Rectangle(width=3.5, height=35.7)
    
    print(f"Rectangle 1 Area: {rect1.getArea():.2f}, Perimeter: {rect1.getPerimeter():.2f}")
    print(f"Rectangle 2 Area: {rect2.getArea():.2f}, Perimeter: {rect2.getPerimeter():.2f}")
    
main()