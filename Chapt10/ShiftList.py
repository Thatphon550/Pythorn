
def shiftDown(lst):
    temp = lst[0]

    for i in range(1, len(lst)):
        lst[i - 1] = lst[i]

    lst[len(lst) - 1 ] = temp

def shiftUp(lst):
    temp = lst[len(lst) - 1]

    for i in range(len(lst) - 1, 0, -1):
        lst[i] = lst[i - 1]

    lst[0] = temp



list1 = [1, 2, 3, 4, 5]

for _ in range(1, 3):
    shiftUp(list1)
    
print(list1)

for _ in range(1, 5):
    shiftDown(list1)

print(list1)
