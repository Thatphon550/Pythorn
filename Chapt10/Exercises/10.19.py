import random

class Ball:
    def __init__(self, slots):
        self.path = [random.randint(0, 1) for _ in range(slots)]

def BeanMachine(lst, totalSlots):
    result = [0 for _ in range(totalSlots + 1)]
    print()
    for ball in lst:
        positionIndex = 0
        for path in ball.path:
            if path:
                positionIndex += 1
                print("R", end = "")
            else:
                print("L", end = "")
        print()
        result[positionIndex] += 1
    print()

    maxResult = max(result)
    k = maxResult
    for _ in range(maxResult):
        for j in result:
            if j >= k:
                print(0, end = "")
            else:
                print(" ", end = "")
        print()
        k -= 1

def main():
    totalBalls = int(input("Enter the number of balls to drop: "))
    totalSlots =int(input("Enter the number of slots in the bean machine: "))
    lst = []
    for _ in range(totalBalls):
        lst.append(Ball(slots=totalSlots))

    BeanMachine(lst, totalSlots)

main()