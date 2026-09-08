def indexOfSmallestElement(lst):
    smallest = lst[0]
    smallestIndex = 0
    for i in range(len(lst)):
        if smallest > lst[i]:
            smallest = lst[i]       
            smallestIndex = i

    return smallestIndex

def main():
    lst = str(input("Enter a list of numbers: "))
    lst = lst.split(' ')

    index = indexOfSmallestElement(lst)
    print(f"The smallest element is at index: {index}")

main()