import os.path

def main():
    vowels = {"A", "E", "I", "O", "U"}
    vowel_count = 0
    consonant_count = 0
    filename = input("Enter a filename: ")
    if os.path.isfile(filename):
        infile = open(filename, "r")
        for ch in infile.read():
            if not ord('a') <= ord(ch.lower()) <= ord('z'):
                continue
            else:
                if ch.upper() in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
        print(f"Total vowels: {vowel_count}")
        print(f"Total consonants: {consonant_count}")
    else:
        print("The file does not exist")

main()
