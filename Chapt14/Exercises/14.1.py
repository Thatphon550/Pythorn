import os.path
import sys

def main():
    keyWords = {"and", "as", "assert", "break", "class",
                "continue", "def", "del", "elif", "else",
                "except", "False", "finally", "for", "from",
                "global", "if", "import", "in", "is", "lambda",
                "None", "nonlocal", "not", "or", "pass", "raise",
                "return", "True", "try", "while", "with", "yield"}

    lst = list(keyWords)
    c = 0
    print("=============== Python Keywords ===============")
    KEYWORDS_PER_LINE = 5
    for i in range(len(keyWords)):
        c += 1
        print(f"{lst[i]:<10}", end= "")
        if c % KEYWORDS_PER_LINE == 0:
            print()
    print()
    print("===============================================")

    filename = input("Enter a Python source code filename: ").strip()

    if not os.path.isfile(filename):
        print("File", filename, "does not exist")
        sys.exit()

    infile = open(filename, "r")

    text = infile.read().split()

    count = 0
    for word in text:
        if word in keyWords:
            count += 1

    print("The number of keywords in", filename, "is", count)

main()
