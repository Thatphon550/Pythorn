def main():
    n = eval(input("Find all prime numbers <= n, enter n: "))

    list = []

    NUMBERS_PER_LINE = 10
    count = 0
    number = 2
    squareRoot = 1

    print("The prime numbers are \n")

    while number <= n:
        isPrime = True

        k = 0
        if squareRoot * squareRoot < number:
            squareRoot += 1

        while k < len(list) and list[k] <= squareRoot:
            if number % list[k] == 0:
                isPrime = False
                break
            k += 1
        if isPrime:
            count += 1
            list.append(number)
            if count % NUMBERS_PER_LINE == 0:
                print(number)
            else:
                print(str(number) + "  ", end= "")
        number += 1
    print("\n" + str(count) + " prime(s) less than or qual to " + str(n))


main()
