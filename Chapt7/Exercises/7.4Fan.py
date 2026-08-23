
SLOW = 1
MEDIUM = 2
FAST = 3

class Fan:

    def __init__(self, speed=SLOW, on=False, radius=5, color="blue"):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color
        
    def getSpeed(self):
        return self.__speed
    
    def setSpeed(self, speed):
        self.__speed = speed
        
    def getOn(self):
        return self.__on
    
    def setOn(self, on):
        self.__on = on
        
    def getRadius(self):
        return self.__radius
    
    def setRadius(self, radius):
        self.__radius = radius
        
    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color
        
    def printFan(self):
        print(f"Speed: {self.__speed}, Radius: {self.__radius}, Color: {self.__color.title()}")
    
def main():
    
    fan1 = Fan(speed=FAST, radius=10, color="yellow", on = True)
    fan2 = Fan(speed=MEDIUM, radius=5, color="blue", on = False)
    
    print('\nFan 1: ', end = "")
    fan1.printFan()
    
    
    print('\nFan 2: ', end = "")
    fan2.printFan()
    
main()