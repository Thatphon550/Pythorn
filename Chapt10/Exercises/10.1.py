def main():
    scores = eval(input("Enter scores: "))

    maxScore = max([x for x in scores if 100 >= x >= 0])
    for (student, score) in enumerate(scores):
        if 100 >= score >= maxScore - 10:
            grade = "A"
        elif maxScore - 10 > score >= maxScore - 20:
            grade = "B"
        elif maxScore - 20 > score >= maxScore - 30:
            grade = "C"
        elif maxScore - 30 > score >= maxScore - 40:
            grade = "D"
        elif maxScore - 40 > score >= 0:
            grade = "F"
        else:
            print(f"Student {student} score is invalid: {score}")
            continue

        print(f"Student {student} score is {score} and grade is {grade}")

main()