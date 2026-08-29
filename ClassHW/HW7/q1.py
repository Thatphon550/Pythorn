import time

class Clock:
    def __init__(self, hour, minute, second):
        if 0 <= hour <= 23:
            self.hour = hour
        else:
            print("Hour Invalid")
        if 0 <= minute <= 59:
            self.minute = minute
        else:
            print("Minutes Invalid")
        if 0 <= second <= 59:
            self.second = second
        else:
            print("Seconds Invalid")
        
    def setTime(self, hour, minute, second):
        if 0 <= hour <= 23:
            self.hour = hour
        else:
            print("Hour Invalid")
        if 0 <= minute <= 59:
            self.minute = minute
        else:
            print("Minutes Invalid")
        if 0 <= second <= 59:
            self.second = second
        else:
            print("Seconds Invalid")
        
    def getTime(self):
        displayedTime = "PM"
        displayedHour = self.hour
        if self.hour >= 12:
            displayedTime = "PM"
            displayedHour = self.hour % 12
        else:
            if self.hour == 0:
                displayedHour = 12
            displayedTime = "AM"
        
        if displayedHour < 10:
            if self.minute < 10:
                if self.second < 10:
                    print(f"0{displayedHour}:0{self.minute}:0{self.second} {displayedTime}")
                else:
                    print(f"0{displayedHour}:0{self.minute}:{self.second} {displayedTime}")
            else:
                if self.second < 10:
                    print(f"0{displayedHour}:{self.minute}:0{self.second} {displayedTime}")
                else:
                    print(f"0{displayedHour}:{self.minute}:{self.second} {displayedTime}")
        else:
            if self.minute < 10:
                if self.second < 10:
                    print(f"{displayedHour}:0{self.minute}:0{self.second} {displayedTime}")
                else:
                    print(f"{displayedHour}:0{self.minute}:{self.second} {displayedTime}")
            else:
                if self.second < 10:
                    print(f"{displayedHour}:{self.minute}:0{self.second} {displayedTime}")
                else:
                    print(f"{displayedHour}:{self.minute}:{self.second} {displayedTime}")
                    
    def tick(self):
        if self.second == 59:
            if self.minute == 59:
                if self.hour == 23:
                    self.hour = 0
                    self.minute = 0
                    self.second = 0
                    return
                
                self.second = 0
                self.minute = 0
                self.hour += 1
                return
            
            self.second = 0
            self.minute += 1
            return
        else:
            self.second += 1

                
def main():
    currentTime = Clock(0, 0, 0)
    while True:
        currentTime.getTime()
        time.sleep(1)
        currentTime.tick()
    
main()