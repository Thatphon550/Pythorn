def sort(points):
    for i in range(1, len(points)):
        currentElement = points[i]
        k = i - 1
        while k >= 0 and points[k][1] > currentElement[1]:
            points[k + 1] = points[k]
            k -= 1
        points[k + 1] = currentElement

def main():
    points = [
        [4, 34], [1, 7.5], [4, 8.5],
        [1, -4.5], [1, 4.5], [4, 6.6]
    ]

    sort(points)
    print(points)

main()
