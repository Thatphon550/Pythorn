def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)

def main():
    m = eval(input("Enter first integer: "))
    n = eval(input("Enter second integer: "))

    print(f"The greatest common divisor for {m} and {n} is {gcd(m, n)}")

main()
