class Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice
        
    def getName(self):
        return self.__name
    
    def setName(self, name):
        self.__name = name
        
    def getSymbol(self):
        return self.__symbol
    
    def setSymbol(self, symbol):
        self.__symbol = symbol
        
    def getChangePercent(self):
        return 100 - ((self.__currentPrice / self.__previousClosingPrice) * 100)
    
def main():
    
    stock1 = Stock("INTC", "Intel Corporation", previousClosingPrice=20.5,currentPrice= 20.35)
    
    print(f"Price change: {stock1.getChangePercent():.2f}%")
    
main()