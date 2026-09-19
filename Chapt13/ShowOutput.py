#13.19

# try:
#     list = 10 * [0]
#     x = list[10]
#     print("Done ")
# except IndexError:
#     print("Index out of bound")

#13.20

# def main():
#     try:
#         f()
#         print("After the function call")
#     except ZeroDivisionError:
#         print("Divided by zero!")
#     except:
#         print("Exception")

# def f():
#     print(1 / 0)

# main()

#13.21

# def main():
#     try:
#         f()
#         print("After the function call")
#     except IndexError:
#         print("Index out of bound")
#     except:
#         print("Exception in main")

# def f():
#     try:
#         s = "abc"
#         print(s[3])
#     except ZeroDivisionError:
#         print("Divided by zero!")

# main()

#13.25

try:
    lst = 10 * [0]
    x = lst[19]
    print("Done")
except IndexError:
    print("index out of bound")
else:
    print("Nothing is wrong")
finally:
    print("FInally we are here")

print("Continue")
