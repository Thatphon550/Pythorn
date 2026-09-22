def equals(m1, m2):
    for row in range(len(m1)):
        for index in range(len(m1[row])):
            if m1[row][index] != m2[row][index]:
                return False

    return True

def main():
    m1 = [
        [51, 22, 25],
        [6, 1, 4],
        [24, 54, 6]
    ]

    m2 = [
        [51, 22, 25],
        [6, 1, 4],
        [24, 54, 6]
    ]

    print(equals(m1, m2))

main()
