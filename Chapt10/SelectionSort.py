def selectionSort(lst):
    for i in range(len(lst) - 1):
        currentMin = lst[i]
        currentMinIndex = i

        for j in range(i + 1, len(lst)):
            if currentMin > lst[j]: # To reverse, simply switch the sign
                currentMin = lst[j]
                currentMinIndex = j

        if currentMinIndex != i:
            lst[currentMinIndex] = lst[i]
            lst[i] = currentMin


def main():
    lst1 = [3.4, 5, 3, 3.5, 2.2, 1.9, 2, 2]
    
    selectionSort(lst1)
    
    print(lst1)

main()