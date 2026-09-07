def insertionSort(lst):
    for i in range(1, len(lst)):
        currentElement = lst[i]

        k = i - 1
        while k >= 0 and lst[k] > currentElement: #to reverse, simple switch the sign
            lst[k + 1] = lst[k]
            k -= 1

        lst[k + 1] = currentElement

def main():
    lst1 = [3.4, 5, 3, 3.5, 2.2, 1.9, 2]

    insertionSort(lst1)

    print(lst1)

main()


