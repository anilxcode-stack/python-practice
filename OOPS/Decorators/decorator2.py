# Types of decorators


# 1. Function Decorators

# def simple_decorator(func):
#     def wrapper():
#         print(">>> Starting function")
#         func()
#         print(">>> Function finished")
#     return wrapper

# @simple_decorator
# def greet():
#     print("Hello, World")
# greet()


# 2 . Method Decorators

def method_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("Before method execution")
        res = func(self, *args, **kwargs)
        print("After method execution")
        return res
    return wrapper

class MyClass:
    @method_decorator
    def say_hello(self):
        print("Hello")

obj = MyClass()
obj.say_hello()
