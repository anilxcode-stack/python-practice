# Getters and Setter in Python

# class Geek:
#     def __init__(self, age=0):
#         self._age = age

#     # getter method 
#     def get_age(self):
#         return self._age
    
#     # setter method
#     def set_age(self, x):
#         self._age = x

# raj = Geek()

# # setting the age using setter
# raj.set_age(21)

# # retrieving age using getter
# print(raj.get_age())

# print(raj._age)


# Using property() function

# class Geeks:
#     def __init__(self):
#         self._age = 0

#     # function to get value of _age
#     def get_age(self):
#         print("getter method called")
#         return self._age
#     # function to set value of _age
#     def set_age(self, a):
#         print("setter method called")
#         self._age = a

#     # function to delete _age attribute
#     def del_age(self):
#         del self._age

#     age = property(get_age, set_age, del_age)


# mark = Geeks()

# mark.age = 10

# print(mark.age)


# Using @property decorators

# class Geeks:
#     def __init__(self):
#         self._age = 0

#     # using property decorator
#     # a getter function
#     @property
#     def age(self):
#         print("getter method called")
#         return self._age
    
#     # a setter function
#     @age.setter
#     def age(self, a):
#         if(a < 18):
#             raise ValueError("Sorry your age is below eligibility criteria")
#         print("Setter method called")
#         self._age = a
    
# mark = Geeks()

# mark.age = 19

# print(mark.age)


