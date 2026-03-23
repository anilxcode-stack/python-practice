# Dunder method in Python

# __init__ Mehtod (Constructor)

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    

# s1 = Student("Anil", 20)

# print(s1.name) # Anil
# print(s1.age) # 20


# __str__ and __repr__

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"Student Name: {self.name}, Age: {self.age}"
    
#     def __repr__(self):
#         return f"Student('{self.name}', {self.age})"
    
# s1 = Student("Anil", 20)

# print(s1)   # Calls __str__()
# print(repr(s1)) # Calls __repr__()


# __len__ Method

# class MyList:
#     def __init__(self, items):
#         self.items = items

#     def __len__(self):
#         return len(self.items)
    
# obj = MyList([1, 2, 3, 4, 5])

# print(len(obj)) # 5


# __call__ Method

# class Multiply:
#     def __init__(self, factor):
#         self.factor = factor

#     def __call__(self, x):
#         return x * self.factor
    
# obj = Multiply(5)

# print(obj(10)) # 50 (acts like function call)



# Combined Example 

# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages

#     def __str__(self):
#         return f"Book: {self.title}"
    
#     def __repr__(self):
#         return f"Book(''{self.title}', {self.pages})"
    
#     def __len__(self):
#         return self.pages
    
#     def __call__(self):
#         return f"You opened {self.title}"
    
# b = Book("Python Guide", 300)

# print(b)  # __str__
# print(repr(b)) # __repr__
# print(len(b))  # __Len__
# print(b())  # __call__