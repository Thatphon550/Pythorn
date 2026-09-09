def selectionSort(lst):


    for i in range(len(lst) - 2, 0, -1):
        currentMax = lst[i]
        currentMaxIndex = i

        for j in range(len(lst) - 1, i + 1, -1):
            if lst[j] > currentMax:
                currentMax = lst[j]
                currentMaxIndex = j

        if currentMaxIndex != i:
            lst[currentMaxIndex] = lst[len(lst) - 1]
            lst[len(lst) - 1] = currentMax

a = [1, 3, 1, 2, 3, 4, 6, 9]
selectionSort(a)
print(a)