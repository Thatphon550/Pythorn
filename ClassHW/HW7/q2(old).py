import math

class Poly:
    
    def __init__(self, zero = 0, first = 0, second = 0, third = 0, fourth = 0, fifth = 0):
        self.zero = zero
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth
        self.fifth = fifth
        
    
        
    def __getitem__(self, index):
        if index == 0:
            return self.zero
        elif index == 1:
            return self.first
        elif index == 2:
            return self.second
        elif index == 3:
            return self.third
        elif index == 4:
            return self.fourth
        elif index == 5:
            return self.fourth
        
    def add(self, p):
        self.zero += p.zero
        self.first += p.first
        self.second += p.second
        self.third += p.third
        self.fourth += p.fourth
        self.fifth += p.fifth
    
    def multiply(self, p):
    
    def diff(self):
        self.zero = self.first
        self.first = self.second * 2
        self.second = self.third * 3
        self.third = self.fourth * 4
        self.fourth = self.fifth * 5
        self.fifth = 0
        
    def printPoly(self):
        string = ""
        if self.zero:
            if self.zero > 0:
                string += f"{self.zero}"
            else:
                string += f"- {abs(self.zero)}"
        if self.first:
            if self.first > 0:
                if string:
                    string += f" + {self.first}x"
                else:
                    string += f"{self.first}x"
            else:
                string += f" - {abs(self.first)}x"
        if self.second:
            if self.second > 0:
                if string:
                    string += f" + {self.second}x^2"
                else:
                    string += f"{self.second}x^2"
            else:
                string += f" - {abs(self.second)}x^2"
        if self.third:
            if self.third > 0:
                if string:
                    string += f" + {self.third}x^3"
                else:
                    string += f"{self.third}x^3"
            else:
                string += f" - {abs(self.third)}x^3"
        if self.fourth:
            if self.fourth > 0:
                if string:
                    string += f" + {self.fourth}x^4"
                else:
                    string += f"{self.fourth}x^4"
            else:
                string += f" - {abs(self.fourth)}x^4"
        if self.fifth:
            if self.fifth > 0:
                if string:
                    string += f" + {self.fifth}x^5"
                else:
                    string += f"{self.fifth}x^5"
            else:
                string += f" - {abs(self.fifth)}x^5"
                
        print(string)
    
    def eval(self, n):
        sum = 0
        for i in range(0, 5):
            sum += self[i] * (n ** i)
        
        return sum
        
        
            
def main():
    poly1 = Poly(0, 0, 5, 1, 0, 0)
    poly1.printPoly()
    poly1.diff()
    poly1.printPoly()
    print(poly1.eval(2))
    
main()
