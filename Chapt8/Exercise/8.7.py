def getNumber(uppercaseLetter):
    
    numberStr = ""
    for char in uppercaseLetter:
        if (48 <= ord(char) <= 57) or char == "-":
            numberStr += char
        else:
            if 97 <= ord(char.lower()) <= 99:
                numberStr += "2"
            elif 100 <= ord(char.lower()) <= 102:
                numberStr += "3"
            elif 103 <= ord(char.lower()) <= 105:
                numberStr += "4"
            elif 106 <= ord(char.lower()) <= 108:
                numberStr += "5"
            elif 109 <= ord(char.lower()) <= 111:
                numberStr += "6"
            elif 112 <= ord(char.lower()) <= 115:
                numberStr += "7"
            elif 116 <= ord(char.lower()) <= 118:
                numberStr += "8"
            elif 119 <= ord(char.lower()) <= 122:
                numberStr += "9"
            elif char == " ":
                numberStr += "0"
    return numberStr
                        
            
    
def main():
    
    string = str(input("Enter a string: "))
    
    print(getNumber(string))

main()