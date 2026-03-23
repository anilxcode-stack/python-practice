# Local and Global Variable in Python

# def greet():
#     msg = "Hello from inside the function!"
#     print(msg)

# greet()

# def greet():
#     msg = "Hello!"
#     print("Inside function:", msg)

# greet()
# print("Outside function: ", msg)  # Error


# Global Variables 
# msg = "Python is awesome!"

# def display():
#     print("Inside function: ", msg)

# display()
# print("Outside function:", msg)


# Use Local and Global variables

# def fun():
#     s = "Me too"
#     print(s)

# s = "I Love Geeksforgeeks"
# fun()
# print(s)


# Modifying Global Variables Inside a Function

# Without global (causes error)
# def fun():
#     s += "GFG"  # Error: Python thinks s is local variable
#     print(s)

# s = "I love Geeksforgeeks"
# fun()  # UnboundedError

# With global (works correctly)

# s = "Python is great!"

# def fun():
#     global s
#     s += "GFG"  # Modify global variable
#     print(s)
#     s = "Look for GeeksforGeeks Python Section" # Reassign global
#     print(s)

# fun()
# print(s)



# Global vs Local with Same Name

a = 1 # Global variable

def f():
    print("f():", a)  # Uses global a

def g():
    a = 2 # Local shadows global
    print("g():", a)

def h():
    global a
    a = 3 # Modifies global a
    print("h():", a)

print("global:", a)
f()
print("global:", a)
g()
print("global:", a)
h()
print("global:", a)