import os

filename = input("Enter a filename: ")
if os.path.isfile(filename):
    infile = open(filename, "r")
    lines = infile.readlines()
    infile.close()

    target = input("Enter the old string to be replaced: ").strip()
    replace = input("Enter the new string to replace the old string: ").strip()
    outfile = open(filename, "w")

    for line in lines:
        for word in line.split():
            if word != target:
                print(word)
                outfile.write(f"{word} ")
            elif word == target:
                outfile.write(f"{replace} ")
        outfile.write("\n")

    outfile.close()
    print("Done")
else:
    print("File does not exist")
