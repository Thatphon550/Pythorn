# Q1

import time

class Clock:
    def __init__(self, hh, mm, ss):
        self.hh = self._checkHour(hh)
        self.mm = self._check(mm)
        self.ss = self._check(ss)

    def run(self):
        time.sleep(1)
        if self.ss == 59:
            if self.mm == 59:
                if self.hh == 23:
                    self.hh = 0
                    self.mm = 0
                    self.ss = 0
                else:
                    self.hh += 1
                    self.mm = 0
                    self.ss = 0
            else:
                self.mm += 1
                self.ss = 0
        else:
            self.ss += 1

        print(f"0{self.hh}" if self.hh < 10 else f"{self.hh}", end=":")
        print(f"0{self.mm}" if self.mm < 10 else f"{self.mm}", end=":")
        print(f"0{self.ss}" if self.ss < 10 else f"{self.ss}")


    def set_time(self, h, m, s):
        self.h = self._checkHour(h)
        self.m = self._check(m)
        self.s = self._check(s)

    def _checkHour(self, hh):
        if not 0 <= hh <= 23:
            raise ValueError
        return hh

    def _check(self, value):
        if not 0 <= value <= 59:
            raise ValueError
        return value

class AlarmClock(Clock):
    def __init__(self, hh, mm, ss, alarm_hh, alarm_mm, alarm_ss):
        super().__init__(hh, mm, ss)
        self.alarm_hh = self._checkHour(alarm_hh)
        self.alarm_mm = self._check(alarm_mm)
        self.alarm_ss = self._check(alarm_ss)
        self.alarm_on_off = False
        self.stopped = False

    def setAlarmTime(self, h, m, s):
        self.alarm_hh = self._checkHour(h)
        self.alarm_mm = self._check(m)
        self.alarm_ss = self._check(s)

    def alarm_on(self):
        self.alarm_on_off = True

    def alarm_off(self):
        self.alarm_on_off = False

    def run(self):
        while not self.stopped:
            super().run()
            if self.alarm_on_off:
                if self.hh == self.alarm_hh and self.mm == self.alarm_mm and self.ss == self.alarm_ss:
                    print("Alarm!")
                    self.stopped = True

def main():
    c = AlarmClock(22, 10, 15, 22, 10, 25)
    c.alarm_on()
    c.run()

main()

# Q2

import turtle

def RobotBattle():
    #robotList stores the list of robots in the battle
    robotList = []

    while True:
        #Clear the screen and draw the robots
        turtle.clear()
        for robot in robotList:
            robot.draw()

        #Display the status of each robot
        print("==== Robots ====")
        i=0
        for robot in robotList:
            print(i, " : ")
            robot.displayStatus()
            i+=1
        print("===============")

        #Ask user which robot to command or to create a new robot
        choice = input("Enter which robot to order, 'c' to create new robot, 'q' to quit: ")
        if choice == "q":
            break
        elif choice == "c":
            print("Enter which type of robots to create")
            robotType = input("'r' for Robot, 'm' for MedicBot, 's' for StrikerBot: ")
            if robotType == "r":
                newRobot = Robot()
            elif robotType == "m":
                newRobot = MedicBot()
            elif robotType == "s":
                newRobot = StrikerBot()
            robotList = robotList + [newRobot]
        else:
            n = int(choice)
            robotList[n].command(robotList)

        #Delete all the robots with health <= 0 from the list
        i=0
        for robot in robotList:
            if(robot.health <=0):
                del robotList[i]
            i+=1

class Robot(object):
    RADIUS = 15
    def __init__(self):
        self.x = 100
        self.y = 100
        self.health = 100
        self.energy = 100

    def move(self, x, y):
        if self.energy <= 0:
            return
        self.x = x
        self.y = y
        self.energy -= 10

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.setheading(90)
        turtle.forward(self.RADIUS)
        turtle.left(90)
        turtle.pendown()
        turtle.circle(self.RADIUS)
        turtle.penup()

    def displayStatus(self):
        print("x=", self.x, "y=", self.y, "health=", self.health, "energy=", self.energy)

    def command(self, robotList):
        print("Possible actions: move")
        newX = int(input("Enter new x-coordinate: "))
        newY = int(input("Enter new y-coordinate: "))
        self.move(newX,newY)

    def _distance(self, r: "Robot") -> float:
        return (((self.x - r.x) ** 2) + ((self.y - r.y) ** 2)) ** (1 / 2)

