# class A:
#     def __init__(self, i = 0):
#         self.i = i

#     def m1(self):
#         self.i += 1

# class B(A):
#     def __init__(self, j=0):
#         super().__init__(3)
#         self.j = j

#     def m1(self):
#         self.i += 1

# def main():
#     b = B()
#     b.m1()
#     print(b.i)
#     print(b.j)

# main()

#========================================

# class A:
#     def __init__(self, i = 0):
#         self.i = i

#     def m1(self):
#         self.i += 1

#     def __str__(self):
#         return str(self.i)

# x = A(8)
# print(x)
#========================================
# class A:
#     def __new__(self):
#         print("A's __new__() invoked")

#     def __init__(self):
#         print("A's __init__() invoked")

# a = A()
#========================================

# class A:
#     def __new__(self):
#         self.__init__(self)
#         print("A's __new__() invoked")

#     def __init__(self):
#         print("A's __init__() invoked")

# class B(A):
#     def __new__(self):      
#         self.__init__(self)
#         print("B's __new__() invoked")

#     def __init__(self):
#         super().__init__(self)
#         print("B's __init__() invoked")

# def main():
#     a = A()
#     b = B()

# main()
#========================================

# class A:
#     def __init__(self):
#         print("A's __init__() invoked")

# class B(A):
#     def __init__(self):
#         print("B's __init__() invoked")

# def main():
#     a = A()
#     b = B()

# main()

#========================================

# class A:
#     def __init__(self, i):
#         self.i = i 

#     def __str__(self):
#         return "A"

# class B(A):
#     def __init__(self, i, j):
#         super().__init__(i)
#         self.j = j

# def main():
#     b = B(1, 2)
#     a = A(1)
#     print(a)
#     print(b)

# main()

#========================================

# class A:
#     def __init__(self, i):
#         self.i = i

#     def __str__(self):
#         return "A"

#     def __eq__(self, other):
#         return self.i == other.i

# def main():
#     x = A(1)
#     y = A(1)
#     print(x == y)

# main()