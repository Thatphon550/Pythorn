import random

def shuffle(m):
    for i in range(len(m)):
        j = random.randint(0, len(m) - 1)
        m[i], m[j] = m[j], m[i]

def main():
    m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    shuffle(m)
    print(m)

main()
