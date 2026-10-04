def display_permutation(s):
    display_permutation_helper("", s)

def display_permutation_helper(s1, s2):
    if len(s1) == len(s2):
        print(s1)
        return
    for i in range(len(s2)):
        if s2[i] not in s1:
            display_permutation_helper(s1 + s2[i], s2)


def show_permutations(built, remaining):
    if remaining == "":
        print(built)
        return

    for i in range(len(remaining)):
        letter = remaining[i]
        rest = remaining[:i] + remaining[i + 1:]
        show_permutations(built + letter, rest)

show_permutations("", "aab")
