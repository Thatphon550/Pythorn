# Q1
# Q1.1

abbreviation = {"be": "b", "because": "cuz", "see": "c", "the": "da",
                "okay": "ok", "are": "r", "you": "u", "without": "w/o",
                "why": "y", "see you": "cu", "ate": "8", "great": "gr8",
                "mate": "m8", "wait": "w8", "later": "l8r", "tomorrow": "2mro",
                "for": "4", "before": "b4", "once": "1ce", "and": "&",
                "Your": "ur", "You're": "ur", "As far as I know": "afaik",
                "As soon as possible": "ASAP", "At the moment": "atm",
                "Be right back": "brb", "By the way": "btw", "For your information": "FYI",
                "In my humble opinion": "imho", "In my opinion": "imo",
                "Laughing out loud": "lol", "Oh my god": "omg",
                "Rolling on the floor laughing": "rofl", "Talk to you later": "ttyl"}

def textese(s):
    punctuation = ".,!?;:"

    lookup = {}
    for key in abbreviation:
        lookup[key.lower()] = abbreviation[key]
        
    longest = 0
    for key in lookup:
        word_count = len(key.split())
        if word_count > longest:
            longest = word_count

    words = s.split()
    result = []
    i = 0

    while i < len(words):
        size = longest
        if size > len(words) - i:
            size = len(words) - i

        found = False
        while size > 0:
            last_word = words[i + size - 1]
            stripped = last_word.rstrip(punctuation)
            trailing = last_word[len(stripped):]

            phrase_words = words[i:i + size - 1] + [stripped]
            phrase = " ".join(phrase_words).lower()

            if phrase in lookup:
                result.append(lookup[phrase] + trailing)
                i = i + size
                found = True
                break
            size = size - 1

        if not found:
            result.append(words[i])
            i = i + 1

    return " ".join(result)



# Q 1.2

def untextese(s):
    punctuation = ".,!?;:"

    reverse_abbreviation = {}
    for full, abbr in abbreviation.items():
        reverse_abbreviation[abbr.lower()] = full

    expanded = []
    for word in s.split():
        stripped = word.rstrip(punctuation)
        trailing = word[len(stripped):]
        key = stripped.lower()

        if key in reverse_abbreviation:
            expanded.append(reverse_abbreviation[key] + trailing)
        else:
            expanded.append(word)

    return " ".join(expanded)


# Q2

def composite(dict1, dict2):
    composite_dict = {}
    for key1, value1 in dict1.items():
        for key2, value2 in dict2.items():
            if value1 == key2:
                composite_dict[key1] = value2
    return composite_dict

def main():
    dict1 = {'a': 'p', 'b': 'r', 'c': 'q', 'd':'p', 'e':'s'}
    dict2 = {'p': '1', 'q': '2', 'r': '3'}

    print(composite(dict1, dict2))

main()

# Q3

def product(*sets):
    result ={()}
    for current_set in sets:
        new_result = set()
        for combination in result:
            for element in current_set:
                new_result.add(combination + (element,))
        result = new_result

    return result

def main():
    s1 = set([1, 2, 3])
    s2 = set(['p', 'q'])
    s3 = set(['a', 'b', 'c'])

    print(product(s1, s2, s3))
    print()
    print(product(s1))

main()
