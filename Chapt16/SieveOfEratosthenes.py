def main():

    n = eval(input("Find all prime numbers <= n, enter n: "))

    primes = []

    for i in range(n + 1):
        primes.append(True)

    k = 2
    while k <= n / k:
        if primes[k]:
             for i in range(k, int(n / k) + 1):
                 primes[k * i] = False
        k += 1

    count = 0
    for i in range(2, len(primes)):
        if primes[i]:
            count += 1
            if count % 10 == 0:
                print(i)
            else:
                print(str(i) + "   ", end="")
    print(f"\n{count} + prime(s) less than or equal to {n}")

main()
