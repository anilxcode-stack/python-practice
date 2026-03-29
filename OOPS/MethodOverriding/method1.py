""" Method Overriding In Python """


# class Parent:
    
#     def __init__(self):
#         self.value = "Inside Parent"


#     # Parent's show method
#     def show(self):
#         print(self.value)

# # Defining child class
# class Child(Parent):

#     def __init__(self):
#         super().__init__()
#         self.value = "Inside Child"

#     # Child's show method
#     def show(self):
#         print(self.value)

# # Driver's Code
# obj1 = Parent()
# obj2 = Child()

# obj1.show() # Should print "Inside Parent"
# obj2.show() # Should print "Inside Child"

# _______________________________________________________________

""" Method overriding with multiple and multilevel Inheritance """

# class Parent1():

#     def show(self):
#         print("Inside Parent1")

# class Parent2():

#     # Parent's show method
#     def display(self):
#         print("Inside Parent2")

# class Child(Parent1, Parent2):

#     # Child's show method
#     def show(self):
#         print("Inside Child")

# # Driver's Code
# obj = Child()

# obj.show()
# obj.display()

# ________________________________________________________________

""" MultiLevel Inheritance """

# class Parent():

#     def display(self):
#         print("inside Parent")

# class Child(Parent):

#     def show(self):
#         print("inside Child")

# class GrandChild(Child):

#     def show(self):
#         print("Inside GrandChild")


# g = GrandChild()
# g.show()
# g.display()


# ______________________________________________________________

""" Calling the Parent's method within the overriden method """

# class Parent():
    
#     def show(self):
#         print("Inside Parent")

# class Child(Parent):

#     def show(self):

#         Parent.show(self)
#         print("Inside Child")

# obj = Child()
# obj.show()


# ________________________________________________________

""" Using Super() """

# class Parent():

#     def show(self):
#         print("Inside Parent")

# class Child(Parent):

#     def show(self):

#         super().show()
#         print("Inside Child")

# obj = Child()
# obj.show()

# ____________________________________________________________________

""" Example 2: """

class GFG1:
    def __init__(self):
        print('HEY !!!!!! GFG I am initialised(Class GFG1)')

    def sub_GFG(self, b):
        print("Printing from class GFG1:", b)

class GFG2(GFG1):
    def __init__(self):
        print("HEY !!!!!! GFG I am initialised(Class GFG2)")
        super().__init__()

    def sub_GFG(self, b):
        print("Prinjting from class GFG2: ", b)
        super().sub_GFG(b + 1)

class GFG3(GFG2):
    def __init__(self):
        print("HEY !!!!!! GFG I am initialised(Class GFG3)")
        super().__init__()

    def sub_GFG(self, b):
        print("Printing from Class GFG3:", b)
        super().sub_GFG(b + 1)


# main function
if __name__ == '__main__':

    # created the object gfg
    gfg = GFG3()

    # calliung the function sub_GFG3() from class GHG3
    # which inherits botj  GFG1 and GFG2 classes
    gfg.sub_GFG(10)