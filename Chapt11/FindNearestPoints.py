import NearestPoints

def main():
    numberOfPoints = eval(input("Enter the number of points: "))

    points = []
    for i in range(numberOfPoints):
        point = 2 * [0]
        point[0], point[1] = eval(input("Enter coordinates separated by a comma: "))
        points.append(point)

    p1, p2 = NearestPoints.nearestPoints(points)

    print("The closest two points are (" +
          str(points[p1][0]) + ", " + str(points[p1][1]) + ") and (" +
          str(points[p2][0]) + ", " + str(points[p2][1]) + ")")

main()