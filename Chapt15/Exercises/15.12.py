def largest(lst):
    return largest_helper(lst, len(lst) - 1)

def largest_helper(lst, i):
    if i == 0:
        return lst[0]
    if lst[i] > largest_helper(lst, i - 1):
        return lst[i]
    else:
        return largest_helper(lst, i - 1)

print(largest([1, 2, 3, 4, 5, 3]))
