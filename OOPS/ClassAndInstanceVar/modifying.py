# Modifying CLass Variable


# Modifying via an Instance (Not Recommended)
# class CSStudent:
#     stream = 'cse' # class variable

#     def __init__(self, name, roll):
#         self.name = name # Instance variable
#         self.roll = roll # Instance variable


# # Creating objects
# a = CSStudent('Rose', 1)
# b = CSStudent('Nat', 2)


# a.stream = 'ece'
# print(a.stream)
# print(b.stream)


# Modifying via the Class Name (Recommended)

# class CSStudent:
#     stream ='cse' # class variable

#     def __init__(self, name, roll):
#         self.name = name # Instance variable
#         self.roll = roll # Instance variable

# a = CSStudent("Rose", 1)
# b = CSStudent("Emil", 9)

# CSStudent.stream = 'mech'
# print(a.stream)
# print(b.stream)