def reverse(s):
    return s[::-1]

def main():
    while True:
        string = str(input("Enter a string: "))
        print(f"The reverse of your string is {reverse(string)}")
        
main()