def isConsecutiveFour(values):
    for i in range(len(values) - 3):
        if values[i] == values[i + 1] == values[i + 2] == values[i + 3]:
            return True
    return False

def main():
    line = input("Enter a series of integers: ").strip().split()
    values = [eval(x) for x in line]
    if isConsecutiveFour(values):
        print("The series contains four consecutive numbers with the same value.")
    else:
        print("The series does not contain four consecutive numbers with the same value.")

main()