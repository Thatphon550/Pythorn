n = str(input("Enter 10 integers: "))
n = n.split()

print("All possible combinations")
for i in range(len(n)):
    for j in range(i + 1, len(n)):
        print(f"({n[i]}, {n[j]})")