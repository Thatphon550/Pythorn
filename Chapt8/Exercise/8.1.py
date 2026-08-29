def checkSSN(string):
    if len(string) != 11:
        return "Invalid SSN"
    
    index0_2 = string[:3]
    hyphen3 = string[3]
    index4_5 = string[4:6]
    hyphen6 = string[6]
    index7_10 = string[7:11]
    
    if index0_2.isalnum() and hyphen3 == "-" and index4_5.isalnum() and hyphen6 == "-" and index7_10.isalnum():
        return "Valid SSN"
    else:
        return "Invalid SSN"
        

def main():
    ssn = str(input("Enter a Social Security number in the format ddd-dd-dddd: "))
    
    print(checkSSN(ssn))
    
main()

