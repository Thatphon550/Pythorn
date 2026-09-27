import os.path

def main():
    if os.path.isfile("Salary.txt"):
        assistant_total, assistant_count = 0, 0
        associate_total, associate_count = 0, 0
        full_total, full_count = 0, 0
        infile = open("Salary.txt", "r")

        for line in infile:
            info = line.split()
            if info[2] == "assistant":
                assistant_count += 1
                assistant_total += float(info[3])
            elif info[2] == "associate":
                associate_count += 1
                associate_total += float(info[3])
            elif info[2] == "full":
                full_count += 1
                full_total += float(info[3])

        print("----------------------------------")
        print(f"TOTAL SALARY")
        print(f"Assistant Professors: ${assistant_total:.2f}")
        print(f"Associate Professors: ${associate_total:.2f}")
        print(f"Full Professors: ${full_total:.2f}")
        print(f"Faculty total: {assistant_total + associate_total + full_total:.2f}")
        print("----------------------------------")
        print(f"AVERAGE SALARY")
        print(f"Assistant Professors: ${assistant_total / assistant_count:.2f}")
        print(f"Associate Professors: ${associate_total / associate_count:.2f}")
        print(f"Full Professors: ${full_total / full_count:.2f}")
        print(f"Faculty average: ${(assistant_total + associate_total + full_total) / (assistant_count + assistant_count + full_count):.2f}")
        print("----------------------------------")

main()
