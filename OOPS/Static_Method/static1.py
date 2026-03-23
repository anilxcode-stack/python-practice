# Static method in Puython

# class Calc:
#     @staticmethod
#     def add(a, b):
#         return a + b
    
# res = Calc.add(2, 3)
# print(res)



# Example 1
# class Check:
#     @staticmethod
#     def is_even(n):
#         return n % 2 == 0
    
# print(Check.is_even(10))


# # This example converts temperature from Celsius to Fahrenheit
# class Temp:
#     @staticmethod
#     def to_fahrenheit(c):
#         return (c * 9/5) + 32
    
# print(Temp.to_fahrenheit(25))

# class Person:
#     @staticmethod
#     def is_adult(age):
#         return age >= 18

# print(Person.is_adult(16))
# print(Person.is_adult(21))

# With Object also works

# class Demo:
#     @staticmethod
#     def greet():
#         print("Hello!")

# obj = Demo()
# obj.greet() # works
# Demo.greet() # also works


# class Validator:
#     @staticmethod
#     def is_even(num):
#         return num % 2 == 0
    
# print(Validator.is_even(10))