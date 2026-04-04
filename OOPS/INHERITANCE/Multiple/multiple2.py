""" Multiple inheritance with constructor in classes """

# class A:
#     def __init__(self):
#         print("Constructor of A")

# class B:
#     def __init__(self):
#         print("Constructor of B")

# class C(A, B):
#     def __init__(self):
#         print("Constructor of C")

# obj = C() #Only child constructor runs, unless you explicitly call parent constructors.

# _____________________________________________________________________

""" Calling Constructor mannually """

# class A:
#     def __init__(self):
#         print("Constructor of A")

# class B:
#     def __init__(self):
#         print("Constructor of B")

# class C(A, B):
#     def __init__(self):
#         A.__init__(self)
#         B.__init__(self)
#         print("Constructor of C")

# obj = C()

# _________________________________________________________________

""" Using super() """

# class A:
#     def __init__(self):
#         print("Constructor of A")

# class B:
#     def __init__(self):
#         print("Constructor of B")

# class C(A, B):
#     def __init__(self):
#         super().__init__()
#         print("Constructor of C")

# obj = C()  # Only first parent (A) is called due to MRO.

# print(C.mro())

# ___________________________________________________________________

class A:
    def __init__(self):
        print("A constructor")
        super().__init__()


class B:
    def __init__(self):
        print("B constructor")
        super().__init__()

class C(A, B):
    def __init__(self):
        print("C constructor")
        super().__init__()

obj = C() # All constructors called once in MRO order.

