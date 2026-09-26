import os

filename = input("Enter a filename: ").strip()

infile = open(filename, "r")
count = 0
total = 0
for line in infile:
    scores = [eval(x) for x in line.split()]
    for score in scores:
        total += score
        count += 1
infile.close()
print(f"There are {count} scores")
print(f"The total is {total}")
print(f"The average is {total / count}")
