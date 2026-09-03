from tkinter import *

class ProcessButtonEvent:
    def __init__(self):
        window = Tk()
        btOk = Button(window, text = "OK", fg = "red", command = self.processOk)
        btCancel = Button(window, text = "Cancel", bg = "yellow", command = self.processCancel)
        btOk.pack()
        btCancel.pack()
        
        window.mainloop()
        
    def processOk(self):
        print("Ok button is clicked")
    
    def processCancel(self):
        print("Cancel button is clicked")
        
ProcessButtonEvent()
