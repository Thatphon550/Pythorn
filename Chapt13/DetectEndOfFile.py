import pickle

def main():
    outfile = open("numbers.dat", "wb")

    data = eval(input("Enter an integer (the input exits " +
                      "if the input is 0): "))
    while data != 0:
        pickle.dump(data, outfile)
        data = eval(input("Enter an integer (the input exits " +
                          "if the input is 0): "))
    outfile.close()

    infile = open("numbers.dat", "rb")

    end_of_file = False

    try:
        while not end_of_file:
            print(pickle.load(infile), end = " ")
    except EOFError:
            print("\nAll objects are read")
    finally:
         infile.close()


main()
