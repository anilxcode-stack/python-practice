# DocString in Python (Documentation Strings)

# def greet(name):
#     """ This function greets the user by their name."""
#     return f"Hello, {name}!"

# print(greet("Anil"))


# def my_function():
#     """ Demonstrates triple quotes docstring and does nothing """
#     return None
# print("Using __doc__: ")
# print(my_function.__doc__)

# print("Using help(): ")
# help(my_function)



# def multiply(a, b):
#     """
#     Multiply two numbers.

#     Args:
#     a(int): First number
#     b(int): Second number
    
#     Returns:
#     int: Product of a and b

#     """
#     return a*b
# print(multiply(3, 5))


# Numpydoc Style DocStrings

# def divide(a, b):
#     """
#     Divide two numbers
#     Parameters
#     ___________

#     a: float
#     Dividend

#     b: float
#     Divisor

#     Returns
#     ________
#     float 
#        Qutient of divisor

#     """
#     if b == 0:
#         raise ValueError("Division by Zero not allowed.")
#     return a/b
# print(divide(6, 2))


# def power(a, b):
#     """ Return a raised to power b."""
#     return a**b
# print(power.__doc__)

