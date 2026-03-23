# Import Statement in Python

# Importing built-in modules

# import math
# pie = math.pi
# print("Value of pi: ", pie)


# Importing external Modules

# import pandas

# # Create simple DataFrame
# data = {
#     "Name" : ["Elon", "Trevor", "swastik"],
#     "Age" : [25, 30, 35]
# }
# df = pandas.DataFrame(data)
# print(df)


# Importing specific functions

# from math import pi
# print(pi)



# Importing Modules with Aliases
# import math as m
# result = m.sqrt(25)
# print("Square root of 25:", result)


# Importing Everything from a Module (*)

# from math import *
# print(pi)
# print(factorial(6))



# Handling Import Errors in Python

# try:
#     import mathematics # Incorrect module name
#     print(mathematics.pi)
# except ImportError:
#     print("Module not found!. Please check the module name or install it if necessary")

