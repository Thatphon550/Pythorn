count = 0

n = eval(input("Enter an index: "))

f0 = 0
f1 = 1

for i in range(2, n + 1):
    count += 1
    current_fib = f0 + f1
    f0 = f1
    f1 = current_fib

print(f"fib({n}) is {current_fib}")
print(count)
