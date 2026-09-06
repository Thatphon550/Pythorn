list1 = list(range(1, 10, 2))
list2 = list1
list1[0] = 111
print(list1)
print(list2)

list1 = list(range(1, 10, 2))
list2 = [] + list1
list1[0] = 111
print(list1)
print(list2)