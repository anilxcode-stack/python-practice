# File Handling in Python

# Opening a File

# f = open("File_Handling/File1/geek.txt", "r")
# print(f.read())


# Closing a File

# file = open("File_Handling/File1/geek.txt", "r")
# # Perform file Operations
# file.close()


# Checking File Properties

# f = open("File_Handling/File1/geek.txt", "r")
# print("Filename:", f.name)
# print("Mode:", f.mode)
# print("Is Closed?", f.closed)

# f.close()
# print("Is Closed?", f.closed)


# Reading a File

# file = open("File_Handling/File1/geek.txt", "r")
# content = file.read()
# print(content)
# file.close()


# Writing a File

# with open("File_Handling/File1/geek.txt", "w") as file:
#     file.write("Hello, Python!\n")
#     file.write("File Handling is easy with Python.")

# print("File written successfully")

# Then Rechecking

# file = open("File_Handling/File1/geek.txt", "r")
# content = file.read()
# print(content)
# file.close()



# Using with Statement

# with open("File_Handling/File1/geek.txt", "r") as file:
#     content = file.read()
#     print(content)


# Handling Exceptions when Closing a File

# try:
#     file = open("File_Handling/File1/geek.txt", "r")
#     content = file.read()
#     print(content)
# finally:
#     file.close()


# Append Mode ('a') -> Add Content without Overwrite

# with open('File_Handling/File1/geek.txt', 'a') as file:
#     file.write('\nThis is a new line')

