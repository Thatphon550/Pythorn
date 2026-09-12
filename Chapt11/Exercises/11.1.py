def sumColumn(m, columnIndex):
    c = 0
    for j in range(len(m)):
        c += m[j][columnIndex]

    return c
    

def main():
    matrix = []
    for i in range(3):
        line = str(input(f"Enter a 3-by-4 matrix row for row {i}: "))
        matrix.append([eval(x) for x in line.split()])

    for col in range(4):
        print(f"Sum of the elements for column {col} is {sumColumn(matrix, col)}")

main() 