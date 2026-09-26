def main():
    n = eval(input("Enter a nonnegative integer: "))
    print(f"Factorial of {n} is {factorial(n)}")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

main()
