import math

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Complex(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)

    def __abs__(self):
        return math.hypot(self.a, self.b)

    def __truediv__(self, other):
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        return Complex((a * c + b * d) / (c ** 2 + d ** 2), (b * c - a * d) / (c ** 2 + d ** 2))

    def __str__(self):
        if self.b != 0:
            return f"({self.a} + {self.b}i)"

        return f"({self.a})"

def main():
    a1, b1 = eval(input("Enter the first complex number: "))
    a2, b2 = eval(input("Enter the second complex number: "))

    c1 = Complex(a1, b1)
    c2 = Complex(a2, b2)

    print(f"{str(c1)} + {str(c2)} = {str(c1 + c2)}")
    print(f"{str(c1)} - {str(c2)} = {str(c1 - c2)}")
    print(f"{str(c1)} * {str(c2)} = {str(c1 * c2)}")
    print(f"{str(c1)} / {str(c2)} = {str(c1 / c2)}")
    print(f"|{str(c1)}| = {abs(c1)}")
main()