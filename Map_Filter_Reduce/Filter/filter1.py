# Filter function in Python

# Filtering Even Numbers

# def is_even(x):
#     return x % 2 == 0

# numbers = [1, 2, 3, 4, 5, 6]

# res = filter(is_even, numbers)

# print(list(res))


# Using filter() with Lambda function

# numbers = [1, 2, 3, 4, 5, 6]

# res = filter(lambda x: x % 2 == 0, numbers)

# print(list(res))



# Filtering Positive Numbers

# numbers = [-5, -2, 0, 3, 7, -1]

# res = filter(lambda x: x>0, numbers)

# print(list(res))

# Filtering Strings Based on Length

# words = ["apple", "hi", "banana", "cat"]

# res = filter(lambda w: len(w) > 3, words)

# print(list(res))


# Removing Empty Strings

# words = ["apple", "", "banana", "", "cherry"]

# res = filter(None, words)

# print(list(res))