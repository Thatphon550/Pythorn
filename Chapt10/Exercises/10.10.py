def reverse(lst):
    lst_rev = []
    for i in lst[::-1]:
        lst_rev.append(i)

    return lst_rev

def main():
    n = str(input("Enter a list of numbers: "))
    n = n.split(' ')
    for j in range(len(n)):
        n[j] = int(n[j])

    print(reverse(n))

main()