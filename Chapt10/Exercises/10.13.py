def eliminateDuplicate(lst):
    distinctLst = []
    for i in range(len(lst)):
        if lst[i] not in distinctLst:
            distinctLst.append(lst[i])

    return distinctLst

def main():
    n = str(input("Enter ten numbers separated by commas: ")) 
    n = n.split(' ')
    for j in range(len(n)):
        n[j] = int(n[j])

    d = eliminateDuplicate(n)
    print(f"The distinct numbers are: ", end = "")
    for j in range(len(d)):
        print(d[j], end=" ")
        
main()