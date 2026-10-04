def count(chars):
    return count_helper(chars, len(chars) - 1)

def count_helper(chars, index):
    if index == 0:
        if chars[0].isupper():
            return 1
        else:
            return 0
    else:
        if chars[index].isupper():
            return 1 + count_helper(chars, index - 1)
        else:
            return count_helper(chars, index - 1)

def main():
    print(count("aNNNbfdHFSDGesdrtghxdfgtrzzhtfgsgrrzgtrfGFFg"))

main()
