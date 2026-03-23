# dir() , __dict__ and help()


# dir() Method
# print(dir(str))


# Listing Object Attributes

# l = [1, 2, 3]

# print(dir(l))


# Checking current scope

# x = 10

# def say_hello():
#     pass

# print(dir()) # List all variables and functions in the current scope



# help() method in Python

# help(str)  # Displays detailed documentation of the str class


# Understanding function behavior
# import math
# help(math.sqrt) # Shows details about the sqrt() f
# # function in math module


# Viewing docstrings of user-defind classes

# class Sample:
#     """This is a simple class."""
#     def method(self):
#         """This is a simple method."""
#         pass

# help(Sample)  # Displays docstrings and method details
# # of the 



# The __dict__ attribute

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 30)
p.__dict__