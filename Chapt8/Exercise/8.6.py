def countLetters(s):
    count = 0
    for char in (s):
        if char == " ":
            continue
        count += 1
        
    return count

def main():
    print(countLetters("python rust"))
    
main()