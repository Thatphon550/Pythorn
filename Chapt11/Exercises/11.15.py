class Line:
    def __init__(self, x1, y1, x2, y2):
        self.m = (y2 - y1) / (x2 - x1)
        self.a = self.m
        self.b = -1
        self.c = y1 - self.m * x1

    def distance(self, x, y):
        return abs(self.a * x + self.b * y + self.c) /  (self.a ** 2 + self.b ** 2) ** 0.5

def main():
    line = str(input("Enter five points: ")).split()

    points = []
    for i in range(0, len(line), 2):
        points.append([eval(line[i]), eval(line[i + 1])])

    if sameLine(points):
        print("The five points are on the same line")
    else:
        print("The five points are not on the same line")

def sameLine(points):
    x1 = points[0][0]
    p1 = points[0]
    x2 = points[0][0]
    p2 = points[0]
    for i in range(len(points)):
        if points[i][0] < x1:
            p1 = points[i]
            x1 = points[i][0]
        elif points[i][0] > x2:
            p2 = points[i]
            x2 = points[i][0]
    for point in points:
        if Line(p1[0], p1[1], p2[0], p2[1]).distance(point[0], point[1]):
            return False
    return True

main()
