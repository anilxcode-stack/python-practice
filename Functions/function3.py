# Return In Function

# def my_function(x, y):
#     return x+y

# result = my_function(3, 4)
# print(result)


# def my_function():
#     return ["apple", "banana", "cherry"]

# fruits = my_function()
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])

# def my_function():
#     return(10, 20)

# x, y = my_function()

# print("x: ", x)
# print("y: ", y)

# def square(n):
#     return n*n

# res = square(4)
#print(res)



# Returning multiple values

# def get_vals():
#     x = 10
#     y = 20
#     return x, y

# a, b = get_vals()
# print(a)
# print(b)

# def calc(n):
#     return [n*n, n*n*n]
# print(calc(3))



# Function Returning Another function
def outer(msg):
    def inner():
        return msg
    return inner

f = outer("Hello! ")
print(f())