def mergeSort(list):
    if len(list) > 1:
        firstHalf = list[:len(list) // 2]
        mergeSort(firstHalf)

        secondHalf = list[len(list) // 2:]
        mergeSort(secondHalf)

        merge(firstHalf, secondHalf, list)

def merge(list1, list2, temp):
    current1 = 0
    current2 = 0
    current3 = 0
    while current1 < len(list1) and current2 < len(list2):
        if list1[current1] < list2[current2]:
            temp[current3] = list1[current1]
            current1 += 1
            current2 += 1
        else:
            temp[current3] = list2[current2]
            current2 += 1
            current3 += 1

    while current1 < len(list1):
        temp[current3] = list1[current1]
        current1 += 1
        current3 += 1

    while current2 < len(list2):
        temp[current3] = list2[current2]
        current2 += 1
        current3 += 1

def main():
    list = [2, 3, 2, 5, 6, 1, -2, 3, 14, 12]
    mergeSort(list)
    print(*list, sep=" ")


main()
