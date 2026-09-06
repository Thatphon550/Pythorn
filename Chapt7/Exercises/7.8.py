import time

class StopWatch:
    def __init__(self, startTime, endTime):
        self.__startTime = startTime
        self.__endTime = endTime

    def start(self):
        self.__startTime = time.time()

    def stop(self):
        self.__endTime = time.time()

    def getElapsedTIme(self):
        return self.__endTime - self.__startTime

def main():
    a = StopWatch(1, 1)
    a.start()
    time.sleep(15.4)
    a.stop()
    print(a.getElapsedTIme())

main()