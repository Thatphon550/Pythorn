def gcd(m, n):
    gcd = 1

    if m % n == 0:
        return n

    for k in range(int(n / 2), 0, -1):
        if m % k == 0 and n % k == 0:
            gcd = k
            break

    return gcd

def main():
    m = eval(input("Enter first integer: "))
    n = eval(input("Enter second integer: "))

    print(f"The greatest common divisor for {m} and {n} is {gcd(m, n)}")

main()
