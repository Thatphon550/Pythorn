import time

class Time:
    def __init__(self):
        currentTime = time.time()
        self.time = currentTime
        self.seconds = int(currentTime % 60)
        currentTime //= 60

        self.minutes = int(currentTime % 60)
        currentTime //= 60

        self.hours = int(currentTime % 24)

    def printTime(self):
        string = ""
        string += f"0{self.hours}:" if self.hours < 10 else f"{self.hours}:"
        string += f"0{self.minutes}:" if self.minutes < 10 else f"{self.minutes}:"
        string += f"0{self.seconds}" if self.seconds < 10 else f"{self.seconds}"

        return string

    def setTime(self, elapseTime):
        self.time += elapseTime
        self.seconds = int(self.time % 60)
        self.time //= 60
        
        self.minutes = int(self.time % 60)
        self.time //= 60
        
        self.hours = int(self.time % 24)

    def getSeconds(self):
        return self.seconds

    def getMinutes(self):
        return self.minutes

    def getHours(self):
        return self.seconds

def main():
    time1 = Time()
    print(f"Current time is {time1.printTime()}")
    elapse = eval(input("Enter elapsed time: "))
    time1.setTime(elapse)
    print(f"The hour:minute:second for the elapsed time is {time1.printTime()}")

main()