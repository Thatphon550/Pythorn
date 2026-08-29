def checkPassWord(password):
    if len(password) >= 8:
        countNum = 0
        
        if password.isalnum():
    
            for num in range(1, 10):
                countNum += password.count(str(num))
            if countNum >= 2:
                
                return "Valid Password"
            
    return "Invalid Password"

def main():
    
    while True:
        pas = str(input("Enter password: "))
        print(checkPassWord(pas))

main()