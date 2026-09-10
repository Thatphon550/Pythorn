def reverseSelectionSort(lst):
    for i in range(len(lst) -1, 0, -1):
        currentMax = lst[i]
        currentMaxIndex = i

        for j in range(i - 1, -1, -1):
            if currentMax < lst[j]:
                currentMax = lst[j]
                currentMaxIndex = j

        if currentMaxIndex != i:
            lst[currentMaxIndex] = lst[i]
            lst[i] = currentMax

a = [1, 3, 1, 2, 3, 4, 6, 9]
reverseSelectionSort(a)
print(a)