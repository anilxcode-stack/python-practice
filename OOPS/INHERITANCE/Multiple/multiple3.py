""" Multiple Inheritace with parametized Constructors """

# class A:
#     def __init__(self, a):
#         print("A Constructor:", a)

# class B:
#     def __init__(self, b):
#         print("B Constructor:", b)

# class C(A, B):
#     def __init__(self, a, b):
#         A.__init__(self, a)
#         B.__init__(self, b)
#         print("C Constructor")

# obj = C(10, 20)


# _________________________________________________________________

""" Using super()  with Parameters """
# To properly pass parameters, use *args and **kwargs


class A:
    def __init__(self, a, *args, **kwargs):
        print("A:", a)
        super().__init__(*args, **kwargs)

class B:
    def __init__(self, b, *args, **kwargs):
        print("B:", b)
        super().__init__(*args, **kwargs)

class C(A, B):
    def __init__(self, a, b):
        print("C Constructor")
        super().__init__(a=a, b=b)

obj = C(10, 20)