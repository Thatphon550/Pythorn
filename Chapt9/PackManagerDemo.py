from tkinter import*

class PackManagerDemo:
    def __init__(self):
        window = Tk()
        window.title("Pack Manager Demo 1")

        Label(window, text= "Blue", bg = "blue").pack()
        Label(window, text= "Red", bg = "red").pack(fill = BOTH, expand= 1)
        Label(window, text="Greenn", bg = "green").pack(fill = BOTH)

        window.mainloop()

PackManagerDemo()