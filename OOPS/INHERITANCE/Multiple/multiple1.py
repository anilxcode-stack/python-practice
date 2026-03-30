""" Multiple Inheritance In Python """

# class Father:
#     def skills(self):
#         print("Father: Gardening, Driving")

# class Mother:
#     def skills(self):
#         print("Mother: Cooking, Painting")

# class Child(Father, Mother):
#     pass

# obj = Child()
# obj.skills()

# ___________________________________________________________

# class A:
#     def show(self):
#         print("A")
    
# class B:
#     def show(self):
#         print("B")

# class C(A, B):
#     pass

# obj = C()
# obj.show()

# ____________________________________________________________

""" Using super() keyword """

# class Base:
#     def show(self):
#         # Safe termination of method chain
#         pass

# class A(Base):
#     def show(self):
#         print("A")
#         super().show()

# class B(Base):
#     def show(self):
#         print("B")
#         super().show()

# class C(A, B):
#     def show(self):
#         print("C")
#         super().show()

# obj = C()
# obj.show()

# ________________________________________________________________

class A:
    def __init__(self):
        print("A Constructor")

class B:
    def __init__(self):
        print("B Constructor")

class C(A, B):
    def __init__(self):
        super().__init__()

obj = C()