class MedicBot(Robot):
    def draw(self):
        super().draw()
        arm = self.RADIUS * 0.6
        turtle.goto(self.x - arm, self.y)
        turtle.pendown()
        turtle.goto(self.x + arm, self.y)
        turtle.penup()
        turtle.goto(self.x, self.y - arm)
        turtle.pendown()
        turtle.goto(self.x, self.y + arm)
        turtle.penup()

    def heal(self, r: Robot):
        if self.energy < 20 or self._distance(r) > 10:
            return
        self.energy -= 20
        r.health += 10

    def command(self, robotList):
        print("Possible actions: move, heal")
        action = input("Enter action (move/heal): ").strip().lower()
        if action == "move":
            newX = int(input("Enter new x-coordinate: "))
            newY = int(input("Enter new y-coordinate: "))
            self.move(newX, newY)
        elif action == "heal":
            if len(robotList) < 2:
                print("No other robots to heal")
                return
            while True:
                n = int(input("Choose which robot to heal: "))
                if n in range(len(robotList)) and robotList[n] is not self:
                    break
                print("Invalid choice")
            self.heal(robotList[n])
        else:
            print("Unknown action")

class StrikerBot(Robot):
    def __init__(self):
        super().__init__()
        self.missile = 5

    def draw(self):
        super().draw()
        d = self.RADIUS * 0.6
        corners = [
            (self.x, self.y + d),
            (self.x + d, self.y),
            (self.x, self.y - d),
            (self.x - d, self.y),
        ]
        turtle.goto(corners[-1])
        turtle.pendown()
        for corner in corners:
            turtle.goto(corner)
        turtle.penup()

    def strike(self, r: Robot):
        if self.energy < 20 or self.missile <= 0 or self._distance(r) > 10:
            return
        self.energy -= 20
        self.missile -= 1
        r.health -= 50

    def displayStatus(self):
        print("x=", self.x, "y=", self.y, "health=", self.health, "energy=", self.energy, "missile=", self.missile)

    def command(self, robotList):
        print("Possible actions: move, strike")
        action = input("Enter action (move/strike): ").strip().lower()
        if action == "move":
            newX = int(input("Enter new x-coordinate: "))
            newY = int(input("Enter new y-coordinate: "))
            self.move(newX,newY)
        elif action == "strike":
            if len(robotList) < 2:
                print("No other robots to strike")
                return
            while True:
                n = int(input("Choose which robot to strike: "))
                if n in range(len(robotList)) and robotList[n] is not self:
                    break
                print("Invalid choice")
            self.strike(robotList[n])
        else:
            print("Unknown action")

RobotBattle()

# Q3

class Rectangle2D:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def getRectangle(points: list) -> Rectangle2D:
    left_x = min(point.x for point in points)
    right_x = max(point.x for point in points)
    top_y = max(point.y for point in points)
    bottom_y = min(point.y for point in points)

    x = (left_x + right_x) / 2
    y = (top_y + bottom_y) / 2

    return Rectangle2D(abs(left_x - right_x), abs(top_y - bottom_y), x, y)

def main():
    line = input("Enter the points: ").split()
    points = []
    for i in range(0, len(line), 2):
        points.append(Point(eval(line[i]), eval(line[i + 1])))
    bounding = getRectangle(points)
    print(f"The bounding rectangle is centered at ({bounding.x}, {bounding.y}) with width {bounding.width} and height {bounding.height}")


main()

# Q4

import turtle
from abc import ABCMeta, abstractmethod

