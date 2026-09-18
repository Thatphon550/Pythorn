rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]

brackets = [
    [8350, 33950, 82250, 171550, 372950],
    [16700, 67900, 137050, 208850, 372950],
    [8350, 33950, 68525, 104425, 186475],
    [11950, 45500, 117450, 190200, 372950]
]

tax = 0

income = eval(input("Enter income: "))
print("Status: 1.Single Filer 2.Married Jointly 3.Married Separately 4.Head of household ")
status = int(input("Enter status: "))

status -= 1
tax = 0

if income < brackets[status][0]:
    tax += income * rates[0]
else:
    tax += brackets[status][0] * rates[0]

for i in range(1, len(brackets[status])):
    if i < len(brackets[status]) - 1:
        if brackets[status][i + 1] > income >= brackets[status][i]:
            tax += (income - brackets[status][i]) * rates[i]
            break
        elif income >= brackets[status][i]:
            tax += (brackets[status][i] - brackets[status][i - 1]) * rates[i]
    else:
        tax += (income - brackets[status][4]) * rates[5]

print(f"Your tax is {tax} $")
