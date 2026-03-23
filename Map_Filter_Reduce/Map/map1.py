# Map Function in Python

# Converting Strings to integers

# s = ['1', '2', '3', '4']
# res = map(int, s)
# print(list(res))


# Converting map Object to List

# def double(val):
#     return val * 2

# a = [1, 2, 3, 4, 5]

# res = list(map(double, a))
# print(res)


# map()  with Lambda Functions

# a = [1, 2, 3, 4]
# res = list(map(lambda x: x**2, a))
# print(res)

# map() with Multiple Iterables

# a = [1, 2, 3]
# b = [4, 5, 6]

# res = map(lambda x, y: x + y, a, b)
# print(list(res))


# Converting Strings to Uppercase

# fruits = ["apple", "banana", "cherry"]
# res = map(str.upper, fruits)

# print(list(res))

# Extracting First Character from Strings

# words = ["apple", "banana", "cherry"]
# res = map(lambda s: s[0], words)

# print(list(res))


# Removing Whitespaces

# s = [" Hello ", " world ", " Python "]

# res = map(str.strip, s)
# print(list(res))