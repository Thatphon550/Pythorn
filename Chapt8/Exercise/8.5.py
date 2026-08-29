def count(s1, s2):
    count = 0
    for index, char in enumerate(s1):
        if s1[index: index + len(s2)] == s2:
            count += 1
            
    return count
            
def main():
    print(count("system error, syntax error", "error"))
    
main()