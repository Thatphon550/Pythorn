import urllib.request

def main():
    url = input("Enter a URL for a file: ").strip()
    infile = urllib.request.urlopen(url)
    s = infile.read().decode()

    counts = countLetters(s.lower())

    for i in range(len(counts)):
        if counts[i]:
            print(f"{chr(ord('a') + i)} appears {counts[i]} {"time" if counts[i] == 1 else "times"}")

def countLetters(s):
    counts = 26 * [0]
    for ch in s:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1

    return counts

main()
