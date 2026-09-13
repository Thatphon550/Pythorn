import random

def game():
    words = ["write", "that", "program", "python", "awesome", "computer", "science", "software", "engineering", "monitor"]
    rand = random.randint(0, len(words) - 1)
    target = [c for c in words[rand]]
    answer = [None for _ in range(len(target))]

    missed = 0
    while True:
        print("(Guess) Enter a letter in word ", end = "")
        for c in answer:
            if c:
                print(c, end="")
            else:
                print("*", end = "")
        char = str(input(" > "))
        if char not in target:
            print(f"{char} is not in the word")
            missed += 1
            continue
        elif answer.count(char) >= target.count(char):
            print(f"{char} is already in the word")
            continue
 
        index = []
        for i in range(len(answer)):
            if target[i] == char:
                index.append(i)

        for slot in range(len(answer)):
            if slot in index and answer[slot]:
                continue
            elif slot in index and not answer[slot]:
                answer[slot] = char
                break
        
        if None not in answer:
            break

    print(f"The word is {words[rand]}. You missed {missed} ", end = "")
    print("time" if missed <= 1 else "times")

def main():
    while True:
        game()
        decision = input("Do you want to guess another word? Enter y or n > ")
        if decision != "y":
            break

main()