class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
        
    def getA(self):
        return self.__a
    
    def getB(self):
        return self.__b
        
    def getC(self):
        return self.__c
        
    def getD(self):
        return self.__d
    
    def getE(self):
        return self.__e
    
    def getF(self):
        return self.__f
    
    def isSolvable(self):
        if (self.__a * self.__d) - (self.__b * self.__c) == 0:
            return False
        return True
    
    def getX(self):
        return ((self.__e * self.__d) - (self.__b * self.__f)) / ((self.__a * self.__d) - (self.__b * self.__c))
    
    def getY(self):
        return ((self.__a * self.__f) - (self.__e * self.__c)) / ((self.__a * self.__d) - (self.__b * self.__c))
        
        
def main():
    a, b, c, d, e, f = eval(input("Enter value of a, b, c, d, e, f separated by commas: "))
    eqn1 = LinearEquation(a, b, c, d, e, f)
    
    if not eqn1.isSolvable():
        print("The equation has no solution.")
    else:
        print(f"The value of x is: {eqn1.getX()}")
        print(f"The value of y is: {eqn1.getY()}")
        
main()