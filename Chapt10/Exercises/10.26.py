def merge(list1, list2):
    return sorted(list1 + list2)

def main():
    list1 = input("Enter list1: ").strip().split()
    list2 = input("Enter list2: ").strip().split()
    print(f"The merged list is {merge([eval(x) for x in list1], [eval(y) for y in list2])}")

main()