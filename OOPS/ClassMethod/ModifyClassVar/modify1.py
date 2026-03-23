# Modify Class Variable (Correct Way)

# class Student:
#     school = "PIEMR" # class variable

# s1 = Student()
# s2 = Student()

# # Modify using class
# Student.school = "IIT indore"

# print(s1.school) #IIT Indore
# print(s2.school) # IIT Indore


# Modify Using Object (Wrong way)

# class Student:
#     school ="PIEMR"

# s1 = Student()
# s2 = Student()

# # Modify using one object

# s1.school = "IIT indore"

# print(s1.school) # IIT Indore
# print(s2.school)  # PIEMR


# Modify Class Varible Using cls (Best Practice)

# class Student:
#     school = "PIEMR"
    
#     @classmethod
#     def change_school(cls, name):
#         cls.school = name

# s1 = Student()
# s2 = Student()

# Student.change_school("IIT Indore")

# print(s1.school) # IIT Indore
# print(s2.school)  # IIT Indore

