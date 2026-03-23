# implicit Type Conversion

# Python automatically convert data type into another data type

# a = 7
# b = 3.0

# c = a+b
# print(c)
# print(type(c))


# Explicit Type Conversion

# convert manually 

# # int -> float

# a = 5
# print(float(a))

# # float -> int
# a = 5.9
# print(int(a))

# # int -> string
# a = 5
# print(str(a))

# # string -> float
# a = "5.9"
# print(int(a))

# # Error case
# a = "hello"
# print(int(a))

# # Important error Case

# a = 5
# b = "7"
# print(a+b)

# Correct way

a = 5
b = "7"

print(a + int(b))