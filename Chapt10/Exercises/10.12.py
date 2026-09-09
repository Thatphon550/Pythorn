def gcd(lst):
    k = 2
    gcd = 1

    while k <= max(lst) / 2:
        divisible = True
        for i in range(len(lst)):
            if lst[i] % k != 0:
                divisible = False
        if divisible:
            gcd = k
        k += 1
        
    return gcd

def main():
    n = str(input("Enter five numbers separated by commas: ")) 
    n = n.split(' ')
    for j in range(len(n)):
        n[j] = int(n[j])

    print(f"The GCD is {gcd(n)}")
    
main()