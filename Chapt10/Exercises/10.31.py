def count(s):
    c = [0 for _ in range(10)]
    for char in s:
        c[ord(char) - ord('0')] += 1

    for i in range(len(c)):
        if c[i]:
            print(f"{i} occurs {c[i]} ", end = "")
            print("time" if c[i] == 1 else "times")

def main():
    string = str(input("Enter a string: "))
    count(string)

main()