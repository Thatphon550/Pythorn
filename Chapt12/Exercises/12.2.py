class Location(list):
    def __init__(self, numberOfRows, numberOfColumns):
        super().__init__()
        self.__numberOfRows = numberOfRows
        self.__numberOfColumns = numberOfColumns
        for i in range(self.__numberOfRows):
            self.append([eval(x) for x in input(f"Enter row {i}: ").strip().split()])

    def locateLargest(self):
        currentMax = self[0][0]
        currentMaxIndex = [0, 0]
        for i in range(self.__numberOfRows):
            for j in range(self.__numberOfColumns):
                if currentMax < self[i][j]:
                    currentMax = self[i][j]
                    currentMaxIndex = [i, j]
        return [currentMax, currentMaxIndex]


def main():
    numRow, numCol = eval(input("Enter the number of rows and columns in the list: "))
    matrix = Location(numRow, numCol)
    a, b = matrix.locateLargest()
    print(f"The location of the largest element is {a} at ({b[0]}, {b[1]})")

main()


