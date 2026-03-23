# Examples of Getter and Setter in Python

# class Student:
#     def __init__(self, name, age):
#         self._age = age #protected attribute
#         self.name = name 

#     # Getter method
#     def get_age(self):
#         return self._age
    
#     # Setter method
#     def set_age(self, age):
#         if age > 0:
#             self._age = age
#         else:
#             print("Age must be positive")

# # Create object
# s = Student("Anil", 20)

# # Using getter
# print(s.get_age())

# # Using setter
# s.set_age(22)
# print(s.get_age())


# Using @property

# class Student:
#     def __init__(self, age):
#         self._age = age
    
#     # Getter
#     @property
#     def age(self):
#         return self._age
    
#     # Setter
#     @age.setter
#     def age(self, value):
#         if value > 0:
#             self._age = value
#         else:
#             print("Age must be positive")

# # Create object
# s = Student(20)

# # Getter
# print(s.age)

# # Setter
# s.age = 25
# print(s.age)


# Example with Validation (Marks)

class Student:
    def __init__(self):
        self.marks = 0

    @property
    def marks(self):
        return self._marks
    
    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            print("Marks must be between 0 and 100")
        
s = Student()

s.marks = 85
print(s.marks)

s.marks = 150