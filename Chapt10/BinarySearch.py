def binarySearch(lst, key):
    high = len(lst) - 1
    low = 0

    while high >= low:
        mid = (high + low) // 2
        if lst[mid] > key:
            high = mid - 1
        elif lst[mid] == key:
            return mid
        else:
            low = mid + 1

    return -low - 1

def checkIndex(index):
    if index >= 0:
        return index
    return f"Insert at {-(index + 1)}"

def main():
    lst = [2, 4, 7, 10, 11, 45, 50, 59, 60, 66, 69, 70, 79]
    print(binarySearch(lst, 2))
    print(binarySearch(lst, 11))
    print(checkIndex(binarySearch(lst, 12)))
    print(binarySearch(lst, 1))
    print(binarySearch(lst, 3))

main()