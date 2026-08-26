def getText(num):
    if num < 0 or num > 999:
        return "I don't know"
    
    if len(str(num)) >= 1:
        if num % 10 == 0 and num != 10:
            digit1 = "zero"
        elif num % 10 == 1:
            digit1 = "one"
        elif num % 10 == 2:
            digit1 = "two"
        elif num % 10 == 3:
            digit1 = "three"
        elif num % 10 == 4:
            digit1 = "four"
        elif num % 10 == 5:
            digit1 = "five"
        elif num % 10 == 6:
            digit1 = "six"
        elif num % 10 == 7:
            digit1 = "seven"
        elif num % 10 == 8:
            digit1 = "eight"
        elif num % 10 == 9:
            digit1 = "nine"
        elif num == 10:
            return "ten"

        if len(str(num)) >= 2:
            num2 = num // 10

                
            if num2 % 10 == 1 and num < 100:
                if num == 11:
                    return "eleven"
                elif num == 12:
                    return "twelve"
                elif num == 13:
                    return "thirteen"
                elif num ==  15:
                    return "fifteen"
                elif num == 18:
                    return "eighteen"
                
                return digit1 + "teen"
                
            elif num2 % 10 == 2:
                digit2 = "twenty"
            elif num2 % 10 == 3:
                digit2 = "thirty"
            elif num2 % 10 == 4:
                digit2 = "forty"
            elif num2 % 10 == 5:
                digit2 = "fifty"
            elif num2 % 10 == 6:
                digit2 = "sixty"
            elif num2 % 10 == 7:
                digit2 = "seventy"
            elif num2 % 10 == 8:
                digit2 = "eighty"
            elif num2 % 10 == 9:
                digit2 = "ninety"
            
            
            if len(str(num)) >= 3:
                if num == 100:
                    return "one hundred"
                num3 = num // 100
                if num3 % 100  == 1:
                    digit3 = "one hundred"
                elif num3 == 2:
                    digit3 = "two hundred"
                elif num3 == 3:
                    digit3 = "three hundred"
                elif num3 == 4:
                    digit3 = "four hundred"
                elif num3 == 5:
                    digit3 = "five hundred"
                elif num3 == 6:
                    digit3 = "six hundred"
                elif num3 == 7:
                    digit3 = "seven hundred"
                elif num3 == 8:
                    digit3 = "eight hundred"
                elif num3 == 9:
                    digit3 = "nine hundred"
                    
                if num2 % 10 == 1:
                    if num % 10 == 1:
                        digit2 = "eleven"
                    elif num % 10 == 2:
                        digit2 = "twelve"
                    elif num % 10 == 3:
                        digit2 = "thirteen"
                    elif num % 10 ==  5:
                        digit2 = "fifteen"
                    elif num % 10 == 8:
                        digit2 = "eighteen"
                    elif num % 10 == 0:
                        digit2 = "ten"
                    else:
                        digit2 = digit1 + "teen"
                    return f"{digit3} and {digit2}"
                
                if num % 100 == 0:
                    return f"{digit3}"
                
                if 1 <= num % 100 <= 9:
                    return f"{digit3} and {digit1}"
                
                if num % 10 == 0:
                    return f"{digit3} and {digit2}"
                
                return f"{digit3} and {digit2} {digit1}"
               
            
            if num % 10 == 0 and num < 100:
                return f"{digit2}"
            return f"{digit2} {digit1}"
             
        return f"{digit1}"
        
    
    

def main():
    # while True:
    #     num = int(input("Enter a number: "))
    #     print(getText(num))
    
    for num in range(1, 1000):
        print(getText(num))
    
main()