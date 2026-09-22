import os.path

name = input("Enter a filename: ")

if os.path.isfile(name):
    infile = open(name, "r")
    string = infile.readlines()
    infile.close()
    outfile = open(name, "w")
    target = input("Enter the string to be removed: ")
    for i in string:
        if i[:-1] == target:
            continue
        else:
            outfile.write(i)
    outfile.close()
    print("Done")
else:
    print("The given filename doesn't exist")
