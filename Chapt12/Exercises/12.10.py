from tkinter import *

class RacingCars(Canvas):
    def __init__(self, container, width, height, cars):
        super().__init__(container, width=width,height=height)
        div = height / cars
        self.cars = []
        for i in range(cars):
            self.cars.append(RacingCar(height - i * div))


        self.drawCar()
        while True:
            for car in self.cars:
                car.refX += 1
            self.after(50)
            self.update()
            self.drawCar()

    def animate(self):

        for car in self.cars:
            car.refX += car.dx
            # self.move("car", car.dx, 0)
            self.after(5)
            self.update()
            if car.refX > 270:
                car.delete("car")
                car.refX = -40
        self.drawCar()

    def drawCar(self):
        self.delete("all")
        for car in self.cars:
            self.create_oval(car.refX + 10, car.refY - 10, car.refX + 20, car.refY, tags="car", fill="black")
            self.create_oval(car.refX + 30, car.refY - 10, car.refX + 40, car.refY, tags="car", fill="black")
            self.create_rectangle(car.refX, car.refY - 20, car.refX + 50, car.refY - 10, fill="red", tags="car")
            self.create_polygon(car.refX + 10, car.refY - 20, car.refX + 20, car.refY - 30,
                                        car.refX + 30, car.refY - 30, car.refX + 40, car.refY - 20, tags="car")

class RacingCar:
    def __init__(self, y):

        self.refX = 0
        self.refY = y
        self.dx = 5



class Display:
    def __init__(self):
        window = Tk()
        window.title("Racing Cars")

        a = RacingCars(window, 400, 220, 4)
        a.pack()

        window.mainloop()

Display()
