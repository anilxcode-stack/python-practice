# Super Keyword in Python

# class Parent:
#     def show(self):
#         print("This is Parent class method")

# class Child(Parent):
#     def show(self):
#         super().show()  # Calling parent method
#         print("This is Child Class method")


# obj = Child()
# obj.show()


# Initialize Parent Attributes with super()

# class Emp:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name

# class fun(Emp):
#     def __init__(self, id, name, email):
#         super().__init__(id, name) # Calls Emp's __init__
#         self.email = email

# obj = fun(101, "Olivia", "olivia@email.com")
# print(obj.id, obj.name, obj.email)


# Effect of Using and Not Using super()

# class Person:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
    

# class Emp(Person):
#     def __init__(self, name, id):
#         self.name = name # Forgot to call Person's __init__

# emp = Emp("Jack", 103)
# print(emp.name)


# Another example

# class Person:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

# class Emp(Person):
#     def __init__(self, name, id):
#         super().__init__(name, id)

# emp = Emp("James", 103)
# print(emp.name, emp.id)


# Using super() in Multilevel Inheritance

# class Mammal:
#     def __init__(self, name):
#         print(name, "is a mammal")

# class CanFly(Mammal):
#     def __init__(self, name):
#         print(name, "Cannot fly")
#         super().__init__(name)

# class CanSwim(CanFly):
#     def __init__(self, name):
#         print(name, "Cannot swim")
#         super().__init__(name)
    
# class Animal(CanSwim):
#     def __init__(self, name):
#         super().__init__(name)

# dog = Animal("Dog")