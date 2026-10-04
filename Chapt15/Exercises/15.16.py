def count(chars, ch):
    return count_helper(chars, ch, len(chars) - 1)

def count_helper(chars, ch, index):
    if index == 0:
        if ord(chars[0]) == ord(ch):
            return 1
        else:
            return 0
    else:
        if ord(chars[index]) == ord(ch):
            return 1 + count_helper(chars, ch, index - 1)
        else:
            return count_helper(chars, ch, index - 1)


def main():
    print(count(["p", "m"], "m"))

main()
