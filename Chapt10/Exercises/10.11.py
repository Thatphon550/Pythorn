import random

def shuffle(lst):
    for i in range(len(lst)):
        j = random.randint(0, len(lst) - 1)
        lst[i], lst[j] = lst[j], lst[i]


def main():
    lst = [1, 2, 3, 4, 5, 6]
    shuffle(lst)
    print(lst)

main()