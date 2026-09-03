from tkinter import *

def processOk():
    print("Ok button is clicked")
    
def processCancel():
    print("Cancel button is clicked")
    
window = Tk()
btOk = Button(window, text = "Ok", fg = "red", command = processOk)
btCancel = Button(window, text = "Cancel", bg = "yellow", command = processCancel)

btOk.pack()
btCancel.pack()

window.mainloop()