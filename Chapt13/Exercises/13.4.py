import os, random

filename = input("Enter a filename: ").strip()

if os.path.isfile(filename):
    print("The file already exists")
else:
    outfile = open(filename, "w")
    for i in range(100):
        outfile.write(f"{random.randint(1, 100)} ")
    outfile.close()
