from circle import Circle

def main():
    myCircle = Circle()

    n = 5
    printAreas(myCircle, n)
    
    print(f"\nRadius is {myCircle.radius}")
    print(f"n is {n}")
    
def printAreas(c, times):
    print("Radius \t\tArea")
    while times >= 1:
        print(c.radius, "\t\t", c.getArea())
        c.radius = c.radius + 1
        times = times - 1
        
main()