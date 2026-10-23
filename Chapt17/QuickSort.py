def quickSort(list):
    quickSortHelper(list, 0, len(list) - 1)

def quickSortHelper(list, first, last):
    if last > first:
        pivotIndex = partition(list, first, last)
        quickSortHelper(list, first, pivotIndex - 1)
        quickSortHelper(list, pivotIndex + 1, last)

def partition(list, first, last):
    pivot = list[first]
    low = first + 1
    high = last

    while high > low:
        while low <= high and list[low] <= pivot:
            low += 1

        while low <= high and list[high] > pivot:
            high -= 1

        if high > low:
            list[high], list[low] = list[low], list[high]

    while high > first and list[high] < pivot:
        high -= 1

    if pivot > list[high]:
        list[first] = list[high]
        list[high] = pivot
        return high
    else:
        return first
