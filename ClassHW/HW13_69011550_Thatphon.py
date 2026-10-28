def perm2(t):
    result = []
    for i in range(len(t)):
        for j in range(len(t)):
            if i != j:
                result.append((t[i], t[j]))
    return result


print(perm2((1, 2, 3)))

def perm3(t):
    result = []
    for i in range(len(t)):
        for j in range(len(t)):
            for k in range(len(t)):
                if t[i] != t[j] and t[i] != t[k] and t[j] != t[k]:
                    result.append((t[i], t[j], t[k]))
    return result

result = perm3((1, 2, 3, 4))
count = 0
for i in result:
    print(i, end=" ")
    count += 1
    if count % 6 == 0:
        print()