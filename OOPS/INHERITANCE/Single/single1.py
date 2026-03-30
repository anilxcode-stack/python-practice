""" Single Inheritance in Python """

# class Parent:
#     def func1(self):
#         print("This function is in parent class.")

# class Child(Parent):
#     def func2(self):
#         print("This function is in child class.")

# obj = Child()
# obj.func1()
# obj.func2()

# ___________________________________________________________

# class Parent:
#     def m1(self):
#         print("Parent class method")
        
# class Child(Parent):
#     def m2(self):
#         print("Child class method")

# child = Child()

# child.m1()
# child.m2()

# parent = Parent()

# parent.m1()

# ___________________________________________________________

# class Animal:
#     def speak(self):
#         return "Animal speaks"
    
# class Dog(Animal):
#     def bark(self):
#         return self.speak() + " and barks"
    
# dog = Dog()

# print(dog.bark())

# _________________________________________________________

# class Teacher:
#     def __init__(self, name):
#         self.name = name

#     def showMe(self):
#         print("Teacher name: ", self.name)

# class Student(Teacher):
#     def showMe(self):
#         print("Student name: ", self.name)

# teach = Teacher("Deepak")
# teach.showMe() # calling method of the Teacher class

# st = Student("Mahika")
# st.showMe()  # calling method of Student class.

# ___________________________________________________________

# class Base:
#     def m1(self, x):
#         print("Parent class m1 method")
#         self.x = x
#         print("Value of x = ", self.x)

# class Derived(Base):
#     def m2(self, y):
#         print("Child class m2 method")
#         self.y = y
#         print("Value of y = ", self.y)

# obj = Derived()

# # Calling methods of Derived class
# obj.m1(10)
# obj.m2(20)

# ____________________________________________________________

class Shape:
    def __init__(self):
        self.length = float(input("Enter the length: "))
        self.breadth = float(input("Enter the breadth: "))

    def display(self):
        print("Length = ", self.length)
        print("Breadth = ", self.breadth)

class Rectangle(Shape):
    def __init__(self):
        Shape.__init__(self)

    def cal_per(self):
        self.per = 2 * (self.length + self.breadth)
        print("Perimeter of rectangle = ", self.per)

    def cal_area(self):
        self.area = self.length * self.breadth
        print("Area of reactangle = ", self.area)

# Create an object of class Rectangle
rt = Rectangle()

# Calling method of subclass using rt.
rt.display()
rt.cal_per()
rt.cal_area()