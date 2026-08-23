class Account:
    def __init__(self, amount=0, locked=False):
        self.__balance = amount
        self.__locked = locked
        
    def withdraw(self, amount):
        if self.__locked:
            print("Error: Account is locked")
        elif amount > self.__balance:
            print("Error: Insufficienet funds")
        elif amount < 0:
            print("Error: Invalid number")
        else:
            self.__balance -= amount
            print(f"Successfully withdrew {amount}")
        
    def deposit(self, amount):
        if self.__locked:
            print("Error: Account is locked")
        elif amount < 0:
            print("Error: Invalid number")
        else:
            self.__balance += amount
            print(f"Successfully deposited {amount}")
            
    def checkBalance(self):
        return self.__balance
    
    def checkLocked(self):
        return self.__locked
    
def main():
    myAccount = Account(amount=500, locked=False)
    
    while True:
        print("\n=== ATM Machine ===")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        action = eval(input("Enter your desired menu: "))
        
        if action == 1:
            depositAmount = eval(input("Enter deposit amount: "))
            myAccount.deposit(depositAmount)
        elif action == 2:
            withdrawAmount = eval(input("Enter withdraw amount: "))
            myAccount.withdraw(withdrawAmount)
        elif action == 3:
            print(f"Current balance: {myAccount.checkBalance()}")
main()