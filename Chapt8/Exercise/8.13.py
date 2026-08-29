def prefix(s1, s2):
    pref = ""
    if len(s1) > len(s2):
        s2, s1 = s1, s2
        
    if s1[0].lower() != s2[0].lower():
        return None
    
    for index, char in enumerate(s1):
        if char == " ":
            return pref
        if s2[index].lower() == char.lower():
            pref += s2[index]
            
    return pref

def main():
    
    string1= str(input("Enter the first string: "))
    string2 = str(input("Enter the second string: "))
    
    pref12 = prefix(string1, string2)
    if pref12:
        print(f"The common prefix is: {pref12.title()}")
    else:
        print("No common prefixes")
        
main()