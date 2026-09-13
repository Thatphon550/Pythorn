def partition(lst):
    pivot = lst[0]
    partitionList = []
    partitionList.extend([x for x in lst if x <= pivot])
    partitionList.append(pivot)
    partitionList.extend([x for x in lst if x > pivot])
    partitionList.remove(pivot)
    return partitionList

def main():
    line = input("Enter a list: ").strip().split()
    print(partition([eval(x) for x in line]))

main()