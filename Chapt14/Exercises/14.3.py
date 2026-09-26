import os
import sys

keyWords = {"and", "as", "assert", "break", "class",
            "continue", "def", "del", "elif", "else",
            "except", "False", "finally", "for", "from",
            "global", "if", "import", "in", "is", "lambda",
            "None", "nonlocal", "not", "or", "pass", "raise",
            "return", "True", "try", "while", "with", "yield"}

filename = input("Enter a filename: ").strip()
if not os.path.isfile(filename):
    print(f"The file {filename} does not exist")
    sys.exit()

infile = open(filename, "r")
text = infile.read().split()

kw_count = {}

for word in text:
    if word in keyWords:
        if word in kw_count:
            kw_count[word] += 1
        else:
            kw_count[word] = 1

print(kw_count)
