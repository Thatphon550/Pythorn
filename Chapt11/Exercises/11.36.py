import turtle as t
import random

def main():
    t.speed(0)
    x = -160
    for y in range(-160, 161, 20):
        t.teleport(x, y)
        t.forward(320)
    t.setheading(90)
    y = -160
    for x in range(-160, 161, 20):
        t.teleport(x, y)
        t.forward(320)


    pos = [[None for _ in range(16)] for _ in range(16)]
    print(pos)

    t.speed(2)
    t.teleport(0, 0)
    dead_end = False
    current_pos = [0, 0]
    t.pencolor("red")
    t.width(3)
    while not dead_end:
        direction = random.randint(1, 3)
        if direction == 1:
            current_pos = [round(t.xcor()), round(t.ycor())]
            if check(pos, current_pos):
                break
            t.forward(20)
            print(current_pos)
        elif direction == 2:
            current_pos = [round(t.xcor()), round(t.ycor())]
            if check(pos, current_pos):
                break
            t.left(90)
            t.forward(20)
            print(current_pos)

        elif direction == 3:
            current_pos = [round(t.xcor()), round(t.ycor())]
            if check(pos, current_pos):
                break
            t.right(90)
            t.forward(20)
            print(current_pos)


    t.done()

def check(pos, current_pos):
    if current_pos[0] < -160 or current_pos[0] > 160 or current_pos[1] < -160 or current_pos[1] > 160:
        return True
    if current_pos not in pos:
        pos.append(current_pos)
    else:
        return True

main()
