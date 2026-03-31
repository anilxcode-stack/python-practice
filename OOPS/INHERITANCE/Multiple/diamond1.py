""" Diamond Problem in Multiple Inheritance """

#todo by MRO order
#! Class4 -> Class2 -> Class3 -> Class1 -> object

# class Class1:
#     def m(self):
#         print("In Class1")

# class Class2(Class1):
#     def m(self):
#         print("In Class2")
#         super().m()

# class Class3(Class1):
#     def m(self):
#         print("In Class3")
#         super().m()

# class Class4(Class2, Class3):
#     def m(self):
#         print("In Class4")
#         super().m()

# print(Class4.mro())
# print(Class4.__mro__)

# _________________________________________________________

# class Class1:
#     def m(self):
#         print("In Class1")

# class Class2(Class1):
#     def m(self):
#         print("In Class2")

# class Class3(Class1):
#     def m(self):
#         print("In Class3")

# class Class4(Class2, Class3):
#     pass

# obj = Class4()
# obj.m()

# ____________________________________________________________

# class Class1:
#     def m(self):
#         print("In Class1")
    
# class Class2(Class1):
#     pass

# class Class3(Class1):
#     def m(self):
#         print("In Class3")

# class Class4(Class2, Class3):
#     pass

# obj = Class4()
# obj.m()

# __________________________________________________________

# class Class1:
#     def m(self):
#         print("In Class1")

# class Class2(Class1):
#     def m(self):
#         print("In Class2")

# class Class3(Class1):
#     def m(self):
#         print("In Class3")

# class Class4(Class2, Class3):
#     def m(self):
#         print("In Class4")


# obj = Class4()
# obj.m()
# Class2.m(obj)
# Class3.m(obj)
# Class1.m(obj)


# ____________________________________________________________

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")
        Class1.m(self)

class Class3(Class1):
    def m(self):
        print("In Class3")
        Class1.m(self)

class Class4(Class2, Class3):
    def m(self):
        print("In Class4")
        Class2.m(self)
        Class3.m(self)

obj = Class4()
obj.m()

