def count(s, ch):
    
    target = ord(ch)
    count = 0
    
    for char in s:
        if ord(char) == target:
            count += 1
            
    return count

def main():
    
    print(count("helleeo", 'e'))
        
main()