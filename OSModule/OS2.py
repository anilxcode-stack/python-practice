# Two function to create folders

# os.mkdir() -> create one folder

# import os

# # 1. check current folder
# print("Before ", os.getcwd())

# # 2. Create a folder named "myfolder"
# os.mkdir("myfolder")
# print("Folder 'myfolder' created")

# # 3. Move inside the new folder
# os.chdir("myfolder")
# print("Now inside: ", os.getcwd())


# os.makedir() -> create many folders (nested)

# import os

# # Create nested folders
# os.makedirs("project/data/input", exist_ok=True)
# print("Folder Created")


# Without exist_ok = True

# import os

# # Try creating a folder that already exist
# os.makedirs("project/data/input") # First time -> works
# os.makedirs("project/data/input") # second time -> Error


# Example with exist_ok = True
# import os

# # first time creates folders
# os.makedirs("project/data/input", exist_ok=True)

# # second time works safely , no error
# os.makedirs("project/data/input", exist_ok=True)
# print("Folders created safely!")



