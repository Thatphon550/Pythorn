def time24hourTo12hour(string):
    hours = int(string[0:2])
    minutes = int(string[3:5])
    
    if hours >= 12:
        hours %= 12
        time = "PM"
    else:
        time = "AM"
        
    return f"{hours}:{minutes} {time}"

def main():
    print(time24hourTo12hour("23:24"))
    print(time24hourTo12hour("05:25"))
    print(time24hourTo12hour("11:59"))
        
main()

