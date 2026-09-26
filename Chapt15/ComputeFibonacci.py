def main():
    index = eval(input("Enter an index for a Fibonacci number: "))
    print(f"The Fibonacci number at index {index} is {fib(index)}")

def fib(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)

def f(n):
    if n > 0:
        print(n % 10)
    return f(n // 10)

f(123)
