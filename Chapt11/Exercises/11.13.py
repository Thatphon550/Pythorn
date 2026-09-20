def locateLargest(a):
    largest = a[0][0]
    largestIndex = [0, 0]
    for row in range(len(a)):
        for col in range(len(a[row])):
            if a[row][col] > largest:
                largest = a[row][col]
                largestIndex = [row, col]
    return largestIndex

def main():
    matrix = []
    numRow = int(input("Enter a number of rows in the list: "))
    for i in range(numRow):
        matrix.append([eval(x) for x in input("Enter a row: ").split()])

    index = locateLargest(matrix)
    print(f"The location of the largest element is at ({index[0]}, {index[1]})")

main()
