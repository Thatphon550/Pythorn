from tkinter import *
import tkinter.messagebox

class InvestmentCalculator:
    def __init__(self):
        window = Tk()
        window.title("Investment Calculator")

        frame = Frame(window)
        frame.pack()

        Label(frame, text="Investment Amount").grid(row=1,column=1,sticky=W)
        Label(frame, text="Years").grid(row=2,column=1,sticky=W)
        Label(frame, text="Annual Interest Rate").grid(row=3,column=1,sticky=W)
        Label(frame, text="Future Value").grid(row=4,column=1,sticky=W)

        

        self.investmentAmount = DoubleVar()
        Entry(frame, textvariable=self.investmentAmount, justify=RIGHT).grid(row=1,column=2)

        self.years = DoubleVar()
        Entry(frame, textvariable=self.years, justify= RIGHT).grid(row = 2, column=2)

        self.annualInterestRate = DoubleVar()
        Entry(frame, textvariable=self.annualInterestRate, justify= RIGHT).grid(row = 3, column=2)

        self.futureValue = StringVar()
        Label(frame, textvariable=self.futureValue, justify=RIGHT).grid(row=4,column=2,sticky=E)

        Button(frame, text="Calculate", command=self.computeValue).grid(row=5,column=2)

        window.mainloop()

    def computeValue(self):
        if not self.investmentAmount.get():
            tkinter.messagebox.showwarning("Error", "Investment Value must be entered.")
            return

        if not self.years.get():
            tkinter.messagebox.showwarning("Error", "Year must be entered.")
            return

        if not self.annualInterestRate.get():
            tkinter.messagebox.showwarning("Error", "Annual Interest Rate must be entered.")
            return
        
        monthlyRate = self.getMonthlyRate()

        value = self.investmentAmount.get() * ((1 + monthlyRate) ** (self.years.get() * 12))
        self.futureValue.set(format(value, "10.2f"))

    def getMonthlyRate(self):
        return ((1 + (self.annualInterestRate.get() / 100)) ** (1 / 12)) - 1
 

InvestmentCalculator()