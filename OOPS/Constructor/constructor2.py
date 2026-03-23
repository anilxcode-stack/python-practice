# Examples of Constructor in Python 

# class Employee:
#     'Common base class for all employees'
#     def __init__(self):
#         self.name = "Bhavana"
#         self.age = 24

# e1 = Employee()
# print(f"Name {e1.name}")
# print(f"Age {e1.age}")



# class Employee:
#     'Common base class for all employees'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# e1 = Employee("Bhavana", 24)
# e2 = Employee("Bharat", 25)

# print(f"Name: {e1.name}")
# print(f"Age: {e1.age}")
# print(f"Name: {e2.name}")
# print(f"Age: {e2.age}")




# class Employee:
#     'Common base class for all employees'
#     def __init__(self, name = "Bhavana", age=24):
#         self.name = name
#         self.age = age
# e1 = Employee()
# e2 = Employee("Bharat", 25)

# print(f"Name {e1.name}")
# print(f"Age: {e1.age}")
# print(f"Name: {e2.name}")
# print(f"Age: {e2.age}")



# class Employee:
#     def __init__(self, name="Bhavana", age=24):
#         self.name = name
#         self.age = age
#     def displayEmployee(self):
#         print("Name : ", self.name, ", age: ", self.age)

# e1 = Employee()
# e2 = Employee("Bharat", 25)

# e1.displayEmployee()
# e2.displayEmployee()