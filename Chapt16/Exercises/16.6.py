import time

def fib(n):
    f0, f1, f2 = 0, 1, 1

    if n == 0: return f0
    elif n == 1: return f1
    elif n == 2: return f2

    for _ in range(3, n + 1):
        f0 = f1
        f1 = f2
        f2 = f0 + f1
    return f2

def gcd_brute(m, n):

    if n > m:
        m, n = n, m
    k = n
    while k > 0:
        if m % k == 0 and n % k == 0:

            return k
        k -= 1
    return 1

def gcd_euclid(m, n):
    if m % n == 0:
        return n
    else:
        return gcd_euclid(n, m % n)

def main():
    print("Brute Force")
    for k in range(40, 45 + 1):
        print(f"k = {k}", end=" | ")
        start_time = time.time()
        gcd_brute(fib(k), fib(k - 1))
        end_time = time.time()
        print(f"It took {end_time - start_time:.2f} seconds to run")

    print(f"Euclid GCD")

    for k in range(40, 45 + 1):
        print(f"k = {k}", end = " | ")
        start_time = time.time()
        gcd_euclid(fib(k), fib(k - 1))
        end_time = time.time()
        print(f"It took {end_time - start_time:.2f} seconds to run")

main()
