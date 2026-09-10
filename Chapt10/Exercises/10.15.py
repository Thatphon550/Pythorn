def isSorted(lst):
    tempList = [x for x in lst]
    insertionSort(tempList)
    return lst == tempList

def insertionSort(lst):
    for i in range(len(lst)):
        currentElement = lst[i]

        k = i - 1
        while k >= 0 and lst[k] > currentElement:
            lst[k + 1] = lst[k]
            k -= 1

        lst[k + 1] = currentElement

def main():
    lst = str(input("Enter list: "))
    lst = lst.split(' ')
    if isSorted(lst):
        print("The list is already sorted")
    else:
        print("The list is not sorted")

main()