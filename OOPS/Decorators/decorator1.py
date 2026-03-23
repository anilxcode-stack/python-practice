# Decorators in Pyhton

# def decorator(func):
#     def wrapper():
#         print("Before calling the function")
#         func()
#         print("After calling the function")
#     return wrapper

# @decorator # Applying the decorator to a function
# def greet():
#     print("Hello, World!")
# greet()



# Decorator with Parameters

# def decorator_name(func):
#     def wrapper(*args, **kwargs):
#         print("Before execution")
#         result = func(*args, **kwargs)
#         print("After execution")
#         return result
#     return wrapper

# @decorator_name
# def add(a, b):
#     return a + b
# print(add(5, 3))


# Functions as First-Class Objects

# # Assigning a function to a variable
# def greet(n):
#     return f"Hello, {n}!"
# say_hi = greet # Assign the greet function to say_hi
# print(say_hi("Alex"))

# # Passing a function as an argument
# def apply(f, v):
#     return f(v)
# res = apply (say_hi, "Elon")
# print(res)

# # Returning a function from another function
# def make_mult(f):
#     def mult(x):
#         return x * f
#     return mult
# dbl = make_mult(2)
# print(dbl(5))


# Higher-Order Functions

# # A Higher-order function that takes another function
# # as argument
# def fun(f, x):
#     return f(x)

# # A simple function to pass
# def square(x):
#     return x * x
# res = fun(square, 5) # Using apply_function to apply the 