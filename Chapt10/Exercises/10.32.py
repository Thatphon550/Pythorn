import turtle as t

def drawLine(p1, p2):
    t.teleport(p1[0], p1[1])
    t.goto(p2[0], p2[1])

def main():
    drawLine([30, -5], [-40, 20])
    t.done()

main()