import os

filename = input("Enter a filename: ").strip()
if os.path.isfile(filename):
    temp = []
    infile = open(filename, "r")
    for line in infile:
        temp.append(line[:-1])
    infile.close()

    outfile = open(filename, "w")
    for line in temp:
        for ch in line:
            outfile.write(chr(ord(ch) - 5))
        outfile.write("\n")
    outfile.close()
