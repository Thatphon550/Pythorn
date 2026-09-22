def linearEquation(a, b):
    if a[0] * a[3] - a[1] * a[2] == 0:
        return
    x = (b[0] * a[3] - b[1] * a[1]) / (a[0] * a[3] - a[1] * a[2])
    y = (b[1] * a[0] - b[0] * a[2]) / (a[0] * a[3] - a[1] * a[2])
    return [x, y]

def main():
    eqn = [9, 4, 3, -5, -6, -21]
    a = eqn[:4]
    b = eqn[4:]
    print(linearEquation(a, b))

main()
