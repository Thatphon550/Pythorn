from tkinter import *
import math
import time

def getTime():
    currentTime = time.time()
    currentTime += 3600 * 7
    seconds = int(currentTime % 60)
    currentTime //= 60
    minutes = int(currentTime % 60)
    currentTime //= 60
    hours = int(currentTime % 24)
    string = ""
    string += f"0{hours}:" if hours < 10 else f"{hours}:"
    string += f"0{minutes}:" if minutes < 10 else f"{minutes}:"
    string += f"0{seconds}" if seconds < 10 else f"{seconds}"
    return string, time.time()

print(getTime())

class Clock:
    def __init__(self):
        window = Tk()
        window.title("Current Time")
        currentTime, raw = getTime()
        raw += 3600 * 7
        self.hours = currentTime[:2]
        self.minutes = currentTime[3:5]
        self.seconds = currentTime[6:]

        self.canvas = Canvas(window, width=500, height=500, bg="white")
        self.canvas.pack()

        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, text= currentTime, bg = "white", font=15).pack()

        self.radius = 220
        self.x = 250
        self.y = 250

        self.canvas.create_oval(self.x - self.radius, self.y - self.radius,
                                self.x + self.radius, self.y + self.radius)
        
        self.canvas.create_text(self.x + self.radius - 20, self.y, text="3", font=14)
        self.canvas.create_text(self.x, self.y  + self.radius - 20, text="6", font=14)
        self.canvas.create_text(self.x - self.radius + 20, self.y, text="9", font=14)
        self.canvas.create_text(self.x, self.y  - self.radius + 20, text="12", font=14)

        secondsArmLen = 200
        
        seconds = raw % 60
        raw //= 60
        radiansSec = math.radians((seconds / 60) * 360)
        secondsArmX = math.sin(radiansSec)
        secondsArmY = math.cos(radiansSec)
        self.canvas.create_line(250, 250, 250 + secondsArmLen * secondsArmX,
                                 250 - secondsArmLen *secondsArmY)
        minutes = raw % 60
        raw //= 60
        radiansMin = math.radians((minutes / 60) * 360)
        minArmX = math.sin(radiansMin)
        minArmY = math.cos(radiansMin)
        minArmLen = 140
        self.canvas.create_line(250, 250, 250 + minArmLen * minArmX,
                                         250 - minArmLen * minArmY, width=3)

        hours = raw % 24
        radiansHr = math.radians((hours / 12) * 360)
        hrArmX = math.sin(radiansHr)
        hrArmY = math.cos(radiansHr)
        hrArmLen = 90
        self.canvas.create_line(250, 250, 250 + hrArmLen * hrArmX,
                                250 - hrArmLen * hrArmY, width=7)

        window.mainloop()

Clock()