import math

def isPrime(n, lst):

    for prime in lst:
        if prime > math.sqrt(n):
            break
        if n % prime == 0:
            return False
        
    return True

def main():
    count = 1
    i = 3
    primeLst = [2]
    while count < 50:
        if isPrime(i, primeLst):
            primeLst.append(i)
            count += 1

        i += 1

    print("============== First 50 Prime Numbers ==============")
    print("|", end = "")
    for i in range(len(primeLst)):
        if i % 10 == 0 and i != 0:
            print("|", end ="")
            print()
            print("|", end = "")
        print(format(primeLst[i], "4d"), end=" ")
    if i == len(primeLst) - 1:
            print("|", end = "")
    print("\n====================================================")

main()