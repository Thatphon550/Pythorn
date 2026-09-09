def main():

    strings = [
        "A B A C C D E E A D",
        "D B A B C A E E A D",
        "E D D A C B E E A D",
        "C B A E D C E E A D",
        "A B D C C D E E A D",
        "B B E C C D E E A D",
        "B B A C C D E E A D",
        "E B E C C D E E A D"
    ]

    answers = []
    for student in strings:
        answers.append(student.split(' '))

    keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']

    for i in range(len(answers)):
        correctCount = 0
        for j in range(len(answers[i])):
            if answers[i][j] == keys[j]:
                correctCount += 1

        print(f"Student {i}'s correct count is {correctCount}")
        
main()