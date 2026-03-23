# File Handling in Python

# Read and Write Mode (r+)

# file = open("File_Handling/File2/data.txt", "r+")
# print(file.read())
# file.write("Hello")
# file.close()

# Write in file 
# file = open("File_Handling/File2/data.txt", "w")
# file.write("Hello Python")
# file.close()

# Write and Read Mode (w+)

# file = open("File_Handling/File2/data.txt", "w+")
# file.write("Python Programming")
# file.seek(0)
# print(file.read())
# file.close()

# Append Mode (a)

# file = open("File_Handling/File2/data.txt", "a")
# file.write("\nNew Line Added")
# file.close()


# Append and Read Mode (a+)

# file = open("File_Handling/File2/data.txt", "a+")
# file.write("\nHello")
# file.seek(0)
# print(file.read())
# file.close()

# Write Binary Mode (wb)

# file = open("File_Handling/File2/file.bin", "wb")
# file.write(b"Hello")
# file.close()


# Write and Read Binary Mode (wb+)

# file = open("File_Handling/File2/file.bin", "wb+")
# file.write(b"Hello")
# file.seek(0)
# print(file.read())
# file.close()


# Append Binary Mode (ab)

# file = open("File_Handling/File2/file.bin", "ab")
# file.write(b"More Data")
# file.close()


# Append and Read Binary Mode (ab+)

# file = open("File_Handling/File2/file.bin", "ab+")
# file.write(b"Data")
# file.seek(0)
# print(file.read())
# file.close()


# seek(0)  

# file = open("File_Handling/File2/data.txt", "r")

# print(file.read()) # reads entire file

# file.seek(0)  # move pointer back to start

# print(file.read())  # reads agaion from beginning

# file.close()