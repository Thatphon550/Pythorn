import os

def main():
    path = input("Enter a directory name: ").strip()
    print(get_num(path))

def get_num(path):
    count = 0
    if not os.path.isfile(path):
        lst = os.listdir(path)
        for subdirectory in lst:
            count += get_num(path + "\\" + subdirectory)
    else:
        return 1
    return count

main()
