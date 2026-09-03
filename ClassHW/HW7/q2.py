class Poly:
    def __init__(self, terms):
        self.terms = terms
        
    def add(self, p):
        largest = self.terms
        smallest = p.terms
        
        if len(p.terms) > len(self.terms):
            largest = p.terms
            smallest = self.terms
        largest_list = list(largest)
        smallest_list = list(smallest)
        
        for index, term in enumerate(smallest_list):
            largest_list[index] += term
        
        addedPoly = tuple(largest_list)
        
        return Poly(addedPoly)
    
    def scalar_multiply(self, n):
        coefficient = list(self.terms)
        for i in range(0, len(coefficient)):
            coefficient[i] *= n
        
        return Poly(tuple(coefficient))
    
    def multiply(self, p):
        mulList = []
        c = 1
        while c < (len(self.terms) + len(p.terms)):
            mulList.append(0)
            c += 1
        
        for i, termSelf in enumerate(self.terms):
            for j, termP in enumerate(p.terms):
                    mulList[i + j] += termSelf * termP
                    
        return Poly(tuple(mulList))
        
    def power(self, n):
        if n == 0:
            return Poly(1)
        
        string = "self"
        for i in range(1, n):
            string += ".multiply(self)"
        
        return eval(string)
        
        
    def diff(self):
        diffList = []

        for index in range(1, len(self.terms)):
            diffList.append(self.terms[index] * index)

        return Poly(tuple(diffList))   
    
    def integrate(self):
        intList = [0]
        
        for index in range(0, len(self.terms)):
            intList.append(self.terms[index] / (index + 1))     
        
        return Poly(tuple(intList))
    
    def evalPoly(self, n):
        sum = 0
        for index, term in enumerate(self.terms):
            sum += term * (n ** index)
        
        return sum
        
    
    def printPoly(self):
        string = ""
        for index in range(0, len(self.terms)):
            if self.terms[index]:
                if index == 1:
                    if string:
                        if self.terms[index] > 0:
                            if self.terms[index] == 1:
                                string += f" + x"             
                            else:
                                string += f" + {self.terms[index]}x"
                        else:
                            if self.terms[index] == -1:
                                string += f" - x"
                            else:
                                string += f" - {abs(self.terms[index])}x"
                            
                    else:
                        if self.terms[index] > 0:
                            if self.terms[index] == 1:
                                string += f"x"
                            else:
                                string += f"{self.terms[index]}x"
                        else:
                            if self.terms[index] == -1:
                                string += f" -x"
                            else:
                                string += f" -{abs(self.terms[index])}x"
                            
                elif string:
                    if self.terms[index] > 0:
                        if self.terms[index] == 1:
                            string += f" + x^{index}"
                        else:
                            string += f" + {self.terms[index]}x^{index}"
                    else:
                        if self.terms[index] == -1:
                            string += f" - x^{index}"
                        else:
                            string += f" - {abs(self.terms[index])}x^{index}"
                else:
                    if index == 0 and self.terms[index]:  
                        if self.terms[index] > 0:
                            string += f"{self.terms[index]}"
                        else:
                            string += f"-{abs(self.terms[index])}"
                    else:
                        if self.terms[index] > 0:
                            if self.terms[index] == 1:
                                string += f"x^{index}"
                            else:
                                string += f"{self.terms[index]}x^{index}"
                        else:
                            if self.terms[index] == -1:
                                string += f"-x^{index}"
                            else:
                                string += f"-{abs(self.terms[index])}x^{index}"
        print(string)
        
    
    
    
        
def main():

    p = Poly((1, 0, -2))
    p.printPoly()
    
    q = p.power(2)
    q.printPoly()
    
    p.evalPoly(3)
    
    r = p.add(q)
    r.printPoly()

    r.diff().printPoly()
    
main()