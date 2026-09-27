def count_uppercase(s):
    return count_uppercase_helper(s, len(s) - 1)

def count_uppercase_helper(s, high):
    if high == 0:
        if s[high].isupper():
            return 1
        else:
            return 0
    if s[high].isupper():
        return 1 + count_uppercase_helper(s, high - 1)
    else:
        return count_uppercase_helper(s, high - 1)

print(count_uppercase("AbcDEffff GdgsGR zdfgb"))
