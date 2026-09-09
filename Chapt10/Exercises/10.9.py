import math

def deviation(lst):
    s = 0
    for i in range(len(lst)):
        s += (lst[i] - mean(lst)) ** 2
    return math.sqrt(s / (len(lst) - 1))

def mean(lst):
    return sum(lst) / len(lst)

def main():
    num = str(input("Enter numbers: "))
    num = num.split(' ')
    
    for j in range(len(num)):
        num[j] = float(num[j])

    print(num)
    print(f"The mean is {mean(num):.4f}")
    print(f"The standard deviation is {deviation(num):.5f}")

main()