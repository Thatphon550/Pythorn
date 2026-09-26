# Q1

from tkinter import *

class PieChart:
    def __init__(self, lst):
        color = ["#FFFFFF", "#DEDEDE", "#BDBBBB", "#A19F9F", "#8F8D8D"]
        window  = Tk()
        window.title("Pie Chart")
        self.radius = 125

        count = [0 for _ in range(max(lst))]
        for num in lst:
            count[num - 1] += 1
        self.canvas = Canvas(window, width=400, height=400, bg="white")
        start_point = 90
        for i in range(len(count)):
            percent = (count[i] / sum(count)) * 100
            self.canvas.create_arc(200 - self.radius, 200 - self.radius,
                                   200 + self.radius, 200 + self.radius,
                                   start = start_point, extent = (percent / 100) * 360,
                                   fill = color[i % len(color)])
            start_point += (percent / 100) * 360

        self.canvas.pack()

        window.mainloop()


def pie_chart(lst):
    PieChart(lst)

pie_chart([3, 1, 3, 3, 2, 3, 3, 2, 3, 2, 4, 3, 3, 3, 3, 3, 4, 3, 3, 4, 3])

# Q2

def bubble_srt(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

lst = [3, 2, 9, 7, 9]
print(f"List before bubble sort {lst}")
bubble_srt(lst)
print(f"List after bubble sort {lst}")

# Q3

def my_union(list1, list2):
    union = []
    for i in list1:
        if i not in union:
            union.append(i)
    for j in list2:
        if j not in union:
            union.append(j)
    return union

def my_intersection(list1, list2):
    intersection = []
    for i in list1:
        if i in list2 and i not in intersection:
            intersection.append(i)
    for j in list2:
        if j in list1 and j not in intersection:
            intersection.append(j)
    return intersection

def my_difference(list1, list2):
    difference = []
    for i in list1:
        if i not in list2 and i not in difference:
            difference.append(i)

    return difference

list1 = [3, 1, 2, 7]
list2 = [4, 1, 2, 5]

print(f"Union: {my_union(list1, list2)}")
list4 = my_intersection(list1, list2)
print(f"Intersection  {list4}")
list5 = my_difference(list1, list2)
print(f"Difference: {list5}")

# Q4

def print_table(lst):
    padding = [len(str(lst[0][c])) + 3 for c in range(len(lst[0]))]

    for col in range(len(lst[0])):
        for row in range(len(lst)):
            if padding[col] < len(str(lst[row][col])) + 3:
                padding[col] = len(str(lst[row][col])) + 3

    for row in range(len(lst)):
        for col in range(len(lst[0])):
            print(f"{lst[row][col]:<{padding[col]}}", end ="")

        print()


lst = [
    ["ID", "Name", "Surname"],
    ["001", "Guido", "van Rossum"],
    ["002", "Donald", "Knuth"],
    ["003", "Gordon", "Moore"],
]

print_table(lst)
print()

lst = [
    ["X", "Y"],
    [0, 0],
    [10, 10],
    [200, 200],
]
print_table(lst)

# Q5

def isAnagram(s1, s2):
    lst1 = sorted(list(s1))
    lst2 = sorted(list(s2))
    return lst1 == lst2


def main():
    s1 = str(input("Enter the first word: "))
    s2 = str(input("Enter the second word: "))
    if isAnagram(s1, s2):
        print("Is an anagram")
    else:
        print("Is not an anagram")

main()
