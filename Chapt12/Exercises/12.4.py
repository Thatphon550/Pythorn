class Rectangle2D:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * self.width + 2 * self.height

    def containsPoint(self, x, y):
        if self.x - (self.width / 2) <= x <= self.x + (self.width / 2) and \
            self.y - (self.height / 2) <= y <= self.y + (self.height / 2):
            return True

        return False

    def contains(self, otherRect):
        if self.x - (self.width / 2) <= otherRect.x - (otherRect.width / 2) and \
            self.x + (self.width / 2) >= otherRect.x + (otherRect.width / 2) and \
            self.y - (self.height / 2) <= otherRect.y - (otherRect.height / 2) and \
            self.y + (self.height / 2) >= otherRect.y + (otherRect.height / 2):
                return True

        return False

    def overlapse(self, otherRect):
        if abs(self.x - otherRect.x) < (self.width + otherRect.width) / 2 and \
           abs(self.y - otherRect.y) < (self.height + otherRect.height) / 2:
                return True

        return False

    def __contains__(self, otherRect):
        if self.contains(otherRect):
            return True

        return False

    def __cmp__(self, otherRect):
        if self.getArea() > otherRect.getArea():
            return 1
        elif self.getArea() == otherRect.getArea():
            return 0
        else:
            return -1

    def __lt__(self, otherRect):
        if self.__cmp__(otherRect) < 0:
            return True
        else:
            return False

    def __le__(self, otherRect):
        if self.__cmp__(otherRect) <= 0:
            return True
        else:
            return False

    def __eq__(self, otherRect):
        if self.__cmp__(otherRect) == 0:
            return True
        else:
            return False

    def __ne__(self, otherRect):
        if self.__cmp__(otherRect) != 0:
            return True
        else:
            return False

    def __gt__(self, otherRect):
        if self.__cmp__(otherRect) > 0:
            return True
        else:
            return False

    def __gt__(self, otherRect):
        if self.__cmp__(otherRect) >= 0:
            return True
        else:
            return False

def getRectangle(points):
    minX = float(points[0][0])
    maxX = float(points[0][0])
    minY = float(points[0][1])
    maxY = float(points[0][1])
    for i in range(len(points)):
        if float(points[i][0]) < minX:
            minX = float(points[i][0])
        if float(points[i][0]) > maxX:
           maxX = float(points[i][0])
        if float(points[i][1]) < minY:
            minY = float(points[i][1])
        if float(points[i][1]) > maxY:
            maxY = float(points[i][1])

    return Rectangle2D((maxX + minX) / 2, (maxY + minY) / 2, width=abs(maxX - minX),height=abs(maxY - minY))

def main():
    line = input("Enter the points: ").strip().split()
    points = []
    for i in range(0, len(line), 2):
        points.append([line[i], line[i + 1]])

    rect = getRectangle(points)
    print(f"The bounding rectangle is centered at ({rect.x:.2f}, {rect.y:.2f}) with width {rect.width:.1f} and height {rect.    height:.1f}")

main()
