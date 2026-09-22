set1 = {"green", "red", "blue", "red"}
print(set1)

set2 = set([7, 1, 2, 23, 2, 4, 5])
print(set2)

print(f"Is red in set1? {"red" in set1}")

print(f"length is {len(set2)}")
print(f"max is {max(set2)}")
print(f"min is {min(set2)}")
print(f"sum is {sum(set2)}")

set3 = set1 | {"green", "yellow"}
print(set3)

set3 = set1 - {"green", "yellow"}
print(set3)


set3 = set1 & {"green", "yellow"}
print(set3)

set3 = set1 ^ {"green", "yellow"}
print(set3)

list1 = list(set2)
print(set1 == {"green", "red", "blue"})

set1.add("yellow")
print(set1)

set1.remove("yellow")
print(set1)