def drawLine(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

class Char(object, metaclass = ABCMeta):
    @abstractmethod
    def draw(self, x, y):
        pass

    @abstractmethod
    def getWidth(self):
        pass

class Char0(Char):
    def __init__(self):
        self.__width = 20

    def draw(self, x, y):
        drawLine(x, y, x + 20, y)
        drawLine(x + 20, y, x + 20, y + 40)
        drawLine(x + 20, y + 40, x, y + 40)
        drawLine(x, y + 40, x, y)

    def getWidth(self):
        return self.__width

class Char1(Char):
    def __init__(self):
        self.__width = 20

    def draw(self, x, y):
        drawLine(x + 10, y, x + 10, y + 40)

    def getWidth(self):
        return self.__width

class Char2(Char):
    def __init__(self):
        self.__width = 20

    def draw(self, x, y):
        drawLine(x, y + 40, x + 20, y + 40)
        drawLine(x + 20, y + 40, x + 20, y + 20)
        drawLine(x + 20, y + 20, x, y + 20)
        drawLine(x, y + 20, x, y)
        drawLine(x, y, x + 20, y)

    def getWidth(self):
        return self.__width

class Char3(Char):
    def __init__(self):
        self.__width = 20

    def draw(self, x, y):
        drawLine(x, y + 40, x + 20, y + 40)
        drawLine(x + 20, y + 40, x + 20, y)
        drawLine(x + 20, y, x, y)
        drawLine(x, y + 20, x + 20, y + 20)

    def getWidth(self):
        return self.__width

class Char4(Char):
    def __init__(self):
        self.__width = 20

    def draw(self, x, y):
        drawLine(x, y + 40, x, y + 20)
        drawLine(x, y + 20, x + 20, y + 20)
        drawLine(x + 20, y + 40, x + 20, y)

    def getWidth(self):
        return self.__width

class Char5(Char):
    def __init__(self):
        self.__width = 20

    def draw(self, x, y):
        drawLine(x + 20, y + 40, x, y + 40)
        drawLine(x, y + 40, x, y + 20)
        drawLine(x, y + 20, x + 20, y + 20)
        drawLine(x + 20, y + 20, x + 20, y)
        drawLine(x + 20, y, x, y)

    def getWidth(self):
        return self.__width

class Char6(Char):
    def __init__(self):
        self.__width = 20

    def draw(self, x, y):
        drawLine(x + 20, y + 40, x, y + 40)
        drawLine(x, y + 40, x, y)
        drawLine(x, y, x + 20, y)
        drawLine(x + 20, y, x + 20, y + 20)
        drawLine(x + 20, y + 20, x, y + 20)

    def getWidth(self):
        return self.__width

class Char7(Char):
    def __init__(self):
        self.__width = 20

    def draw(self, x, y):
        drawLine(x, y + 40, x + 20, y + 40)
        drawLine(x + 20, y + 40, x + 20, y)

    def getWidth(self):
        return self.__width

class Char8(Char):
    def __init__(self):
        self.__width = 20

    def draw(self, x, y):
        drawLine(x, y, x + 20, y)
        drawLine(x + 20, y, x + 20, y + 40)
        drawLine(x + 20, y + 40, x, y + 40)
        drawLine(x, y + 40, x, y)
        drawLine(x, y + 20, x + 20, y + 20)

    def getWidth(self):
        return self.__width

class Char9(Char):
    def __init__(self):
        self.__width = 20

    def draw(self, x, y):
        drawLine(x + 20, y + 20, x, y + 20)
        drawLine(x, y + 20, x, y + 40)
        drawLine(x, y + 40, x + 20, y + 40)
        drawLine(x + 20, y + 40, x + 20, y)
        drawLine(x + 20, y, x, y)

    def getWidth(self):
        return self.__width

def drawNum(x):
    chars = {0: Char0(), 1: Char1(), 2: Char2(), 3: Char3(), 4: Char4(),
             5: Char5(), 6: Char6(), 7: Char7(), 8: Char8(), 9: Char9()}

    xPos = -200
    for digit in str(x):
        c = chars[int(digit)]
        c.draw(xPos, 0)
        xPos += c.getWidth() + 10

def main():
    turtle.speed(0)
    turtle.pensize(3)
    turtle.hideturtle()
    drawNum(1234567890)
    turtle.done()

main()


# Q5

from abc import ABCMeta, abstractmethod

class StationaryGood(metaclass = ABCMeta):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    @abstractmethod
    def getCost(self):
        pass

class Magazine(StationaryGood):
    def __init__(self, name, price):
        super().__init__(name)
        self.price = price

    def getCost(self):
        return self.price

class Book(StationaryGood):
    def __init__(self, name, price):
        super().__init__(name)
        self.price = price

    def getCost(self):
        return self.price * 0.9

class Ribbon(StationaryGood):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    def getCost(self):
        return self.length * 5

def getTotalCost(basket):
    total = 0
    for good in basket:
        total += good.getCost()
    return total

def main():
    basket = [Magazine("Computer World", 70),
              Magazine("Computer World", 70),
              Magazine("Computer World", 70),
              Book("Windows 7 for Beginners", 200),
              Book("Windows 7 for Beginners", 200),
              Ribbon("Blue ribbon", 10)]

    for good in basket:
        print(good.getName(), ":", good.getCost(), "Baht")

    print("Total cost is", getTotalCost(basket), "Baht")

main()
