
class Student:
    school = "PIEMR" # class variable

s1 = Student()
s2 = Student()

# Modify using class
Student.school = "IIT indore"

print(s1.school) #IIT Indore
print(s2.school) # IIT Indore