# Class Alternative Constructor

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_string(cls, data):
#         name, age = data.split("-")
#         return cls(name, int(age))
    
# # Normal constructor
# s1 = Student("Anil", 20)

# # Alternative Constructor
# s2 = Student.from_string("Rahul-21")

# print(s2.name, s2.age)


# List Input

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     @classmethod
#     def from_list(cls, data_list):
#         return cls(data_list[0], data_list[1])
    
# emp = Employee.from_list(["Anil", 50000])

# print(emp.name, emp.salary)


# Default Values Constructor

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def default_student(cls):
#         return cls("Unknown", 18)
    
# s = Student.default_student()
# print(s.name, s.age)


# Multiple Alternative Constructors
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_string(cls, data):
#         name, age = data.split("-")
#         return cls(name, int(age))
    
#     @classmethod
#     def from_dict(cls, data_dict):
#         return cls(data_dict["name"], data_dict["age"])
    
# s1 = Student.from_string("Anil-20")
# s2 = Student.from_dict({"name":"Rahul", "age":22})

# print(s1.name, s2.name)


# Inheritance 

# class Person:
#     def __init__(self, name):
#         self.name = name
    
#     @classmethod
#     def create(cls, name):
#         return cls(name)
    
# class Student(Person):
#     pass

# s = Student.create("Anil")
# print(type(s))


# Real - World Use Case

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    @classmethod
    def from_database(cls, db_row):
        return cls(db_row["username"], db_row["email"])
    
# Simulated DB data
data = {"username": "anil123", "email":"anil@gmail.com"}

user = User.from_database(data)
print(user.username)