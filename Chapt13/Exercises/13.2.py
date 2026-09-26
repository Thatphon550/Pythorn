import os

filename = input("Enter a filename: ").strip()

if not os.path.isfile(filename):
    print("File does not exist.")
else:
    char = 0
    word = 0
    line_count = 0
    infile = open(filename, "r")
    for line in infile:
        line_count += 1
        word += len(line.split())
        for ch in line:
            char += 1
    infile.close()
    print(f"{char} characters")
    print(f"{word} words")
    print(f"{line_count} lines")
