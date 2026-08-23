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
    
    account1 = Account(
        id = 1122,
        initialBalance=20000,
        annualInterestRate=4.5,
    )
    
    account1.withdraw(2500)
    account1.deposit(3000)
    print(f"Account ID {account1.getID()}")
    print(f"Balance: {account1.getBalance()}")
    print(f"Monthly Interest Rate: {account1.getMonthlyInterestRate():.2f}%")
    print(f"Monthly Interest: ${account1.getMonthlyInterest():.2f}")
    
main()