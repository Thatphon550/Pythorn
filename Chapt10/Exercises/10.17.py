def isAnagram(s1, s2):
    lst1 = sorted(list(s1))
    lst2 = sorted(list(s2))
    return lst1 == lst2


def main():
    s1 = str(input("Enter the first word: "))
    s2 = str(input("Enter the second word: "))
    if isAnagram(s1, s2):
        print("Is an anagram")
    else:
        print("Is not an anagram")

main()