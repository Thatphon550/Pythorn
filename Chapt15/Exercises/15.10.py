def count(s, a):
    if len(s) == 1:
        if s == a:
            return 1
        else:
            return 0

    if s.startswith(a):
        return 1 + count(s[1:], a)
    else:
        return count(s[1:], a)

print(count("Welcome", "e"))
