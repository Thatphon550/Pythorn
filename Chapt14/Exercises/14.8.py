import os

def main():
    words = set()

    filename = input("Enter a filename: ").strip()
    if os.path.isfile(filename):
        infile = open(filename, "r")
        for word in infile.read().split():
            words.add(word)

        for word in words:
            print(word)
    else:
        print("File doesnt exist")

main()
