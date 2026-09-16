class Account:
    def __init__(self, id=0, initialBalance=100, annualInterestRate=0):
        self.__id = id
        self.__balance = initialBalance
        self.__annualInterestRate = annualInterestRate

    def getID(self):
        return self.__id

    def setID(self, id):
        self.__id = id

    def getBalance(self):
        return self.__balance

    def setBalance(self, balance):
        self.__balance = balance

    def getAnnualInterestRate(self):
        return self.__annualInterestRate

    def setAnnualInterestRate(self, annualInterestRate):
        self.__annualInterestRate = annualInterestRate

    def getMonthlyInterestRate(self):
        return (self.__annualInterestRate / 12)

    def getMonthlyInterest(self):
        return self.__balance * (self.getMonthlyInterestRate() / 100)

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

def main():
    lst = [Account(id = i) for i in range(10)]

    accountID = int(input("Enter an account id: "))
    currentAcc = lst[accountID]
    while True:

        if 0 <= accountID <= 9:
            print("\nMain menu")
            print("1: check balance")
            print("2: withdraw")
            print("3: deposit")
            print("4: exit")
            choice = int(input("Enter a choice: "))
            if choice == 1:
                print(f"\nThe balance is {currentAcc.getBalance():.2f}")
            elif choice == 2:
                amount = eval(input("Enter an amount to withdraw: "))
                if amount > currentAcc.getBalance() or amount <= 0:
                    print("Invalid Amount")
                    continue
                currentAcc.withdraw(amount)
                print(f"The balance is {currentAcc.getBalance():.2f}")
            elif choice == 3:
                amount = eval(input("Enter an amount to withdraw: "))
                if amount <= 0:
                    print("Invalid Amount")
                    continue

                currentAcc.deposit(amount)
                print(f"The balance is {currentAcc.getBalance():.2f}")
            elif choice == 4:
                accountID = int(input("Enter an account id: "))
                currentAcc = lst[accountID]
                continue
        else:
            print("Invalid ID")
            accountID = int(input("Enter an account id: "))
            currentAcc = lst[accountID]

main()
