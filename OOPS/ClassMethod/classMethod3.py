# Class Mehtod in Python ('cls') keyword example

# class Student:
#     school_name = "PIEMR"

#     @classmethod
#     def show_school(cls):
#         print("School Name: ", cls.school_name)

    
# # Call without creating object
# Student.show_school()



# Ex - 2

# class Student:
#     school_name = "PIEMR"

#     @classmethod
#     def change_school(cls, new_name):
#         cls.school_name = new_name

# Student.change_school("IIT Indore")
# print(Student.school_name)


# class Student:
#     school = "PIEMR"

#     def __init__(self, name):
#         self.name = name
    
#     def show_name(self):
#         print("Name: ", self.name)

#     @classmethod
#     def show_school(cls):
#         print("School: ", cls.school)


# s1 = Student("Anil")

# s1.show_name() # instance method
# Student.show_school()  # class method



# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_string(cls, data):
#         name, age = data.split("-")
#         return cls(name, int(age))
    
# # Using normal constructor
# s1 = Student("Anil", 20)

# # Using class method constructor
# s2 = Student.from_string("Rahul-21")

# print(s2.name, s2.age)


# Working with Multiple Class Variables

# class Company:
#     company_name = "TCS"
#     location = "India"

#     @classmethod
#     def update_details(cls, name, loc):
#         cls.company_name = name
#         cls.location = loc

# Company.update_details("Infosys", "Bangalore")

# print(Company.company_name)
# print(Company.location)


# Using cls with Inheritance

# class Person:
#     def __init__(self, name):
#         self.name = name

#     @classmethod
#     def create(cls, name):
#         return cls(name)
    
# class Student(Person):
#     pass

# s = Student.create("Anil")
# print(type(s)) # <class '__main__.Student'>



# Factory Pattern using Class Method

# class Shape:
#     @classmethod
#     def create_shape(cls, type):
#         if type == "circle":
#             return Circle()
#         elif type == "square":
#             return Square()
#         else:
#             return None
        
# class Circle:
#     def draw(self):
#         print("Drawing Circle")


# class Square:
#     def draw(self):
#         print("Drawing Square")

# shape = Shape.create_shape("circle")
# shape.draw()


# Class Method + Counter Example

# class Student:
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Student.count += 1

#     @classmethod
#     def total_student(cls):
#         return cls.count
    
# s1 = Student("A")
# s2 = Student("B")

# print(Student.total_student())