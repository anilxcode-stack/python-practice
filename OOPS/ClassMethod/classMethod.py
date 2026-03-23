# Class Method in Python

# class Geeks:
#     course = "DSA"
#     list_of_instances = []

#     def __init__(self, name):
#         self.name = name
#         Geeks.list_of_instances.append(self)

#     @classmethod
#     def get_course(cls):
#         return f"Course: {cls.course}"
    
#     @classmethod
#     def get_instance_count(cls):
#         return f"Number of instances: {len(cls.list_of_instances)}"
    
#     @staticmethod
#     def welcome_message():
#         return "Welcome to Geeks for Geeks!"
    
# #Creating instances]
# g1 = Geeks("Alice")
# g2 = Geeks("BOb")

# # Calling class Method
# print(Geeks.get_course())
# print(Geeks.get_instance_count())

# # Calling static method
# print(Geeks.welcome_message())



# Create class method using classmethod()

# class Student:

#     # Create a variable
#     name = "GeeksforGeeks"

#     # Create a funciton
#     def print_name(obj):
#         print("The name is: ", obj.name)

# # create print_name classmethod
# # before creating this line print_name()
# # It can be called only with object not with class

# Student.print_name = classmethod(Student.print_name)

# # now this method can be called as classmethod
# # print_name() method is called a class method
# Student.print_name()



# Python Program to demonstrate
# use of a class method and statice method

# from datetime import date

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # a Class method to create a 
#     # Person object by birth year.
#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year - year)
    
#     # a static method to check if a
#     # Person is adult or not.
#     @staticmethod
#     def isAdult(age):
#         return age >= 18
    

# # Creating an instance using the constructor
# person1 = Person("Mayank", 21)

# # Creating an instance using the class method
# person2 = Person.fromBirthYear("Mayank", 1996)

# print(f"Person1 Age: {person1.age}")
# print(f"Person2 Age: {person2.age}")

# # Checking if person1 is an adult
# print(f"Is Person1 and adult? {"Yes" if Person.isAdult(person1.age) else 'No'}")

# # Checking if Person2 is an adult
# print(f"Is Person2 an adult {"Yes" if Person.isAdult(person2.age)  else 'No'}")


