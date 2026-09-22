def equals(m1 ,m2):
    for row in range(len(m1)):
        if sorted(m1[row]) != sorted(m2[row]):
            return False
    return True



def main():
    m1 = [
        [51, 5, 25],
        [6, 1, 4],
        [24, 54, 6]
    ]

    m2 = [
        [51, 22, 25],
        [6, 4, 1],
        [24, 54, 6]
    ]

    print(equals(m1, m2))

main()
