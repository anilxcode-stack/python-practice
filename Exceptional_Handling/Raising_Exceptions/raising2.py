# Python Raise Keyword 


# a = 5
# if a % 2 != 0:
#     raise Exception("The number should'nt be an odd integer")

s = "apple"
try:
    num = int(s)
except ValueError:
    raise ValueError("String can't be changed into integer")
