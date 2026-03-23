# Inheritance in python

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def info(self):
#         print("Animal name: ", self.name)

# class Dog(Animal):
#     def sound(self):
#         print(self.name, "barks")

# d = Dog("Buddy")
# d.info() # Inherited method
# d.sound()



# Inheritace with Child Method

# class Animal:
#     def eat(self):
#         print("Animal is eating")
    
# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# d = Dog()
# d.eat() # inherited method
# d.bark()  # child class method


# Inheritance with Constructor

# class Person:
#     def __init__(self, name):
#         self.name = name

# class Student(Person):
#     def display(self):
#         print("Student name: ", self.name)

# s = Student("Anil")
# s.display()


# Overriding Parent Method

# class Animal:
#     def speak(self):
#         print("Animal sound")

# class Cat(Animal):
#     def speak(self):
#         print("Meow")

    
# c = Cat()
# c.speak()