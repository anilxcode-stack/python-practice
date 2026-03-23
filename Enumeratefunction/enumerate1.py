# Enumerate function in python

# a = ["Python", "Java", "C++"]
# for i, v in enumerate(a):
#     print(i, v)


# a = ["A", "B", "C"]
# r = list(enumerate(a))  # gives in a list with tuple
# print(r)

# a = ['x', 'y', 'z']
# e = enumerate(a)
# print(next(e))
# print(next(e))


# d = {"a":10, "b":20}
# for i, (k, v) in enumerate(d.items()):
#     print(i, k, v)

# students = ["Alice", "Bob", "Charlie"]

# for roll_no, name in enumerate(students, start=101):
#     print(f"Roll No: {roll_no}, Name: {name}")



# numbers = [10, 25, 30, 34, 25, 50]
# indices = [i for i, value in enumerate(numbers) if value == 25]
# print(indices)


# Modifying List Element Using Enumerate 
# prices = [100, 200, 300]

# for i, price in enumerate(prices):
#     prices[i] = price * 1.1
    
# print(prices)        


# data = ["apple", "", "banana", "", "cherry"]
# for index, value in enumerate(data):
#     if value == "":
#     print(f"Empty String found at position {index}")

# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 95, 78]

# for index,(name, score) in enumerate(zip(names, scores)):
#     print(f"{index}, {name} scored {score}")

