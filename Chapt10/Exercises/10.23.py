def solveQuadraic(eqn):
    a, b, c = eqn

    if (b ** 2) - (4 * a * c) < 0:
        return

    root1 = (- b + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
    root2 = (- b - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
    return [root1, root2]

def main():
    print(solveQuadraic([-6, -5, 4]))

main()