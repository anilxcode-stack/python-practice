# Further more examples of super keyword

# class Parent:
#     def display(self):
#         print("Parent display")

# class Child(Parent):
#     def display(self):
#         super().display()  # call parent method
#         print("Child display")

# obj = Child()
# obj.display()


# Using super() in class method

# class Parent:
#     @classmethod
#     def show(cls):
#         print("Parent class method")

# class Child(Parent):
#     @classmethod
#     def show(cls):
#         super().show()
#         print("Child class method")

# Child.show()