from Linear import LinearEquation

def main():
    x1, y1, x2, y2 = eval(input("Enter the endpoints of the first line segment: "))
    x3, y3, x4, y4 = eval(input("Enter the endpoints of the second line segment: "))

    m12 = (y2 - y1) / (x2 - x1)
    m34 = (y4 - y3) / (x4 - x3)

    a = -m12
    b = 1
    e = y1 -  (m12 * x1)
    c = -m34
    d = 1
    f = y3 - (m34 * x3)

    eqn = LinearEquation(a, b, c, d, e, f)


    if not eqn.isSolvable():
        print("The two lines are parallel and do not have one intersection point.")
    else:
        x = eqn.getX()
        y = eqn.getY()

        if (min(x1, x2) <= x <= max(x1, x2) and
            min(y1, y2) <= y <= max(y1, y2) and
            min(x3, x4) <= x <= max(x3, x4) and
            min(y3, y4) <= y <= max(y3, y4)):

            print(f"The line segments intersect at ({x}, {y})")

        else:
            print("The line segments do not intersect.")

main()