class Fraction:
    def __init__(self, numerator=1, denominator=1):
        divisor = gcd(numerator, denominator)
        self.numerator = (1 if denominator > 0 else -1) * int(numerator / divisor)
        self.denominator = abs(int(denominator / divisor))

    def __getitem__(self, index):
        if index == 0:
            return self.numerator
        elif index == 1:
            return self.denominator

    def __add__(self, secondFraction):
        n = (self.numerator * secondFraction[1]) + (self.denominator * secondFraction[0])
        d = self.denominator * secondFraction[1]
        return Fraction(n, d)

    def __sub__(self, secondFraction):
        n = (self.numerator * secondFraction[1]) - (self.denominator * secondFraction[0])
        d = self.denominator * secondFraction[1]
        return Fraction(n, d)

    def __mul__(self, secondFraction):
        n = self.numerator * secondFraction[0]
        d = self.denominator * secondFraction[1]
        return Fraction(n, d)

    def __truediv__(self, secondFraction):
        n = self.numerator * secondFraction[1]
        d = self.denominator * secondFraction[0]
        return Fraction(n, d)

    def display(self):
        print(f"{self.numerator} / {self.denominator}")

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return str(self.numerator) + " / " + str(self.denominator)

def gcd(n1, n2):
    n1 = abs(n1)
    n2 = abs(n2)

    gcd = 1
    k = 1
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k
        k += 1

    return gcd

def main():
    a = Fraction(1, 2)
    b = Fraction(1, 3)

    print(a + b)
    print(b - a)

main()