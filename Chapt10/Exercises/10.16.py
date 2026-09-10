def bubbleSort(lst):
    for i in range(len(lst)):
       for j in range(len(lst) - i - 1):
           if lst[j] > lst[j + 1]:
               lst[j], lst[j + 1] = lst[j + 1], lst[j] 

def main():
    lst = [6, 5, 4, 3, 2, 4, 7, 9, 0, 7, -4]
    bubbleSort(lst)
    print(lst)

main()