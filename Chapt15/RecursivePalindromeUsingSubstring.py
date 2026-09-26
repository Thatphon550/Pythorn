def isPalindrome(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[len(s) - 1]:
        return False
    else:
        return isPalindrome(s[1: len(s) - 1])

def main():
    print(f"Is moon a palindrome? {isPalindrome("moon")}")
    print(f"Is noon a palindrome? {isPalindrome("noon")}")
    print(f"Is a a palindrome? {isPalindrome("a")}")
    print(f"Is aba a palindrome? {isPalindrome("aba")}")

main()
