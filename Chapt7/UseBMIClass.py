from BMI import BMI

def main():
    bmi1 = BMI("John Doe", 18, 145, 70)
    print("The BMI for", bmi1.getName(), "is", bmi1.getBMI(), bmi1.getStatus())
    

    
main()